# Data construction and causal validation

## Historical source universe

The October 13, 2026 risk-screening audit recorded these source-universe sizes:

| Feed | Original calls | Price-aligned entry candidates | Candidates with liquidity available by decision time | Last eligible call |
| --- | ---: | ---: | ---: | --- |
| VIP | 86,836 | 32,449 | 21,404 | 2026-09-10 UTC |
| DSB | 7,815 | 3,419 | 2,875 | 2026-08-22 UTC |
| CTO 15-second | 2,060 | 270 | 250 | 2026-08-24 UTC |
| CTO 1-second sensitivity | 2,060 | 55 | 54 | 2026-08-25 UTC |

**Not every call has a recorded tradable price history.** The eligible populations above are subsets and can be biased. CTO one-second data was used only as an auxiliary sensitivity sample, not double-counted as an independent fourth feed.

## Five different timestamps

1. Telegram message / source-event timestamp.
2. Market observation timestamp.
3. Earliest legally knowable data-availability timestamp.
4. Strategy decision timestamp.
5. Simulated or actually recorded execution timestamp.

In a causal simulation, a feature is admissible only when its **availability time is no later than the decision time**. If the data were edited or produced later, the final archival value should not be treated as known at the original call unless independently verified.

## Fixed liquidity rule

For **every Birdeye 1-minute liquidity observation**:

**Earliest allowed availability = recorded observation timestamp + 63 seconds**.

The October audit found zero mismatches among the inspected historical liquidity points. The delay is mandatory in all present and future strategy experiments, not an optional sensitivity toggle.

## Baseline experimental frictions

A commonly used conservative October 2026 proxy model employed:

- Delay between decision and price-proxy fill, typically modeled as at least five seconds.
- Fees of **1% per leg** (buy and sell).
- A **10x gross return cap** in certain sweeps.
- A **single global active position**, with token address deduplication across feeds.
- Explicit accounting for missing exit prices, commonly contrasting hypothetical **-25%** versus **0%**, and sometimes **-100%** outcomes.
- Chronological training, validation and newest-period comparisons; bootstrapping by calendar day where suitable.

Specific experimental details vary; results from different assumptions should not be aggregated casually. A missing recorded price does **not** prove a 25% loss, but silently discarding trades without an exit price is also biased. Separate these scenarios visibly.

## Simulator quality gates

- Strict array bounds and fallback behavior for absent later ticks.
- No use of future token outcomes to accept entries or define features.
- No source update permitted before its publication time.
- No use of final edited market-cap fields as historical truth without provenance.
- Comparable candidate universe for filtered and unfiltered baselines where possible.
- Enforced chronological ordering and explicit concurrency conflicts.
- Separate price-history reconstruction from router-executable transaction outcomes.

[Return to overview](../README.md)
