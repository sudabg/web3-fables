---
title: "The Keyless City"
title_cn: "无钥之城"
concept: "Account Abstraction (ERC-4337)"
concept_cn: "账户抽象"
category: "infrastructure"
difficulty: "advanced"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/账户抽象erc-4337详解.md"
tags: [infrastructure, account-abstraction, erc-4337, smart-wallet, aa]
---

# The Keyless City

> *A city where you need no key to enter. Your face, your voice, or simply your reputation is enough.*

## The Story

In Yunzhou City, every house had a lock, and every lock had a key. Lose the key, and you could never enter again. There were no locksmiths. There was no "forgot my password" button.

This system was simple and secure—if you had the key. But it was unforgiving. A merchant who lost his key in the river had to build a new house. A widow whose husband had died with the key could never access the family vault.

Then the Keyless City was built.

In the Keyless City, houses had no locks. Instead, each house had a "guardian spirit"—a small, intelligent entity that decided who could enter based on rules set by the owner.

One house might say: "Let in anyone who knows the secret rhyme."
Another: "Let in anyone carrying the jade talisman."
Another: "Let in anyone approved by three of the ten council members."

The guardian spirit was not a physical lock. It was a piece of logic—rules encoded in language that anyone could understand.

---

## What This Fable Is About

This fable illustrates **Account Abstraction (ERC-4337)**—a proposal that turns Ethereum accounts from simple key-controlled addresses into smart contract wallets with programmable access rules, social recovery, and custom transaction logic.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Traditional lock and key | EOA (Externally Owned Account) | Controlled by a single private key; lose the key, lose the account |
| Keyless City | Smart Contract Wallet | An account controlled by code rather than a single key |
| Guardian spirit | Smart contract logic | Programmable rules determining who can authorize transactions |
| Secret rhyme | Password / multi-factor | Authentication beyond just a private key |
| Jade talisman | Hardware token / NFT | Ownership of a specific token can grant access |
| Council approval | Social recovery | Multiple guardians can collectively recover an account |
| No locksmiths | No centralized recovery | The system is self-sovereign; no third party can reset your access |

### Why This Story?

Account abstraction is the most important UX improvement in Ethereum's roadmap. The Keyless City metaphor makes the shift from "key = identity" to "rules = identity" viscerally clear.

### Further Reading

- wiki-web3: Account Abstraction ERC-4337 Explained
- [ERC-4337: Account Abstraction via Entry Point Contract](https://eips.ethereum.org/EIPS/eip-4337)
- [Vitalik: Soulbound Tokens and Account Abstraction](https://vitalik.eth.limo/general/2022/01/26/soulbound.html)
