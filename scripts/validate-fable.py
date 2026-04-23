#!/usr/bin/env python3
"""
validate-fable.py — 校验寓言文件的结构合规性

用法:
    python scripts/validate-fable.py <fable-file.md>
    python scripts/validate-fable.py --all
    python scripts/validate-fable.py --category security

退出码:
    0 = 全部通过
    1 = 存在错误
"""

import argparse
import re
import sys
import yaml
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent
FABLES_DIR = ROOT / "fables"
REQUIRED_FIELDS = {"title", "title_cn", "concept", "concept_cn", "category", "difficulty", "author", "created", "sources", "tags"}
VALID_CATEGORIES = {"consensus", "defi", "security", "evm", "cryptography", "governance", "infrastructure", "solana", "other"}
VALID_DIFFICULTIES = {"beginner", "intermediate", "advanced"}


class ValidationError:
    def __init__(self, file: Path, msg: str, line: Optional[int] = None):
        self.file = file
        self.msg = msg
        self.line = line

    def __str__(self):
        loc = f":{self.line}" if self.line else ""
        return f"  {self.file}{loc} — {self.msg}"


class FableValidator:
    def __init__(self, file_path: Path):
        self.file = file_path
        self.errors: list[ValidationError] = []
        self.meta: dict = {}
        self.body = ""
        self.lines: list[str] = []

    def load(self) -> bool:
        try:
            text = self.file.read_text(encoding="utf-8")
            self.lines = text.splitlines()
        except Exception as e:
            self.errors.append(ValidationError(self.file, f"Cannot read file: {e}"))
            return False

        match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
        if not match:
            self.errors.append(ValidationError(self.file, "Missing or malformed YAML frontmatter"))
            return False

        try:
            self.meta = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError as e:
            self.errors.append(ValidationError(self.file, f"Invalid YAML frontmatter: {e}"))
            return False

        self.body = match.group(2)
        return True

    def validate_frontmatter(self):
        missing = REQUIRED_FIELDS - set(self.meta.keys())
        if missing:
            self.errors.append(ValidationError(self.file, f"Missing frontmatter fields: {', '.join(sorted(missing))}"))

        cat = self.meta.get("category")
        if cat and cat not in VALID_CATEGORIES:
            self.errors.append(ValidationError(self.file, f"Invalid category '{cat}'. Must be one of: {', '.join(sorted(VALID_CATEGORIES))}"))

        diff = self.meta.get("difficulty")
        if diff and diff not in VALID_DIFFICULTIES:
            self.errors.append(ValidationError(self.file, f"Invalid difficulty '{diff}'. Must be one of: {', '.join(sorted(VALID_DIFFICULTIES))}"))

        sources = self.meta.get("sources")
        if sources and not isinstance(sources, list):
            self.errors.append(ValidationError(self.file, "'sources' must be a list"))

        tags = self.meta.get("tags")
        if tags and not isinstance(tags, list):
            self.errors.append(ValidationError(self.file, "'tags' must be a list"))

    def validate_content(self):
        # 检查标题
        if not self.body.strip().startswith("#"):
            self.errors.append(ValidationError(self.file, "Body must start with an H1 title (# Title)"))

        # 检查故事分隔符
        story_section = re.search(r"## 故事\s*\n", self.body) or re.search(r"## Story\s*\n", self.body)
        if not story_section:
            self.errors.append(ValidationError(self.file, "Missing '## 故事' or '## Story' section"))

        # 检查解释章节
        explain_section = re.search(r"## 这则寓言在说什么", self.body)
        if not explain_section:
            self.errors.append(ValidationError(self.file, "Missing '## 这则寓言在说什么' explanation section"))

        # 检查映射表
        if "| 故事元素 |" not in self.body and "| Story Element |" not in self.body:
            self.errors.append(ValidationError(self.file, "Missing key mappings table"))

        # 字数检查
        story_text = self.extract_story_text()
        word_count = len(story_text)
        if word_count < 800:
            self.errors.append(ValidationError(self.file, f"Story too short: {word_count} chars (min ~800)"))
        if word_count > 6000:
            self.errors.append(ValidationError(self.file, f"Story very long: {word_count} chars (suggest ≤4000)"))

        # 检查代码块中是否意外包含真实 Solidity 代码（寓言应尽量避免直接代码）
        code_blocks = re.findall(r"```solidity\s*\n(.*?)\n```", self.body, re.DOTALL)
        if code_blocks:
            self.errors.append(ValidationError(self.file, f"Contains {len(code_blocks)} Solidity code block(s). Fables should avoid raw code; use metaphors instead."))

    def extract_story_text(self) -> str:
        """提取故事章节的纯文本。"""
        # 优先匹配 ## 故事 到 ## 这则寓言在说什么 之间的内容
        m = re.search(r"## 故事\s*\n(.*?)\n## 这则寓言在说什么", self.body, re.DOTALL)
        if m:
            return re.sub(r"[#*|>`\-\n]", "", m.group(1)).strip()
        # 备用：匹配到文件中的下一个 H2
        m = re.search(r"## 故事\s*\n(.*?)\n## ", self.body, re.DOTALL)
        if m:
            return re.sub(r"[#*|>`\-\n]", "", m.group(1)).strip()
        return ""

    def validate(self) -> bool:
        if not self.load():
            return False
        self.validate_frontmatter()
        self.validate_content()
        return len(self.errors) == 0

    def report(self):
        if self.errors:
            print(f"\n[FAIL] {self.file.relative_to(ROOT)}")
            for e in self.errors:
                print(str(e))
            return False
        else:
            story_len = len(self.extract_story_text())
            print(f"[PASS] {self.file.relative_to(ROOT)} (story ~{story_len} chars)")
            return True


def validate_all(category: Optional[str] = None) -> int:
    targets = []
    search_dir = FABLES_DIR / category if category else FABLES_DIR
    for f in sorted(search_dir.rglob("*.md")):
        targets.append(f)

    passed = 0
    failed = 0
    for f in targets:
        v = FableValidator(f)
        ok = v.validate()
        if v.report():
            passed += 1
        else:
            failed += 1

    print(f"\n{'=' * 50}")
    print(f"Total: {passed + failed} | Passed: {passed} | Failed: {failed}")
    return 0 if failed == 0 else 1


def main():
    parser = argparse.ArgumentParser(description="Validate fable markdown files")
    parser.add_argument("file", nargs="?", type=Path, help="Single fable file to validate")
    parser.add_argument("--all", action="store_true", help="Validate all fables")
    parser.add_argument("--category", help="Validate only a specific category")
    args = parser.parse_args()

    if args.file:
        v = FableValidator(args.file)
        v.validate()
        sys.exit(0 if v.report() else 1)

    if args.all or args.category:
        sys.exit(validate_all(args.category))

    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
