# 链上寓言 / Web3 Fables

> 用故事理解 Web3。每个概念，一则寓言。
>
> *Learn Web3 through stories. One concept, one fable.*

---

## 这是什么？

Web3 领域充斥着抽象概念、数学证明和难以直觉理解的安全陷阱。传统的技术文档告诉你**"是什么"**，但很少让你感受到**"为什么是这样"**。

**链上寓言**是一个开源项目，将 Web3 核心概念改写为独立成篇的寓言故事。每则寓言遵循统一的叙事契约：

1. **先讲故事** —— 一个完整的、自洽的虚构世界，直到结尾读者才逐渐意识到它在映射哪个技术概念。
2. **后作注解** —— 在故事之后明确点出概念，并用对照表逐层拆解故事元素与技术实现的映射关系。
3. **标注来源** —— 每则寓言链接回 `wiki-web3` 中对应的概念原文，方便读者深入技术细节。

## 项目结构

```
web3-fables/
├── fables/                  # 寓言正文
│   ├── consensus/           # 共识机制：PoW, PoS, BFT, 分叉选择
│   ├── defi/                # 去中心化金融：AMM, 借贷, 预言机, MEV
│   ├── security/            # 安全：重入, 抢跑, 预言机操纵, 权限绕过
│   ├── evm/                 # EVM 底层：Gas, 存储布局, 内存, 操作码
│   ├── cryptography/        # 密码学：ZK, Merkle 树, 签名, 阈值密码
│   ├── governance/          # 治理：DAO, 投票机制, 委托治理
│   ├── infrastructure/      # 基础设施：Rollup, 桥, 账户抽象, 代理合约
│   └── solana/              # Solana 生态：SVM, 账户模型, Staking
├── templates/
│   └── fable-template.md    # 贡献者模板
├── scripts/
│   ├── generate-fable.py    # 从 wiki-web3 概念自动生成寓言草稿
│   └── validate-fable.py    # 结构校验与质量门禁
├── concepts-catalog.md      # wiki-web3 概念 → 寓言映射目录
└── README.md
```

## 阅读示例

| 寓言 | 概念 | 难度 |
|------|------|------|
| [无限借贷者](fables/security/01-the-infinite-borrower.md) | 重入攻击 (Reentrancy) | 中级 |
| [影之剧场](fables/infrastructure/02-the-theater-of-shadows.md) | 代理合约与可升级性 | 中级 |
| [无钥之城](fables/infrastructure/03-the-keyless-city.md) | 账户抽象 (ERC-4337) | 高级 |

## 快速开始（贡献者）

```bash
# 1. 克隆仓库
git clone https://github.com/your-username/web3-fables.git
cd web3-fables

# 2. 查看待写概念
python scripts/generate-fable.py --list-unmapped

# 3. 基于 wiki 概念生成草稿
python scripts/generate-fable.py \
  --source "wiki-web3/concepts/solidity-重入攻击与防御.md" \
  --output fables/security/04-the-ghost-in-the-vault.md

# 4. 手动精修后校验
python scripts/validate-fable.py fables/security/04-the-ghost-in-the-vault.md
```

详细贡献指南见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 叙事契约（必须遵守）

1. **延迟揭示**：不要在故事前三分之一明确提及任何区块链术语。读者应在阅读过程中逐渐"猜到"映射关系。
2. **完整映射**：故事中的每个核心设定都必须在注解中有对应的技术概念。不允许"为了文学性而虚设情节"。
3. **概念准确**：故事可以被简化，但不能歪曲技术原理。如果为了叙事流畅牺牲了准确性，必须在注解中明确标注。
4. **双语友好**：每则寓言包含英文标题和中文标题，正文语言由作者选择，但鼓励提供对照版本。

## 自动化流水线

- **概念映射**：`concepts-catalog.md` 自动追踪 wiki-web3 中的概念覆盖度。
- **生成辅助**：`generate-fable.py` 读取 wiki 概念，结合提示词模板输出初稿。
- **质量门禁**：`validate-fable.py` 检查 frontmatter、字数、映射表完整性。
- **CI 检查**：PR 自动运行校验脚本，确保格式合规。

## 许可

MIT License — 故事属于所有人，知识不设围墙。

---

> *"技术文档告诉你规则，寓言让你理解规则背后的恐惧与欲望。"*
