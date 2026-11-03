# Similarweb Deduplicated Audience API: pricing, parameters and code examples

`similarweb/deduplicated-audience` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.525 per call · **Modes:** sync

Get a website's deduplicated monthly audience across desktop and mobile web, with each platform's share.

## Pricing

- Depends on parameters (`params.end_date`, `params.start_date`).

Formula: `0.525 * Math.max(1.0, (params.start_date != nil && params.end_date != nil ? ((int(split(params.end_date, "-")[0]) - int(split(params.start_date, "-")[0])) * 12 + int(split(params.end_date, "-")[1]) - int(split(params.start_date, "-")[1]) + 1) * 1.0 : 12.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/deduplicated-audience", "domain": "cnn.com", "end_date": "2026-09", "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/deduplicated-audience', {'domain': 'cnn.com', 'end_date': '2026-09', 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/deduplicated-audience", {
  "domain": "cnn.com",
  "end_date": "2026-09",
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/deduplicated-audience", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/deduplicated-audience` with the body above minus `model`.

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

This API returns the deduplicated monthly audience of a website, counted once even if the same person visits on desktop and mobile web. It needs a `domain`, a `start_date` and an `end_date` in `YYYY-MM` format. The response gives visitor counts and shares for desktop only, mobile web only, and both platforms.

### Use cases

- Measure how many unique people reach a news site each month, without double counting people who use both desktop and phone.
- Compare the share of desktop-only and mobile-web-only readers to decide where to focus ad spend or site design.
- Track the size of the cross-device audience over several months to see if more users switch between platforms.
- Compare the deduplicated audience of two competing domains by calling the API once for each.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/deduplicated-audience" \
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
      "date": "2026-09-01",
      "desktop_and_mobile_web_audience_share": 0.32484400771842364,
      "desktop_and_mobile_web_audience_visitors": 9005207.086507518,
      "desktop_only_audience_share": 0.14004679349515559,
      "desktop_only_audience_visitors": 3882326.123492483,
      "mobile_web_only_audience_share": 0.5351091987864207,
      "mobile_web_only_audience_visitors": 14834102.013492484,
      "total_deduplicated_audience": 27721635.223492485
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
        "total_deduplicated_audience"
      ],
      "start_date": "2026-09-01"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].date` | First day of the month the row covers, such as `2026-09-01`. |
| `data[].total_deduplicated_audience` | Total unique visitors for the month across desktop and mobile web, with overlap counted once. |
| `data[].desktop_only_audience_visitors / data[].desktop_only_audience_share` | Visitors who used only desktop, and their share of the total audience. The share is a fraction between 0 and 1. |
| `data[].mobile_web_only_audience_visitors / data[].mobile_web_only_audience_share` | Visitors who used only mobile web, and their share of the total audience. |
| `data[].desktop_and_mobile_web_audience_visitors / data[].desktop_and_mobile_web_audience_share` | Visitors who used both desktop and mobile web, and their share of the total audience. |
| `meta.last_updated` | Date shown by the response as the last update, such as `2026-09-30`. |
| `meta.request` | Echo of the parameters the request used, with dates expanded to full days such as `2026-09-01` and `2026-09-30`. |
| `meta.status` | Shows `success` when the call worked. |

### Notes

- The three shares add up to 1, and the three visitor counts add up to `total_deduplicated_audience`.
- Use `YYYY-MM` for `start_date` and `end_date`. The response returns one row in `data` for each month in the range.
- `country` accepts only `ww` (worldwide) and `granularity` accepts only `monthly`.
- For more on a site's traffic, call [Similarweb Traffic & Engagement](/apis/similarweb/traffic-engagement) or [Similarweb Audience Overlap](/apis/similarweb/audience-overlap).

### Pricing

Billed at the actual cost of each call, about $0.525 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/deduplicated-audience.json`](../../../catalog/models/similarweb/deduplicated-audience.json) · Store page: https://www.sandbase.ai/model/similarweb/deduplicated-audience
