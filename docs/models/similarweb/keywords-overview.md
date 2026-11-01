# Similarweb Keywords Overview

`similarweb/keywords-overview` · api · Similarweb

Get search metrics for keywords: clicks, volume, CPC, competition, intent and SERP features such as AI Overviews.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `1.275 * Math.max(1.0, Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/keywords-overview", "end_date": "2026-09", "granularity": "monthly", "keywords": "running shoes", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/keywords-overview', {'end_date': '2026-09', 'granularity': 'monthly', 'keywords': 'running shoes', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/keywords-overview", {
  "end_date": "2026-09",
  "granularity": "monthly",
  "keywords": "running shoes",
  "limit": 1,
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/keywords-overview", sandbase.Params{
	"end_date": "2026-09",
	"granularity": "monthly",
	"keywords": "running shoes",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/keywords-overview` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer | yes | limit range 1–20 |
| `format` | string |  | format one of: `json` |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | end_date  |
| `keywords` | string | yes | keywords  |
| `start_date` | string | yes | start_date  |
| `web_source` | string |  | web_source one of: `total` |
| `granularity` | string | yes | granularity one of: `monthly` |
| `main_domain_only` | boolean |  | main_domain_only  |

## Details

Get search metrics for keywords: clicks, volume, CPC, competition, intent and SERP features such as AI Overviews.

The response is the official Similarweb API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/keywords-overview" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "keywords": "running shoes", "limit": 1, "granularity": "monthly"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `end_date` | string | Yes | end_date |
| `format` | string | No | format |
| `granularity` | string | Yes | granularity |
| `keywords` | string | Yes | keywords |
| `limit` | integer | Yes | limit |
| `main_domain_only` | boolean | No | main_domain_only |
| `start_date` | string | Yes | start_date |
| `web_source` | string | No | web_source |

### Pricing

$1.275 per returned row (17 Similarweb credits), up to 20 rows; billed on rows returned. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/keywords-overview.json`](../../../catalog/models/similarweb/keywords-overview.json) · Store page: https://www.sandbase.ai/model/similarweb/keywords-overview
