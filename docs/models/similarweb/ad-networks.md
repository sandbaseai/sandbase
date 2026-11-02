# Similarweb Ad Networks API: pricing, parameters and code examples

`similarweb/ad-networks` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.225 per call · **Modes:** sync

Get the ad networks behind a website's display-ad traffic, with each network's traffic share and change over the selected months.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.225 * Math.max(1.0, Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/ad-networks", "domain": "cnn.com", "end_date": "2026-09", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/ad-networks', {'domain': 'cnn.com', 'end_date': '2026-09', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/ad-networks", {
  "domain": "cnn.com",
  "end_date": "2026-09",
  "limit": 1,
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/ad-networks", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/ad-networks` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer | yes | limit range 1–20 |
| `domain` | string | yes | domain  |
| `offset` | integer |  | offset range 0–100000 |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | end_date  |
| `start_date` | string | yes | start_date  |
| `web_source` | string |  | web_source one of: `desktop`, `mobile_web`, `total` |
| `granularity` | string |  | granularity one of: `monthly` |
| `traffic_source` | string |  | traffic_source  |
| `main_domain_only` | boolean |  | main_domain_only  |

## Details

Get the ad networks behind a website's display-ad traffic, with each network's traffic share and change over the selected months.

The response is the official Similarweb API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/ad-networks" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domain": "cnn.com", "limit": 1, "granularity": "monthly"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `domain` | string | Yes | domain |
| `end_date` | string | Yes | end_date |
| `granularity` | string | No | granularity |
| `limit` | integer | Yes | limit |
| `main_domain_only` | boolean | No | main_domain_only |
| `offset` | integer | No | offset |
| `start_date` | string | Yes | start_date |
| `traffic_source` | string | No | traffic_source |
| `web_source` | string | No | web_source |

### Pricing

$0.225 per returned row (3 Similarweb credits), up to 20 rows; billed on rows returned. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/ad-networks.json`](../../../catalog/models/similarweb/ad-networks.json) · Store page: https://www.sandbase.ai/model/similarweb/ad-networks
