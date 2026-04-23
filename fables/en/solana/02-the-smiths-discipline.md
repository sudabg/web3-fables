---
title: "The Smith's Discipline"
title_cn: "铁匠的纪律"
concept: "Rust Safe Programming"
concept_cn: "Rust 安全编程"
category: "solana"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/rust-智能合约安全编程规范.md"
tags: [solana, rust, memory-safety, ownership, borrow-checker, type-system]
---

# The Smith's Discipline

> *It is not that mistakes are not allowed, but the compiler closes the door before you can make one.*

## The Story

Yunzhou City had two blacksmith schools. One taught "free forging"; the other taught "disciplined forging."

---

**Free Forging School**

The free forging school's philosophy was: give apprentices maximum freedom. You could use any tool, any material, any method. The school only taught basic techniques; the rest was up to you.

Free forging's advantage was flexibility. If you wanted to forge a blade of bizarre shape, no rules stopped you.

But free forging's cost was: frequent accidents.

- An apprentice poured molten iron onto himself—because he forgot to check the temperature.
- An apprentice's blade broke on first use—because he used cracked raw materials, but the school had no mandatory raw material inspection system.
- An apprentice caused a fire during quenching—because he opened both the oil trough and water trough simultaneously, and the school allowed this.

The most serious accident: an advanced apprentice built an automatic forging machine. The machine operated well but had a hidden flaw—under specific conditions, it would operate two hammers simultaneously, causing them to collide and the entire machine to explode. This flaw did not appear during testing because test conditions happened to avoid that "specific condition." But the client triggered it during use.

Free forging school graduates who survived often became more creative. But many became disabled—literally.

---

**Disciplined Forging School**

The disciplined forging school's philosophy was completely different. In their view, forging's dangers did not come from tools but from human carelessness. So the school designed an entire "discipline"—not punishing errors after the fact, but preventing them before they occurred.

Specific rules:

**First: ownership system.**

Every tool, every piece of raw material, at any time had only one "owner." If Jia took the hammer, Yi could not use it simultaneously. If Yi wanted to use it, he had to wait for Jia to return it, or Jia explicitly "lent" the hammer to Yi.

This rule prevented "two people simultaneously operating the same hammer" accidents. It also prevented "I thought the hammer was in my hand, but someone else had already taken it" confusion.

**Second: borrowing check.**

When you borrowed a tool from someone, the school checked three things:
- Does this tool actually exist (not fictional)?
- Is this tool currently borrowed by someone else (or borrowing methods do not conflict)?
- Will your borrowing time exceed the agreed period?

If any condition was not met, the school would not allow you to start work. Not punishing you, but simply not opening the workshop door.

**Third: type matching.**

The school's forge only heated specific types of metal. If you tried to put wood into the iron forge, the forge door would not open—not because you did something wrong, but because the forge's design did not allow non-metal materials to enter.

This seemed like a restriction but was actually protection. It prevented "putting things that shouldn't be heated into the furnace" accidents.

**Fourth: no null pointers.**

In the free forging school, apprentices could point at an empty spot and say "the hammer is there"—even if there was nothing there. This led to disaster: the apprentice reached for air, lost balance, and fell into the furnace.

The disciplined forging school eliminated "null pointers." If you wanted to point at a position, that position must have something. If something might not exist, you had to explicitly handle the "non-existence" situation—such as checking first or preparing a backup plan. You could not pretend it definitely existed.

---

**Output of Both Schools**

Free forging school graduates, if they survived, were often more creative. Because from childhood they were allowed to try all kinds of crazy ideas.

Disciplined forging school graduates almost never had serious accidents. Their work might not be stunning, but it was extremely reliable. An employer said: "I've hired graduates from both schools. Free forging school people occasionally surprise me, but also occasionally shock me. Disciplined forging school people never surprise me, but also never shock me. When building bridges, I choose people who don't shock me."

---

**Cost of Disciplined Forging**

Disciplined forging was not free.

Apprentices complained: "I clearly know I won't make mistakes, but the school still forces me to check every step. This wastes too much time."

Teachers answered: "You didn't make mistakes yesterday doesn't mean you won't today. And when projects grow larger and more people participate, you cannot assume others are as mistake-free as you. Discipline is not designed for you alone; it is designed for the entire team."

The more practical cost was: some designs easily implemented in free forging school required many detours in disciplined forging school. The school required you to write more "boilerplate code" to prove "I have considered all possible error situations."

An old craftsman said: "Free forging lets you run faster; disciplined forging makes you fall less. When forging a kitchen knife, free forging may be better. When building a great bridge, disciplined forging is the only choice."

---

## What This Fable Is About

This fable illustrates **Rust's safe programming model**—Solana smart contracts' primary development language. Rust eliminates memory safety vulnerabilities at compile time through ownership, borrowing checking, type systems, and null-pointer elimination, rather than relying on runtime testing.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Free forging school | C/C++ / traditional system programming | Gives developers maximum freedom; manual memory management; prone to errors |
| Disciplined forging school | Rust | Compile-time enforcement of safety rules; memory safety without garbage collection |
| Ownership system | Ownership System | Each value has only one owner at any time. When owner leaves scope, value is automatically released |
| Borrowing check | Borrow Checker | Compiler checks all references are valid: no dangling references, no data races, no simultaneous mutable and immutable borrows |
| Type matching | Type System / Pattern Matching | Rust's strong type system and exhaustive pattern matching ensure all cases are handled |
| No null pointers | `Option<T>` / no null | Rust has no null. Values that may not exist must be explicitly handled with `Option<T>`; compiler forces checks |
| Forge door won't open | Compilation error | Unsafe operations are rejected at compile time rather than crashing at runtime |
| Automatic forging machine explosion | Memory safety vulnerability (UAF, Double Free, Buffer Overflow) | Common vulnerabilities in C/C++; eliminated in Rust through ownership and borrowing checking at compile time |
| Boilerplate code | Rust's explicit error handling | `Result<T, E>` and `Option<T>` require explicit error handling; code volume may increase but safety greatly improves |
| Kitchen knife vs. great bridge | Application scenario choice | System-level software (blockchain, OS) needs Rust's safety. Rapid prototyping may use more flexible languages |
| Team discipline | Rust suitable for large-scale collaboration | Compiler as "gatekeeper," ensuring even developers unfamiliar with the codebase cannot introduce memory safety issues |

### Why This Story?

Solana chose Rust as its native development language, with core reason being safety. Once blockchain code is deployed, it cannot be modified; a memory safety vulnerability could cause millions of dollars in losses.

The "blacksmith school" metaphor for Rust vs. C/C++ offers several intuitive advantages:
1. **Ownership visualization**: One hammer, one person at a time = Rust's ownership rules
2. **Compile-time checking**: Forge door won't open = compile error blocking unsafe code
3. **No null pointers**: Cannot point at empty spot saying hammer is there = `Option<T>` forcing explicit handling of missing values
4. **Cost of creativity**: Disciplined forging more tedious but more reliable = Rust's development efficiency vs. safety tradeoff

### Further Reading

- [wiki-web3: Rust Smart Contract Safe Programming Standards](../../wiki-web3/concepts/rust-智能合约安全编程规范.md)
- [The Rust Programming Language Book](https://doc.rust-lang.org/book/)
- [Rust Ownership Explained](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)
- [Rust Borrow Checker](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)
- [Why Rust for Smart Contracts](https://docs.solana.com/developing/on-chain-programs/overview)
