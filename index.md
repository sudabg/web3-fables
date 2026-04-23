---
layout: home

hero:
  name: "Web3 Fables"
  text: "用寓言学习 Web3"
  tagline: 42 篇以中国古代为背景的寓言故事，将重入攻击、AMM、零知识证明、MEV 等复杂概念化为直觉
  image:
    src: /logo.svg
    alt: Web3 Fables
  actions:
    - theme: brand
      text: 开始阅读
      link: /fables/security/01-the-infinite-borrower
    - theme: alt
      text: 搜索寓言
      link: /site/search.html
    - theme: alt
      text: GitHub
      link: https://github.com/sudabg/web3-fables

features:
  - icon: 🛡️
    title: Security
    details: 重入攻击、整数溢出、MEV 抢跑、预言机操纵、蜜罐合约……6 篇寓言带你穿透攻击原理。
    link: /fables/security/01-the-infinite-borrower
  - icon: 🏗️
    title: Infrastructure
    details: 代理合约、账户抽象、跨链桥、Rollup、Gas 机制、数据可用性……7 篇故事讲清底层基建。
    link: /fables/infrastructure/02-the-theater-of-shadows
  - icon: 💰
    title: DeFi
    details: Uniswap V2/V3/V4、Aave、闪电贷、稳定币设计、0xSplits、MEV……7 篇叙事把公式变成剧情。
    link: /fables/defi/01-the-automated-market
  - icon: ⚙️
    title: EVM
    details: Storage Slot、Memory、Calldata、CREATE2、Delegatecall、EOF、Opcode……7 篇深入字节码世界。
    link: /fables/evm/01-the-numbered-lockers
  - icon: 🔐
    title: Cryptography
    details: Merkle Patricia Trie、ECDSA、哈希函数、ZK-SNARKs……4 篇把数学写成江湖传说。
    link: /fables/cryptography/01-the-proof-of-the-family-tree
  - icon: 🤝
    title: Consensus & Governance
    details: PoS、Slashing、Finality、Timelock、代币投票……5 篇解构权力与共识。
    link: /fables/consensus/01-the-stakers-roulette
  - icon: ☀️
    title: Solana
    details: SVM 并行架构、Rust 安全、账户模型与租金、PDA……4 篇走进高性能链的设计哲学。
    link: /fables/solana/01-the-assembly-line-workshop
  - icon: 🌍
    title: Bilingual
    details: 全部 42 篇寓言提供中英文双语版本，适合全球开发者阅读与分享。
    link: /fables/en/security/01-the-infinite-borrower
---

## 这是什么？

**Web3 Fables** 是一个开源的知识项目。我们相信：

> *最高级的理解，是能把一个概念讲成一个故事。*

每一篇寓言都在故事的末尾才揭示它真正要讲的 Web3 概念。阅读的过程不是被灌输定义，而是像侦探一样，在伏笔和隐喻中逐步逼近真相。

## 阅读方式

- **按分类浏览**：左侧侧边栏按 Security、DeFi、EVM 等 9 个领域组织。
- **按难度筛选**：入门 (beginner)、进阶 (intermediate)、高阶 (advanced)。
- **搜索**：点击右上角搜索框，或前往 [搜索页面](/site/search.html) 按标签/概念过滤。
- **英文版**：每篇寓言都有对应的英文翻译，点击页面底部的 "Next Fable" 或在侧边栏切换。

## 贡献

这是一个社区驱动的项目。如果你有一个想讲的概念，欢迎提交 PR：

1. 阅读 [贡献指南](https://github.com/sudabg/web3-fables#contributing)
2. 使用 `scripts/create-fable.py` 创建新寓言
3. 确保通过 `scripts/validate-fable.py` 校验
4. 提交 Pull Request

## 许可证

[MIT License](https://github.com/sudabg/web3-fables/blob/main/LICENSE)
