# Xigua Video Search API: pricing, parameters and code examples

`xigua/app-v2/search-video` · data API · Xigua · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search Xigua Video (ByteDance long-form video) by keyword: titles, creators, duration, publish time and comment counts, with sort and duration filters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xigua/app-v2/search-video", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xigua/app-v2/search-video', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xigua/app-v2/search-video", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xigua/app-v2/search-video", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/xigua/app-v2/search-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests default `0` |
| `keyword` | string | yes | Keyword  |
| `order_type` | string |  | Order type, empty for default sorting, the following are optional sorting methods.  |
| `max_duration` | integer |  | Maximum duration, default empty, in seconds.  |
| `min_duration` | integer |  | Minimum duration, default empty, in seconds.  |

## Details

Search Xigua Video for a keyword and get matching videos. Filter by duration and paginate with `offset`.

### Use cases

- Research long-form video content in China.
- Find creators for a topic.
- Monitor brand mentions in video.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xigua/app-v2/search-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `offset` | integer | No | Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests |
| `order_type` | string | No | Order type, empty for default sorting, the following are optional sorting methods. |
| `max_duration` | integer | No | Maximum duration, default empty, in seconds. |
| `min_duration` | integer | No | Minimum duration, default empty, in seconds. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "offset": 10,
  "results": [
    {
      "data": {
        "group_id": "7306123103342592551",
        "title": "Open AI 宫斗大戏始末，一场人工智能向人类发起的挑衅！",
        "publish_time": 1701089344,
        "video_duration": 793,
        "comment_count": 20,
        "source": "<user>"
      }
    }
  ]
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Get single video data](/apis/xigua/app-v2/one-video): Get single video data (less information, does not include title and other information, but includes information about related videos).
- [Get single video play URL](/apis/xigua/app-v2/one-video-play-url): App V2 One Video Play Url provides a focused capability for applications, automation, and data workflows.
- [Personal information](/apis/xigua/app-v2/user-info): Personal information.

---
Machine-readable: [`catalog/models/xigua/app-v2/search-video.json`](../../../../catalog/models/xigua/app-v2/search-video.json) · Store page: https://www.sandbase.ai/model/xigua/app-v2/search-video
