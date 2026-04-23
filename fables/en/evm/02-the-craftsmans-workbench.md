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

> *The larger the workbench, the more expensive the work. But after each job, the table automatically clears itself.*

## The Story

In the workshops of Yunzhou City, every craftsman had a workbench. The workbench's rules were quite peculiar:

**First: the workbench is temporary.**

When a craftsman began work, the bench was empty. He laid out tools, parts, half-finished pieces. When the job was done, he removed the finished product—and the bench automatically cleared itself, leaving nothing behind. The next craftsman faced a brand-new empty table.

This meant: nothing on the workbench could stay overnight. Today's drawings, today's markings, would not exist tomorrow.

**Second: the workbench could expand.**

The bench started small, barely holding a few tools. If a craftsman needed more space, he could pull the table wider. But pulling the table had a cost—every extra inch required paying an "expansion tax."

And the expansion tax was not linear. Stretching from three feet to four was cheap. But stretching from one hundred feet to one hundred one was shockingly expensive. Because workshop floor space was a scarce resource; the more you occupied, the higher the marginal cost.

**Third: the workbench was linear.**

A craftsman could not place items at arbitrary positions. He had to arrange them from left to right: first placing things at the far left, then progressively to the right. If he wanted to skip the empty middle and place something on the right—he could, but he had to first "claim" the middle empty space as his own, which also required paying tax.

**Fourth: the workbench was public.**

When a craftsman needed help from a master in another workshop, he could not invite the master to his own workshop—he had to "copy" his workbench and send it to the other workshop. The master worked on this copied table and sent the results back. The original workshop's workbench was unaffected.

---

A clever young craftsman discovered these properties and designed an extremely efficient workflow:

1. Before starting each job, mark the "current used length" at the table corner—like a ship's waterline.
2. During work, only expand the table within necessary limits.
3. After finishing, clear everything before the waterline, returning the table to its initial state.

This workflow cost him only one-third the expansion tax of other craftsmen.

But one trap many fell into: some thought "the bench auto-clears anyway," and left things on it "thinking they might use them later." Next time they started work, they found the bench was indeed empty—those things were gone. They had to recalculate and rearrange, wasting more time.

The old craftsman's advice was: "Only put 'things needed for this job' on the workbench. If you want to save something, carve it into stone (storage), not leave it on the table (memory)."

---

## What This Fable Is About

This fable illustrates the **EVM Memory mechanism**. Memory is EVM's temporary data area during execution, byte-addressable, linearly expandable, and reset after each message call.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Workbench | EVM Memory | Temporary data area during contract execution for storing dynamically sized data |
| Temporariness | Memory lifecycle | Data in memory exists only during the current message call. Automatically cleared after call ends |
| Expandable | Memory expansion | Memory expands dynamically. Writing beyond current size triggers automatic expansion, consuming gas |
| Expansion tax | Memory expansion gas cost | Memory expansion cost = `memory_size_word^2 / 512 + 3 * memory_size_word`. Quadratic cost; larger expansion is more expensive |
| Linear arrangement | Memory linear address space | Memory starts at address 0 and is written sequentially. MSTORE/MLOAD operate in 32-byte word units |
| Waterline | Free Memory Pointer | The Solidity compiler maintains a pointer at memory's start, recording the end of currently used memory to avoid redundant calculation |
| Calling external help | External contract call (CALL) | Calling an external contract creates a new execution context with independent memory. Original memory is unaffected upon return |
| Copying workbench | CALL memory passing | When calling an external contract, input data must be copied to memory for the callee. Return data also requires memory space |
| Carving into stone | Storage vs Memory | Storage is persistent but expensive; memory is temporary but cheap. Data destination depends on whether persistence is needed |
| Thinking they'd use it later | Memory data is not persistent | If you cache data in memory expecting to use it next call—impossible. Each call starts with fresh memory |

### Why This Story?

Storage and Memory are among the first core concepts Solidity developers must understand, but the abstraction of "temporary vs persistent" is vague for beginners.

The "workbench" metaphor for memory offers several intuitive advantages:
1. **Temporariness**: After work, the table auto-clears—corresponding to memory's lifecycle
2. **Expansion cost**: Pulling the table wider is increasingly expensive—corresponding to memory expansion's quadratic gas cost
3. **External calls**: Copying the table to another workshop—corresponding to CALL's memory isolation and passing costs

### Further Reading

- [wiki-web3: EVM Memory Mechanism Deep Dive](../../wiki-web3/concepts/evm-内存机制深入解析.md)
- [EVM Deep Dives: Memory](https://noxx3xxon.notion.site/noxx3xxon/EVM-Deep-Dives-61b5e3e045e2482aa4e112d97823d37d)
- [Ethereum Yellow Paper: Memory](https://ethereum.github.io/yellowpaper/paper.pdf)
