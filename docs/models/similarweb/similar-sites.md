# Similarweb SimilarSites

`similarweb/similar-sites` · api · Similarweb

Get websites similar to a domain, with affinity score, category and global rank. The date range must span exactly 3 months.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.375 * Math.max(1.0, Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/similar-sites", "domain": "cnn.com", "end_date": "2026-09", "limit": 1, "start_date": "2026-07"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/similar-sites', {'domain': 'cnn.com', 'end_date': '2026-09', 'limit': 1, 'start_date': '2026-07'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/similar-sites", {
  "domain": "cnn.com",
  "end_date": "2026-09",
  "limit": 1,
  "start_date": "2026-07"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/similar-sites", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"limit": 1,
	"start_date": "2026-07",
})
```

Same call via the path form: `POST /v1/api/similarweb/similar-sites` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer | yes | limit range 1–20 |
| `domain` | string | yes | domain  |
| `offset` | integer |  | offset range 0–100000 |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | End month (YYYY-MM). The range must span exactly 3 months, e.g. 2026-07 to 2026-09.  |
| `start_date` | string | yes | Start month (YYYY-MM). The range must span exactly 3 months, e.g. 2026-07 to 2026-09.  |
| `web_source` | string |  | web_source one of: `desktop`, `mobile_web`, `total` |
| `granularity` | string |  | granularity one of: `monthly` |
| `traffic_source` | string |  | traffic_source  |
| `main_domain_only` | boolean |  | main_domain_only  |

## Details

Get websites similar to a domain, with affinity score, category and global rank. The date range must span exactly 3 months.

The response is the official Similarweb API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/similar-sites" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "cnn.com", "start_date": "2026-07", "end_date": "2026-09", "limit": 1}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `domain` | string | Yes | domain |
| `end_date` | string | Yes | End month (YYYY-MM). The range must span exactly 3 months, e.g. 2026-07 to 2026-09. |
| `granularity` | string | No | granularity |
| `limit` | integer | Yes | limit |
| `main_domain_only` | boolean | No | main_domain_only |
| `offset` | integer | No | offset |
| `start_date` | string | Yes | Start month (YYYY-MM). The range must span exactly 3 months, e.g. 2026-07 to 2026-09. |
| `traffic_source` | string | No | traffic_source |
| `web_source` | string | No | web_source |

### Pricing

$0.375 per returned row (5 Similarweb credits), up to 20 rows; billed on rows returned. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/similar-sites.json`](../../../catalog/models/similarweb/similar-sites.json) · Store page: https://www.sandbase.ai/model/similarweb/similar-sites
