# Bilibili Hot Searches API: pricing, parameters and code examples

`bilibili/web/hot-search` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns current trending search keywords along with their heat scores from Bilibili. Results are restricted according to the specified count limit.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/hot-search", "limit": 10}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/hot-search', {'limit': 10})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/hot-search", {
  "limit": 10
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/hot-search", sandbase.Params{
	"limit": 10,
})
```

Same call via the path form: `POST /v1/api/bilibili/web/hot-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer | yes | Return number  |

## Details

Returns the current list of trending search keywords on Bilibili, each with a heat score. The only input is `limit`, the number of keywords to return.

### Use cases

- Track which topics are trending on Bilibili right now.
- Compare `heat_score` values to see which keywords draw the most interest.
- Feed a search suggestion box with current popular Bilibili queries.
- Log the trending list at set times to see how topics rise and fall.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/hot-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 10}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | Yes | Return number |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "trending": {
      "list": [
        {
          "goto": "",
          "heat_score": 3216045,
          "icon": "https://i0.hdslb.com/bfs/activity-plat/static/20251027/aafcb8031fd171c428daaa9b4…",
          "keyword": "FaZe Falcons",
          "show_name": "FaZe vs Falcons IEM北京",
          "uri": ""
        }
      ],
      "title": "bilibili热搜",
      "top_list": [],
      "trackid": "5327011950951300418"
    }
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.trending.list[].keyword` | The trending search term. Use this value as the query text. |
| `data.trending.list[].show_name` | The title shown to users in the hot search list. It can differ from `keyword`. |
| `data.trending.list[].heat_score` | Numeric heat score for the keyword. A higher number means a hotter topic. |
| `data.trending.list[].icon` | URL of a badge image shown next to the keyword. It is an empty string when the entry has no badge. |
| `data.trending.list[].goto / data.trending.list[].uri` | Link target fields for the entry. They are empty strings in this response. |
| `data.trending.title` | Title of the list, for example `bilibili热搜`. |
| `data.trending.top_list` | List of pinned entries. It is empty in this response. |
| `data.trending.trackid` | Tracking ID string for this list. |
| `code / message` | Status of the call. `code` is `0` and `message` is `OK` on success. |

### Notes

- Set `limit` to the number of keywords you want. It is the only parameter and it is required.
- Pass a `keyword` to [Bilibili Web General Search](/apis/bilibili/web/general-search) to find content for a trending topic.
- Pass a `keyword` to [Bilibili Video Search](/apis/bilibili/search-video) to list videos that match it.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/hot-search.json`](../../../../catalog/models/bilibili/web/hot-search.json) · Store page: https://www.sandbase.ai/model/bilibili/web/hot-search
