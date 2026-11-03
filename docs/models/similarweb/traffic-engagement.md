# Similarweb Traffic & Engagement API: pricing, parameters and code examples

`similarweb/traffic-engagement` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.075 per call · **Modes:** sync

Get a website's traffic and engagement metrics month by month: visits, page views, visit duration, bounce rate and more.

## Pricing

- Depends on parameters (`params.end_date`, `params.metrics`, `params.start_date`).

Formula: `0.075 * Math.max(1.0, len(split(params.metrics ?? "visits", ",")) * 1.0) * Math.max(1.0, (params.start_date != nil && params.end_date != nil ? ((int(split(params.end_date, "-")[0]) - int(split(params.start_date, "-")[0])) * 12 + int(split(params.end_date, "-")[1]) - int(split(params.start_date, "-")[1]) + 1) * 1.0 : 12.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/traffic-engagement", "domain": "cnn.com", "end_date": "2026-09", "metrics": "visits", "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/traffic-engagement', {'domain': 'cnn.com', 'end_date': '2026-09', 'metrics': 'visits', 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/traffic-engagement", {
  "domain": "cnn.com",
  "end_date": "2026-09",
  "metrics": "visits",
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/traffic-engagement", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"metrics": "visits",
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/traffic-engagement` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mtd` | boolean |  | mtd  |
| `domain` | string | yes | domain  |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `metrics` | string | yes | metrics  |
| `end_date` | string | yes | end_date  |
| `start_date` | string | yes | start_date  |
| `web_source` | string |  | web_source one of: `desktop`, `mobile_web`, `total` |
| `granularity` | string |  | granularity one of: `monthly`; default `"monthly"` |
| `main_domain_only` | boolean |  | main_domain_only default `true` |

## Details

Returns monthly traffic and engagement metrics for a website, such as visits, page views, visit duration and bounce rate. You send a `domain`, a `start_date` and `end_date` in `YYYY-MM` format, and the `metrics` you want.

### Use cases

- Track monthly visits for a news site over a date range.
- Compare a competitor's traffic month by month against your own site.
- Pull bounce rate and pages per visit to check how engaged a site's visitors are.
- Build a traffic time series for a domain to feed a dashboard or report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/traffic-engagement" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domain": "cnn.com", "metrics": "visits", "granularity": "monthly"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | domain |
| `end_date` | string | Yes | end_date |
| `metrics` | string | Yes | metrics |
| `start_date` | string | Yes | start_date |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `granularity` | string | No | granularity |
| `main_domain_only` | boolean | No | main_domain_only |
| `mtd` | boolean | No | mtd |
| `web_source` | string | No | web_source |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "average_visit_duration": null,
      "bounce_rate": null,
      "date": "2026-09-01",
      "new_users": null,
      "page_views": null,
      "pages_per_visit": null,
      "returning_users": null,
      "unique_visitors": null,
      "visits": 188658557.46746868
    }
  ],
  "meta": {
    "last_updated": "2026-09-30",
    "request": {
      "country": "ww",
      "domain": "cnn.com",
      "end_date": "2026-09-30",
      "format": "json",
      "granularity": "monthly",
      "main_domain_only": true,
      "metrics": [
        "visits"
      ],
      "mtd": false,
      "start_date": "2026-09-01",
      "state": null,
      "web_source": "total",
      "week_start_day": "default"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].date` | First day of the month the row covers, for example `2026-09-01`. |
| `data[].visits` | Estimated number of visits to the domain in that month. This is a decimal number, not a rounded count. |
| `data[].page_views / data[].unique_visitors` | Page view and unique visitor counts for the month. They are `null` unless you request those metrics. |
| `data[].average_visit_duration / data[].bounce_rate / data[].pages_per_visit` | Engagement metrics for the month. They are `null` unless you request them in `metrics`. |
| `data[].new_users / data[].returning_users` | Split of new and returning users for the month. They are `null` when not requested. |
| `meta.last_updated` | Date of the most recent data update, shown as `YYYY-MM-DD`. |
| `meta.request.web_source` | Traffic source the data covers. The response shows `total` when you do not set `web_source`. |
| `meta.request.metrics` | List of the metrics the call applied. |
| `meta.status` | Shows `success` when the call worked. |

### Notes

- Metrics you do not request come back as `null` in each `data[]` row, so set `metrics` to the ones you need.
- Send `start_date` and `end_date` as `YYYY-MM`. The response echoes them as full dates, such as `2026-09-01` and `2026-09-30`.
- Set `web_source` to `desktop`, `mobile_web` or `total` to pick the traffic source. `country` accepts only `ww` (worldwide) and `granularity` accepts only `monthly`.
- For a ready-made trend view, see [Similarweb Website Traffic Trend](/apis/similarweb/website-traffic-trend) or [Similarweb Website Traffic Snapshot](/apis/similarweb/website-traffic-snapshot).

### Pricing

Billed at the actual cost of each call, about $0.075 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/traffic-engagement.json`](../../../catalog/models/similarweb/traffic-engagement.json) · Store page: https://www.sandbase.ai/model/similarweb/traffic-engagement
