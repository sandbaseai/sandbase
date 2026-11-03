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

This API registers one view count increment on a Pipixia post. It needs the post's `cell_id` and returns a status code, a message, and a response timestamp. The `data` object in the response is empty.

### Use cases

- Send a view event for a single Pipixia video by its `cell_id`.
- Check the `status_code` value to confirm that a view increment request was accepted.
- Run a view event call after you resolve a share link to a video ID.
- Compare a post's view numbers before and after the call by pairing it with a post statistics lookup.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/increase-post-view-count" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cell_id": "7411241327297299263"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cell_id` | string | Yes | AKA video id, can be obtained from the share link. |
| `cell_type` | integer | No | Video type, 1 for video, keep the default value for other types. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {},
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691711611
}
```

### Response fields

| Field | Meaning |
|---|---|
| `status_code` | Result code of the call. `0` means the request succeeded. |
| `message` | Short text result. The value is `success` when the call worked. |
| `time` | Response timestamp as a number. The value looks like a Unix time in milliseconds. |
| `data` | Payload object. It is empty in this response, so the call returns no post data. |
| `prompt` | Extra text field. It is an empty string in this response. |

### Notes

- Get `cell_id` from the Pipixia post share link. It is the same as the video ID. Use [Pipixia Short URL Conversion](/apis/pipixia/app/short-url) to resolve a short link.
- Set `cell_type` to `1` for a video. Leave it out for other post types.
- To read the post's current counts, call [Pipixia Post Statistics](/apis/pipixia/app/post-statistics) or [Pipixia Post Detail](/apis/pipixia/app/post-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/increase-post-view-count.json`](../../../../catalog/models/pipixia/app/increase-post-view-count.json) · Store page: https://www.sandbase.ai/model/pipixia/app/increase-post-view-count
