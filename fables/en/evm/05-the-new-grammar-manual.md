---
title: "The New Grammar Manual"
title_cn: "新语法手册"
concept: "EVM Object Format (EOF)"
concept_cn: "EVM 对象格式"
category: "evm"
difficulty: "advanced"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/evm对象格式eof初步了解.md"
tags: [evm, eof, container, validation, bytecode, section]
---

# The New Grammar Manual

> *The old writing had no punctuation. The new manual divides sentences into chapters.*

## The Story

Yunzhou City's legal documents had a five-hundred-year tradition: all documents were continuous rolls of parchment, without paragraphs, without headings, without punctuation. Judges had to read from beginning to end to know whether a document was a contract, a lawsuit, or a will.

This tradition brought three problems.

---

**First Problem: Unable to Quickly Identify**

When a courier delivered a new document to the court, the judge could not tell at a glance what type of document it was. He had to unroll the parchment and read from the beginning until discovering keywords—like "hereby" or "witness"—before judging the document type.

If someone maliciously disguised a poison recipe as a contract (writing a contract-like opening, then suddenly turning into a poison recipe midway), the judge would only discover something was wrong halfway through. But by then it might be too late—certain actions had already been executed based on the misread first half.

---

**Second Problem: Unable to Verify Integrity**

Parchment could be worm-eaten, water-damaged, or cut. If a document's ending was missing, the judge could not easily discover this—because he did not know how long the original document should have been. He could only read to where it "suddenly ended," then guess: was this how it originally ended, or was the ending missing?

Some cunning lawyers would deliberately delete unfavorable final clauses from contracts, then present the truncated contracts in court. Judges could not distinguish whether this was originally a short contract or a truncated long contract.

---

**Third Problem: Inefficient Execution**

The court's executors (responsible for carrying out document contents) had to read the entire document line by line from the first line. They could not skip any paragraph, because they did not know which paragraph was relevant.

If a document's first half was background introduction ("Party A is a Yunzhou City resident, Party B is an Eastern Sea merchant..."), executors had to read all this background before reaching the truly important execution clauses. This greatly wasted time.

---

**The New Grammar Manual Revolution**

A young judge named Zhang Jie proposed an entirely new document format: "chaptered documents."

Chaptered documents were no longer continuous rolls of parchment. They were explicitly divided into several parts:

1. **Type declaration** (first page): Explicitly stating "this is a contract" or "this is a lawsuit." The judge knew how to handle it the moment he received the document.
2. **Header information** (second page): Listing basic document information—author, date, version. Metadata could be obtained without unrolling the full text.
3. **Body** (from third page): The actual content, clearly divided into paragraphs, each with a heading.
4. **Verification page** (last page): A special text generated through mathematical operations on the full text. If any page of the document was altered, the verification page would not match, and the judge would immediately know the document had been tampered with.

More critically: before being sent to court, chaptered documents had to pass a "format reviewer's" inspection. The reviewer did not look at document content, only whether the format was correct—whether the type declaration came first, whether the verification page was complete, whether chapters had clear separators.

If format review failed, the document never reached the judge. This meant: all documents reaching judges had correct format, complete structure, and were not truncated.

---

**Unexpected Benefits**

After chaptered documents were introduced, judges discovered unexpected benefits:

1. **Execution became faster.** Executors no longer needed to read the entire document. If it was an "execution order," they could flip directly to the "execution clauses" chapter, skipping the preceding background.

2. **Errors were easier to find.** If a lawyer tried to insert an "automatic transfer" clause into a contract, the format reviewer would notice this clause was not among the allowed chapter types and reject the document outright.

3. **Version compatibility.** New-format documents could be executed in old courts (old courts could still read continuous text), but new courts could fully utilize chaptered advantages. This was a gradual upgrade, not a revolutionary break.

---

Years later, all legal documents in Yunzhou City adopted the chaptered format. Someone asked Judge Zhang Jie: "What is your greatest contribution?"

Zhang Jie said: "I did not invent any new content. I gave documents 'structure.' In the old format, content and structure were mixed, inseparable. In the new format, structure is visible, verifiable, and optimizable. Once structure is made explicit, many things naturally improve."

---

## What This Fable Is About

This fable illustrates **EVM Object Format (EOF)**—a new bytecode container format being introduced to Ethereum. EOF transforms EVM bytecode from a "flat continuous byte sequence" into a "structured container" containing type declarations, header metadata, code sections, data sections, and introduces pre-deployment validation.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Continuous parchment roll | Traditional EVM bytecode | Flat byte sequence; no structure; EVM interprets byte by byte |
| Unable to quickly identify type | Cannot distinguish code/data | Traditional bytecode mixes code and data; JUMP targets require runtime resolution |
| Poison recipe disguised as contract | Malicious bytecode / code injection | Can embed executable code in data sections, or jump to arbitrary locations via JUMP to execute unintended logic |
| Unable to verify integrity | Cannot statically verify | Traditional bytecode cannot have its completeness and security verified without execution |
| Inefficient execution | JUMP parsing overhead | EVM needs to calculate JUMP targets at runtime; cannot pre-optimize execution paths |
| Chaptered document | EOF container format | Bytecode is organized as structured containers: magic number + version + header + code sections + data section |
| Type declaration | EOF header type information | Explicitly declares the contract's number of code segments, data segment size, and other metadata |
| Verification page | EOF built-in verification | Container format checksum/length fields ensuring bytecode has not been truncated or tampered with |
| Format reviewer | Pre-deployment EOF validation | EOF contracts must pass static validation before deployment, ensuring correct structure, legal JUMP targets, safe stack depth, etc. |
| Format failure means no court | Invalid EOF cannot be deployed | Bytecode not conforming to EOF format is rejected at deployment |
| Execution faster | EOF performance optimization | Because structure is known, EVM can precompile and optimize execution paths without runtime JUMP parsing |
| Gradual upgrade | EOF coexists with old bytecode | EOF is opt-in; old bytecode remains compatible; new contracts can choose to use EOF |

### Why This Story?

EOF is one of the longest and most complex improvements in the EVM ecosystem, involving changes to the underlying execution model. For those unfamiliar with EVM internals, "bytecode container format" sounds extremely abstract.

The "chaptered document" metaphor for EOF offers several intuitive advantages:
1. **Visualization of structure**: From "a roll of parchment" to "a document divided into chapters"—letting readers understand the core value of a "container format"
2. **Safety improvement**: The format reviewer intercepts problems before documents reach judges—corresponding to EOF's pre-deployment validation
3. **Source of performance optimization**: Executors flipping directly to relevant chapters—corresponding to optimizations EOF can make by knowing code structure in advance

### Further Reading

- wiki-web3: EVM Object Format EOF Introduction
- [EIP-3540: EOF - EVM Object Format v1](https://eips.ethereum.org/EIPS/eip-3540)
- [EIP-3670: EOF - Code Validation](https://eips.ethereum.org/EIPS/eip-3670)
- [EIP-4200: EOF - Static relative jumps](https://eips.ethereum.org/EIPS/eip-4200)
- [EVM Object Format (EOF) Overview](https://notes.ethereum.org/@ipsilon/evm-object-format-overview)
