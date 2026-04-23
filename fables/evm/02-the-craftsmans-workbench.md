---
title: "The Craftsman's Workbench"
title_cn: "工匠的工作台"
concept: "EVM Memory Mechanism"
concept_cn: "EVM 内存机制"
category: "evm"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/evm-内存机制深入解析.md"
tags: [evm, memory, mload, mstore, mszie, temporary, expansion]
---

# The Craftsman's Workbench

> *"工作台越大，干活越贵。但每次干完活，桌子会自动清空。"*

## 故事

云州城的工坊里，每个工匠都有一张工作台。工作台的规矩非常特别：

**第一，工作台是临时的。**

工匠开始干活时，工作台是空的。他在上面摆放工具、零件、半成品。干完活，他把成品搬走——工作台自动清空，什么都不留下。下一个工匠来，面对的又是一张全新的空桌子。

这意味着：工作台上的东西不能过夜。今天画的图纸、做的记号，明天就不存在了。

**第二，工作台可以扩展。**

工作台一开始很小，只够放几样工具。如果工匠需要更大的空间，他可以把桌子往两边拉。但拉桌子是有代价的——每多拉一寸，就需要多交一寸的"扩展税"。

而且扩展税不是线性的。第一张桌子从三尺拉到四尺，很便宜。但从一百尺拉到一百零一尺，贵得惊人。因为工坊的地板空间是稀缺资源，占用越大，边际成本越高。

**第三，工作台是线性的。**

工匠不能在桌子的任意位置放东西。他必须从左到右依次摆放：先把东西放在最左边，然后依次向右。如果他想跳过中间的空位，直接把东西放在右边——可以，但他必须先"声明"中间的空位属于自己，这也要交税。

**第四，工作台是公共的。**

当工匠需要请另一个工坊的师傅帮忙时，他不能把师傅请到自己的工坊——他必须把自己的工作台"复制"一份，送到对方的工坊。师傅在这张复制的桌子上干活，干完把结果送回来。原工坊的工作台不受影响。

---

有个聪明的年轻工匠，他发现工作台的这些特性后，设计了一套极其高效的工作流程：

1. 每次开工前，先在桌角记下"当前已用长度"——就像船上的吃水线。
2. 干活过程中，只在必要的范围内扩展桌子。
3. 干完活，把吃水线之前的东西全部清掉，让桌子回到初始状态。

这套流程让他交的扩展税只有其他工匠的三分之一。

但有一个陷阱很多人踩过：有人觉得"反正桌子会自动清空"，就在桌上留下了一些"以为以后还会用到"的东西。结果下次开工时，发现桌子确实是空的——那些东西不在了。他不得不重新计算、重新摆放，反而更浪费时间。

老工匠的忠告是："工作台上只能放'这次干活需要的东西'。如果你想保存什么，把它刻到石头上（storage），而不是留在桌子上（memory）。"

---

## 这则寓言在说什么

这则寓言对应的是 **EVM 的内存（Memory）机制**。Memory 是 EVM 执行期间的临时数据区域，按字节寻址，线性扩展，每次消息调用后重置。

### 关键映射

| 故事元素 | 技术概念 | 说明 |
|---------|---------|------|
| 工作台 | EVM Memory | 合约执行期间的临时数据区域，用于存储动态大小的数据 |
| 临时性 | Memory 的生命周期 | Memory 中的数据只在当前消息调用期间存在。调用结束后自动清空 |
| 可扩展 | Memory expansion | Memory 是动态扩展的。写入超出当前大小的地址时，memory 会自动扩展，消耗 gas |
| 扩展税 | Memory expansion gas cost | Memory 扩展的 gas 成本 = `memory_size_word^2 / 512 + 3 * memory_size_word`。是二次成本，扩展越大越贵 |
| 线性摆放 | Memory 的线性地址空间 | Memory 从地址 0 开始，按顺序写入。MSTORE/MLOAD 操作按 32 字节 word 为单位 |
| 吃水线 | 空闲内存指针（Free Memory Pointer） | Solidity 编译器在 memory 开头维护一个指针，记录当前已用 memory 的末尾位置，避免重复计算 |
| 请外援 | 外部合约调用（CALL） | 调用外部合约时，EVM 会为被调用者创建新的 execution context，拥有独立的 memory。返回时原 memory 不受影响 |
| 复制工作台 | CALL 的 memory 传递 | 调用外部合约时，需要把输入数据复制到 memory 中传递给被调用者。返回数据也需要 memory 空间 |
| 刻到石头上 | Storage vs Memory | Storage 是持久的但昂贵，Memory 是临时的但便宜。数据该存哪里取决于是否需要持久化 |
| 以为以后还会用到 | Memory 中的数据不持久 | 如果在 memory 中缓存了数据，期望下次调用还能用——不可能。每次调用 memory 都是全新的 |

### 为什么是这个故事？

Storage 和 Memory 的区别是 Solidity 开发者最早需要理解的核心概念之一，但"临时 vs 持久"的抽象对初学者来说很模糊。

用"工作台"来隐喻 Memory，有几个直觉优势：
1. **临时性**：干完活桌子自动清空——对应了 memory 的生命周期
2. **扩展成本**：拉桌子越来越贵——对应了 memory expansion 的二次 gas 成本
3. **外部调用**：把桌子复制到对方工坊——对应了 CALL 时的 memory 隔离和传递成本

### 延伸阅读

- [wiki-web3 概念原文：EVM 内存机制深入解析](../../wiki-web3/concepts/evm-内存机制深入解析.md)
- [EVM Deep Dives: Memory](https://noxx3xxon.notion.site/noxx3xxon/EVM-Deep-Dives-61b5e3e045e2482aa4e112d97823d37d)
- [Ethereum Yellow Paper: Memory](https://ethereum.github.io/yellowpaper/paper.pdf)
