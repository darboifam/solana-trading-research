# Research findings and limitations

## October 2026 risk-screening study

Exploratory model: pooled LightGBM classifier for **net losses of at least 15%** among eligible entry candidates. Features comprised early price movement plus optionally historical liquidity whose recorded timestamp had already passed the mandatory **+63s availability rule**.

### Severe-loss ranking AUC, newest eligible 20% per feed

| Feed | Newest eligible candidates | Price only | Price + liquidity |
| --- | ---: | ---: | ---: |
| VIP | 6,359 | 0.640 | **0.645** |
| DSB | 646 | 0.659 | **0.663** |
| CTO 15-second | 51 | 0.622 | **0.637** |
| CTO 1-second sensitivity | 11 | 0.571 | 0.536 |

AUC ~0.5 indicates random ranking; above that indicates *some* discriminatory ability. It does not imply profitable trading. CTO has insufficient observations for a strong inference.

### One-global-position replay, newest eligible segment

1% fee per buy and sell leg; missing exit modeled hypothetically as -25%. The filtered and unfiltered groups compete for one position slot, so counts can differ non-monotonically.

| Feed | Baseline trades / mean | Price-only screened trades / mean | Price + liquidity screened trades / mean |
| --- | --- | --- | --- |
| VIP | 5,343 / **-3.36%** | 3,740 / -3.06% | 3,553 / **-3.01%** |
| DSB | 628 / **-3.86%** | 464 / -3.20% | 499 / **-1.71%** |
| CTO 15-second | 45 / **-3.46%** | 48 / -3.53% | 48 / **-3.53%** |

All screened mean returns remain **negative**, including when unresolved exits were hypothetically treated as break-even. For DSB, a separate day-cluster bootstrap of candidate-level differences estimated +1.79 percentage points of improvement (95% interval +0.22 to +3.35 percentage points), **but its screened mean itself was still negative**.

![Mean returns in newest archived segment](../assets/causal-risk-screen.png)

## Why these numbers require caution

- The newest price-eligible samples generally ended in **August or September 2026**, not October.
- No performance in this repository is claimed to come from verified live SolanaTracker fills.
- Historical prices can diverge substantially from executable swap quotes, especially in low-liquidity tokens.
- Missing price histories, missing exits and differences between price sampling resolutions limit inference.
- Many chronological segments had been repeatedly explored; they are **not pristine untouched holdouts**.
- Strong outliers may dominate a few apparent positive returns; sensitivity to removing large winners is necessary.
- One-position simulation has its own assumptions if liquidation time is unresolved; do not present missing-exit slot release as a real sale.
- Research-tested strategies in these notes are **not validated or approved for live deployment**.

## Negative findings are findings

Across the large October asymmetric-payoff scan, **0 / 11,021** qualified candidates passed the all-three-feed profitability test after the simulator indexing defect was corrected. Older breakout strategies did not consistently reproduce. An optimistic resting take-profit fill assumption did not solve the universality problem. Documenting why they failed is as important as documenting what they tested.

[Return to overview](../README.md)
