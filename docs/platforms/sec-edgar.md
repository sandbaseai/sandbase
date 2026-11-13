# SEC EDGAR API: 1 endpoints with pricing and code examples

Call 1 SEC EDGAR endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`sec/filings`](../models/sec/filings.md) | List a public company's SEC EDGAR filings - form type, filing date, accession number, and document links - by ticker, company name, or… | about $0.00132 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sec/filings"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
