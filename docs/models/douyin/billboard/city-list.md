# Douyin Billboard City List API: pricing, parameters and code examples

`douyin/billboard/city-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the list of Chinese cities supported by Douyin billboard rankings. Use this data to populate regional filters for location-specific trending lists.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/city-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/city-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/city-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/city-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/city-list` with the body above minus `model`.

## Details

Returns the list of Chinese cities that Douyin billboard rankings support. Each city has a display name and a numeric code. The API takes no input.

### Use cases

- Fill a city dropdown in a dashboard that shows local Douyin trending lists.
- Store the city codes so you can pass them to city-based billboard queries.
- Check whether a city is supported before you build a regional report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/city-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": [
    {
      "label": "北京",
      "value": 110000
    }
  ],
  "extra": {
    "now": 1793691103000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `code` | Status code of the response. The sample shows `0`. |
| `data[]` | One entry for each supported city. |
| `data[].label` | City name in Chinese, such as `北京` or `上海`. |
| `data[].value` | Numeric code for the city, such as `110000` for `北京`. Use it to identify the city in other requests. |
| `extra.now` | Timestamp of the response as a number, in the form of 13 digits (milliseconds). |
| `message` | Message text. It is an empty string in the sample. |

### Notes

- Send an empty JSON object `{}` as the request body. The API has no parameters.
- Call [Douyin City Hot List](/apis/douyin/billboard/hot-city-list) next to get city-based rankings.
- The `value` codes look like Chinese administrative region codes, for example `110000` and `440100`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.
- [Douyin Account Fan Interest Search Terms](/apis/douyin/billboard/hot-account-fans-interest-search-list): Returns the top ten search terms reflecting fan interest over the last three days for a specified Douyin creator account using their user sec_id.

---
Machine-readable: [`catalog/models/douyin/billboard/city-list.json`](../../../../catalog/models/douyin/billboard/city-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/city-list
