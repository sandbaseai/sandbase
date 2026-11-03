# Douyin Keyword Crowd Portrait API: pricing, parameters and code examples

`douyin/index/portrait` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns crowd portrait analysis for a specific keyword over a defined date range. Allows querying data for Douyin or Toutiao platforms.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/portrait", "end_date": "example", "keyword": "example", "start_date": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/portrait', {'end_date': 'example', 'keyword': 'example', 'start_date': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/portrait", {
  "end_date": "example",
  "keyword": "example",
  "start_date": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/portrait", sandbase.Params{
	"end_date": "example",
	"keyword": "example",
	"start_date": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/index/portrait` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | The keyword to analyze  |
| `app_name` | string |  | Platform, aweme=Douyin, toutiao=Toutiao one of: `aweme`, `toutiao` |
| `end_date` | string | yes | End date YYYYMMDD  |
| `start_date` | string | yes | Start date YYYYMMDD  |

## Details

Returns crowd portrait analysis for one keyword over a date range on Douyin or Toutiao. It needs a `keyword`, a `start_date` and an `end_date`. `app_name` is optional and picks the platform.

### Use cases

- Check which audience a search term such as `人工智能` attracts on Douyin.
- Compare the crowd behind the same keyword on Douyin (`aweme`) and Toutiao (`toutiao`).
- Run the same keyword over different date ranges to see how its audience changes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/portrait" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "1735660799", "keyword": "人工智能", "start_date": "1730044800"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End date YYYYMMDD |
| `keyword` | string | Yes | The keyword to analyze |
| `start_date` | string | Yes | Start date YYYYMMDD |
| `app_name` | string | No | Platform, aweme=Douyin, toutiao=Toutiao |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 500,
    "StatusMessage": "日期格式满足%Y%m%d"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `BaseResp` | Status block of the response. In the sample call it is the only top-level key. |
| `BaseResp.StatusCode` | Numeric status of the call. The sample call returned `500`, which means the request failed. |
| `BaseResp.StatusMessage` | Text that explains the status. The sample call returned `日期格式满足%Y%m%d`, which says the date must match the `%Y%m%d` format. |

### Notes

- Send `start_date` and `end_date` as `YYYYMMDD` strings, for example `20241101`. The sample request used Unix-style numbers such as `1730044800`, and the call failed with the date format error shown above.
- Set `app_name` to `aweme` for Douyin or `toutiao` for Toutiao.
- To pick dates that have data, call [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date) first.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/portrait.json`](../../../../catalog/models/douyin/index/portrait.json) · Store page: https://www.sandbase.ai/model/douyin/index/portrait
