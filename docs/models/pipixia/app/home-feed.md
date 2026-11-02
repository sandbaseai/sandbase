# Pipixia App Home Feed API: pricing, parameters and code examples

`pipixia/app/home-feed` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended posts from the Pipixia home feed. Supports cursor-based pagination to browse subsequent pages of feed items.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/home-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/home-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/home-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/home-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/pipixia/app/home-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. default `"0"` |

## Details

Access the Pipixia mobile home feed by passing an optional `cursor` parameter. It returns feed items including cell IDs, item contents, and timestamps.

### Use cases

- Browse trending content from the Pipixia recommendation stream.
- Monitor newly posted media and text in the general feed.
- Ingest public feed entries for community sentiment tracking.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/home-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "data": [
      {
        "cell_id": 7648926325327010111,
        "cell_id_str": "7648926325327010111",
        "cell_type": 1,
        "city_name": "江苏",
        "display_time": 1780904439,
        "last_view_time": 0,
        "item": {
          "ancestor_id": "7648834223972817161",
          "author_tags": "互互互",
          "content": "怎么会事",
          "create_time": 1780904439,
          "duration": 9.2,
          "item_cell_type": 1
        }
      }
    ]
  }
}
```

### Notes

- Defaults to 0 for the initial page.
- Pass the `loadmore_cursor` value from the previous response into `cursor` to retrieve subsequent pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hashtag Details](/model/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/model/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia Home Short Drama Feed](/model/pipixia/app/home-short-drama-feed): Returns short drama and novel recommendations from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/home-feed.json`](../../../../catalog/models/pipixia/app/home-feed.json) · Store page: https://www.sandbase.ai/model/pipixia/app/home-feed
