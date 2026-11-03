# Similarweb Website Technologies API: pricing, parameters and code examples

`similarweb/technologies` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.75 per call · **Modes:** sync

Get the technologies a website uses (analytics, advertising, CMS and more), with category and first-seen date.

## Pricing

- **$0.75 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/technologies", "domain": "cnn.com", "end_date": "2026-09", "granularity": "monthly", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/technologies', {'domain': 'cnn.com', 'end_date': '2026-09', 'granularity': 'monthly', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/technologies", {
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
run, err := c.Run(ctx, "similarweb/technologies", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"granularity": "monthly",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/technologies` with the body above minus `model`.

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

Returns the technologies a website has used, such as advertising, analytics and CMS tools. Each row has the technology name, category, sub-category, status and the date it was first seen. It needs a `domain` plus a monthly date range.

### Use cases

- List the ad servers and advertising tools a competitor site has installed or dropped.
- Check which technologies a prospect's site runs before a sales outreach.
- Track when a site removed a technology by filtering for rows with `status` set to `removed`.
- Build a technology adoption list by grouping sites by `category` and `sub_category`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/technologies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domain": "cnn.com", "granularity": "monthly", "limit": 1}'
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
      "category": "Advertising",
      "description": "24/7 Media creates the tools for business advantage in the digital world.",
      "first_seen_date": "2018-04-21",
      "pricing_model": "Free",
      "status": "removed",
      "sub_category": "Publisher Ad Server",
      "technology": "24 7 Media"
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
      "category": null,
      "domain": "cnn.com",
      "end_date": "2026-09-30",
      "format": "json",
      "granularity": "monthly",
      "main_domain_only": false,
      "metrics": [
        "sub_category"
      ],
      "start_date": "2026-09-01",
      "status": "installed_and_removed"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].technology` | Name of the technology found on the domain. |
| `data[].category / data[].sub_category` | Broad group and narrower group of the technology, for example `Advertising` and `Publisher Ad Server`. |
| `data[].description` | Short text describing what the technology does. |
| `data[].first_seen_date` | Date the technology was first seen on the domain, in `YYYY-MM-DD` format. |
| `data[].status` | Whether the technology is still on the site or was `removed`. |
| `data[].pricing_model` | Pricing model of the technology, for example `Free`. |
| `meta.request.status` | Status filter applied to the query. The sample call used `installed_and_removed`, so both current and dropped technologies are returned. |
| `meta.query.limit / meta.query.offset` | Page size and start position used for this result list. |
| `meta.last_updated` | Date the dataset was last updated, in `YYYY-MM-DD` format. |

### Notes

- Pass `start_date` and `end_date` as `YYYY-MM` values. The response expands them to the first and last day of the month in `meta.request`.
- Use `limit` (1 to 20) to set the page size. `meta.query.offset` shows the current position in the list.
- Set `main_domain_only` to `true` or `false` to control whether the lookup covers only the main domain. The sample call returned `false`.
- To see the site's ad networks next, call [Similarweb Ad Networks](/apis/similarweb/ad-networks).

### Pricing

$0.75 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/technologies.json`](../../../catalog/models/similarweb/technologies.json) · Store page: https://www.sandbase.ai/model/similarweb/technologies
