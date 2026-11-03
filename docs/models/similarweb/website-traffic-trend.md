# Similarweb Website Traffic Trend API: pricing, parameters and code examples

`similarweb/website-traffic-trend` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.45 per call · **Modes:** sync

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

Returns a month-by-month series of traffic metrics for one website, such as `visits`. It needs a bare `domain` and can take a month range and up to four metrics.

### Use cases

- Chart monthly `visits` for a news site over the past year to spot seasonal peaks.
- Compare the monthly traffic of a competitor domain against your own by calling the API once per domain.
- Track how a site's traffic changes after a redesign or a big news event.
- Pull several metrics for the same months to build a traffic report for a client.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/website-traffic-trend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "cnn.com", "metrics": "visits", "start_date": "2026-09", "end_date": "2026-09"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | Bare website hostname without scheme, path, port, or credentials. |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `end_date` | string | No | Inclusive last complete UTC month in YYYY-MM. |
| `metrics` | string | No | One to four supported Traffic & Engagement metrics. |
| `start_date` | string | No | Inclusive first month in YYYY-MM; provide together with end_date. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "domain": "cnn.com",
    "metrics": [
      "visits"
    ],
    "points": [
      {
        "month": "2026-09",
        "values": {
          "visits": 188658557.46746868
        }
      }
    ]
  },
  "meta": {
    "country": "ww",
    "end_date": "2026-09",
    "granularity": "monthly",
    "request_id": "imc_91aa25a81e679d4b7772b913a288205efd08f83d9fb1f33e22cd849fd23f7b4e",
    "retrieved_at": "2026-11-03T07:43:23.747988977Z",
    "source": "similarweb",
    "start_date": "2026-09"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.domain` | The website the series describes, echoed from the request. |
| `data.metrics` | List of the metrics included in the response, for example `visits`. |
| `data.points[].month` | The month for this data point, in `YYYY-MM` format. |
| `data.points[].values.visits` | The value of the `visits` metric for that month. The response shows it as a decimal number, so round it before display. Other requested metrics appear as sibling keys under `values`. |
| `meta.country` | The region the data covers. The response shows `ww`. |
| `meta.start_date / meta.end_date` | The first and last month of the range the response covers. |
| `meta.granularity` | Time step between points. The response shows `monthly`. |
| `meta.retrieved_at` | UTC timestamp of when the data was fetched. |

### Notes

- Send `start_date` and `end_date` together, both in `YYYY-MM` format. `end_date` must be a complete UTC month.
- Pass `domain` as a bare hostname such as `cnn.com`, with no scheme, path or port.
- `metrics` takes one to four values in a single string. It defaults to `visits`.
- For a single-period view, see [Similarweb Website Traffic Snapshot](/apis/similarweb/website-traffic-snapshot). For more engagement metrics, see [Similarweb Traffic & Engagement](/apis/similarweb/traffic-engagement).

### Pricing

$0.45 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/website-traffic-trend.json`](../../../catalog/models/similarweb/website-traffic-trend.json) · Store page: https://www.sandbase.ai/model/similarweb/website-traffic-trend
