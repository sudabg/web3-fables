---
title: "The Breath Tax"
title_cn: "呼吸税"
concept: "EVM Gas Mechanism"
concept_cn: "EVM Gas 机制"
category: "infrastructure"
difficulty: "beginner"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/evm-gas-机制与手续费详解.md"
tags: [infrastructure, evm, gas, fee, opcode, pricing]
---

# The Breath Tax

> *In this city, every breath is taxed. The deeper you breathe, the more you pay.*

## The Story

In Yunzhou City, there was an unusual tax: the breath tax. Every inhabitant paid a small fee for each breath they took. The fee was tiny—fractions of a copper coin per breath—but it added up.

The tax was not arbitrary. It was calculated based on how much work your breathing caused the city. A shallow breath, barely noticeable, cost almost nothing. A deep, lung-filling breath that required the city's bellows to pump harder cost significantly more.

Some activities required many deep breaths. Running a mile might cost a hundred breaths. Lifting a heavy stone might cost fifty. Standing still, breathing shallowly, might cost only one.

The city used the breath tax revenue to pay the workers who maintained the air pumps. Without the tax, the pumps would stop, and the city would suffocate.

But the tax also served another purpose: it prevented waste. A prankster who wanted to run around the city square blowing a horn all day would face an enormous breath tax bill. The tax made frivolous activity economically unviable, preserving the city's air for those who truly needed it.

---

## What This Fable Is About

This fable illustrates the **EVM Gas mechanism**—the pricing system that charges users for computational resources consumed by their transactions, preventing spam and ensuring network sustainability.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Breath tax | Gas fee | Every EVM operation consumes gas; users pay for total gas consumed |
| Shallow breath | Cheap operation | Simple operations like ADD cost 3 gas |
| Deep breath | Expensive operation | Complex operations like SSTORE (storage write) cost 20,000 gas |
| Running a mile | Complex transaction | A transaction with many operations consumes more gas |
| Air pump workers | Validators / miners | Gas fees compensate validators for processing and securing transactions |
| Prankster blowing horn | Spam / DoS attack | High gas costs make spam and denial-of-service attacks economically prohibitive |
| Breath tax prevents waste | Gas as resource control | Gas limits ensure the network is not overwhelmed by computation |

### Why This Story?

Gas is the most fundamental concept in Ethereum UX. The breath tax makes the abstract idea of "paying for computation" viscerally intuitive.

### Further Reading

- wiki-web3: EVM Gas Mechanism and Fees Explained
- [Ethereum.org: Gas and Fees](https://ethereum.org/en/developers/docs/gas/)
- [EVM Opcodes and Gas Costs](https://www.evm.codes/)
