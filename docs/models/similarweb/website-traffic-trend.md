# Similarweb Website Traffic Trend

`similarweb/website-traffic-trend` · api · Similarweb

Get a website's monthly traffic trend for chosen metrics over a date range.

## Pricing

- **$0.45 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/website-traffic-trend", "domain": "cnn.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/website-traffic-trend', {'domain': 'cnn.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/website-traffic-trend", {
  "domain": "cnn.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/website-traffic-trend", sandbase.Params{
	"domain": "cnn.com",
})
```

Same call via the path form: `POST /v1/api/similarweb/website-traffic-trend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | Bare website hostname without scheme, path, port, or credentials.  |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `metrics` | string |  | One to four supported Traffic & Engagement metrics. default `"visits"` |
| `end_date` | string |  | Inclusive last complete UTC month in YYYY-MM.  |
| `start_date` | string |  | Inclusive first month in YYYY-MM; provide together with end_date.  |

## Details

Get a website's monthly traffic trend for chosen metrics over a date range.

The response is the official Similarweb API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/website-traffic-trend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "cnn.com", "metrics": "visits", "start_date": "2026-09", "end_date": "2026-09"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `domain` | string | Yes | Bare website hostname without scheme, path, port, or credentials. |
| `end_date` | string | No | Inclusive last complete UTC month in YYYY-MM. |
| `metrics` | string | No | One to four supported Traffic & Engagement metrics. |
| `start_date` | string | No | Inclusive first month in YYYY-MM; provide together with end_date. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/website-traffic-trend.json`](../../../catalog/models/similarweb/website-traffic-trend.json) · Store page: https://www.sandbase.ai/model/similarweb/website-traffic-trend
