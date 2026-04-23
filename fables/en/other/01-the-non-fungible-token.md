---
title: "The Non-Fungible Token"
title_cn: "独一无二的令牌"
concept: "NFT (Non-Fungible Token)"
concept_cn: "非同质化代币"
category: "other"
difficulty: "beginner"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/nft非同质化代币入门.md"
tags: [nft, non-fungible, ownership, digital-collectible, metadata, provenance]
---

# The Non-Fungible Token

> *Two identical gold coins can be exchanged, but two paintings never can.*

## The Story

Yunzhou City's mint produced two types of currency.

The first was **standard copper coins**. Each copper coin was identical—the same weight, same pattern, same value. You exchanged one copper coin for another copper coin; there was no difference. This was called "fungibility."

The second was **unique tokens**. Each token was different—bearing different patterns, representing different rights, belonging to different owners. You could not exchange one token for another, because they represented completely different things.

---

**Birth of Tokens**

Tokens were originally created to solve a specific problem: how to prove "ownership" in the digital world.

In the physical world, if you owned a painting, you hung it on the wall and everyone knew it was yours. But in the digital world, an image could be infinitely copied—copies and the original file were bitwise identical. Who owned the "original"?

Tokens solved this problem. They did not say "this file is yours" (because files could be copied), but said "this token represents a claim of ownership over something." The token itself could not be copied—like a property deed in the physical world that could not be copied (you could photocopy it, but the copy had no legal effect).

---

**Three Core Properties of Tokens**

**First: uniqueness.**

Each token had a globally unique number. Two tokens might have similar patterns, but numbers were never the same. This number was written on the public ledger; anyone could look it up.

**Second: public ownership.**

Who currently owned the token was written on the public ledger. No need to ask anyone, no need for any proof; the ledger itself was proof. If you wanted to transfer the token to someone else, you only needed to update the record on the ledger—from your name to theirs.

**Third: traceable history.**

From minting to the present, every transfer of the token was recorded on the ledger. You could trace a token's complete history—who minted it, who bought it, who sold it, and at what price each time. This was called "provenance."

---

**Uses of Tokens**

**Digital art**:
Artists bound works to tokens. Buyers bought not the image file (files could be copied) but the token—representing "I am the official owner of this work." Although anyone could save image copies, only the token holder owned "recognized ownership."

**Game items**:
A legendary sword in a game was represented by a token. This sword could be transferred between different games—because the token did not depend on any single game's server. If the game company shut down, players still owned the token and could use it in other games supporting the token.

**Membership**:
A token represented "lifetime membership to a certain club." The club did not need to maintain a membership database—the ledger itself was the database. When the token was transferred, membership automatically transferred.

**Identity credentials**:
A token represented "you attended a certain event" or "you hold a certain degree." The credential issuer signed the token; anyone could verify the signature's authenticity.

---

**Limitations of Tokens**

Tokens are not omnipotent.

- Tokens represent ownership but do not automatically grant copyright. You bought an NFT, but that does not mean you obtained commercial usage rights for the work—unless the issuer explicitly granted them.
- Token value depends entirely on community consensus. If the community no longer recognizes a token's value, it becomes a meaningless string of numbers.
- Tokens themselves store numbers and ownership records; the "thing itself" (e.g., image files) is usually stored elsewhere (e.g., IPFS or centralized servers). If that place shuts down, the token you own may point to a broken link.

---

Years later, tokens became part of Yunzhou City's digital life. A collector said: "Tokens did not change the essence of 'ownership'—ownership has always been a social consensus. Tokens only wrote that consensus on an immutable ledger, making lies harder."

---

## What This Fable Is About

This fable illustrates **NFT (Non-Fungible Token)**—a token standard on blockchain (e.g., ERC-721, ERC-1155) representing unique assets. NFT's core value lies in providing digital scarcity and verifiable ownership history.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Standard copper coins | Fungible Token (ERC-20) | Interchangeable tokens; each unit is identical |
| Unique tokens | NFT (ERC-721 / ERC-1155) | Each token has a unique ID; not interchangeable |
| Digital images infinitely copyable | Digital content easy to copy | Files can be perfectly copied; traditional methods cannot distinguish "original" from "copy" |
| Tokens cannot be copied | Blockchain uniqueness guarantee | Each NFT's ID is unique within its contract; cannot be forged |
| Property deed photocopy | NFT ownership meaning | Owning NFT does not equal owning copyright unless contract explicitly authorizes |
| Public ledger | Blockchain / distributed ledger | Ownership records are public and transparent; immutable |
| Ledger update | Transfer | Changing ownerOf by calling contract's transfer function |
| Traceable history | Provenance | Blockchain records NFT's complete transaction history from minting to present |
| Game items cross-games | Interoperability / metaverse assets | NFTs are not bound to single platforms; can be used in different applications supporting the standard |
| Membership | Token-gated access | Holding specific NFT grants access to content, communities, or functions |
| Images stored elsewhere | Off-chain metadata | NFT metadata (images, descriptions, etc.) is usually stored on IPFS or centralized servers; only URI is stored on-chain |
| Link broken | Link rot / metadata failure | If off-chain storage fails, NFT may point to empty links |

### Why This Story?

NFT is one of Web3's most mainstream concepts, but many people misunderstand its essence—the "owning a JPG" meme is typical. Understanding NFT's true value (verifiable ownership, provenance, interoperability) is crucial for transcending hype.

The "unique token" metaphor for NFT offers several intuitive advantages:
1. **Fungible vs. non-fungible comparison**: Copper coins vs. tokens = ERC-20 vs. ERC-721
2. **Essence of ownership**: Ownership is social consensus = NFT's value depends on community recognition
3. **Value of provenance**: History traceable = blockchain provenance's unique value
4. **Honest limitations**: Does not represent copyright; may point to failed links = NFT's true boundaries

### Further Reading

- [wiki-web3: NFT Non-Fungible Token Introduction](../../wiki-web3/concepts/nft非同质化代币入门.md)
- [ERC-721 Standard](https://eips.ethereum.org/EIPS/eip-721)
- [ERC-1155 Multi-Token Standard](https://eips.ethereum.org/EIPS/eip-1155)
- [OpenSea: What is an NFT?](https://opensea.io/learn/nft/what-is-nft)
- [The Non-Fungible Token Bible](https://opensea.io/blog/articles/non-fungible-tokens/)
