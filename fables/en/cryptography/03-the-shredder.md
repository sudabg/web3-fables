---
title: "The Shredder"
title_cn: "碎纸机"
concept: "Cryptographic Hash Function"
concept_cn: "密码学哈希函数"
category: "cryptography"
difficulty: "beginner"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/哈希函数与默克尔树.md"
tags: [cryptography, hash, keccak256, preimage, collision, deterministic]
---

# The Shredder

> *Whether you put in one page or a book, the output is always the same size of shreds. You cannot reconstruct the original from the shreds, but the same input always produces the same shreds.*

## The Story

In Yunzhou City's archives, there was a miraculous machine: the shredder.

The shredder's rules were quite special:

**First: any size of input, output is always fixed size.**

You put in one page, out came one hundred shreds. You put in a thousand-page book, out came one hundred shreds—no more, no less. Input could be infinitely large; output was always fixed.

**Second: same input always produces same output.**

If you put the same page through twice, the shred patterns were exactly the same. This seemed obvious, but in Yunzhou City's application scenarios, it was extremely important: it meant anyone could independently verify "this document was indeed processed by this machine."

**Third: output appears completely random.**

You changed one character in the input, and the shred pattern became completely different—bearing no resemblance to the original output. You could not infer input content from the output pattern.

**Fourth: impossible to find two different inputs producing the same output.**

Theoretically possible (because input is infinite while output is finite), but in practice, finding such two inputs required more attempts than the universe's lifetime. Yunzhou City's mathematicians called this "collision resistance."

---

**Shredder Applications**

The shredder had countless uses in Yunzhou City:

**Password verification**:
Yunzhou City's inns no longer stored guests' real passwords. When a guest first checked in, they spoke their password; the inn shredded the password, only saving the shred pattern. Next time the guest came, they spoke it again; the inn shredded it and compared patterns. If they matched, entry was granted.

The benefit: even if the inn's ledger was stolen, thieves only got a pile of shred patterns, unable to reverse-engineer original passwords.

**Document integrity**:
After merchants signed contracts, both parties shredded the full contract text, saving shred patterns. Later, if either party claimed "the contract was altered," the other could resubmit the contract to the shredder and compare patterns. If the pattern changed, the contract had indeed been modified.

**Addressing**:
Yunzhou City's library used shredders to number books. Not sequential numbering, but putting book contents into the shredder and using the output shred pattern as the book's number. Thus each book's number was unique and directly bound to its content. If book content was altered, the number would also change.

---

**Shredder Limitations**

The shredder was not omnipotent.

If the input "space" was small—like a password of only four digits—attackers could try all ten thousand combinations, finding the input that produced the target shred pattern. This was called "brute force."

So Yunzhou City required passwords to be at least twelve characters. Possible combinations became so large that brute force was impossible within the universe's lifetime.

Another limitation: the shredder could not distinguish "similar inputs." You put "agree" and "agree." (with an extra period) into the shredder separately, and the shred patterns were completely different—though to humans these two words meant almost the same thing.

---

## What This Fable Is About

This fable illustrates **cryptographic hash functions** (like Keccak-256, the hashing algorithm used by Ethereum). Hash functions map inputs of any length to fixed-length outputs (e.g., 32 bytes), with properties of determinism, collision resistance, and one-wayness.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Shredder | Hash function (Keccak-256) | Maps any input to a fixed-length output through a deterministic function |
| Any size input, fixed size output | Fixed output length | Keccak-256 always outputs 32 bytes regardless of input size |
| Same input, same output | Deterministic | Same input always produces same hash value; this is the foundation of verification |
| Change one character, output completely different | Avalanche Effect | Tiny input changes cause huge output changes |
| Cannot reverse-engineer input | One-wayness / Preimage Resistance | Deriving input from hash value is computationally infeasible |
| Collision resistance | Collision Resistance | Finding two different inputs producing the same hash value is computationally infeasible |
| Password verification | Password hash storage | Do not store plaintext passwords; only store hash values. Verify by recalculating and comparing hashes |
| Document integrity | Data integrity check | File hash value serves as fingerprint; any modification causes hash change |
| Library addressing | Content Addressing | IPFS, Swarm, etc. use content hash values as addresses |
| Four-digit password brute force | Weak input space | If input space is too small (e.g., short password), hash one-wayness cannot provide effective protection |
| Twelve-character requirement | Sufficiently large input space | Ensures brute force is computationally infeasible |

### Why This Story?

Hash functions are the cornerstone of cryptography and ubiquitous tools in blockchain—from address generation to transaction hashes to Merkle Trees. But their abstract nature makes it hard for many to understand "why the same input always produces the same output while looking completely random."

The "shredder" metaphor for hash functions offers several intuitive advantages:
1. **Fixed output**: Whether the book is thick or thin, shred count is fixed = hash length is fixed
2. **Determinism**: Same page shredded twice produces same result = hash determinism
3. **One-wayness**: Shreds cannot be reassembled into original paper = hash one-wayness
4. **Integrity check**: Compare shred patterns = compare hash values to verify data integrity

### Further Reading

- [wiki-web3: Hash Functions and Merkle Trees](../../wiki-web3/concepts/哈希函数与默克尔树.md)
- [Keccak Team: The Keccak Reference](https://keccak.team/files/Keccak-reference-3.0.pdf)
- [NIST: SHA-3 Standard](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
- [Ethereum: Accounts and Keys](https://ethereum.org/en/developers/docs/accounts/)
