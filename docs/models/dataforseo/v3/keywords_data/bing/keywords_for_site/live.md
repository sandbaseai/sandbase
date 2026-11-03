# DataForSEO Bing Keywords for Site API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/bing/keywords_for_site/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.09 per call · **Modes:** sync

Returns Bing keyword suggestions and search metrics associated with a specified target website. Helps teams discover search terms relevant to a site domain.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.09**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/bing/keywords_for_site/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/bing/keywords_for_site/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/bing/keywords_for_site/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/bing/keywords_for_site/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/bing/keywords_for_site/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | string |  | Target domain or page, e.g. "nike.com".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns a list of Bing keywords tied to a target domain or page, with search volume, competition and cost per click for each keyword. It needs a `target` plus a `location_code` and `language_code`.

### Use cases

- Build a keyword list for a competitor site such as nike.com to see which Bing queries relate to it.
- Check recent monthly search volume for site-related queries before planning new content.
- Compare `competition` values across keywords to pick terms that look less contested on Bing.
- Seed a Bing Ads keyword plan with terms already linked to a given domain.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/bing/keywords_for_site/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |
| `target` | string | No | Target domain or page, e.g. "nike.com". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "keywords_data",
        "function": "keywords_for_site",
        "language_code": "en",
        "location_code": 2840,
        "se": "bing",
        "target": "nike.com"
      },
      "id": "11030829-1614-0441-0000-c9f4826a6628",
      "path": [
        "v3"
      ],
      "result": [
        {
          "categories": null,
          "competition": 0.1,
          "cpc": 0,
          "device": "all",
          "keyword": "nike innovative products",
          "language_code": "en",
          "location_code": 2840,
          "monthly_searches": [
            {
              "month": 10,
              "search_volume": 0,
              "year": 2026
            }
          ]
        }
      ],
      "result_count": 694,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "2.1262 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "2.1476 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].keyword` | The suggested search term related to the target site. |
| `tasks[].result[].competition` | Competition score for the keyword. Values in the sample are decimals such as `0.1`. |
| `tasks[].result[].cpc` | Cost per click for the keyword. It is `0` for the sampled rows. |
| `tasks[].result[].monthly_searches[].year / tasks[].result[].monthly_searches[].month` | Year and month number for each monthly search entry. |
| `tasks[].result[].monthly_searches[].search_volume` | Search volume for that month. |
| `tasks[].result[].device` | Device scope of the metrics. The sample shows `all`. |
| `tasks[].result[].language_code / tasks[].result[].location_code` | Language and location the keyword data applies to. |
| `tasks[].result[].categories` | Category list for the keyword. It is `null` in the sample. |
| `tasks[].result_count` | Number of keyword rows found for the target. It is `694` in this example. |

### Notes

- `location_code` takes numeric codes such as `2840` for the United States. `language_code` takes codes such as `en`.
- `target` can be a domain like `nike.com` or a page.
- Each call runs one task. The keyword rows are in `tasks[].result[]`, and `tasks[].data` echoes the request values.
- Months in `monthly_searches` are plain numbers (for example `10`) paired with a four-digit `year`.

### Pricing

Billed at the actual cost of each call, about $0.09 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/bing/keywords_for_site/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/bing/keywords_for_site/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/bing/keywords_for_site/live
