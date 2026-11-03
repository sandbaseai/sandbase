# Similarweb Website Traffic Snapshot API: pricing, parameters and code examples

`similarweb/website-traffic-snapshot` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.3 per call · **Modes:** sync

Get a one-month snapshot of a website's traffic: visits, visit duration, pages per visit and bounce rate.

## Pricing

- **$0.3 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/website-traffic-snapshot", "domain": "cnn.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/website-traffic-snapshot', {'domain': 'cnn.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/website-traffic-snapshot", {
  "domain": "cnn.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/website-traffic-snapshot", sandbase.Params{
	"domain": "cnn.com",
})
```

Same call via the path form: `POST /v1/api/similarweb/website-traffic-snapshot` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `month` | string |  | Complete month in YYYY-MM.  |
| `domain` | string | yes | Bare website hostname without scheme, path, port, or credentials.  |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |

## Details

Returns a one-month traffic snapshot for a website: visits, average visit duration, pages per visit and bounce rate. It needs a bare hostname in `domain`, such as `cnn.com`. You can pass a complete month in `month`.

### Use cases

- Compare the monthly visit count of a competitor's site with your own.
- Check whether a site's visitors stay and browse by reading its bounce rate and pages per visit.
- Add a traffic figure to a lead list or an investment screen for each domain.
- Pull a single month's engagement numbers for a report without fetching a full time series.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/website-traffic-snapshot" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "cnn.com"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | Bare website hostname without scheme, path, port, or credentials. |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `month` | string | No | Complete month in YYYY-MM. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "domain": "cnn.com",
    "metrics": {
      "average_visit_duration": 197.57361621705832,
      "bounce_rate": 0.6352565984600038,
      "pages_per_visit": 1.9900475193331115,
      "visits": 188658557.46746868
    },
    "month": "2026-09"
  },
  "meta": {
    "country": "ww",
    "end_date": "2026-09",
    "granularity": "monthly",
    "request_id": "imc_fefb0e65533d7032dd730ff1f2aa41eb6bb6f3bef45533349755e5e34fd75281",
    "retrieved_at": "2026-11-03T07:43:23.674777096Z",
    "source": "similarweb",
    "start_date": "2026-09"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.domain` | The hostname the metrics describe. |
| `data.month` | The month the snapshot covers, in `YYYY-MM` format. |
| `data.metrics.visits` | Estimated number of visits to the site in that month. The value is a decimal, so round it for display. |
| `data.metrics.average_visit_duration` | Average length of a visit. The value is not labeled with a unit, so check it against a known site before you display it. |
| `data.metrics.pages_per_visit` | Average number of pages viewed in one visit. |
| `data.metrics.bounce_rate` | Share of visits that left after one page, as a fraction between 0 and 1. A value of `0.635` means about 63.5%. |
| `meta.country` | The country scope of the data. Only `ww` (worldwide) is supported. |
| `meta.start_date / meta.end_date` | The first and last month covered. They match `data.month` for a snapshot. |
| `meta.granularity` | How the data is bucketed. This API returns `monthly`. |

### Notes

- Pass the hostname only. Leave out the scheme, path, port and credentials.
- If you omit `month`, the response still returns a month in `data.month`. Set `month` to a complete month in `YYYY-MM` format to choose one yourself.
- `country` accepts only `ww`, and the value is case-insensitive.
- To see how visits change over several months, call [Similarweb Website Traffic Trend](/apis/similarweb/website-traffic-trend). For more engagement detail, try [Similarweb Traffic & Engagement](/apis/similarweb/traffic-engagement).

### Pricing

$0.3 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/website-traffic-snapshot.json`](../../../catalog/models/similarweb/website-traffic-snapshot.json) · Store page: https://www.sandbase.ai/model/similarweb/website-traffic-snapshot
