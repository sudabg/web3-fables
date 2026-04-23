---
title: "The Stakers' Roulette"
title_cn: "押注者的轮盘"
concept: "Proof of Stake Consensus"
concept_cn: "权益证明共识机制"
category: "consensus"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/权益证明-pos-共识机制.md"
tags: [consensus, pos, validator, stake, attestation, epoch, finality]
---

# The Stakers' Roulette

> *It is not about who is strongest that keeps the ledger, but who stakes the most and longest that earns the right. But staking more also means losing more when wrong.*

## The Story

Yunzhou City's ledger was once maintained by a group of miners. They competed by solving mathematical puzzles to determine who had the right to write new entries. Whoever solved the puzzle first earned the right and the reward.

This system's problem was: the puzzle-solving competition consumed vast resources and electricity. Yunzhou City's north even had a dedicated coal mountain solely to supply the miners' computational race.

---

**New System: The Stakers' Roulette**

Yunzhou City's sages proposed a new system: instead of competing through puzzles, they would compete through "staking."

The specific rules were:

1. Anyone could become a "ledger keeper," but the prerequisite was that you must lock a security deposit in the city's public treasury. The larger the amount locked and the longer the lock time, the higher "weight" you received.

2. Every minute, the roulette spun once. Each sector on the roulette represented a ledger keeper. Sector size depended on the keeper's weight—those who staked more had larger sectors; those who staked less had smaller sectors.

3. When the roulette stopped, whoever the pointer pointed to earned that minute's ledger right—writing new transactions onto the ledger and receiving fee rewards.

4. But ledger keeping was not one person's decision alone. The selected keeper wrote the new page, and other keepers needed to "confirm"—checking whether the page's content was correct. If most people confirmed it was correct, the page was officially accepted.

---

**Staking Risks**

The stakers' roulette had a strict penalty mechanism:

If a keeper wrote incorrect content—such as deliberately omitting a transaction, or writing a false transaction—other keepers would refuse confirmation. If the keeper's error was proven, part or all of their locked security deposit would be confiscated.

This was called "slashing." Those who staked more had greater probability of earning ledger rights, more opportunities to earn money. But once they made mistakes, their losses were also greater.

An old keeper said: "Under the old system, miners wasted electricity. Under the new system, keepers risk money. Wasted electricity can be regenerated; confiscated money is truly gone. So people under the new system are more cautious."

---

**Queuing and Exiting**

The stakers' roulette also had a feature: you could not withdraw your security deposit at any time.

When you decided to stop being a keeper, you needed to "apply to exit." From application to actually receiving your money, there was a "cooling period"—during which you might still be selected to keep the ledger, but if you made mistakes during this time, your security deposit would still be fined.

The cooling period existed to prevent one type of attack: an attacker stakes a large sum, makes one malicious ledger entry, then immediately withdraws and runs. The cooling period gives the system time to discover and punish such attacks.

---

**Roulette Fairness**

Someone questioned: Those who stake more have larger sectors; doesn't this mean the rich always have the advantage?

The sage answered: "Yes. But under the old system, those who could afford more mining machines also had advantages. Under any system, those with more resources have advantages. The stakers' roulette at least changes resource consumption from 'wasting electricity' to 'locking capital.' Moreover, small stakers can unite, pooling their funds to share ledger rights and rewards."

Indeed, Yunzhou City quickly saw "staking pools" emerge—dozens of small stakers pooling their money, managed by professional operators running ledger nodes. Rewards were distributed according to contribution. This let small participants also share in consensus benefits.

---

## What This Fable Is About

This fable illustrates **Proof of Stake (PoS)** consensus mechanism—the algorithm used by Ethereum (and most modern blockchains). Validators participate in block proposal and confirmation by staking ETH; the more they stake, the higher their probability of being selected to propose a block. Misbehavior causes their staked funds to be slashed.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Miners solving puzzles | Proof of Work (PoW) | Bitcoin and early Ethereum consensus mechanism; competing for block rights through computational power |
| Public treasury lock | Staking / Delegation | Validators deposit ETH into Beacon Chain contract as security for consensus participation |
| Weight | Effective Balance | Validator weight determined by staked amount; cap of 32 ETH per validator |
| Roulette spin | RANDAO / Random Beacon | Each slot (12 seconds) selects a block proposer through a verifiable random function |
| Sector size | Selection probability | More staked = higher probability of becoming proposer |
| Other keepers confirm | Attestation / Validator Committee | Each slot has a validator committee responsible for voting to confirm block validity |
| Most people confirm | Committee consensus / Supermajority | If 2/3 of committee members vote to confirm, the block is accepted |
| Error proven | Slashable offense | Double voting, surround voting, and other malicious behaviors can be proven and punished |
| Confiscate deposit | Slashing | Misbehaving validators' staked funds are destroyed (up to 1 ETH immediate slashing; remaining portion gradually slashed over 36 days) |
| Cooling period | Exit Queue / Withdrawal period | Validators must wait to exit and still participate in consensus until fully exited; prevents "misbehave then immediately withdraw" |
| Staking pool | Staking Pool / Lido / Rocket Pool | Small holders participate in staking through pooling, receiving liquid staking tokens (e.g., stETH) as vouchers |

### Why This Story?

PoS is the core of blockchain's shift from energy-intensive to capital-intensive consensus. Understanding "why staking can replace computational power" and "how slashing prevents misbehavior" is key to understanding modern blockchain.

The "stakers' roulette" metaphor for PoS offers several intuitive advantages:
1. **Probabilistic block visualization**: Roulette = random proposer selection; sector size = staking weight
2. **Capital replacing energy**: From burning coal to locking capital—corresponding to PoS's economic design
3. **Slashing deterrence**: Stake more earn more but wrong more lose more—corresponding to PoS incentive compatibility
4. **Staking pools**: Small participants' unions—corresponding to liquid staking protocols (Lido, etc.)

### Further Reading

- [wiki-web3: Proof of Stake Consensus Mechanism](../../wiki-web3/concepts/权益证明-pos-共识机制.md)
- [Ethereum PoS FAQ](https://ethereum.org/en/roadmap/merge/)
- [Consensys: Ethereum 2.0 Economics](https://consensys.net/blog/blockchain-explained/ethereum-2.0-economics/)
- [Slashing Conditions in Ethereum PoS](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/)
