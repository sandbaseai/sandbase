# Pipixia Post View Count Increment API: pricing, parameters and code examples

`pipixia/app/increase-post-view-count` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Registers an increment for a Pipixia post view count using the specified cell ID. Returns a status code along with a response timestamp.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/increase-post-view-count", "cell_id": "7411241327297299263"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/increase-post-view-count', {'cell_id': '7411241327297299263'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/increase-post-view-count", {
  "cell_id": "7411241327297299263"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/increase-post-view-count", sandbase.Params{
	"cell_id": "7411241327297299263",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/increase-post-view-count` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cell_id` | string | yes | AKA video id, can be obtained from the share link.  |
| `cell_type` | integer |  | Video type, 1 for video, keep the default value for other types.  |

## Details

Registers a view count increment on a Pipixia post using `cell_id` and an optional `cell_type` parameter.

### Use cases

- Increment view counts on specific Pipixia posts programmatically.
- Simulate audience views during automated engagement workflows.
- Trigger view event registrations for verified video links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/increase-post-view-count" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cell_id": "7411241327297299263"}'
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
  "status_code": 0,
  "time": 1791290486790
}
```

### Notes

- `cell_id` corresponds to the video ID and can be obtained from the post share link.
- `cell_type` accepts integer values, where `1` specifies video content.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/increase-post-view-count.json`](../../../../catalog/models/pipixia/app/increase-post-view-count.json) · Store page: https://www.sandbase.ai/model/pipixia/app/increase-post-view-count
