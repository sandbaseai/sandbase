# Similarweb Marketing Channel Sources API: pricing, parameters and code examples

`similarweb/marketing-channel-sources-legacy` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.525 per call · **Modes:** sync

Get a website's visits by marketing channel (direct, search, social, referrals, mail, display) month by month.

## Pricing

- Depends on parameters (`params.end_date`, `params.start_date`).

Formula: `0.525 * Math.max(1.0, (params.start_date != nil && params.end_date != nil ? ((int(split(params.end_date, "-")[0]) - int(split(params.start_date, "-")[0])) * 12 + int(split(params.end_date, "-")[1]) - int(split(params.start_date, "-")[1]) + 1) * 1.0 : 12.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/marketing-channel-sources-legacy", "domain": "cnn.com", "end_date": "2026-09", "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/marketing-channel-sources-legacy', {'domain': 'cnn.com', 'end_date': '2026-09', 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/marketing-channel-sources-legacy", {
  "domain": "cnn.com",
  "end_date": "2026-09",
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/marketing-channel-sources-legacy", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/marketing-channel-sources-legacy` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | domain  |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | end_date  |
| `start_date` | string | yes | start_date  |
| `web_source` | string |  | web_source one of: `desktop`, `mobile_web`, `total` |
| `granularity` | string |  | granularity one of: `monthly`; default `"monthly"` |
| `main_domain_only` | boolean |  | main_domain_only default `true` |

## Details

Returns estimated website visits split by marketing channel for each month in a date range. It needs a `domain`, a `start_date` and an `end_date` in `YYYY-MM` format.

### Use cases

- Compare how much of a competitor's traffic comes from direct visits versus display ads or mail.
- Track month by month how a site's channel mix changes after a campaign.
- Build a channel breakdown chart for a domain in a market research report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/marketing-channel-sources-legacy" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domain": "cnn.com", "granularity": "monthly"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | domain |
| `end_date` | string | Yes | end_date |
| `start_date` | string | Yes | start_date |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `granularity` | string | No | granularity |
| `main_domain_only` | boolean | No | main_domain_only |
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
      "pages_per_visit": null,
      "source_type": "Direct",
      "visits": 124416521.07111368
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
      "web_source": "total"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One row per channel and month. The response lists one row for each `source_type` in each month of the range. |
| `data[].source_type` | The marketing channel for the row, such as `Direct`, `Display Ads` or `Mail`. |
| `data[].visits` | Estimated number of visits from that channel in that month. The value is a decimal number. |
| `data[].date` | First day of the month the row covers, in `YYYY-MM-DD` format, for example `2026-09-01`. |
| `data[].average_visit_duration / bounce_rate / pages_per_visit` | Engagement metrics for the channel. They are `null` in this response, because only the `visits` metric was returned. |
| `meta.request.metrics` | List of metrics returned for the request. This response contains `visits` only. |
| `meta.request.web_source` | Device scope used for the data. This response used `total`. |
| `meta.last_updated` | Date of the most recent data update, for example `2026-09-30`. |

### Notes

- Pass dates as `YYYY-MM`. The echoed request in `meta.request` shows them expanded to the first and last day of the month.
- `country` accepts only `ww`, which is worldwide data. `granularity` accepts only `monthly`.
- Set `web_source` to `desktop`, `mobile_web` or `total` to choose the device scope. The response showed `total` when it was not set.
- To see which sites send referral traffic, call [Similarweb Referrals](/apis/similarweb/referrals). For total visits over time, call [Similarweb Website Traffic Trend](/apis/similarweb/website-traffic-trend).

### Pricing

Billed at the actual cost of each call, about $0.525 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/marketing-channel-sources-legacy.json`](../../../catalog/models/similarweb/marketing-channel-sources-legacy.json) · Store page: https://www.sandbase.ai/model/similarweb/marketing-channel-sources-legacy
