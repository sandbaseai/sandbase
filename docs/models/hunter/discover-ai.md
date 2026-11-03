# Hunter Discover Ai API: pricing, parameters and code examples

`hunter/discover-ai` · data API · Hunter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.1 per call · **Modes:** async

Describe target companies in plain language; an AI picks the filters and runs the search.

## Pricing

- **$0.1 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hunter/discover-ai", "query": "AI startups in Paris"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hunter/discover-ai', {'query': 'AI startups in Paris'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hunter/discover-ai", {
  "query": "AI startups in Paris"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hunter/discover-ai", sandbase.Params{
	"query": "AI startups in Paris",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/hunter/discover-ai` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Companies per page. Default and max 100. range 1–100 |
| `query` | string | yes | Natural-language description of the target companies, e.g. 'fintech startups in Singapore founded after 2020'.  |
| `offset` | integer |  | Companies to skip. Max 10,000. range 0–10000 |

## Details

This API turns a plain-language description of target companies into search filters and returns the matching companies. It needs one input, `query`, such as `AI startups in Paris`. Each result gives a company domain, name, and a count of email addresses found for it.

### Use cases

- Build a lead list of companies in a given city and sector for outbound sales.
- Check which filters the AI chose for a query, then reuse them in a structured search.
- Rank prospects by `emails_count.personal` to find companies with many named contacts.
- Size a market by reading the total number of matching companies in `meta.results`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/hunter/discover-ai" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "AI startups in Paris"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Natural-language description of the target companies, e.g. 'fintech startups in Singapore founded after 2020'. |
| `limit` | integer | No | Companies per page. Default and max 100. |
| `offset` | integer | No | Companies to skip. Max 10,000. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "domain": "oecd.ai",
      "emails_count": {
        "generic": 0,
        "personal": 67,
        "total": 67
      },
      "organization": "OECD.AI"
    }
  ],
  "meta": {
    "filters": {
      "headcount": [
        "1-10"
      ],
      "headquarters_location": {
        "include": [
          {
            "city": "Paris",
            "country": "FR"
          }
        ]
      },
      "keywords": {
        "include": [
          "ai"
        ],
        "match": "any"
      },
      "year_founded": {
        "from": 2020
      }
    },
    "limit": 100,
    "offset": 0,
    "params": {
      "query": "AI startups in Paris"
    },
    "results": 1612
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].domain` | Website domain of the company, for example `omi.so`. |
| `data[].organization` | Company name. |
| `data[].emails_count.total` | Total number of email addresses found for the domain. It equals `generic` plus `personal` in the sample. |
| `data[].emails_count.generic / data[].emails_count.personal` | Count of generic addresses and count of addresses tied to a person. |
| `meta.filters` | The filters the AI built from your `query`. In the sample these are headcount, headquarters location, keywords and founding year. |
| `meta.filters.headquarters_location.include[].city / meta.filters.headquarters_location.include[].country` | City and country code used to filter company headquarters. |
| `meta.filters.keywords.include` | Keywords the search matched on. `meta.filters.keywords.match` shows whether any or all must match. |
| `meta.results` | Total number of companies that match the filters, across all pages. |
| `meta.limit / meta.offset` | Page size and number of companies skipped for this response. |

### Notes

- The AI sets the filters, so read `meta.filters` to see how it interpreted your `query`. Rewrite the query if the filters look wrong.
- To page through results, increase `offset` by `limit`. `limit` is at most 100 and `offset` is at most 10,000.
- Use the `domain` value as input when you want more detail on a single company with [Hunter Companies Find](/apis/hunter/companies-find).

### Pricing

$0.1 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hunter/discover-ai.json`](../../../catalog/models/hunter/discover-ai.json) · Store page: https://www.sandbase.ai/model/hunter/discover-ai
