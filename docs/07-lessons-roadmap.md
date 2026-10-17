# Engineering lessons and roadmap

## Lessons from the project

**1. Causality is a system property.** Market-data timestamps, publication delays, edited source posts and execution times must be represented separately. A +63-second availability offset on one-minute liquidity values can materially change which observations are knowable.

**2. Simulators need adversarial audits.** A trailing-exit grid-boundary defect produced an attractive false result. The correct response was to fix the code, rerun the full search and discard the apparent profitability.

**3. Backtest portability matters more than a best-in-sample configuration.** Rules that looked promising on one archive often failed in later periods or on different source populations.

**4. Selection bias can hide inside missing data.** Treating a token with no later recorded price as if the trade never occurred can select winners using future data. Missing data needs stated assumptions and sensitivity bounds.

**5. Extreme winners are not the same as capturable winners.** Hindsight path maximums overstate what an event-driven bot with routing delays could capture. Exit timing and quote quality are separate problems from predicting upward movement.

**6. Partial prediction is not sufficient for positive expectancy.** A downside classifier can exceed random ranking performance and still leave accepted trades with negative average modeled returns.

## Future research plan

1. Record quote request time, quote response time, both buy and sell quotes, route impact, size, availability/failure codes and eventual transaction outcomes.
2. Collect transaction-flow features using a clock-consistent ingestion pipeline. Compare them with ordinary price-only features on comparable observations.
3. Freeze models and thresholds **before** collecting a genuinely new future period; maintain strict chronological and feed-level evaluation.
4. Validate quote-to-fill drift and rejections at the actual intended order sizes.
5. Preserve a one-position portfolio replay with cross-feed address deduplication and trade-level audit logs.
6. Continue measuring stability across sample periods, token lifecycle segments, liquidity strata and worst-case fill assumptions.

## Engineering competencies illustrated

Event-driven Python, API integration, distributed/remote deployment, message parsing, failure handling, blockchain infrastructure, stateful automation, data engineering, causal time-series evaluation, simulation, machine-learning diagnostics and research reproducibility.

[Return to overview](../README.md)
