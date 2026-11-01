# Pipixia Hot Search Board Detail

`pipixia/app/hot-search-board-detail` · api · Pipixia

Returns detailed items from a Pipixia hot search board, including item identifiers, like metrics, and highlighted comments for a specified board type.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/hot-search-board-detail", "block_type": 12}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/hot-search-board-detail', {'block_type': 12})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/hot-search-board-detail", {
  "block_type": 12
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/hot-search-board-detail", sandbase.Params{
	"block_type": 12,
})
```

Same call via the path form: `POST /v1/api/pipixia/app/hot-search-board-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `block_type` | integer | yes | Board type, can be obtained from the `/fetch_hot_search_board_list` interface.  |

## Details

Fetch detailed contents from a Pipixia hot search board by providing the target `block_type` identifier.

### Use cases

- Track trending media items on Pipixia hot search leaderboards.
- Monitor top comments and engagement counts for ranked content.
- Analyze trending video durations and daily like volumes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/hot-search-board-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"block_type": 12}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `block_type` | integer | Yes | Board type, can be obtained from the `/fetch_hot_search_board_list` interface. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "board": {
      "board_items": [
        {
          "today_digg_num": 2448,
          "god_comment": {
            "bds_origin_type": 1,
            "bury_count": -1,
            "city_name": "海南",
            "comment_count": 32,
            "comment_id": 7692734173965976335,
            "comment_id_str": "7692734173965976335"
          },
          "item": {
            "create_time": 1791085444,
            "duration": 60.072,
            "item_cell_type": 1,
            "item_id": 7692653405960935721,
            "item_id_str": "7692653405960935721",
            "item_type": 2
          }
        }
      ]
    }
  }
}
```

### Notes

- Obtain the required `block_type` value from the hot search board list endpoint.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hashtag Details](/model/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/model/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/model/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/hot-search-board-detail.json`](../../../../catalog/models/pipixia/app/hot-search-board-detail.json) · Store page: https://www.sandbase.ai/model/pipixia/app/hot-search-board-detail
