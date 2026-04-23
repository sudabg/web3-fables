---
title: "The Factory of Echoes"
title_cn: "回声工坊"
concept: "EIP-1167 Minimal Proxy / Clone Factory"
concept_cn: "EIP-1167 最小代理合约"
category: "infrastructure"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/eip-1167-最小代理合约深入解析.md"
tags: [infrastructure, eip-1167, minimal-proxy, clone, factory, gas-optimization]
---

# The Factory of Echoes

> *A workshop that does not build new instruments, but creates perfect echoes of a single master instrument.*

## The Story

In Yunzhou City, a master instrument maker named Chen created the perfect scale. It was precise, beautiful, and expensive to build. Other merchants wanted similar scales, but they could not afford Chen's fees.

Chen had an idea. Instead of building each scale from scratch, he built a single "echo chamber." The chamber contained a perfect copy of his master scale. When a merchant wanted a scale, Chen did not build a new one—he simply opened a small window into the echo chamber.

Through the window, the merchant saw the master scale. The window itself was tiny and cost almost nothing to make. But through it, the merchant could use all the precision of the master scale.

The echo chamber had one rule: it never changed. All windows looked into the same chamber. If Chen improved the master scale, every window automatically showed the improvement. If he discovered a flaw and fixed it, every window was fixed simultaneously.

The merchants loved it. They paid a fraction of the cost and received the same quality. Chen loved it too—he maintained only one instrument, not a thousand.

---

## What This Fable Is About

This fable illustrates **EIP-1167 Minimal Proxy Contracts**—a pattern that allows deploying lightweight proxy contracts that delegate all calls to a single implementation contract, dramatically reducing deployment costs.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Master scale | Implementation Contract | The single contract containing all logic |
| Echo chamber | Proxy pattern | Lightweight contracts that forward calls to the implementation |
| Window into the chamber | Minimal Proxy | A tiny contract (only 45 bytes) that delegates all calls to the master |
| Tiny cost to make a window | Low deployment cost | EIP-1167 proxies are extremely cheap to deploy compared to full contracts |
| Improvement reflected everywhere | Single point of maintenance | Updating the implementation benefits all proxies simultaneously |
| Flaw fixed everywhere | Bug fix propagation | A single fix applies to all clones instantly |

### Why This Story?

EIP-1167 is one of the most elegant gas optimizations in Ethereum. The echo chamber metaphor captures the essence: thousands of cheap windows into a single, well-maintained master.

### Further Reading

- [wiki-web3: EIP-1167 Minimal Proxy Deep Dive](../../wiki-web3/concepts/eip-1167-最小代理合约深入解析.md)
- [EIP-1167: Minimal Proxy Contract](https://eips.ethereum.org/EIPS/eip-1167)
- [OpenZeppelin: Clones](https://docs.openzeppelin.com/contracts/4.x/api/proxy#Clones)
