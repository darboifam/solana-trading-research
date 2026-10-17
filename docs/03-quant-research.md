# Quantitative research program

## Primary question

Could a trading rule survive across multiple Solana Telegram call populations, after accounting for realistic execution friction, incomplete historical coverage and the restriction of a single open position globally?

## Experiment inventory

| Period | Research area | What was tested | Historical finding |
| --- | --- | --- | --- |
| Earlier iterations | Momentum/breakout | Relative-price triggers, confirmation waits, hold duration and early risk exits. | Attractive older backtests did not transfer reliably to later VIP, DSB and CTO data. |
| Oct 2026 | Asymmetric winners | Fixed holding, open-ended upside, wide stops, trailing exits, partial cash-outs and runners. | Corrected audit: **0** configurations consistently profitable across three datasets among **11,021** eligible configurations (541 fixed-hold; 2,920 asymmetric exit; 7,560 partial-profit). |
| Oct 2026 | Lifecycle adaptation | Entry time, early price behavior, cap bands and holding-time combinations. | **0** qualifying universal training winners in the tested common-sample scan. Feed-specific training winners often failed later or had unreliable exit coverage. |
| Oct 2026 | Price structure | Compression, expansion, reversals, breakdowns, post-pump consolidation. | 4,400 configurations screened; no stable newest-period universal winner. |
| Oct 2026 | Market regime | Gate trades using the most recent simulated results. | No supported universal latest-period winner under the primary missing-exit scenario. |
| Oct 2026 | Trailing/TP execution | Trailing-stop activation, distance, hard stop; optimistic resting take-profit touch fills. | Better simulated profit-taking alone did not establish cross-feed profitability. |
| Oct 2026 | Source updates | Published Telegram multiple announcements as exit/entry timing signals. | Some mean-loss reduction, especially in DSB exits, but not positive universal expectancy. |
| Oct 2026 | Independent replication | Previously selected older breakout rules on newer archives. | No reliable portability; corrected trading assumptions and missing data matter. |
| Oct 2026 | Crash-risk screening | Early price-path features and causally available liquidity. | Modest observed severe-loss ranking AUC; screened returns still negative. |

## Structural observations

- **Tail concentration:** Rare extreme winners dominate certain historical averages; removing the top 1% can reverse positive-looking means.
- **Short-lived upside:** Future maximum prices vastly overstate the achievable returns of causal exit policies.
- **Feed differences:** VIP and DSB become more similar after controlling for lifecycle stage, while CTO still behaves differently in the observed window.
- **Recording coverage:** Archived price history availability differs sharply by feed and date. Eligibility based on future exit availability is invalid selection.
- **Timeline integrity:** A trailing-stop implementation once indexed beyond the valid price grid, producing artificial successes. The positive results were **discarded**, not promoted.

## Risk-screening hypothesis

Rather than relying on detecting an unusually large future winner, test whether call-time and near-call characteristics identify trades likely to experience severe losses. In the October audit, the model evaluated early price return, drawdown, volatility, gap/momentum characteristics and eligible one-minute liquidity. A decision at call+60s could use only liquidity with `observation_time + 63s <= call+60s`.

The initial result was **predictive discrimination, not profitable selection**. Future experiments require true executable two-way quotes and fresh held-out calls.

[Methods](04-data-validation.md) · [Results](05-results-limitations.md) · [Overview](../README.md)
