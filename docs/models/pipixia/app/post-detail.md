# Pipixia Post Detail

`pipixia/app/post-detail` · api · Pipixia

Returns detailed data for a Pipixia post, including video and photo content, using a specific post identifier and optional post type.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/post-detail", "cell_id": "7411193113223371043"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/post-detail', {'cell_id': '7411193113223371043'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/post-detail", {
  "cell_id": "7411193113223371043"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/post-detail", sandbase.Params{
	"cell_id": "7411193113223371043",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cell_id` | string | yes | AKA video id, can be obtained from the share link.  |
| `cell_type` | integer |  | Video type, 1 for video, keep the default value for other types. default `1` |

## Details

Retrieve detailed post and video information from Pipixia by providing a `cell_id` and optional `cell_type`.

### Use cases

- Retrieve metadata and media content for a specific Pipixia video post.
- Inspect hashtag and post details linked to a shared Pipixia link.
- Extract post attributes for individual Pipixia photo or video items.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cell_id": "7411193113223371043"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cell_id` | string | Yes | AKA video id, can be obtained from the share link. |
| `cell_type` | integer | No | Video type, 1 for video, keep the default value for other types. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "data": {
      "hashtag": {
        "base_hashtag": {
          "avatars": [
            {}
          ]
        }
      }
    }
  }
}
```

### Notes

- Obtain `cell_id` directly from the Pipixia share link.
- Set `cell_type` to 1 for video posts, or keep the default value for other media types.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hashtag Details](/model/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/model/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/model/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/post-detail.json`](../../../../catalog/models/pipixia/app/post-detail.json) · Store page: https://www.sandbase.ai/model/pipixia/app/post-detail
