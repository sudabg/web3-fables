---
title: "The Message Tube"
title_cn: "传令筒"
concept: "EVM Calldata"
concept_cn: "EVM Calldata"
category: "evm"
difficulty: "beginner"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/evm-内存机制深入解析.md"
tags: [evm, calldata, msg.data, read-only, external-call, encoding]
---

# The Message Tube

> *A tube that can only be read, never written. Words passed to others that you yourself cannot change.*

## The Story

Yunzhou City's communication system had three ways to deliver messages.

---

**First: Oral Messages**

The oldest method was direct oral delivery. You walked up to someone and spoke. They heard what they heard.

Oral messages were simple and direct. The downside: if you wanted to tell someone a hundred names, you had to recite them one by one. What if they could not remember? You had to recite again.

And oral messages could not be "passed on"—you could not have a friend relay your oral message to a third person. Oral messages only worked between speaker and listener.

---

**Second: Letters**

You wrote a letter, put it in an envelope, and gave it to a courier. The courier delivered it to the recipient, who opened and read it.

Letters could carry complex content—a hundred names could be written on paper without omission. Letters could also be forwarded—the recipient could pass the original letter to someone else.

But letters had a cost: writing required paper and ink; delivery required courier payment. And once sent, the content could not be changed. If you wanted to modify, you had to write a new letter.

---

**Third: Message Tubes**

Yunzhou City's army used a special communication tool: message tubes.

A message tube was a sealed copper pipe containing a slip of paper. The paper's content was fixed when placed in the tube—anyone could open the tube and read the paper's content, but no one could modify it.

Message tubes had three unique properties:

**First: read-only.**

The recipient could only read the tube's content, not add, modify, or delete words. If the general's order was "advance ten miles," the paper in the tube always said these four characters. The recipient could not change it to "advance twenty miles."

**Second: transparently public.**

The tube had no lock. Anyone passing by could open and read the content. In the army, this was not a problem—the orders themselves did not need secrecy, only needed to ensure they were not tampered with.

**Third: single-use.**

After reaching its destination, the tube completed its mission. The paper inside could be copied and archived, but the tube itself was not reused. Next time a message was sent, a new tube was used.

---

**Message Tubes' Ingenious Use: Remote Command**

Yunzhou City's general was stationed on the northern frontier; the emperor was in the capital. The emperor wanted to command the general to do something, but he could not personally travel to the frontier to deliver oral orders. He could write a letter, but letters could be intercepted or altered en route.

The message tube solved this problem: the emperor wrote the order on paper, placed it in the tube, and sealed it. The courier transported the tube, not a bare letter. Along the way, anyone could open the tube to read the order (transparent), but no one could modify the order without breaking the seal (tamper-proof).

After receiving the tube, the general opened it, read the order, and executed it. During execution, the general could cross-reference the tube's order to confirm he had not misunderstood.

---

**Limitations of Message Tubes**

But message tubes also had limitations.

If the emperor wanted the general to "flexibly decide based on frontline conditions," message tubes were insufficient—because tube orders were fixed; the general could not request real-time instructions from the emperor. He could only execute according to the received order after getting the tube.

If the order contained large amounts of data—like "here is a list of five hundred names; please distribute grain according to the list"—the tube could hold the list (because it was paper), but if the general needed to input these names one by one into a ledger, he had to manually copy them. The tube's data could not be directly "imported" into the ledger; it could only be read.

---

## What This Fable Is About

This fable illustrates **EVM Calldata**—read-only data carried in transactions or message calls. Calldata is external call input data, stored in the transaction body, cannot be modified by the called contract, and can only be read via `msg.data` or function parameters.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Oral message | Internal call / local computation | Internal function calls within a contract; data passes on stack and memory without serialization |
| Letter | Memory / Storage | Writable data storage areas that can be modified and passed |
| Message tube | Calldata | Read-only data from external calls, transmitted with the transaction; called contracts can only read, not modify |
| Read-only | Calldata immutability | `calldata` location data cannot be modified. Solidity parameters marked `calldata` are read-only |
| Transparently public | Calldata publicity | Transaction data is public to the entire network; anyone can read via blockchain explorer |
| Single-use | Calldata lifecycle | Calldata exists only during the current message call; inaccessible after call ends |
| Sealed copper pipe | Transaction integrity | After a transaction is signed, calldata cannot be tampered with (otherwise signature verification fails) |
| Remote command | Cross-contract call | Contract A calls Contract B, passing function selector and parameters via calldata |
| Large data in tube | Calldata capacity | Calldata can carry large data (e.g., arrays, strings), but reading and parsing require gas |
| Manual copying | Calldata to Memory/Storage copy | If you need to modify calldata, you must first copy it to memory or storage |
| Cannot request real-time instructions | Calldata unidirectionality | In a single call, calldata is one-way. The callee cannot modify calldata and return it to the caller |

### Why This Story?

Calldata is one of EVM's three main data locations (storage, memory, calldata), but its "read-only" and "external" properties confuse many beginners.

The "message tube" metaphor for calldata offers several intuitive advantages:
1. **Read-only**: Tubes can only be read, not modified—corresponding to calldata immutability
2. **Externality**: Tubes are for remote communication—corresponding to calldata existing only in external calls
3. **Transparency**: Anyone can open and read—corresponding to the public nature of on-chain transactions

### Further Reading

- [wiki-web3: EVM Memory Mechanism Deep Dive](../../wiki-web3/concepts/evm-内存机制深入解析.md)
- [Solidity Docs: Data Location](https://docs.soliditylang.org/en/latest/types.html#data-location)
- [Ethereum Yellow Paper: Message Call](https://ethereum.github.io/yellowpaper/paper.pdf)
- [ABI Encoding Specification](https://docs.soliditylang.org/en/latest/abi-spec.html)
