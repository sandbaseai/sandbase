# Weibo Real-Time Hot Search API: pricing, parameters and code examples

`weibo/web-v2/hot-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the Weibo real-time hot search ranking: trending keywords with rank, heat value and labels such as new or hot.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/hot-search"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/hot-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/hot-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/hot-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/hot-search` with the body above minus `model`.

## Details

Returns the current Weibo real-time hot search list. Each entry has the keyword, a heat value, a position and a label such as new or hot. The request takes no input parameters, so you send an empty JSON object.

### Use cases

- Track which topics are trending on Weibo right now and store each snapshot for later comparison.
- Alert a team when a brand name or product keyword appears in `realtime[].word`.
- Build a dashboard that ranks trending topics by `num` and shows their `label_name` tags.
- Spot topics that carry the new label to find stories as they start to trend.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/hot-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "hotgov": {
    "flag": 2,
    "icon": "https://simg.s.weibo.com/moter/flags/2_0.png",
    "icon_desc": "热",
    "icon_desc_color": "#ff9406",
    "icon_height": 24,
    "icon_width": 24,
    "is_gov": 1,
    "is_hot": 1,
    "mid": "5361069742886874",
    "name": "#乌镇网事#",
    "note": "#乌镇网事#",
    "pos": 1
  },
  "hotgovs": [
    {
      "flag": 2,
      "icon": "https://simg.s.weibo.com/moter/flags/2_0.png",
      "icon_desc": "热",
      "icon_desc_color": "#ff9406",
      "icon_height": 24,
      "icon_width": 24,
      "name": "#乌镇网事#",
      "pos": 1,
      "small_icon_desc": "热",
      "small_icon_desc_color": "#ff9406",
      "topic_flag": 1,
      "word": "#乌镇网事#"
    }
  ],
  "realtime": [
    {
      "emoticon": "",
      "flag": 2,
      "icon": "https://simg.s.weibo.com/moter/flags/2_0.png",
      "icon_desc": "热",
      "icon_desc_color": "#ff9406",
      "icon_height": 24,
      "icon_width": 24,
      "label_name": "热",
      "note": "赴港看演唱会女孩低保已被取消",
      "num": 2173490,
      "rank": 0,
      "realpos": 1
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `realtime[].word` | The hot search keyword as plain text. |
| `realtime[].word_scheme` | The same keyword wrapped in `#` marks, the way Weibo writes a topic tag. Use it as a search term. |
| `realtime[].num` | The heat value of the topic. A larger number means a hotter topic. |
| `realtime[].rank` | Zero-based rank in the list. The first entry has `rank` 0. |
| `realtime[].realpos` | One-based position in the list. The first entry has `realpos` 1. |
| `realtime[].label_name` | Text label for the topic, such as `热` (hot) or `新` (new). |
| `realtime[].icon_desc / realtime[].icon_desc_color` | The text and color code of the label badge shown beside the topic. |
| `realtime[].icon` | URL of the label badge image. |
| `hotgov.word / hotgov.url` | The pinned topic shown at the top of the board, with a link to the related Weibo post. `hotgov.name` holds the topic name. |
| `hotgovs[].word / hotgovs[].pos` | Pinned topics in a list, with the position of each one. |

### Notes

- The request has no parameters. Send `{}` as the body.
- `realtime` holds the ranked list. `hotgov` and `hotgovs` hold the pinned topic, which does not appear in `realtime`.
- For a list with a search link for each topic, call [Weibo Hot Search List](/apis/weibo/web-v2/hot-search-summary).
- To read posts about a trending keyword, pass it to [Weibo Real-Time Search](/apis/weibo/web-v2/realtime-search) or [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo Hot Search List](/apis/weibo/web-v2/hot-search-summary): Get the complete real-time Weibo hot search ranking (top 50): keyword, rank, heat tag and search link for each trending topic.
- [Weibo Post Comments](/apis/weibo/web-v2/post-comments): Get the first-level comments on a Weibo post: comment text, author, time, likes and reply counts, with cursor pagination.

---
Machine-readable: [`catalog/models/weibo/web-v2/hot-search.json`](../../../../catalog/models/weibo/web-v2/hot-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/hot-search
