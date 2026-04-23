---
title: "The Timed Safe"
title_cn: "计时保险箱"
concept: "Solana Account Model & Rent"
concept_cn: "Solana 账户模型与租金"
category: "solana"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/solana账户模型与租金机制详解.md"
tags: [solana, account, rent, lamports, state, data]
---

# The Timed Safe

> *Safes are not free. The longer you store, the higher the rent. Stop paying rent, and your things are cleared out.*

## The Story

Yunzhou City's bank offered a special safe deposit service, completely different from traditional safes.

---

**Traditional Safe vs. Timed Safe**

In traditional banks, you rented a safe and paid a fixed annual rent. As long as you paid rent, the box was permanently yours. You could put anything inside—gold, jewelry, deeds, even air. The bank did not care.

Yunzhou City's new bank launched a "timed safe." Its rules were extremely special:

**First: each safe had a fixed size.**

You could rent a large safe (holding one hundred items) or a small safe (holding only ten items). But you could not rent an "infinite" safe. If you wanted to store more things, you had to rent more safes.

**Second: safes had minimum deposit requirements.**

To rent a large safe, you had to pre-deposit at least one thousand taels of silver inside. This money was not rent—it still belonged to you—but it had to remain in the safe. If you withdrew it, the safe automatically became invalid, and its contents were cleared out.

**Third: safes were "ownerless."**

Traditional safes belonged to the renter—only you could open them. Timed safes had no fixed owner. Anyone who knew the opening method could open them. Safe security did not come from "who owns them" but from "who can provide the correct opening password."

**Fourth: safes could "authorize programs."**

You could set: "This safe can only be opened by such-and-such program." Programs were public, immutable rules. For example: "Only when I provide the correct password does the program allow item withdrawal." Or: "The program automatically withdraws ten taels of silver from my safe every month, transferring to another safe."

---

**Rent Mechanism**

Timed safe rent was not collected annually. It was calculated by "occupied space" and "occupied time."

Specific rules:
- A safe required a certain amount of rent annually.
- The pre-deposited one thousand taels in the safe automatically generated interest.
- If interest was sufficient to pay rent, the safe could be maintained permanently.
- If interest was insufficient to pay rent, the safe's balance would gradually decrease. When balance reached zero, the safe was "recycled"—its contents discarded, the safe itself reassigned to others.

This meant: timed safes were not "buy and own forever." They were resources requiring continuous maintenance. If you did not maintain them, they disappeared.

---

**Unexpected Applications of Timed Safes**

Timed safe design spawned many innovative uses:

**Automatic execution will**:
Someone deposited money in a safe, setting the program: "If I do not open this safe for two years, automatically transfer the money to my son." If the owner died, the safe automatically executed the transfer after two years. No lawyer, no court, no will certification needed.

**Subscription service**:
A merchant provided monthly ten-tael consulting services. The client deposited one hundred twenty taels in the safe, setting the program: "Automatically transfer ten taels to the merchant every month. Stop service when balance is insufficient." The merchant did not need to collect debts; the client did not need to manually transfer monthly.

**Composable financial instruments**:
A complex financial product consisted of over a dozen safes, each responsible for one function—storing principal, calculating interest, distributing earnings, managing risk. These safes were interconnected through programs, forming an automatic operating system. Failure of any single safe would affect the entire system, but the system itself had no central controller.

---

**Criticism of Timed Safes**

But timed safes also had critics.

- "Minimum deposit requirements" kept the poor out. If you only had one hundred taels, you could not even afford the smallest safe.
- "Rent mechanism" meant your assets would shrink over time (if interest was insufficient). This violated the intuition of "saving preserves value."
- "Ownerless" design made many people uncomfortable. Traditional bank customers asked: "If my password leaks, can't anyone open my safe?" The bank answered: "Yes. So we recommend you use more complex passwords, or use programs to add extra security layers."

A traditional banker said: "Timed safes are not designed for ordinary people. They are designed for programs. In the world of timed safes, what truly owns assets is not your identity, but your password and your programs."

---

## What This Fable Is About

This fable illustrates **Solana's account model and rent mechanism**. Unlike Ethereum's "contract is account," Solana stores all data in independent accounts, each with fixed space, requiring maintenance of a minimum balance (rent-exempt) to avoid being recycled, and accounts can designate "owner programs" to manage access permissions.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Traditional safe | Ethereum account model | Contracts store their own states; no explicit storage limits |
| Timed safe | Solana Account | All data in Solana is stored in independent accounts; each account has fixed size |
| Fixed-size safe | Account space limit | Solana accounts have fixed sizes at creation; cannot dynamically expand |
| Minimum deposit | Rent-exempt balance | Accounts must maintain minimum lamport balance to avoid recycling. This balance is proportional to account size |
| Pre-deposited interest | Balance does not generate interest but maintains exemption | Actually Solana has no interest, but rent-exempt minimum balance is a one-time deposit |
| Ownerless | Account has no private key control | Solana accounts are controlled by "owner program," not directly by private key |
| Opening password | Account signature / permission verification | Defined by owner program who can operate the account |
| Authorizing programs | Owner Program | Each account has an owner program (e.g., System Program, Token Program); only the owner can modify account data |
| Rent consumption | Rent mechanism | Accounts need to periodically pay rent (or be rent-exempt). If balance is insufficient, account data is recycled |
| Automatic execution will | Program Derived Address (PDA) + conditional execution | Solana programs can automatically execute operations based on conditions without external triggers |
| Subscription service | Automated transfers / program-controlled fund flows | SPL Token program supports automated token transfer logic |
| Composable financial instruments | Solana DeFi composability | Multiple programs call each other through accounts, forming complex financial protocols |
| Poor kept out | Rent threshold | Creating accounts requires minimum balance; unfriendly to small users |

### Why This Story?

Solana's account model is completely different from Ethereum's and is one of the most confusing aspects for EVM developers. Understanding "accounts need rent," "accounts have fixed sizes," and "programs own accounts" is key to entering Solana.

The "timed safe" metaphor for Solana accounts offers several intuitive advantages:
1. **Fixed size**: Safe size fixed = Solana account fixed space
2. **Minimum deposit**: Pre-deposited silver maintaining safe = rent-exempt minimum balance
3. **Ownerless design**: Password opening rather than identity = Solana's program-owned account model
4. **Rent consumption**: No maintenance leads to recycling = Solana rent mechanism preventing state膨胀

### Further Reading

- wiki-web3: Solana Account Model and Rent Mechanism
- [Solana Docs: Accounts](https://docs.solana.com/developing/programming-model/accounts)
- [Solana Rent Economics](https://docs.solana.com/implemented-proposals/rent)
- [Anatomy of a Solana Account](https://2501babe.github.io/posts/solana-account.html)
