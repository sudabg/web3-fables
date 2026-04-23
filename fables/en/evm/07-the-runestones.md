---
title: "The Runestones"
title_cn: "符文石"
concept: "EVM Opcodes & Bytecode"
concept_cn: "EVM 操作码与字节码"
category: "evm"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/solidity汇编与内存布局优化.md"
tags: [evm, opcode, bytecode, assembly, instruction, stack-machine]
---

# The Runestones

> *Each stone bears only one character, but arranged in the correct order, they can build a city.*

## The Story

In Yunzhou City's construction sites, no blueprints were used. Craftsmen used an ancient system: runestones.

Each runestone was a palm-sized rock with a symbol carved on it. There were few symbol types—only about two hundred. But these two hundred symbols, arranged in different orders, could express the construction method of any building.

---

**How Runestones Worked**

At the center of the construction site stood a large stone platform that could hold only thirty-two runestones at once. This was the platform's physical limit—no more could fit.

The craftsman's workflow was:

1. He retrieved runestones from the warehouse and placed them on the platform in order.
2. When the platform held enough runestones for a certain operation, an action was automatically triggered.
3. After the action completed, the runestones on the platform were replaced by the action's result.
4. He continued placing new runestones, triggering the next action.

For example:
- Operation "add": required two runestones on the platform (e.g., "3" and "5"). When triggered, both stones were removed and replaced by a new stone "8."
- Operation "duplicate": required one stone on the platform. When triggered, the stone was duplicated; now there were two identical stones on the platform.
- Operation "swap": required at least two stones on the platform. When triggered, the top two stones exchanged positions.

---

**Translation of Runestones**

High-level architects never dealt directly with runestones. They used a language called "blueprint language" to design buildings—"build a wall here, ten feet high, two feet wide."

Then, a specialized "translator" converted blueprint language into runestone sequences. This process was deterministic: the same blueprint always produced the same runestone sequence.

But translation was not one-to-one. A single line like "wall ten feet high" might be translated into dozens of runestone operations—calculating area, checking load-bearing, allocating materials. The translator also optimized: if the blueprint repeatedly said "wall ten feet high," the translator would not translate it three times but cache the result for reuse.

---

**Direct Runestone Manipulation**

Some extremely precise buildings could not be accurately expressed in blueprint language. At these times, master-level craftsmen directly wrote runestone sequences.

Direct manipulation advantages:
- **Precise**: Every stone's position was under the craftsman's control; no translator ambiguity.
- **Efficient**: The translator added many checks for safety; direct manipulation could skip unnecessary checks, saving time and materials.
- **Access hidden functions**: Blueprint language only exposed common operations, but some special operations could only be used by directly manipulating runestones.

Risks were equally obvious:
- If a craftsman reversed the order of two stones, the entire building might collapse.
- If a craftsman forgot to clear the platform after a certain step, the platform would fill up, and subsequent operations could not proceed.
- If a craftsman used a "self-destruct" rune—a special stone that could make the entire construction site disappear—the consequences were irreversible.

---

**Immutability of Runestones**

Once a runestone sequence was carved and delivered to the construction site, it could not be changed. If the architect discovered a design flaw, the only option was to carve a new runestone sequence and discard the old.

This meant: runestone writing required extreme caution. A small error—like confusing "add" with "subtract"—could produce completely wrong results, and could not be corrected on-site.

---

Years later, Yunzhou City's tallest tower was built with runestones. Its designer was a master who directly manipulated runestones. He said: "Blueprint language lets ordinary people build houses. But if you want to build a tower touching the clouds, you must understand the meaning of every single stone."

---

## What This Fable Is About

This fable illustrates **EVM Opcodes and Bytecode**. EVM is a stack-based virtual machine; all smart contracts are ultimately compiled into bytecode—a sequence of opcode instructions. Solidity is a high-level language; the compiler translates it into EVM bytecode.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Runestones | EVM bytecode / opcodes | Each opcode is one byte (or more); EVM interprets and executes them one by one |
| About two hundred symbols | ~150 valid opcodes | EVM defines about 150 opcodes covering arithmetic, logic, storage, calls, environment info, etc. |
| Platform holds thirty-two stones | EVM stack depth limit | EVM stack maximum depth is 1024 256-bit words. Exceeding causes stack overflow |
| Operation "add" | ADD opcode | Pops two values from stack top, adds them, pushes result back to stack top. All EVM computation occurs on the stack |
| Operation "duplicate" | DUP opcode | Duplicates a value from the stack to the stack top |
| Operation "swap" | SWAP opcode | Exchanges positions of top two stack values |
| Blueprint language | Solidity / Vyper and other high-level languages | Developers write contracts in high-level languages; compiler translates to EVM bytecode |
| Translator | Solidity compiler (solc) | Translates high-level language to EVM bytecode and optimizes |
| Translation optimization | Compiler optimization | Constant folding, dead code elimination, loop optimization, etc. |
| Direct runestone manipulation | Inline assembly (Yul / Inline Assembly) | Developers can directly write opcode sequences for more precise control and higher efficiency |
| Access hidden functions | Assembly accesses底层 | Certain EVM features (e.g., fine-grained `create2` control, memory layout optimization) can only be accessed via assembly |
| Platform filled | Stack too deep error | Too many local variables in a Solidity function cause stack depth to exceed 16-slot compiler limit |
| Self-destruct rune | SELFDESTRUCT opcode | Destroys contract, sends balance to specified address; irreversible |
| Carved, cannot be changed | Deployed bytecode is immutable | After contract deployment, code cannot be modified (unless using proxy contract pattern) |

### Why This Story?

EVM bytecode and opcodes are smart contracts' "final form," but most developers only write Solidity and never directly look at bytecode. Understanding "what lies beneath the high-level language" is crucial for debugging, optimization, and security auditing.

The "runestones" metaphor for bytecode offers several intuitive advantages:
1. **Stack machine concretized**: Platform = stack; placing stones = push; operations = pop and compute
2. **Compilation process visualized**: Blueprint → translator → runestones = Solidity → solc → bytecode
3. **Value of assembly**: Direct runestone manipulation = inline assembly; precise but dangerous

### Further Reading

- wiki-web3: Solidity Assembly and Memory Layout Optimization
- [EVM Opcodes Reference](https://www.evm.codes/)
- [Ethereum Yellow Paper](https://ethereum.github.io/yellowpaper/paper.pdf)
- [Solidity Inline Assembly](https://docs.soliditylang.org/en/latest/assembly.html)
- [EVM Deep Dives by noxxx3xxon](https://noxx3xxon.notion.site/noxx3xxon/EVM-Deep-Dives-61b5e3e045e2482aa4e112d97823d37d)
