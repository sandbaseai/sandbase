# Similarweb Website Keywords API: pricing, parameters and code examples

`similarweb/search-website-keywords` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.15 per call · **Modes:** sync

Get the search keywords a website's search traffic comes from, with clicks, position, competition and search intent.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.075 * Math.max(1.0, Math.ceil(Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0) * 100000.0 / 1000000.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/search-website-keywords", "domain": "cnn.com", "end_date": "2026-09", "granularity": "monthly", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/search-website-keywords', {'domain': 'cnn.com', 'end_date': '2026-09', 'granularity': 'monthly', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/search-website-keywords", {
  "domain": "cnn.com",
  "end_date": "2026-09",
  "granularity": "monthly",
  "limit": 1,
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/search-website-keywords", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"granularity": "monthly",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/search-website-keywords` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer | yes | limit range 1–20 |
| `domain` | string | yes | domain  |
| `format` | string |  | format one of: `json` |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | end_date  |
| `start_date` | string | yes | start_date  |
| `web_source` | string |  | web_source one of: `total` |
| `granularity` | string | yes | granularity one of: `monthly` |
| `main_domain_only` | boolean |  | main_domain_only  |

## Details

Returns the search keywords that send traffic to a website, with clicks, traffic share, competition, search intent and SERP features for each keyword. It needs a `domain`, a `start_date` and `end_date` in `YYYY-MM` format, a `granularity` of `monthly` and a `limit`.

### Use cases

- Find which keywords bring the most search clicks to a competitor's site.
- Split a site's top keywords into navigational and informational intent to see how much traffic is brand-driven.
- Check which SERP features, such as news or video, appear for a site's top keywords.
- Find the keywords with the highest `traffic_share` for a domain as a starting point for content planning.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/search-website-keywords" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domain": "cnn.com", "limit": 1, "granularity": "monthly"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | domain |
| `end_date` | string | Yes | end_date |
| `granularity` | string | Yes | granularity |
| `limit` | integer | Yes | limit |
| `start_date` | string | Yes | start_date |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `format` | string | No | format |
| `main_domain_only` | boolean | No | main_domain_only |
| `web_source` | string | No | web_source |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "clicks": 7199467.86166735,
      "competition": 0,
      "keyword": "cnn",
      "position": null,
      "primary_intent": "Navigational",
      "secondary_intent": "Informational",
      "serp_features": [
        "news"
      ],
      "top_url": "cnn.com",
      "traffic_share": 0.2427171438297492,
      "url_count": 1291
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
      "branded_type": "all",
      "country": "ww",
      "domain": "cnn.com",
      "end_date": "2026-09-30",
      "format": "json",
      "granularity": "monthly",
      "keywords_filter_rules": [],
      "metrics": [
        "clicks"
      ],
      "start_date": "2026-09-01",
      "traffic_source": "all",
      "web_source": "total"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].keyword` | The search keyword that sends traffic to the domain. |
| `data[].clicks` | Estimated number of search clicks for this keyword in the requested period. |
| `data[].traffic_share` | This keyword's share of the domain's search traffic, as a fraction. A value of `0.24` means about 24%. |
| `data[].position` | Ranking position of the domain for the keyword. It can be `null` when no position is returned. |
| `data[].competition` | Competition value for the keyword. The sample row returns `0`. |
| `data[].primary_intent / data[].secondary_intent` | Search intent labels for the keyword, such as `Navigational` or `Informational`. |
| `data[].serp_features` | List of result types shown on the search page for this keyword, such as `news`, `video` and `organic`. |
| `data[].top_url` | The page of the domain that ranks highest for this keyword. |
| `data[].url_count` | Number of URLs tied to this keyword. |
| `meta.query.limit / meta.query.offset` | The row limit and starting offset applied to this response. |

### Notes

- `country` accepts only `ww` (worldwide). `limit` runs from 1 to 20.
- Dates in the request use `YYYY-MM`. The response `meta.request` shows them expanded to full days, for example `2026-09-01` to `2026-09-30`.
- `meta.request` shows the defaults applied to the call, such as `branded_type` set to `all` and `traffic_source` set to `all`.
- To see which pages receive this search traffic, call [Similarweb Landing Pages](/apis/similarweb/search-landing-pages). For rival sites on the same keywords, call [Similarweb Keyword Competitors](/apis/similarweb/search-keyword-competitors).

### Pricing

Billed at the actual cost of each call, about $0.15 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/search-website-keywords.json`](../../../catalog/models/similarweb/search-website-keywords.json) · Store page: https://www.sandbase.ai/model/similarweb/search-website-keywords
