# Weibo Region City List API: pricing, parameters and code examples

`weibo/web-v2/city-list` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a directory of provinces and cities on Weibo. Supports toggling a normalized data structure via the normalized parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/city-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/city-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/city-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/city-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/city-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `normalized` | boolean |  | Whether to return normalized structure (default True) default `true` |

## Details

Returns a list of provinces and the cities inside each one, as used on Weibo. Each entry has a numeric `code` and a Chinese `name`. The only input is the optional `normalized` boolean, so you can send an empty body.

### Use cases

- Fill a province and city dropdown in a tool that filters Weibo data by region.
- Match region codes found in Weibo user data to province and city names.
- Build a lookup table from region `code` values to Chinese place names.
- Check that a city name is spelled the way Weibo spells it before you use it in a query.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/city-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `normalized` | boolean | No | Whether to return normalized structure (default True) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "provinces": [
    {
      "cities": [
        {
          "code": 0,
          "name": "城市/地区"
        }
      ],
      "code": 0,
      "name": "省/直辖市"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `provinces[]` | One entry for each province or municipality. Each entry holds its own `code` and `name` and a list of `cities`. |
| `provinces[].code` | Numeric code of the province or municipality. For example, `34` is 安徽 and `11` is 北京. |
| `provinces[].name` | Province or municipality name in Chinese. |
| `provinces[].cities[]` | The cities or districts that belong to this province. |
| `provinces[].cities[].code` | Numeric code of the city or district. The value counts up from `1` inside each province, so the same code can appear under different provinces. |
| `provinces[].cities[].name` | City or district name in Chinese, such as 合肥 or 东城区. |

### Notes

- The first province entry has `code` `0` and the name 省/直辖市. Its only city has `code` `0` and the name 城市/地区. These look like placeholder labels for a dropdown, not real places.
- City `code` values are only unique inside one province. Keep the province `code` together with the city `code` when you store a location.
- The `normalized` parameter defaults to `true`. The request in this example sent `{}`, so it used the default.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/city-list.json`](../../../../catalog/models/weibo/web-v2/city-list.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/city-list
