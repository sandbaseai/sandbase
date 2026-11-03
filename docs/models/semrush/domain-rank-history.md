# Semrush Domain Rank History API: pricing, parameters and code examples

`semrush/domain-rank-history` · data API · Semrush · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02 per call · **Modes:** sync

Monthly history of a domain's Semrush rank, organic keywords, organic traffic and traffic cost.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/domain-rank-history", "database": "us", "domain": "nike.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('semrush/domain-rank-history', {'database': 'us', 'domain': 'nike.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("semrush/domain-rank-history", {
  "database": "us",
  "domain": "nike.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "semrush/domain-rank-history", sandbase.Params{
	"database": "us",
	"domain": "nike.com",
})
```

Same call via the path form: `POST /v1/api/semrush/domain-rank-history` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | Domain to analyze, e.g. "nike.com".  |
| `database` | string | yes | Regional Semrush database, e.g. "us", "uk", "de".  |

## Details

Returns a monthly history of a domain's Semrush rank, organic keywords, organic traffic and organic cost. It needs a regional Semrush `database` and a `domain`. The response is a semicolon-separated text table with a header line and one row per period.

### Use cases

- Chart how many organic keywords nike.com ranks for over time.
- Spot sudden drops in organic traffic that point to a ranking loss.
- Compare the growth of organic cost against organic traffic for a competitor.
- Track a domain's Semrush rank before and after a content or link-building campaign.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/semrush/domain-rank-history" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"database": "us", "domain": "nike.com"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `database` | string | Yes | Regional Semrush database, e.g. "us", "uk", "de". |
| `domain` | string | Yes | Domain to analyze, e.g. "nike.com". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
"Rank;Organic Keywords;Organic Traffic;Organic Cost\r\n76;3789540;26551513;13860391…"
```

### Response fields

| Field | Meaning |
|---|---|
| `[].1` | First column, headed `Rank`. It holds the domain's Semrush rank for that row. The first data row shows `76`. |
| `[].2` | Second column, headed `Organic Keywords`. It holds the number of organic keywords counted for the domain in that row. The first data row shows `3789540`. |
| `[].3` | Third column, headed `Organic Traffic`. It holds the organic traffic figure for the domain in that row. The first data row shows `26551513`. |
| `[].4` | Fourth column, headed `Organic Cost`. It holds the organic cost figure for the domain in that row. The first data row shows `13860391`. |

### Notes

- The response is plain text, not JSON. Lines are separated by `\r\n` and columns by `;`. The first line is the header, and each later line is one row.
- The response shown has no date column. Do not assume a date for a row beyond its position in the list.
- Set `database` to a regional code such as `us`, `uk` or `de`. Pass the bare domain, such as `nike.com`.
- For a current snapshot of the same domain, call [Semrush Domain Overview](/apis/semrush/domain-overview). For the keywords behind the traffic, call [Semrush Domain Organic Keywords](/apis/semrush/domain-organic-keywords).

### Pricing

Billed at the actual cost of each call, about $0.02 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/semrush/domain-rank-history.json`](../../../catalog/models/semrush/domain-rank-history.json) · Store page: https://www.sandbase.ai/model/semrush/domain-rank-history
