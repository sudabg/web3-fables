---
title: "The Deterministic Address"
title_cn: "确定性门牌"
concept: "Program Derived Address (PDA)"
concept_cn: "程序派生地址"
category: "solana"
difficulty: "advanced"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/solana-pda程序派生地址详解.md"
tags: [solana, pda, deterministic-address, program-derived, bump, canonical]
---

# The Deterministic Address

> *The address is not randomly assigned, but determined by the house's owner and its purpose.*

## The Story

Yunzhou City's address system underwent a revolution.

---

**Old Addresses: Random Assignment**

Under the old system, addresses were randomly assigned. When you built a new house, the authorities gave you a random address number. You could not predict what number you would get, nor could you choose.

This system had problems:
1. If you wanted to tell others your address before the house was built, you couldn't—because you did not yet know the address number.
2. If you rebuilt the house (e.g., after a fire), the new house might get a completely different address. All previously registered addresses would become invalid.
3. Two different houses would never get the same address—ensuring uniqueness, but also meaning addresses had no pattern whatsoever.

---

**New Addresses: Deterministic Assignment**

Under the new system, addresses were no longer random. They were determined by two factors:

1. **Who the house's owner is**
2. **What the house is used for**

Specific rules:
- Address = Hash(Owner's Identity + House's Purpose + "Salt")

Where salt is an adjustment number—if the first calculated address was already occupied, change the salt, recalculate, until finding an empty address.

This meant: as long as you knew who the owner was and what the house was used for, you could calculate its address before the house was built.

---

**Addresses Without Private Keys**

Deterministic addresses had a peculiar property: they were not in the traditional address sequence.

Under the old system, every address corresponded to a key—only the key holder could open the door. Under the deterministic address system, some addresses were outside the traditional sequence—they had no corresponding keys.

This sounded dangerous: a door without a key—could anyone open it?

No. Doors without keys could only be opened by "the house's program."

Specific rules:
- If an address was deterministic (not in the traditional sequence), no one could directly open it with a key.
- Only the house's owner (through their program) could apply to the authorities: "Please open my house used for such-and-such purpose."
- The authorities checked: does the applicant's identity + house's purpose indeed correspond to this address? If so, the authorities opened the door.

This meant: deterministic address security did not come from "who has the key" but from "who can prove to the authorities that this house indeed belongs to them."

---

**Applications of Deterministic Addresses**

**Predicting addresses**:
A merchant wanted to open a chain of tea houses. Before building the first tea house, he could calculate all future tea house addresses—because he knew he was the owner and knew the purpose was "Tea House No. N." He could print business cards and register contracts in advance without waiting for houses to be built.

**Address mapping**:
Yunzhou City's household registration system used deterministic addresses to establish "one-to-many" relationships. For example: a large family had a main address (traditional address); all family members' addresses were derived from this main address—Hash(Main Address + "Eldest Son"), Hash(Main Address + "Second Daughter"). Thus, knowing the main address allowed calculating all family members' addresses.

**Seedless control**:
Some public facilities (like public wells, roads) used deterministic addresses. These facilities had no private owners but were controlled by public programs. Anyone could apply to the program to use the facility; the program decided whether to allow based on rules. Because facilities had no private keys, no one could "steal" them—they belonged to no one, only to the program.

---

**The Art of Salt**

Deterministic address calculation involved a key variable: salt.

Theoretically, Hash(Owner + Purpose) should directly produce an address. But sometimes, this address happened to fall in the traditional address sequence—meaning it might already be occupied by someone else (because traditional addresses had keys).

When this happened, the system automatically decremented salt from 255 and recalculated Hash until finding an address not in the traditional sequence.

This "finding valid salt" process was deterministic—given the same owner and purpose, the system always found the same salt. So addresses were still deterministic; only the calculation process was slightly more complex.

---

Years later, all new buildings in Yunzhou City used deterministic addresses. An urban planner said: "Deterministic addresses transformed addresses from 'random identifiers' into 'meaningful names.' An address is no longer just a string of numbers; it encodes the building's identity, purpose, and history."

---

## What This Fable Is About

This fable illustrates **Solana's Program Derived Address (PDA)**—a deterministically generated account address derived from program address and seeds. PDAs are not on the Ed25519 curve's public key space, so they have no corresponding private keys and can only be signature-controlled by the generating program through CPI (Cross-Program Invocation).

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Old random addresses | Traditional public key addresses | Generated from private key through Ed25519; random and unpredictable |
| New deterministic addresses | PDA | `findProgramAddress([seeds], program_id)` deterministically generates addresses |
| Owner's identity | Program ID | PDA calculation includes deployer address, ensuring different programs' PDA spaces do not conflict |
| House's purpose | Seeds | Arbitrary byte arrays for distinguishing different PDAs generated by the same program |
| Salt | Bump (nonce) | Decremented from 255 to 0, finding a valid value making PDA not on Ed25519 curve |
| Not in traditional sequence | PDA has no corresponding private key | PDA is not on elliptic curve; no private key; cannot be externally signed |
| Door without key | PDA has no external signature | Only the program generating the PDA can "sign" for the PDA through CPI |
| Program applies to authorities | Cross-Program Invocation (CPI) | Solana programs can call other programs and provide signatures for derived PDAs |
| Authorities check | Runtime verification | Solana runtime verifies CPI calls are legitimate, ensuring only correct programs can sign for PDAs |
| Chain tea houses | Deterministic address prediction | Can predict PDA addresses before account creation for pre-configuration and referencing |
| Household mapping | One-to-many relationship modeling | One main account can derive multiple child accounts, establishing hierarchical structures |
| Public facilities without owners | PDA for program-controlled state | PDAs can be fully controlled by programs for storing program states, configurations, etc. |

### Why This Story?

PDA is one of Solana development's most core and unique concepts. It allows programs to "own" accounts, control states, and establish deterministic address relationships—things without direct equivalents in EVM.

The "deterministic address" metaphor for PDA offers several intuitive advantages:
1. **Determinism**: Given owner and purpose, address is always the same = PDA deterministic generation
2. **No private key**: No key; only program can open = PDA has no external signature, only program CPI control
3. **Salt**: Adjustment number finding valid address = bump seed search process
4. **Applications**: Predicting addresses, one-to-many mapping, program-controlled states = PDA practical use cases

### Further Reading

- wiki-web3: Solana PDA Program Derived Address Deep Dive
- [Solana Docs: Program Derived Addresses](https://docs.solana.com/developing/programming-model/calling-between-programs#program-derived-addresses)
- [Anchor Framework: PDA](https://www.anchor-lang.com/docs/features/pda)
- [Solana PDA Deep Dive](https://solana.com/developers/cookbook/accounts/pda)
