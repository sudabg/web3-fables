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
| [七道门](fables/security/02-the-seven-gates.md) | Solidity 常见安全漏洞 | 初级 |
| [伪造的秤](fables/security/03-the-counterfeit-scale.md) | 整数溢出攻击 | 中级 |
| [信使与拍卖行](fables/security/04-the-messenger-and-the-auction-house.md) | 抢跑攻击 | 中级 |
| [沼泽中的灯塔](fables/security/05-the-lighthouse-in-the-swamp.md) | 蜜罐合约 | 中级 |
| [风向旗的骗局](fables/security/06-the-weather-vane-deception.md) | 预言机操纵 | 高级 |
| [影之剧场](fables/infrastructure/02-the-theater-of-shadows.md) | 代理合约与可升级性 | 中级 |
| [无钥之城](fables/infrastructure/03-the-keyless-city.md) | 账户抽象 (ERC-4337) | 高级 |
| [回声工坊](fables/infrastructure/04-the-factory-of-echoes.md) | EIP-1167 最小代理 | 中级 |
| [雪崩后的账本](fables/infrastructure/05-the-ledger-after-the-avalanche.md) | 数据可用性 | 高级 |
| [压缩商队](fables/infrastructure/06-the-compressed-caravan.md) | Rollup / L2 扩容 | 中级 |
| [呼吸税](fables/infrastructure/07-the-breath-tax.md) | EVM Gas 机制 | 初级 |
| [自动市集](fables/defi/01-the-automated-market.md) | Uniswap V2 AMM | 中级 |
| [锚定之舟](fables/defi/02-the-anchored-vessel.md) | 现代稳定币设计 | 高级 |
| [当铺与保险库](fables/defi/03-the-pawnshop-and-the-vault.md) | Aave 借贷协议 | 中级 |
| [暗巷中的信使](fables/defi/04-the-messengers-in-the-alley.md) | MEV 与 Flashbots | 高级 |
| [深井与浅池](fables/defi/05-the-deep-well-and-the-shallow-pond.md) | Uniswap V3 集中流动性 | 高级 |
| [分水渠](fables/defi/06-the-water-dividers.md) | 0xSplits 收入拆分 | 中级 |
| [可编程市集](fables/defi/07-the-programmable-bazaar.md) | Uniswap V4 Hooks | 高级 |
| [编号柜](fables/evm/01-the-numbered-lockers.md) | EVM 存储布局与 Slot | 中级 |
| [工匠的工作台](fables/evm/02-the-craftsmans-workbench.md) | EVM 内存机制 | 中级 |
| [预言家的模具](fables/evm/03-the-prophets-mold.md) | CREATE2 预测地址 | 高级 |
| [借身还魂](fables/evm/04-the-soul-in-borrowed-body.md) | Delegatecall | 高级 |
| [新语法手册](fables/evm/05-the-new-grammar-manual.md) | EVM 对象格式 EOF | 高级 |
| [传令筒](fables/evm/06-the-message-tube.md) | EVM Calldata | 初级 |
| [符文石](fables/evm/07-the-runestones.md) | EVM 操作码与字节码 | 中级 |
| [家谱树的证明](fables/cryptography/01-the-proof-of-the-family-tree.md) | Merkle Patricia Trie | 高级 |
| [指纹印章](fables/cryptography/02-the-fingerprint-seal.md) | 椭圆曲线数字签名 | 中级 |
| [碎纸机](fables/cryptography/03-the-shredder.md) | 密码学哈希函数 | 初级 |
| [零知识洞穴](fables/cryptography/04-the-cave-of-zero-knowledge.md) | ZK-SNARKs | 高级 |
| [押注者的轮盘](fables/consensus/01-the-stakers-roulette.md) | PoS 共识机制 | 中级 |
| [失信者的烙印](fables/consensus/02-the-brand-of-the-faithless.md) | Slashing 惩罚机制 | 中级 |
| [不可撤销的印章](fables/consensus/03-the-irrevocable-seal.md) | 区块最终性 | 中级 |
| [冷却室](fables/governance/01-the-cooling-chamber.md) | 时间锁与治理 | 中级 |
| [砝码民主](fables/governance/02-the-weighted-democracy.md) | 代币投票治理 | 中级 |
| [流水线工坊](fables/solana/01-the-assembly-line-workshop.md) | Solana 架构与 SVM | 高级 |
| [铁匠的纪律](fables/solana/02-the-smiths-discipline.md) | Rust 安全编程 | 中级 |
| [计时保险箱](fables/solana/03-the-timed-safe.md) | Solana 账户模型与租金 | 中级 |
| [确定性门牌](fables/solana/04-the-deterministic-address.md) | Solana PDA | 高级 |
| [桥梁守卫](fables/infrastructure/08-the-bridge-guard.md) | 跨链桥 | 高级 |
| [独一无二的令牌](fables/other/01-the-non-fungible-token.md) | NFT | 初级 |
| [一日借款](fables/other/02-the-one-day-loan.md) | 闪电贷 | 中级 |

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
