# Pipixia Hot Search API: pricing, parameters and code examples

`pipixia/app/hot-search-board-list` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the Pipixia hot search boards: trending posts with daily likes and top comments.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/hot-search-board-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/hot-search-board-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/hot-search-board-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/hot-search-board-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/pipixia/app/hot-search-board-list` with the body above minus `model`.

## Details

Fetch the current Pipixia hot boards and the trending items on each.

### Use cases

- Track trending content on Pipixia.
- Find viral formats.
- Build trend digests.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/hot-search-board-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "boards": [
      {
        "title": "神评热榜",
        "board_items": [
          {
            "today_digg_num": 2448,
            "item": {
              "item_id_str": "7692653405960935721",
              "create_time": 1791085444,
              "duration": 60.072,
              "item_type": 2
            }
          }
        ]
      }
    ]
  }
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Search](/apis/pipixia/app/search): Search Pipixia (ByteDance humor community) by keyword across posts, videos, images, users and hashtags.
- [Get hashtag detail](/apis/pipixia/app/hashtag-detail): Get hashtag detail data.
- [Get hashtag post list](/apis/pipixia/app/hashtag-post-list): Get hashtag post list data.

---
Machine-readable: [`catalog/models/pipixia/app/hot-search-board-list.json`](../../../../catalog/models/pipixia/app/hot-search-board-list.json) · Store page: https://www.sandbase.ai/model/pipixia/app/hot-search-board-list
