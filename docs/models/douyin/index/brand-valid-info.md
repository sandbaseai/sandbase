# Douyin Brand Valid Information API: pricing, parameters and code examples

`douyin/index/brand-valid-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns brand details including brand ID and category information on Douyin. Queries are filtered using comma-separated brand keywords.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/brand-valid-info", "keyword_list": "华为"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/brand-valid-info', {'keyword_list': '华为'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/brand-valid-info", {
  "keyword_list": "华为"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/brand-valid-info", sandbase.Params{
	"keyword_list": "华为",
})
```

Same call via the path form: `POST /v1/api/douyin/index/brand-valid-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword_list` | string | yes | Brand name list, comma separated  |

## Details

Returns the Douyin brand records that match each keyword you send, including `brand_id` and the categories the brand is listed under. It needs one input, `keyword_list`, a comma-separated string of brand names.

### Use cases

- Check whether a brand name such as `华为` is a recognized Douyin brand before you query other brand endpoints.
- Get the `brand_id` for a brand name so you can store it or pass it to later lookups.
- List every category a brand appears in, for example `手机` and `家用电器` for `华为`.
- Check `brand_status` and `yuntu_status` for a batch of brand names in one call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/brand-valid-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword_list": "华为"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword_list` | string | Yes | Brand name list, comma separated |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "keyword_info": [
    {
      "brand_info": [
        {
          "brand_id": "9117",
          "brand_name": "华为",
          "category_id": "11",
          "category_name": "手机"
        }
      ],
      "brand_status": "1",
      "keyword": "华为",
      "yuntu_status": "1"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `keyword_info[].keyword` | The keyword from your request that this result belongs to. |
| `keyword_info[].brand_info[]` | List of brand and category matches for the keyword. The same brand can appear more than once, once per category. |
| `keyword_info[].brand_info[].brand_id` | ID of the brand, returned as a string. It stays the same across the category rows of one brand. |
| `keyword_info[].brand_info[].brand_name` | Name of the matched brand. |
| `keyword_info[].brand_info[].category_id / keyword_info[].brand_info[].category_name` | ID and name of a category the brand is listed under, such as `手机` (`11`) or `家用电器` (`28`). |
| `keyword_info[].brand_status` | Status flag for the brand, returned as a string. `1` for `华为`. |
| `keyword_info[].yuntu_status` | Status flag named `yuntu_status`, returned as a string. `1` for `华为`. |
| `BaseResp.StatusCode / BaseResp.StatusMessage` | Status of the call. `0` with an empty message means the request succeeded. |

### Notes

- Send several brand names in `keyword_list` as one comma-separated string. Each name gets its own entry in `keyword_info`.
- If a brand has several categories, `brand_info` holds one row per category with the same `brand_id`.
- If you do not know the exact brand name, call [Douyin Brand Search Suggestions](/apis/douyin/index/brand-suggest) first.
- To see popularity data for a brand, use [Douyin Brand Trend Lines](/apis/douyin/index/brand-lines).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/brand-valid-info.json`](../../../../catalog/models/douyin/index/brand-valid-info.json) · Store page: https://www.sandbase.ai/model/douyin/index/brand-valid-info
