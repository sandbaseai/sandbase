# Similarweb Demographics - Specific Groups

`similarweb/traffic-by-demographics-aggregated` · api · Similarweb

Get the traffic share of one visitor age group on a website for the selected period.

## Pricing

- Depends on parameters (`params.end_date`, `params.metrics`, `params.start_date`).

Formula: `0.45 * Math.max(1.0, len(split(params.metrics ?? "share", ",")) * 1.0) * Math.max(1.0, ((int(split(params.end_date, "-")[0]) - int(split(params.start_date, "-")[0])) * 12 + int(split(params.end_date, "-")[1]) - int(split(params.start_date, "-")[1]) + 1) * 1.0)`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/traffic-by-demographics-aggregated", "age_bucket": "25", "domain": "cnn.com", "end_date": "2026-09", "granularity": "monthly", "metrics": "share", "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/traffic-by-demographics-aggregated', {'age_bucket': '25', 'domain': 'cnn.com', 'end_date': '2026-09', 'granularity': 'monthly', 'metrics': 'share', 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/traffic-by-demographics-aggregated", {
  "age_bucket": "25",
  "domain": "cnn.com",
  "end_date": "2026-09",
  "granularity": "monthly",
  "metrics": "share",
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/traffic-by-demographics-aggregated", sandbase.Params{
	"age_bucket": "25",
	"domain": "cnn.com",
	"end_date": "2026-09",
	"granularity": "monthly",
	"metrics": "share",
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/traffic-by-demographics-aggregated` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | domain  |
| `format` | string |  | format one of: `json` |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `metrics` | string | yes | Comma-separated metrics. Supported: share.  |
| `end_date` | string | yes | end_date  |
| `age_bucket` | string | yes | Select one age bucket; age_bucket must be provided exactly once. one of: `18`, `25`, `35`, `45`, `55`, `65` |
| `start_date` | string | yes | start_date  |
| `web_source` | string |  | web_source one of: `total` |
| `granularity` | string | yes | granularity one of: `monthly` |
| `main_domain_only` | boolean |  | main_domain_only  |

## Details

Get the traffic share of one visitor age group on a website for the selected period.

The response is the official Similarweb API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/traffic-by-demographics-aggregated" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "cnn.com", "start_date": "2026-09", "end_date": "2026-09", "granularity": "monthly", "metrics": "share", "age_bucket": "25"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `age_bucket` | string | Yes | Select one age bucket; age_bucket must be provided exactly once. |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `domain` | string | Yes | domain |
| `end_date` | string | Yes | end_date |
| `format` | string | No | format |
| `granularity` | string | Yes | granularity |
| `main_domain_only` | boolean | No | main_domain_only |
| `metrics` | string | Yes | Comma-separated metrics. Supported: share. |
| `start_date` | string | Yes | start_date |
| `web_source` | string | No | web_source |

### Pricing

$0.45 per metric per month between start_date and end_date. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/traffic-by-demographics-aggregated.json`](../../../catalog/models/similarweb/traffic-by-demographics-aggregated.json) · Store page: https://www.sandbase.ai/model/similarweb/traffic-by-demographics-aggregated
