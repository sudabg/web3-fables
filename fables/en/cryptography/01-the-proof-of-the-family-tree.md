---
title: "The Proof of the Family Tree"
title_cn: "家谱树的证明"
concept: "Merkle Patricia Trie"
concept_cn: "Merkle Patricia Trie"
category: "cryptography"
difficulty: "advanced"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/merkle-patricia-trie-explained.md"
tags: [cryptography, merkle, trie, proof, state, verification]
---

# The Proof of the Family Tree

> *You do not need to unfold the entire genealogy; only a leaf and a path are needed to prove you belong to this family.*

## The Story

Yunzhou City's household registration system preserved genealogies for all one hundred thousand families in the city. The genealogy was not a book but a giant family tree—starting from the founding ancestor, each generation branching out, eventually reaching every living person.

Traditionally, if someone wanted to prove "Zhang San belongs to this family," the authorities needed to unfold the entire family tree, tracing from the founding ancestor all the way to Zhang San. This was manageable with hundreds of people, but with one hundred thousand, each proof required flipping through thousands of pages of parchment.

A mathematician named Meike invented a new proof method.

---

**Reorganization of the Family Tree**

Meike transformed the family tree into a "hash family tree."

The rules were:
1. Every person had a "name hash"—their name run through a mathematical formula to produce a unique digital fingerprint.
2. Each pair of parents' name hashes were added together and run through the same formula to produce a "family hash."
3. Each pair of grandparents' family hashes were added to produce a "clan hash."
4. Layer by layer upward, eventually producing a "tree root hash"—a unique fingerprint representing the entire family tree.

The tree's marvelous property was: the tree root hash contained all information of the entire tree. If any person's name was altered, all hashes from that person to the root path would change, and the tree root hash would change.

---

**Meike's Proof**

Now, to prove he was a family member, Zhang San did not need to unfold the entire tree. He only needed to provide two things:

1. **His own name**
2. **A "path"**—from himself to the root, the hash values of siblings at each layer

The verifier took these two items, started from Zhang San's name, and successively added the sibling hashes from the path, calculating upward layer by layer. If the final calculated tree root hash matched the authorities' recorded tree root hash, the proof passed.

If Zhang San lied, claiming to be a family member when he was not, he would either:
- Provide a fake name—but verification would not produce the correct tree root hash.
- Forge a sibling hash on the path—but hashes were mathematically computed and could not be forged.

Most critically: the verifier did not need to know who the other ninety-nine thousand nine hundred ninety-nine family members were. He only needed the small path Zhang San provided—usually only dozens of hash values—to complete verification.

---

**Patricia Compression**

Meike later made an optimization: he discovered the family tree had many "only children"—a family with one child, who had one child, with single inheritance continuing for over a dozen generations.

In the traditional family tree, each of these dozen generations occupied a separate layer, wasting much space. Meike's optimization was: compress consecutive single inheritance into one layer. For example, "Zhang San → Zhang Si → Zhang Wu → Zhang Liu" (all only sons) compressed into "Zhang San → Zhang Liu," skipping the middle three generations.

This greatly reduced tree depth and the path length required for proofs.

---

**Applications of the Family Tree**

The hash family tree found wide application in Yunzhou City:

- **Household verification**: proving whether someone belonged to Yunzhou City.
- **Property registration**: proving a piece of land was indeed registered under someone's name, without needing to review all land records.
- **Transaction records**: proving a transaction had indeed occurred, without downloading the entire ledger.

In transaction record applications, the accountant treated each transaction as a leaf of the family tree. The tree root hash updated every minute, posted at the city gate. Anyone wanting to prove "a transaction indeed occurred this minute" only needed to provide the transaction's path—dozens of bytes—to let any passerby verify.

---

## What This Fable Is About

This fable illustrates **Merkle Patricia Trie (MPT)**—the core data structure Ethereum uses to store account states, transactions, receipts, and other data. MPT combines Merkle Tree (verifiability) and Patricia Trie (compression efficiency), allowing extremely small "proofs" to verify whether a key-value pair exists in a massive state tree.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Family tree | Merkle Patricia Trie | Ethereum's state tree storing all account states, contract code, storage, etc. |
| Name hash | Keccak256 hash | Keys (e.g., account addresses) are hashed to determine their positions in the tree |
| Family hash / clan hash | Internal node hashes | Each node's hash = combination of its child node hashes; layered upward |
| Tree root hash | State Root / Merkle Root | A 32-byte hash representing the entire tree state; stored in block headers |
| Meike's proof | Merkle Proof | Proving a leaf exists in the tree only requires providing sibling node hashes on the path from leaf to root |
| No need to unfold entire tree | Light client verification | Light nodes do not need to download all states; only block headers and Merkle proofs are needed to verify a specific state |
| Single child compression | Patricia Trie compression | If there are no branches on a path (only one child node), Patricia Trie compresses the path, reducing tree depth |
| Property registration | Account state proof | Can prove an address's balance, nonce, codeHash, storageRoot |
| Transaction records | Transaction receipt proof | Can prove a transaction was indeed included in a specific block |
| Ledger | Blockchain state | The entire collection of Ethereum world states |

### Why This Story?

Merkle Tree is the cornerstone of blockchain scalability—without it, light clients would be impossible. But the concepts of "tree" and "proof" are very abstract for non-technical readers.

The "family tree" metaphor for MPT offers several intuitive advantages:
1. **Path proof visualization**: Leaf to root path = descendant-to-ancestor bloodline chain
2. **Compression intuition**: Consecutive single inheritance compression = Patricia Trie path compression
3. **Light client value**: Not needing to know all family members = light nodes not needing to download all states

### Further Reading

- wiki-web3: Merkle Patricia Trie Explained
- [Ethereum Wiki: Patricia Tree](https://eth.wiki/en/fundamentals/patricia-tree)
- [Merkle Trees and SPV](https://bitcoin.org/en/glossary/merkle-tree)
- [EVM Deep Dives: State Trie](https://noxx3xxon.notion.site/noxx3xxon/EVM-Deep-Dives-61b5e3e045e2482aa4e112d97823d37d)
