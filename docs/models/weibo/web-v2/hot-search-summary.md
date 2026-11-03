# Weibo Hot Search List API: pricing, parameters and code examples

`weibo/web-v2/hot-search-summary` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Get the complete real-time Weibo hot search ranking (top 50): keyword, rank, heat tag and search link for each trending topic.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/hot-search-summary"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/hot-search-summary', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/hot-search-summary", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/hot-search-summary", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/hot-search-summary` with the body above minus `model`.

## Details

Returns the current Weibo hot search ranking as a list of trending topics. Each entry has a keyword, rank, tag and a search link. The request takes no input parameters.

### Use cases

- Track which topics trend on Weibo right now and log the list at set times.
- Send an alert when a brand name or product keyword appears in the hot list.
- Build a daily report of trending topics and how long each stays in the ranking.
- Feed trending keywords into a post search to collect the discussion around each topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/hot-search-summary" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "heat": "",
      "is_top": true,
      "keyword": "乌镇网事",
      "keyword_url": "/weibo?q=%23%E4%B9%8C%E9%95%87%E7%BD%91%E4%BA%8B%23&Refer=new_time",
      "rank": 0,
      "tag": "热"
    }
  ],
  "total": 51
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].keyword` | The trending topic text as shown on the hot search list. |
| `data[].rank` | Position of the topic in the list. The first entry has `rank` set to `0`, so the count starts at zero. |
| `data[].tag` | Short label for the topic, such as `热` (hot) or `新` (new). |
| `data[].keyword_url` | Relative Weibo search path for the topic. The `q` value is the URL-encoded keyword wrapped in `#` hashtag marks. |
| `data[].is_top` | `true` for the pinned entry at the top of the list, `false` for the others. |
| `data[].heat` | Heat value for the topic. It can be an empty string, as in the sample response. |
| `total` | Number of items counted for the list. It can be one higher than the number of ranked entries. |

### Notes

- The request body is an empty JSON object `{}`. There is no pagination.
- `keyword_url` is a relative path. Add the Weibo domain before you open it in a browser.
- To read the posts behind a topic, pass the `keyword` to [Weibo Real-Time Search](/apis/weibo/web-v2/realtime-search) or [Weibo Topic Search](/apis/weibo/web-v2/topic-search).
- For a different view of the ranking, see [Weibo Real-Time Hot Search](/apis/weibo/web-v2/hot-search).

### Pricing

$0.0015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo Post Detail](/apis/weibo/web-v2/post-detail): Get the full data of a single Weibo post by its ID: text (including long posts), author, publish time, location and repost, comment and like counts.
- [Weibo AI Search Content Extension](/apis/weibo/web-v2/ai-related-search): Get content extensions related to keyword (related questions, blogger recommendations, reference posts).

---
Machine-readable: [`catalog/models/weibo/web-v2/hot-search-summary.json`](../../../../catalog/models/weibo/web-v2/hot-search-summary.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/hot-search-summary
