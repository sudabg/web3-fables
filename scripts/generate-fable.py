#!/usr/bin/env python3
"""
generate-fable.py — 从 wiki-web3 概念自动生成寓言草稿

用法:
    python scripts/generate-fable.py --list-unmapped
    python scripts/generate-fable.py --source PATH --output PATH [--model MODEL]
    python scripts/generate-fable.py --batch --limit N

环境变量:
    OPENAI_API_KEY    如需调用 LLM API 生成草稿
"""

import argparse
import os
import re
import sys
import yaml
from pathlib import Path
from typing import Optional

# 项目根目录
ROOT = Path(__file__).resolve().parent.parent
WIKI_ROOT = Path.home() / "wiki-web3"
FABLES_DIR = ROOT / "fables"
CONCEPTS_CATALOG = ROOT / "concepts-catalog.md"

# 生成寓言的核心提示词模板（与项目创始人提供的提示词一致）
FABLE_PROMPT_TEMPLATE = """你是一位精通 Web3 技术的寓言作家。你的任务是将一个 Web3 概念改写为一则寓言故事。

## 叙事契约（必须严格遵守）

1. **延迟揭示**：不要在故事前三分之一明确提及任何区块链术语。读者应在阅读过程中逐渐"猜到"映射关系。
2. **有角色，有动机**：角色不只是概念的传声筒。他们有自己的利益和盲点，这些盲点恰好对应技术中的常见误解。
3. **有冲突，有代价**：故事中的错误决策必须带来可感知的后果，让读者"痛"到记住这个教训。
4. **完整映射**：故事中的每个核心设定都必须在注解中有对应的技术概念。
5. **故事长度**：1500-3000 字。
6. **故事之后**：必须包含一个"这则寓言在说什么"的解释章节（500-1000 字），包含关键映射表、为什么是这个故事、延伸阅读。

## 输出格式

使用以下 frontmatter 开头：

---
title: "English Title"
title_cn: "中文标题"
concept: "{concept_en}"
concept_cn: "{concept_cn}"
category: "{category}"
difficulty: "intermediate"
author: "your-name"
created: "{date}"
sources:
  - "{source_path}"
tags: [{tags}]
---

# English Title

> *"一句点题的引语，可选。"*

## 故事

[写寓言故事，1500-3000 字]

---

## 这则寓言在说什么

[解释概念，500-1000 字]

### 关键映射

| 故事元素 | 技术概念 | 说明 |
|---------|---------|------|
| ... | ... | ... |

### 为什么是这个故事？

[解释隐喻选择理由]

### 延伸阅读

- [wiki-web3 概念原文]({source_path})

## 来源概念

{concept_content}

请基于以上概念，创作一则高质量的寓言故事。输出完整的 Markdown 文件内容，不需要任何额外解释。
"""


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """提取 frontmatter 和正文。"""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not match:
        return {}, text
    try:
        meta = yaml.safe_load(match.group(1))
    except Exception:
        meta = {}
    return meta, match.group(2)


def guess_category(concept_path: Path) -> str:
    """根据概念文件路径或内容猜测类别。"""
    name = concept_path.name.lower()
    pmap = {
        "reentrancy": "security",
        "security": "security",
        "hack": "security",
        "audit": "security",
        "vulnerability": "security",
        "proxy": "infrastructure",
        "upgrade": "infrastructure",
        "delegatecall": "infrastructure",
        "account abstraction": "infrastructure",
        "erc-4337": "infrastructure",
        "rollup": "infrastructure",
        "bridge": "infrastructure",
        "amm": "defi",
        "uniswap": "defi",
        "lending": "defi",
        "aave": "defi",
        "mev": "defi",
        "oracle": "defi",
        "gas": "evm",
        "storage": "evm",
        "memory": "evm",
        "opcode": "evm",
        "evm": "evm",
        "solidity": "evm",
        "yul": "evm",
        "pos": "consensus",
        "pow": "consensus",
        "consensus": "consensus",
        "fork": "consensus",
        "validator": "consensus",
        "zk": "cryptography",
        "merkle": "cryptography",
        "signature": "cryptography",
        "cryptography": "cryptography",
        "dao": "governance",
        "governance": "governance",
        "vote": "governance",
        "solana": "solana",
        "svm": "solana",
        "spl": "solana",
        "anchor": "solana",
    }
    for key, cat in pmap.items():
        if key in name:
            return cat
    return "infrastructure"  # 默认


def list_unmapped() -> list[Path]:
    """列出 wiki-web3 中尚未被映射为寓言的概念。"""
    if not WIKI_ROOT.exists():
        print(f"[ERROR] wiki-web3 not found at {WIKI_ROOT}")
        return []

    # 收集已有寓言的来源
    mapped_sources: set[str] = set()
    for fable_file in FABLES_DIR.rglob("*.md"):
        text = fable_file.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(text)
        for src in meta.get("sources", []):
            mapped_sources.add(src.replace("../../", "").replace("../", ""))

    # 扫描 wiki-web3 概念
    concepts_dir = WIKI_ROOT / "concepts"
    unmapped: list[Path] = []
    for concept_file in sorted(concepts_dir.glob("*.md")):
        rel = f"wiki-web3/concepts/{concept_file.name}"
        if rel not in mapped_sources:
            unmapped.append(concept_file)

    return unmapped


def generate_fable(source: Path, output: Path, dry_run: bool = False) -> str:
    """生成寓言草稿。如果配置了 LLM API，则调用 API；否则输出提示词到 stdout。"""
    content = source.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(content)

    concept_cn = meta.get("title", source.stem)
    concept_en = source.stem.replace("-", " ").replace("_", " ")
    category = guess_category(source)
    tags = ", ".join(f'"{t}"' for t in meta.get("tags", [category]))
    from datetime import date
    today = date.today().isoformat()
    rel_source = f"wiki-web3/concepts/{source.name}"

    prompt = FABLE_PROMPT_TEMPLATE.format(
        concept_en=concept_en,
        concept_cn=concept_cn,
        category=category,
        date=today,
        source_path=rel_source,
        tags=tags,
        concept_content=content[:8000],  # 截断避免过长
    )

    if dry_run:
        print("=" * 60)
        print("PROMPT PREVIEW (first 2000 chars):")
        print("=" * 60)
        print(prompt[:2000])
        print("\n...")
        return ""

    # 优先尝试调用 OpenAI API
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        try:
            import openai
            client = openai.OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model=os.getenv("FABLE_MODEL", "gpt-4.1"),
                messages=[
                    {"role": "system", "content": "你是一位精通 Web3 的寓言作家。你输出完整的 Markdown 文件，不加任何额外解释。"},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.8,
                max_tokens=6000,
            )
            draft = response.choices[0].message.content or ""
            if not draft.strip():
                raise RuntimeError("Empty response from LLM")
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(draft, encoding="utf-8")
            print(f"[OK] Draft written to {output}")
            return draft
        except Exception as e:
            print(f"[WARN] LLM call failed: {e}")
            print("[INFO] Falling back to prompt-only mode...")

    # 回退：将提示词写入文件，供人工使用
    prompt_file = output.with_suffix(".prompt.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    prompt_file.write_text(prompt, encoding="utf-8")
    print(f"[OK] Prompt written to {prompt_file}")
    print(f"[INFO] No API key found. Set OPENAI_API_KEY to auto-generate drafts.")
    return ""


def main():
    parser = argparse.ArgumentParser(description="Generate fable drafts from wiki-web3 concepts")
    parser.add_argument("--list-unmapped", action="store_true", help="List concepts not yet mapped to fables")
    parser.add_argument("--source", type=Path, help="Path to wiki-web3 concept markdown file")
    parser.add_argument("--output", type=Path, help="Output path for generated fable")
    parser.add_argument("--dry-run", action="store_true", help="Print prompt preview without calling API")
    parser.add_argument("--batch", action="store_true", help="Batch generate for all unmapped concepts (dry run only)")
    parser.add_argument("--limit", type=int, default=10, help="Limit for batch mode")
    args = parser.parse_args()

    if args.list_unmapped:
        unmapped = list_unmapped()
        print(f"Unmapped concepts: {len(unmapped)}\n")
        for p in unmapped[:50]:
            print(f"  - {p.name}")
        if len(unmapped) > 50:
            print(f"  ... and {len(unmapped) - 50} more")
        return

    if args.batch:
        unmapped = list_unmapped()
        for p in unmapped[:args.limit]:
            out = FABLES_DIR / guess_category(p) / f"{p.stem}.md"
            print(f"\n[GEN] {p.name} -> {out}")
            generate_fable(p, out, dry_run=True)
        return

    if args.source and args.output:
        generate_fable(args.source, args.output, dry_run=args.dry_run)
        return

    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
