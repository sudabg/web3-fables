---
title: "The Prophet's Mold"
title_cn: "预言家的模具"
concept: "CREATE2 Predictable Contract Address"
concept_cn: "CREATE2 预测合约地址"
category: "evm"
difficulty: "advanced"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/create2-创建合约预测合约地址看这一篇就够了.md"
tags: [evm, create2, deterministic-address, salt, factory, counterfactual]
---

# The Prophet's Mold

> *Before the object is cast, you already know exactly where it will appear.*

## The Story

In Yunzhou City, blacksmiths had a tradition: whenever someone commissioned a blade, the smith forged it and engraved a serial number on the hilt. The number was random—depending on which blade number was reached that day. Buyers only knew which blade was theirs after it was forged.

This tradition had operated for three hundred years until a young smith named Shen Suan proposed a bold idea.

---

**Old Method: Random Numbers**

The old method's problems were obvious:

1. Buyers could not know the blade's exact serial number in advance. If a buyer needed to assemble the blade with other components, he had to wait until the blade was forged before starting assembly.
2. If the smithy relocated or the smith changed, the serial number sequence might be interrupted, causing conflicts.
3. Buyers could not "reserve" a number. If they wanted to ensure their blade was number 777, they could only pray that the day happened to reach that number.

---

**New Method: The Prophet's Mold**

Shen Suan designed a "prophet's mold." The mold's marvelous property was: before the blade was cast, you could accurately predict its final serial number.

The prophecy formula was carved on the mold itself:

**Blade Number = Hash(Mold Number + Material Recipe + Salt)**

Where:
- Mold number was fixed—each mold was born with a unique, unchangeable number.
- Material recipe was chosen by the buyer himself—different recipes produced different blades.
- Salt was an arbitrary number—the buyer could freely choose it to "adjust" the final number.

This meant: before the blade was cast, anyone could plug these three parameters into the formula and calculate the blade's number. No need to wait for forging, no need to trust the smith, no need for any prophecy.

---

**Applications of the Prophet's Mold**

This invention sparked a revolution in Yunzhou City.

**First application: advance assembly.**

A scabbard craftsman needed to make a custom scabbard for a commissioned blade. Under the old method, he had to wait for the blade to be forged and know its serial number before starting—because the scabbard had to match a specific blade.

Under the new method, the buyer knew the blade's number when placing the order. The scabbard craftsman could start making the matching scabbard while the blade was still in the furnace. When the blade was forged, the scabbard was also complete.

**Second application: state channels.**

Two merchants needed to establish a "joint account" in Yunzhou City to manage their transactions. Under the old method, they had to first establish the account, then start trading.

But under the new method, they could "prophesy" the account's number before establishing it, then sign a contract based on this prophecy: "When we finally establish the account, its number will be XYZ, and the contract automatically takes effect then."

This state of "the account does not yet exist, but can already be referenced" is called "counterfactual."

**Third application: batch casting.**

An army needed one thousand standard-issue blades. Under the old method, the smith forged them one by one, numbers random, unable to pre-allocate.

Using the prophet's mold, the army could pre-calculate each blade's number before casting began, engraving numbers on scabbards in advance. After casting, blades and scabbards automatically matched.

---

**The Art of Salt**

The prophet's mold introduced an interesting variable: salt.

Salt itself had no meaning—its only purpose was to let buyers "adjust" the final number. If the first calculated number was already occupied, the buyer could change the salt, recalculate, and repeat until finding an unoccupied number.

This spawned "number hunters"—a profession dedicated to finding "pretty numbers." Some would pay a premium for a blade whose number contained eight 8s, or ended with specific digits. Number hunters used computers to continuously try different salts, searching for numbers that met buyers' requirements.

---

Years later, Shen Suan's prophet's mold had become standard equipment for all craftsmen in Yunzhou City. Someone asked Shen Suan: "What is the most powerful aspect of your mold?"

Shen Suan said: "It is not the prophecy. It is that it makes 'things that do not yet exist' become 'addressable.' Before the blade is cast, it is already an entity that can be referenced, trusted, and used. This changes our definition of 'existence.'"

---

## What This Fable Is About

This fable illustrates **CREATE2**—a deterministic contract creation method in EVM. Unlike CREATE, CREATE2's contract address is determined solely by `deployer_address + salt + init_code_hash`, independent of the creation nonce. This means you can predict a contract's address precisely before deployment.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Traditional random numbers | CREATE (based on nonce) | Contract address = `keccak256(rlp([sender, nonce]))`. Each contract creation increments nonce; address is unpredictable |
| Prophet's mold | CREATE2 | Contract address = `keccak256(0xff + sender + salt + keccak256(init_code))[12:]`. Completely deterministic; can be pre-computed |
| Mold number | Deployer address | CREATE2 calculation includes the deployer address, ensuring different deployers' address spaces do not conflict |
| Material recipe | Init code (initialization bytecode) | Contract creation bytecode determining contract logic. Different init code produces different addresses |
| Salt | Salt (bytes32) | A 32-byte value freely chosen by the deployer to generate different addresses with the same init code |
| Advance assembly | Pre-computed address application | Can know a contract's address before deployment, pre-configuring other contracts to reference it |
| Counterfactual | Counterfactual instantiation | Accounts or contracts not yet deployed on-chain can already be referenced and interacted with (e.g., state channels, Layer 2) |
| State channels | State Channels / Layer 2 | Based on counterfactual addresses, contracts can be pre-signed off-chain; on-chain deployment only occurs in disputes |
| Number hunters | Vanity address mining | Brute-forcing salt values to find addresses with specific prefixes or patterns |
| Batch casting | Batch deployment + pre-calculation | Can pre-calculate large numbers of contract addresses for batch configuration and initialization |

### Why This Story?

CREATE2 is a seemingly simple but profoundly deep technology. It gives "not-yet-deployed contracts" addressability, which is the foundation for counterfactual states, state channels, batch deployment, and other advanced applications.

The "prophet's mold" metaphor for CREATE2 offers several intuitive advantages:
1. **Determinism visualized**: Knowing the number before casting—corresponding to CREATE2's address predictability
2. **Counterfactual concretized**: Scabbard work begins before blade forging—corresponding to counterfactual instantiation
3. **Salt flexibility**: Adjusting salt to find ideal numbers—corresponding to the salt parameter's role

### Further Reading

- wiki-web3: CREATE2 Contract Creation and Address Prediction
- [EIP-1014: Skinny CREATE2](https://eips.ethereum.org/EIPS/eip-1014)
- [Counterfactual Instantiation](https://docs.statechannels.org/)
- [Uniswap V3 Factory CREATE2 Usage](https://docs.uniswap.org/contracts/v3/reference/core/UniswapV3Factory)
