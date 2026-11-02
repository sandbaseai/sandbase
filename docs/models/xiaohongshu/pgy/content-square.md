# Xiaohongshu PGY content square leaderboards API: pricing, parameters and code examples

`xiaohongshu/pgy/content-square` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

PGY content square leaderboards on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/content-square", "biz_type": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/content-square', {'biz_type': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/content-square", {
  "biz_type": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/content-square", sandbase.Params{
	"biz_type": 1,
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/content-square` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `fans` | object |  | Creator fans range, board 4 only  |
| `price` | object |  | Creator price, board 4 only  |
| `theme` | string |  | 4/5/7/Theme  |
| `biz_type` | integer | yes | Leaderboard one of: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` |
| `category` | string |  | Board 1 only  |
| `industry` | string |  | 3/4/5/6/7/Industry, values differ per board  |
| `order_by` | string |  | Sort field, empty=board default  |
| `page_num` | integer |  | Page; each board has only 100 items default `1` |
| `note_type` | integer |  | Content type one of: `1`, `2` |
| `page_size` | integer |  | Page size, 1-34 default `34` |
| `placement` | integer |  | 3/5/7/Traffic placement one of: `1`, `2`, `3` |
| `date_range` | integer |  | 7/14/Date window in days one of: `3`, `7`, `14`, `30`; default `7` |
| `author_type` | integer |  | Board 4 only one of: `1`, `2` |
| `search_word` | string |  | Keyword, comma-separated for batch  |
| `content_type` | integer |  | Content source one of: `1`, `2`, `3`, `5`, `6`, `11`, `-1` |
| `sub_biz_type` | integer |  | Board 8 only one of: `1`, `2`, `3` |
| `marketing_target` | integer |  | Board 3 only one of: `3`, `8` |

## Details

PGY content square leaderboards on Xiaohongshu. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/content-square" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"biz_type": 1, "page_num": 1, "page_size": 20, "date_range": 7}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `biz_type` | integer | Yes | Leaderboard |
| `author_type` | integer | No | Board 4 only |
| `category` | string | No | Board 1 only |
| `content_type` | integer | No | Content source |
| `date_range` | integer | No | 7/14/Date window in days |
| `fans` | object | No | Creator fans range, board 4 only |
| `industry` | string | No | 3/4/5/6/7/Industry, values differ per board |
| `marketing_target` | integer | No | Board 3 only |
| `note_type` | integer | No | Content type |
| `order_by` | string | No | Sort field, empty=board default |
| `page_num` | integer | No | Page; each board has only 100 items |
| `page_size` | integer | No | Page size, 1-34 |
| `placement` | integer | No | 3/5/7/Traffic placement |
| `price` | object | No | Creator price, board 4 only |
| `search_word` | string | No | Keyword, comma-separated for batch |
| `sub_biz_type` | integer | No | Board 8 only |
| `theme` | string | No | 4/5/7/Theme |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/content-square.json`](../../../../catalog/models/xiaohongshu/pgy/content-square.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/content-square
