# Finance Pipeline (Live)

Personal finance data pipeline powering live Open Banking data collection and storage via TrueLayer.

## What it does

- Fetches live account balances and transactions via TrueLayer API
- Stores daily balance snapshots and transaction history to PostgreSQL
- Runs automated LLM-based transaction categorisation
- Feeds data to a separate personal dashboard project

## Tech Stack

Python • PostgreSQL • TrueLayer API • Claude AI • Railway

## Architecture

- **Data source**: TrueLayer Open Banking API (live accounts)
- **Storage**: PostgreSQL on Railway
- **Categorisation**: Anthropic Claude via batch processing
- **Orchestration**: n8n / scheduled jobs

---

Created by Remy Fernando