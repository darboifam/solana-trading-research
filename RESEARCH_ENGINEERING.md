# Research methods and engineering lessons

These examples summarize saved investigations. Their reported findings were reviewed for this portfolio; the original experiments were not rerun during preparation of this repository.

## Candle timing and reconciliation

A one-second simulation audit identified a mismatch between candle-start labels and the time a completed candle could be observed. A close-aware replay changed the historical result. A separate reconciliation used recorded forward-simulation entry times to reproduce exits and accounting.

**Engineering lesson:** validate event timing against observable data and actual recorded process behavior, rather than relying on similar-looking aggregate results.

## Historical liquidity and provider availability

Liquidity research compared observations made during a minute with the provider's later historical values and measured settlement availability. Historical liquidity levels and executable swap impact were treated as different measurements.

**Engineering lesson:** final historical data can arrive later than its nominal interval. Execution feasibility also needs current route and quote evidence.

## Original calls versus future updates

Signal studies separated original-call information from later updates. Cross-source confirmation became actionable only when the second message arrived; an eventual duplicate could not justify an earlier entry.

**Engineering lesson:** build features from information available at the decision, including message content and source membership.

## Missing data and incomplete exits

Different studies used documented conservative losses or fallback estimates based on prior realized observations. Data gaps, missing paths, and unresolved exits were reported rather than silently removed.

**Engineering lesson:** missingness is part of the system being evaluated. Its treatment changes both returns and selection bias.

## Holdout discipline and repeated research

Experiments used chronological splits, frozen configurations, and restricted evaluation gates. Reports also disclosed when a historical window had been inspected elsewhere or a new candidate was designed after its results were visible.

**Engineering lesson:** a holdout can be untouched within one run while already familiar across the broader research process. Post-holdout exploration needs fresh future evidence.

## Stress testing and independent reconstruction

Larger audits examined timing variants, parameter neighborhoods, component removal, portfolio ordering, resampling, concentration, and historical-prefix consistency. Some candidates passed mechanical causality checks while failing robustness or capacity requirements.

**Engineering lesson:** causal simulation is necessary, but a causal historical profit is not sufficient evidence for deployment.

## Broader SOL and futures research

Separate studies evaluated liquid-SOL strategy families, psychological levels, and a Coinbase futures-oriented strategy tournament. Several attractive development results weakened on later data; some studies failed their stated promotion criteria entirely.

**Engineering lesson:** selection criteria, trade count, payoff, costs, regime stability, and execution assumptions matter alongside win rate.

## How results are presented here

The public repository emphasizes methodology, engineering decisions, and lessons. Private reports contain exact rules, datasets, and numerical outcomes. No return figure in this case study is presented as verified live performance, and no study is promoted merely because its historical equity curve looked attractive.
