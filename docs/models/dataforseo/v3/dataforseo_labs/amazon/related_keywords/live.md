# DataForSEO Amazon Related Keywords API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/amazon/related_keywords/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0126 per call · **Modes:** sync

Get Amazon keywords related to a seed, with search volume.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0126**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/amazon/related_keywords/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/amazon/related_keywords/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/amazon/related_keywords/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/amazon/related_keywords/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/amazon/related_keywords/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

This API returns Amazon keywords related to a seed keyword, with the Amazon search volume for each one. It needs a `keyword`, and you can also set `location_code`, `language_code` and `limit`.

### Use cases

- Expand a product listing's keyword set from a seed like `wireless earbuds` to find terms shoppers also search.
- Rank related Amazon search terms by `search_volume` to pick which ones to target in titles and ads.
- Map how a product category connects to nearby categories using the `related_keywords` lists.
- Compare demand for competing product terms, such as `airpods` and `wireless headphones`, in one call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/amazon/related_keywords/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "wireless earbuds", "limit": 5, "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query. |
| `language_code` | string | No | Language code, e.g. "en". |
| `limit` | integer | No | Maximum number of results (up to 100). |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "dataforseo_labs",
        "function": "related_keywords",
        "keyword": "wireless earbuds",
        "language_code": "en",
        "limit": 5,
        "location_code": 2840,
        "se_type": "amazon"
      },
      "id": "11030828-2190-0387-0000-4752ce873051",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "depth": 1,
              "keyword_data": {
                "keyword": "airpods",
                "keyword_info": {
                  "last_updated_time": "2026-11-03 03:44:11 +00:00",
                  "se_type": "amazon",
                  "search_volume": 184195
                },
                "language_code": "en",
                "location_code": 2840,
                "se_type": "amazon"
              },
              "related_keywords": [
                "airpods pro"
              ],
              "se_type": "amazon"
            }
          ],
          "items_count": 5,
          "language_code": "en",
          "location_code": 2840,
          "se_type": "amazon",
          "seed_keyword": "wireless earbuds",
          "seed_keyword_data": null,
          "total_count": 7
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0412 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0475 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].seed_keyword` | The keyword you sent in the request. |
| `tasks[].result[].items[].keyword_data.keyword` | A keyword in the related set. The seed keyword can appear in the list too. |
| `tasks[].result[].items[].keyword_data.keyword_info.search_volume` | Search volume for that keyword on Amazon. |
| `tasks[].result[].items[].keyword_data.keyword_info.last_updated_time` | Timestamp for the keyword data, for example `2026-11-03 03:44:11 +00:00`. |
| `tasks[].result[].items[].depth` | Distance of the keyword from the seed. The seed itself has `0` and the keywords linked directly to it have `1`. |
| `tasks[].result[].items[].related_keywords` | A list of other keywords related to this item. |
| `tasks[].result[].items_count / tasks[].result[].total_count` | `items_count` is the number of items in this response. `total_count` is the total number of related keywords found. |
| `tasks[].result[].location_code / tasks[].result[].language_code` | The location and language the results apply to. |

### Notes

- Results sit under `tasks[].result[].items[]`.
- Use `limit` to cap the number of items, up to 100. Compare `items_count` with `total_count` to see whether more related keywords exist.
- `seed_keyword_data` can be `null`, so read the seed's volume from the item with `depth` `0` instead.
- Use `location_code` `2840` for the United States and `language_code` `en` for English.

### Pricing

Billed at the actual cost of each call, about $0.0126 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/amazon/related_keywords/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/amazon/related_keywords/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/amazon/related_keywords/live
