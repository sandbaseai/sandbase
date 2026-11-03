# Douyin School Search API: pricing, parameters and code examples

`douyin/search/school-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns school information search results from Douyin matching search queries. Filter schools by entering a specific school name or city query via the keyword parameter.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/school-search", "keyword": "北京"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/school-search', {'keyword': '北京'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/school-search", {
  "keyword": "北京"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/school-search", sandbase.Params{
	"keyword": "北京",
})
```

Same call via the path form: `POST /v1/api/douyin/search/school-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search keyword, e.g., school name "Peking University" or city "Beijing" default `"北京"` |

## Details

Returns a list of Douyin schools whose names match a search keyword. The input is a `keyword` string, such as a school name or a city name.

### Use cases

- Check how a school name is written on Douyin before you search for content about it.
- List schools that match a city name such as `北京` to build a school picker.
- Collect school names for a city to use as keywords in other Douyin searches.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/school-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search keyword, e.g., school name "Peking University" or city "Beijing" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "2026110315322051AE9BB2F3DCC44F33AD",
    "now": 1793691140000
  },
  "log_pb": {
    "impr_id": "2026110315322051AE9BB2F3DCC44F33AD"
  },
  "schools": [
    {
      "name": "北京中学"
    }
  ],
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `schools[]` | List of schools that match `keyword`. |
| `schools[].name` | School name as shown on Douyin, for example `北京大学`. |
| `status_code` | Status of the request. `0` in the sample response. |
| `log_pb.impr_id / extra.logid` | Request identifiers. Both hold the same value in the sample response. |
| `extra.now` | Timestamp in the response, a 13-digit number that looks like milliseconds. |

### Notes

- The response lists only the school `name`. It has no school ID, so you cannot pass a result to another API directly.
- `keyword` is the only input. The schema shows no pagination parameter.
- To search Douyin content about a school, pass the returned `name` to [Douyin General Search](/apis/douyin/search/general-search-v1) or [Douyin Video Search](/apis/douyin/search/video-search-v2).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/school-search.json`](../../../../catalog/models/douyin/search/school-search.json) · Store page: https://www.sandbase.ai/model/douyin/search/school-search
