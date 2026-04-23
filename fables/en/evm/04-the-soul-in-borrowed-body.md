---
title: "The Soul in Borrowed Body"
title_cn: "借身还魂"
concept: "Delegatecall"
concept_cn: "Delegatecall 委托调用"
category: "evm"
difficulty: "advanced"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/代理合约-可升级.md"
tags: [evm, delegatecall, proxy, context, storage-collision, library]
---

# The Soul in Borrowed Body

> *Speak through another's body, but the words' consequences fall entirely on your own head.*

## The Story

Yunzhou City had an ancient secret art called "body borrowing." The practitioner could temporarily move his soul into another person's body, using that body to act. But body borrowing had an extremely dangerous property:

**Everything you do in the borrowed body, the consequences fall on your original body.**

---

**Normal Visitation**

Normally, if one person visited another, he stood in the other person's home speaking. The other person's furnishings, furniture, and property belonged to the host. The visitor merely borrowed a space to express himself.

This was "normal visitation"—the visitor had his own body, just speaking on the host's turf. The visitor said "I want water," drinking the host's water, interacting with the host's property.

**Body Borrowing Is Different**

Body borrowing was entirely different. When Jia moved his soul into Yi body:

- Jia used Yi's body, Yi's throat, Yi's limbs.
- But Jia's words, decisions, and consequences all fell on Jia's head.
- If Jia broke Bing's window using Yi's body, Bing would demand compensation from Jia, not Yi.
- If Jia signed a contract using Yi's body, the contract bound Jia, not Yi.

More critically: when Jia acted in Yi's body, he thought he was still in his own home. The environment he saw was actually Yi's home—Yi's furniture, Yi's property, Yi's diary. If Jia tried to "put something in his own safe," he was actually putting it in Yi's safe.

---

**Body Borrowing's Ingenious Use: The Substitute Actor**

Yunzhou City's theater troupe discovered a marvelous use for body borrowing: substitute actors.

The troupe had a lead actor named A-Long. A-Long had extraordinary performing talent, but he was advanced in age and could no longer perform on stage. The troupe found a young, vigorous substitute named A-Hu.

During performances, A-Long moved his soul into A-Hu's body. The audience saw A-Hu's body performing, but every movement, every line was controlled by A-Long's soul. A-Hu was merely a human shell.

A-Long could continuously "upgrade" his performance skills—practicing new moves backstage, then having A-Hu's body execute them in the next performance through body borrowing. The audience always saw "A-Hu," but experienced A-Long's ever-evolving art.

If A-Long passed away, the troupe only needed to find a new substitute, and A-Long's soul—if backed up in advance—could continue performing through borrowing. The troupe did not need to rebuild the entire stage; they only needed to change substitutes.

---

**Body Borrowing's Disaster: Soul Displacement**

But body borrowing was also the most dangerous secret art in Yunzhou City's history.

One time, a practitioner made an error during borrowing: he tried to "put something in his own pocket," but forgot he was in a borrowed body. The item ended up in the substitute body's pocket—and this pocket's location happened to correspond to a hidden compartment storing deadly poison in the substitute's body.

Poison leaked; the substitute died instantly; the practitioner's soul was forever trapped in the dead body.

This accident was called "soul displacement"—when the practitioner thought he was operating "his own space," he was actually operating the substitute's space, and the two spaces had completely different layouts.

---

**Body Borrowing Rules**

After countless accidents, Yunzhou City's practitioners summarized body borrowing's safety code:

1. **The borrowed body's internal layout must exactly match the original body.** If the original body's "heart position" was on the left, the substitute's "heart position" must also be on the left. Otherwise, the soul would get lost.

2. **The borrowed body must not have its own soul.** If the substitute body already had a soul, two souls would fight for control, with disastrous results.

3. **During borrowing, the original body enters a dormant state.** The original body could not act simultaneously; otherwise, a paradox of "two me's doing different things at the same time" would arise.

4. **After borrowing ends, no secrets may be left in the borrowed body.** Because when the soul departed, it took memories with it, but physical traces left in the substitute body (like words written on paper) would be exposed to the next borrower.

---

## What This Fable Is About

This fable illustrates **EVM's `delegatecall`**—a special low-level call method. Unlike normal `call`, `delegatecall` executes in the **target contract's code** but uses the **calling contract's storage, balance, and state**.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Normal visitation | CALL | Executed in target contract's context: uses target's storage; msg.sender is the caller |
| Body borrowing | DELEGATECALL | Executed in target contract's code, but uses caller's storage; msg.sender and msg.value remain unchanged |
| Jia's soul in Yi's body | Caller uses proxy contract code to execute | Logic code comes from the called contract (implementation), but storage is the caller's (proxy) |
| Consequences fall on Jia | msg.sender remains unchanged | `delegatecall` does not change `msg.sender`; caller identity is preserved |
| Substitute actor | Proxy contract pattern | Proxy contract uses `delegatecall` to delegate execution to Implementation contract; proxy itself only stores state |
| A-Long upgrades moves | Upgradeable contract | Replacing Implementation contract address; proxy storage unchanged; logic upgraded |
| A-Long passes, new substitute found | Contract migration | Old implementation abandoned; new implementation connected to same proxy; state inherited |
| Soul displacement / poison compartment | Storage collision | If Implementation and Proxy storage layouts are inconsistent, `delegatecall` writes to wrong locations, potentially causing severe vulnerabilities (e.g., Parity multi-sig wallet vulnerability) |
| Layouts must match | Storage layout compatibility | Upgraded Implementations must maintain the same storage layout as old versions; new variables can only be appended at the end |
| Substitute must not have soul | No state conflicts | Implementation contracts should not have their own important state; all state should be in the Proxy |
| No secrets after borrowing | Self-destruct risk | If an Implementation contract executes `selfdestruct`, it destroys the Proxy contract through `delegatecall` (one of delegatecall's dangers) |

### Why This Story?

`delegatecall` is one of Solidity's most difficult concepts to understand and the source of many serious security vulnerabilities (e.g., Parity multi-sig wallet lockup, various proxy contract vulnerabilities).

The "body borrowing" metaphor for `delegatecall` offers several intuitive advantages:
1. **Context switching visualized**: In another's body, but consequences are your own—corresponding to `delegatecall`'s context preservation
2. **Proxy contract intuition**: Substitute actor = Proxy, A-Long = Implementation, audience always sees Proxy address
3. **Storage collision danger**: Soul displacement = catastrophic consequences of storage layout mismatch

### Further Reading

- wiki-web3: Proxy Contracts and Upgradeability
- [EVM Deep Dives: Delegatecall](https://noxx3xxon.notion.site/noxx3xxon/EVM-Deep-Dives-61b5e3e045e2482aa4e112d97823d37d)
- [OpenZeppelin: Proxy Patterns](https://docs.openzeppelin.com/upgrades-plugins/1.x/proxies)
- [Parity Multi-Sig Wallet Hack Analysis](https://blog.openzeppelin.com/on-the-parity-wallet-multisig-hack-405a8c12e8f7)
