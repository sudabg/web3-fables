---
title: "The Infinite Borrower"
title_cn: "无限借贷者"
concept: "Reentrancy Attack"
concept_cn: "重入攻击"
category: "security"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/solidity重入攻击与防御.md"
tags: [security, reentrancy, attack, smart-contract, vulnerability]
---

# The Infinite Borrower

> *A man enters a bank to withdraw his deposit. Before the teller records the withdrawal, the man asks to borrow against the same deposit again. The cycle repeats until the vault is empty.*

## The Story

In the city of Yunzhou, there was a wealthy merchant named Lin who ran the largest pawnshop in the city. Business was straightforward: customers deposit collateral and receive loans. When the loan is repaid, the collateral is returned.

One day, a mysterious stranger arrived at the pawnshop. He placed a jade pendant on the counter and said, "I wish to borrow one hundred taels against this pendant."

The clerk examined the jade, recorded the loan in the ledger, and handed over one hundred taels. But before the clerk could mark the transaction as complete, the stranger said, "I have changed my mind. I wish to borrow another one hundred taels."

The clerk, following protocol, checked the ledger. The jade pendant was still recorded as collateral—because the first withdrawal had not yet been finalized. So the clerk approved the second loan.

But before the second transaction could be recorded, the stranger asked for a third. And a fourth. And a fifth.

Each time, the clerk checked the ledger and saw the jade still listed as collateral. Each time, another one hundred taels were handed over. By the time the clerk finally updated the ledger, the stranger had received one thousand taels—for a pendant worth only one hundred.

The stranger departed, never to be seen again. The pawnshop discovered the fraud too late. The ledger showed the jade as collateral for a single one-hundred-tael loan, but the vault was missing one thousand taels.

---

## What This Fable Is About

This fable illustrates the **reentrancy attack**—one of the most famous and costly vulnerabilities in smart contract history. The attack exploits the fact that a contract's state is updated *after* external calls are made, allowing an attacker to recursively re-enter the function before the state change is recorded.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Pawnshop | Smart Contract | The vulnerable contract holding funds |
| Ledger | Contract State / Storage | The internal accounting of balances |
| Jade Pendant | Collateral / Deposit | The asset deposited by the user |
| Loan Withdrawal | Withdrawal Function | The function that sends funds to the user |
| Clerk checks ledger before recording | State update after external call | The contract checks balance *before* deducting it |
| Stranger asks for multiple loans before completion | Reentrant recursive calls | The attacker's contract calls back into the vulnerable contract before the first call completes |
| One thousand taels stolen | Drained contract balance | All funds are extracted through recursive calls |
| Ledger still shows original amount | State not yet updated | The balance deduction happens *after* the external call |

### Why This Story?

The reentrancy attack is abstract until you see it as a timing problem. The "check-then-act" pattern—where a contract verifies conditions, performs an external operation, and only then updates state—is exactly where reentrancy strikes.

The pawnshop clerk represents the contract's execution flow. The stranger's repeated requests before the ledger is updated represent the attacker's recursive calls. Making this concrete helps developers understand why the "checks-effects-interactions" pattern (update state *before* external calls) is non-negotiable.

### Further Reading

- wiki-web3: Solidity Reentrancy Attack and Defense
- [ConsenSys: Reentrancy](https://consensys.github.io/smart-contract-best-practices/attacks/reentrancy/)
- [The DAO Hack Explained](https://blog.ethereum.org/2016/06/17/critical-update-re-dao-vulnerability)
- [OpenZeppelin: ReentrancyGuard](https://docs.openzeppelin.com/contracts/4.x/api/security#ReentrancyGuard)
