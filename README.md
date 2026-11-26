# Agentic Data Analyst

An LLM-powered agent that answers business questions about the public [Olist Brazilian E-Commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce). It looks up business definitions in a semantic layer, writes and runs SQL, and explains its answers in plain language.

> **Status:** early development. The architecture below is the target design; most components are not implemented yet.

## What it does

Ask a question in natural language, for example:

- *"What was the monthly revenue in 2017?"*
- *"Which product categories have the worst average review score?"*
- *"What is the average delivery delay by state?"*
- *"Which sellers have the highest share of late deliveries?"*

The agent then:

1. **Understands the question** and identifies the business concepts involved (revenue, delivery delay, active customer, and so on).
2. **Retrieves context from the semantic layer** using RAG: table and column descriptions, metric definitions, join paths and business rules.
3. **Generates SQL** grounded in that context.
4. **Executes the query** against a local database and checks the result. If the query fails or returns something implausible, it revises the SQL and tries again.
5. **Explains the answer**: the result, how it was computed, which definitions were used, and any caveats.

## Architecture

```text
            ┌──────────────────────┐
 question ─▶│        Agent         │
            │  (LLM + tool loop)   │
            └──┬────────┬───────┬──┘
               │        │       │
     retrieve  │  run   │       │  explain
     context   ▼  SQL   ▼       ▼
   ┌────────────────┐ ┌──────────────┐ ┌──────────────┐
   │ Semantic layer │ │ SQL executor │ │  Answer +    │
   │ (vector index) │ │  (database)  │ │  explanation │
   └────────────────┘ └──────────────┘ └──────────────┘
```

### Components

| Component | Responsibility |
| --- | --- |
| **Agent** | Orchestrates the reasoning loop and decides when to retrieve context, run SQL, retry or answer. |
| **Semantic layer** | Human-curated definitions of tables, columns, metrics, dimensions and business rules for the Olist schema. |
| **Retriever (RAG)** | Embeds the semantic layer and returns the definitions most relevant to the question. |
| **SQL tool** | Runs read-only SQL with guardrails (only `SELECT`, row limits, timeouts) and returns results and errors to the agent. |
| **Explainer** | Turns the query result into an answer that shows the SQL and the definitions used. |

## Dataset

The Olist dataset contains about 100k orders placed between 2016 and 2018 on several Brazilian marketplaces. It covers orders, items, payments, reviews, customers, sellers, products and geolocation.

Main tables:

- `orders`: order status and purchase, approval and delivery timestamps
- `order_items`: products, sellers, prices and freight per order
- `order_payments`: payment type, installments and values
- `order_reviews`: review scores and comments
- `customers`, `sellers`, `geolocation`: who bought and sold, and where
- `products`, `product_category_name_translation`: product attributes and English category names

The raw data is **not** committed to this repository. Instructions will be included in [Getting started](#getting-started) for how to download it.

## Getting started

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- An API key for the LLM provider

### Installation

```bash
git clone https://github.com/KarendaMata/agentic-data-analyst.git
cd agentic-data-analyst
uv sync
```

### Data setup

TBD.

### Usage

TBD.

## Project structure

```text
agentic-data-analyst/
├── src/agentic_data_analyst/   # Package source
├── docs/
├── evals/
├── tests/
├── pyproject.toml
├── uv.lock
└── README.md
```

## Roadmap

TBD.

## License

TBD.
