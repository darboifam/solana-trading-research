# Public disclosure and privacy boundary

## Repository policy

**The proprietary trading-bot implementation is private.** This public repository is deliberately limited to manually reviewed explanatory Markdown files and one aggregate, non-identifying research figure.

### Not included

- Any trading-bot `.py` implementation or internal research scripts.
- Private strategy implementation details, source trees or git commit history.
- Private wallet material, seed phrases, keypair exports, `.env` files or API keys.
- Telegram authentication session files, access hashes, private channel IDs or credentials.
- VPS IPs, access details, logs containing authentication headers or internal file paths.
- Raw Telegram messages, source-channel exports, transaction-by-transaction records or token-address-level datasets.
- Raw matched-call, tick-price, liquidity archives and performance/research ZIP bundles.

### Safe contents

- High-level architecture diagrams.
- Research questions and documented failure modes.
- Aggregated results where caveats, chronology and assumptions are preserved.
- Links to upstream libraries and official public tools.
- Manually reviewed, non-sensitive aggregate figures.

## Before publishing

Use a **new** repository with a clean commit history. Do not simply switch a private code repository to public or upload an entire working directory and hope `.gitignore` fixes it: `.gitignore` does not delete already tracked content or history. Review every file, image and document before committing. If credentials are accidentally committed publicly, rotate them immediately; deleting a later commit does not reliably erase them from history.

## Licensing

This repository intentionally does not contain distributable implementation source code. Attribution to upstream projects does not grant licenses to copy their code into this repository. A license for this documentation can be selected intentionally later; **no license is asserted in the starter package**.

[Return to overview](../README.md)
