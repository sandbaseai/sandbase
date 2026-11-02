# TikTok Ad Transparency Search API: pricing, parameters and code examples

`tiktok/ad-transparency-search` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

Search TikTok's EU Commercial Content Library by keyword or advertiser ID.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ad-transparency-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ad-transparency-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ad-transparency-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ad-transparency-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/ad-transparency-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `days` | integer |  | Number of days of Commercial Content Library history to search, from 1 to 365. Defaults to 30. default `30`; range 1–365 |
| `sort` | string |  | Upstream sort expression. Defaults to last_shown_date,desc. default `"last_shown_date,desc"` |
| `limit` | integer |  | Maximum number of ads to return, from 1 to 50. Defaults to 20. Billing is flat per request. default `20`; range 1–50 |
| `query` | string |  | Keyword to search in TikTok's EU Commercial Content Library. Provide query or advertiserId.  |
| `cursor` | string |  | Search cursor from a previous response's nextCursor.  |
| `offset` | integer |  | Zero-based result offset. Defaults to 0. default `0`; range 0– |
| `region` | string |  | Region code for the transparency search. Defaults to DE. default `"DE"` |
| `advertiserId` | string |  | TikTok Commercial Content Library advertiser ID. Provide advertiserId or query.  |

## Details

Search TikTok's EU Commercial Content Library by keyword or advertiser ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ad-transparency-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"days": 30, "limit": 20, "query": "nike", "region": "DE"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `advertiserId` | string | No | TikTok Commercial Content Library advertiser ID. Provide advertiserId or query. |
| `cursor` | string | No | Search cursor from a previous response's nextCursor. |
| `days` | integer | No | Number of days of Commercial Content Library history to search, from 1 to 365. Defaults to 30. |
| `limit` | integer | No | Maximum number of ads to return, from 1 to 50. Defaults to 20. Billing is flat per request. |
| `offset` | integer | No | Zero-based result offset. Defaults to 0. |
| `query` | string | No | Keyword to search in TikTok's EU Commercial Content Library. Provide query or advertiserId. |
| `region` | string | No | Region code for the transparency search. Defaults to DE. |
| `sort` | string | No | Upstream sort expression. Defaults to last_shown_date,desc. |

### Pricing

Billed at the actual cost of each call, usually $0.0008 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/ad-transparency-search.json`](../../../catalog/models/tiktok/ad-transparency-search.json) · Store page: https://www.sandbase.ai/model/tiktok/ad-transparency-search
