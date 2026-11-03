# Weibo Hot Search API: pricing, parameters and code examples

`weibo/hot-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get the current Weibo hot-search ranking. Use it to identify trending topics for newsroom monitoring, content planning, or timely topic discovery.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/hot-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/hot-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/hot-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/hot-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/hot-search` with the body above minus `model`.

## Details

Returns the current Weibo hot-search ranking as a list of trending topics with a heat number, rank and label. It takes no input, so you send an empty JSON object `{}`.

### Use cases

- Track which topics are trending on Weibo right now for newsroom monitoring.
- Spot newly listed topics by checking the `label_name` value `新` on each entry.
- Rank topics by `num` to plan content around the busiest conversations.
- Check which topic currently holds the pinned government or promoted slot in `data.hotgov`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/hot-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "curTab": "hot",
  "data": {
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
  },
  "logs": {
    "act_code": 7948,
    "ext": "cate:1003|words:#赴港看演唱会女孩低保已被取消#,#警方通报九寨沟景区游客冲突事件#,#本届乌镇峰会分论坛数量创新高#,#九寨沟打人事件双方已和…"
  },
  "ok": 1,
  "topLogs": {
    "act_code": 7948,
    "ext": "cate:1002|words:#乌镇网事#"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.realtime[]` | The ranked list of hot-search topics, in display order. |
| `data.realtime[].word / data.realtime[].note` | The topic text. In the sample both hold the same plain text without hash marks. |
| `data.realtime[].word_scheme` | The topic written as a Weibo hashtag with `#` marks on both sides. Use it as a search term. |
| `data.realtime[].num` | A numeric heat value for the topic. Higher values appear earlier in the list. |
| `data.realtime[].rank` | Zero-based rank of the topic in the list. The first item has `0`. |
| `data.realtime[].realpos` | One-based position of the topic in the list. The first item has `1`. |
| `data.realtime[].label_name / data.realtime[].icon_desc` | The short label shown beside the topic, such as `热` (hot) or `新` (new). |
| `data.realtime[].icon` | URL of the label icon image for the topic. |
| `data.hotgov.word / data.hotgov.url` | The pinned topic at the top of the board and a link to the related post. |
| `data.hotgovs[]` | List of pinned topics. Each entry has `word`, `pos` and label icon fields. |

### Notes

- The request has no parameters. Send `{}` as the body.
- `data.realtime[].rank` starts at `0`, while `data.realtime[].realpos` starts at `1`. Pick one and use it consistently.
- `data.hotgov.stime` looks like a Unix timestamp in seconds.
- For other Weibo ranking views, see [Weibo Real-Time Hot Search](/apis/weibo/web-v2/hot-search) or [Weibo Hot Search Categories](/apis/weibo/app/hot-search-categories).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/weibo/hot-search.json`](../../../catalog/models/weibo/hot-search.json) · Store page: https://www.sandbase.ai/model/weibo/hot-search
