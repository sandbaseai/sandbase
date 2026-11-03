# Similarweb Landing Pages API: pricing, parameters and code examples

`similarweb/search-landing-pages` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.15 per call · **Modes:** sync

Get the landing pages that receive a website's search traffic, with clicks, keyword counts and desktop/mobile split.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.075 * Math.max(1.0, Math.ceil(Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0) * 100000.0 / 1000000.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/search-landing-pages", "domain": "cnn.com", "end_date": "2026-09", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/search-landing-pages', {'domain': 'cnn.com', 'end_date': '2026-09', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/search-landing-pages", {
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
run, err := c.Run(ctx, "similarweb/search-landing-pages", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/search-landing-pages` with the body above minus `model`.

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

Returns the landing pages that receive search traffic for a website on Similarweb. Each row has estimated clicks, keyword count, traffic share and desktop/mobile split. You send a `domain`, a `start_date`, an `end_date` and a `limit`.

### Use cases

- Find which pages on a news site bring in the most organic search clicks.
- Compare how much search traffic goes to the home page versus deeper article pages.
- Check the desktop and mobile split of search visits for a competitor's top pages.
- Spot pages that rank for many keywords to plan content updates.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/search-landing-pages" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domain": "cnn.com", "limit": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | domain |
| `end_date` | string | Yes | end_date |
| `limit` | integer | Yes | limit |
| `start_date` | string | Yes | start_date |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `granularity` | string | No | granularity |
| `main_domain_only` | boolean | No | main_domain_only |
| `offset` | integer | No | offset |
| `traffic_source` | string | No | traffic_source |
| `web_source` | string | No | web_source |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "ads": null,
      "clicks": 5016867.363643058,
      "desktop_share": 0.5662671565382268,
      "keywords": 1603,
      "mobile_share": 0.43373284346177327,
      "serp_features": [
        "organic"
      ],
      "spend": null,
      "top_keyword": "cnn",
      "traffic_share": 0.16950791592879255,
      "url": "cnn.com"
    }
  ],
  "meta": {
    "last_updated": "2026-09-30",
    "query": {
      "asc": null,
      "limit": 1,
      "offset": 0,
      "sort": null
    },
    "request": {
      "country": "ww",
      "domain": "cnn.com",
      "end_date": "2026-09-30",
      "format": "json",
      "granularity": "monthly",
      "start_date": "2026-09-01",
      "traffic_source": "organic",
      "web_source": "total"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].url` | The landing page URL. A value like `cnn.com` means the domain's home page. |
| `data[].clicks` | Estimated search clicks to this page in the selected period. |
| `data[].keywords` | Number of keywords that send search traffic to this page. |
| `data[].top_keyword` | The keyword that sends the most search traffic to this page. |
| `data[].traffic_share` | Share of the domain's search traffic that goes to this page, as a fraction of 1. |
| `data[].desktop_share / data[].mobile_share` | Share of the page's clicks from desktop and from mobile web. The two values add up to 1. |
| `data[].serp_features` | List of search result types the page appears in, such as `organic` and `organic_sitelinks`. |
| `data[].ads / data[].spend` | Ad and spend values for the page. Both are `null` in this response. |
| `meta.request.traffic_source / meta.request.web_source` | The traffic source and device filter the call used. This response shows `organic` and `total`. |

### Notes

- Send dates as `YYYY-MM`. The response echoes them as full dates, such as `2026-09-01` and `2026-09-30`.
- Use `limit` (1 to 20) and `offset` to page through the landing pages of a domain.
- Set `web_source` to `desktop`, `mobile_web` or `total` to choose the device filter.
- To see the keywords behind a domain's search traffic, call [Similarweb Website Keywords](/apis/similarweb/search-website-keywords).

### Pricing

Billed at the actual cost of each call, about $0.15 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/search-landing-pages.json`](../../../catalog/models/similarweb/search-landing-pages.json) · Store page: https://www.sandbase.ai/model/similarweb/search-landing-pages
