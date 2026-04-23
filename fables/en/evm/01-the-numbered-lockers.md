---
title: "The Numbered Lockers"
title_cn: "编号柜"
concept: "EVM Storage Layout & Slot"
concept_cn: "EVM 存储布局与 Slot"
category: "evm"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/solidity私有数据的链上透明性与slot存储机制.md"
tags: [evm, storage, slot, layout, packing, optimization]
---

# The Numbered Lockers

> *You think secrets locked in a cabinet are safe, but the cabinet itself stands in the middle of the hall.*

## The Story

In Yunzhou City's administrative hall stood a vast wall lined with countless numbered lockers—from number 0 to infinity. Each locker held exactly thirty-two characters, no more, no less.

Anyone could walk up to this wall, open any locker, and read its contents. No locks, no passwords. The numbered lockers' design philosophy was: transparency.

---

**Locker Rules**

The hall administrator established strict storage and retrieval rules:

1. Each locker had a fixed size: thirty-two characters. If an item was smaller than thirty-two characters, multiple items could be packed into the same locker. This was called "packing."
2. If an item exceeded thirty-two characters, it had to occupy consecutive lockers.
3. The administrator placed items in order: locker 0, locker 1, locker 2...
4. Once an item was placed in a locker, it could not be moved. Unless you actively cleared the locker, its contents remained there forever.

A shrewd merchant stored his trade secrets in the lockers—his cost prices, his client lists, his secret codes. He thought locking them in cabinets made them safe.

But he forgot: the lockers had no doors. Anyone who knew the number could open and read them.

One day, a competitor walked into the hall, opened locker 3—there was the merchant's cost price. Opened locker 4—the client list. Opened locker 5—the secret code.

The merchant collapsed: "This is my privacy!"

The administrator replied coldly: "The hall's rules are transparency. You should have known this when you put them in."

---

**The Art of Packing**

Clever storers learned "packing."

The locker size was thirty-two characters. If you had two sixteen-character items, you could pack them into one locker—left sixteen, right sixteen. This way you occupied only one locker, not two.

But packing had a subtle limitation: items had to be arranged from largest to smallest. If you placed an eight-character item first, then tried to fit a twenty-four-character item—the remaining space was insufficient. But if you placed the twenty-four-character item first, then the eight-character one, it fit perfectly.

An experienced storage consultant made a fortune from this. His job was to help clients optimize packing order, allowing the same number of items to occupy the fewest lockers. Each locker saved meant one less storage tax paid.

---

**Dynamic Lockers**

Some storers needed to store quantities that were not fixed—like a constantly growing list. The administrator designed "dynamic lockers" for them:

- The list's contents were not placed directly in numbered lockers, but in another place called the "hall warehouse."
- The numbered locker only held a pointer—an address telling you where to find the actual list.
- When the list grew, the warehouse automatically expanded. The pointer in the numbered locker never changed.

This design's cost was: every time you read the list, you had to first read the pointer in the numbered locker, then go to the warehouse to find the actual contents. Slower than direct storage, but more flexible.

---

**The Trap of Clearing**

A common misconception: take an item out of a locker, and the locker is empty.

No. In the world of numbered lockers, "clearing" meant setting the locker's contents to zero. But the locker itself remained, its number remained, it still occupied wall space, and you still had to pay storage tax for it.

The only exception: if you created a locker, then zeroed it, the administrator would refund part of your storage tax as a reward for "releasing space."

---

Years later, a traveler from a foreign land stood before the wall of numbered lockers and said something that was carved into the wall: "This is not storage. This is nakedness."

---

## What This Fable Is About

This fable illustrates the **EVM Storage Layout and Slot mechanism**. EVM storage is a massive key-value mapping where each slot is 32 bytes (256 bits). Solidity packs data into slots in declaration order, and all stored data is visible to everyone on-chain.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Wall of numbered lockers | EVM Storage | Each contract has a storage space of 2^256 slots; each slot is 32 bytes |
| Thirty-two characters | 32 bytes / 256 bits | The fixed size of a storage slot |
| No locks, transparent | On-chain data is publicly readable | Any data in `storage` can be read by anyone via `eth_getStorageAt` |
| Trade secrets read | Storage is not private | Many beginners mistakenly believe `private` variables are secret; they are only restricted at the Solidity level, fully transparent on-chain |
| Packing | Storage Packing | Solidity attempts to pack multiple small variables (e.g., multiple `uint128`) into one slot to save gas |
| Packing order limitation | Packing rules | Variables are placed in slots in declaration order. Poor ordering (e.g., `uint8` before `uint256`) causes unnecessary slot waste |
| Dynamic lockers | Dynamic arrays and mappings | `mapping` and dynamic `array` use keccak256 hashing to calculate slot positions; data is stored in "hash space" rather than sequential slots |
| Pointer | Hash value in slot | A mapping's slot does not store actual data, only a seed for calculating offsets |
| Clearing | `delete` / zeroing | Setting a slot to zero refunds some gas (15,000 gas refund), but the slot still exists in state |
| Storage tax | SSTORE gas cost | First write to non-zero costs 20,000 gas; modification costs 5,000 gas; zeroing refunds 15,000 gas |

### Why This Story?

"On-chain data is public" is one of the most counterintuitive facts in Web3. Many developers mistakenly believe `private` variables are secure, leading to serious vulnerabilities (like the famous Parity wallet bug).

The "numbered lockers" metaphor for storage offers several intuitive advantages:
1. **Visualization of transparency**: Lockers have no doors; anyone can open them—corresponding to the complete publicity of on-chain data
2. **Packing concretized**: Packing data into fixed-size slots is like packing items into fixed-size lockers
3. **Gas cost intuition**: Creating lockers (SSTORE) is expensive, reading is cheap, clearing gives refunds—corresponding to EVM's gas pricing logic

### Further Reading

- wiki-web3: Solidity Private Data On-Chain Transparency and Slot Storage
- [EVM Deep Dives: Storage Layout](https://noxx3xxon.notion.site/noxx3xxon/EVM-Deep-Dives-61b5e3e045e2482aa4e112d97823d37d)
- [Solidity Docs: Storage Layout](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html)
