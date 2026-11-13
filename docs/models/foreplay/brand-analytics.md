# Foreplay Brand Ad Analytics API: pricing, parameters and code examples

`foreplay/brand-analytics` · data API · Foreplay · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.1225 per call · **Modes:** sync

Get ad analytics for a brand by Foreplay brand ID: active and total ads, formats, platforms, launch cadence and longest-running creatives over a date range.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.1225**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "foreplay/brand-analytics", "id": "3YfFtyvZ3viTAbbLaWLV"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('foreplay/brand-analytics', {'id': '3YfFtyvZ3viTAbbLaWLV'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("foreplay/brand-analytics", {
  "id": "3YfFtyvZ3viTAbbLaWLV"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "foreplay/brand-analytics", sandbase.Params{
	"id": "3YfFtyvZ3viTAbbLaWLV",
})
```

Same call via the path form: `POST /v1/api/foreplay/brand-analytics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Page ID or Brand ID. Brand IDs are 20-25 character alphanumeric strings with mixed case. Page IDs are numeric Facebook page identifiers.  |
| `order` | string |  | Order of results: 'newest' (default), 'oldest', 'longest_running', or 'most_relevant'. Sorts ads by creation date, longest running duration, or relevance to the search query. one of: `newest`, `oldest`, `longest_running`, `most_relevant`; default `"newest"` |
| `end_date` | string |  | End date (inclusive). Format: 'YYYY-MM-DD', 'YYYY-MM-DDTHH:MM:SS', or 'YYYY-MM-DD HH:MM:SS'. If you provide only the date (e.g. '2024-11-12'), it will be interpreted as '2024-11-12 00:00:00'. To include all results for…  |
| `start_date` | string |  | Start date (inclusive). Format: 'YYYY-MM-DD', 'YYYY-MM-DDTHH:MM:SS', or 'YYYY-MM-DD HH:MM:SS'. If you provide only the date (e.g. '2024-11-12'), it will be interpreted as '2024-11-12 00:00:00'. To get all ads from a…  |

## Details

Get ad analytics for a brand by Foreplay brand ID: active and total ads, formats, platforms, launch cadence and longest-running creatives over a date range.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/foreplay/brand-analytics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "3YfFtyvZ3viTAbbLaWLV"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Page ID or Brand ID. Brand IDs are 20-25 character alphanumeric strings with mixed case. Page IDs are numeric Facebook page identifiers. |
| `end_date` | string | No | End date (inclusive). Format: 'YYYY-MM-DD', 'YYYY-MM-DDTHH:MM:SS', or 'YYYY-MM-DD HH:MM:SS'. If you provide only the date (e.g. '2024-11-12'), it will be interpreted as '2024-11-12 00:00:00'. To include all results for a |
| `order` | string | No | Order of results: 'newest' (default), 'oldest', 'longest_running', or 'most_relevant'. Sorts ads by creation date, longest running duration, or relevance to the search query. |
| `start_date` | string | No | Start date (inclusive). Format: 'YYYY-MM-DD', 'YYYY-MM-DDTHH:MM:SS', or 'YYYY-MM-DD HH:MM:SS'. If you provide only the date (e.g. '2024-11-12'), it will be interpreted as '2024-11-12 00:00:00'. To get all ads from a spec |

### Pricing

Billed at the actual upstream cost of each call (about $0.1225 for the request above). Failed calls are not charged.

---
Machine-readable: [`catalog/models/foreplay/brand-analytics.json`](../../../catalog/models/foreplay/brand-analytics.json) · Store page: https://www.sandbase.ai/model/foreplay/brand-analytics
