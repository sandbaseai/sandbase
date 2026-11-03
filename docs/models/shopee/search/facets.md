# Shopee Search Category Facets API: pricing, parameters and code examples

`shopee/search/facets` · data API · Shopee · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get the category facets Shopee shows for a search keyword, to see which categories a query maps to on each site.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shopee/search/facets", "site": "TW", "keyword": "iphone case"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('shopee/search/facets', {'site': 'TW', 'keyword': 'iphone case'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("shopee/search/facets", {
  "site": "TW",
  "keyword": "iphone case"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "shopee/search/facets", sandbase.Params{
	"site": "TW",
	"keyword": "iphone case",
})
```

Same call via the path form: `POST /v1/api/shopee/search/facets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `site` | string | yes | Shopee marketplace site. one of: `TW`, `ID`, `TH` |
| `keyword` | string | yes | Product search keyword.  |

## Details

This API returns the category facets Shopee shows for a search keyword on one marketplace site. It also returns related brands, shipping options and location filters. You send a `site` (`TW`, `ID` or `TH`) and a `keyword`.

### Use cases

- Check which product categories the keyword `iphone case` maps to on the Taiwan site.
- Compare how many listings fall into each category to find the main category for a keyword.
- Collect the top brand names and brand IDs that appear for a search term.
- List the shipping channels Shopee offers as filters for a keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/shopee/search/facets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"site": "TW", "keyword": "iphone case"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Product search keyword. |
| `site` | string | Yes | Shopee marketplace site. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "bff_meta": null,
    "brands": [
      {
        "brandid": 1105002,
        "name": "RHINOSHIELD 犀牛盾"
      }
    ],
    "colorful_block": [],
    "disabled_filters": null,
    "dynamic_filter": null,
    "error": null,
    "error_msg": null,
    "facets": [
      {
        "category": {
          "display_name": "iPhone保護殼",
          "is_default_subcat": null,
          "name": "iPhone Cases&Covers",
          "parent_category_detail": {
            "category": {
              "display_name": "手機平板與周邊",
              "is_default_subcat": null,
              "name": "Mobile & Gadgets",
              "parent_category_detail": null,
              "parentids": null
            },
            "catid": 11041546,
            "count": 426277,
            "show_parent_category": null
          },
          "parentids": [
            11041546
          ]
        },
        "catid": 11041605,
        "count": 363271,
        "show_parent_category": null
      }
    ],
    "filter_algorithm": "",
    "locations": [
      {
        "display_name": "台灣",
        "level": "-1",
        "name": "台灣",
        "sub_location": null,
        "tag_ids": [
          822059780857868
        ],
        "translations": []
      }
    ],
    "price_ranges": [],
    "shippings": [
      {
        "channelids": "30015",
        "display_name": "蝦皮店到店",
        "item_tag_ids": [
          840902217782303
        ],
        "name": "蝦皮店到店",
        "positionid": 1
      }
    ]
  },
  "market": "Taiwan",
  "site": "TW"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.facets[].catid` | ID of a category that matches the keyword. |
| `data.facets[].count` | Number of listings in that category for the keyword. |
| `data.facets[].category.name / data.facets[].category.display_name` | Category name in English (`name`) and in the local site language (`display_name`). |
| `data.facets[].category.parent_category_detail.catid` | ID of the parent category. |
| `data.facets[].category.parent_category_detail.count` | Number of listings in the parent category. |
| `data.brands[].brandid / data.brands[].name` | ID and name of a brand that appears for the keyword. |
| `data.shippings[].display_name` | Name of a shipping option shown as a filter. |
| `data.shippings[].channelids` | Shipping channel IDs for that option. Multiple IDs are separated by `;`. |
| `data.locations[].display_name` | Seller location filter, such as local or overseas. |
| `market / site` | Market name and site code for the request. |

### Notes

- Use only `TW`, `ID` or `TH` for `site`.
- Category names in `display_name` use the local language of the site. `name` is in English in the sample response.
- The `data.facets[].catid` values are category IDs. Parent categories sit under `category.parent_category_detail`.
- Some fields can be empty or `null`, such as `data.price_ranges` and `data.dynamic_filter`.

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/shopee/search/facets.json`](../../../../catalog/models/shopee/search/facets.json) · Store page: https://www.sandbase.ai/model/shopee/search/facets
