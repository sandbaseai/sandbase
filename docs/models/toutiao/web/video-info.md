# Toutiao Specified Video Details API: pricing, parameters and code examples

`toutiao/web/video-info` · data API · Toutiao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specified Toutiao video post. Retrieve post metadata and related video attributes using a valid post identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/web/video-info", "aweme_id": "7431543350882206242"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('toutiao/web/video-info', {'aweme_id': '7431543350882206242'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("toutiao/web/video-info", {
  "aweme_id": "7431543350882206242"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "toutiao/web/video-info", sandbase.Params{
	"aweme_id": "7431543350882206242",
})
```

Same call via the path form: `POST /v1/api/toutiao/web/video-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Post ID  |

## Details

Returns details for one Toutiao video post, looked up by its post ID in `aweme_id`. The sample response for this ID holds only a `delete` flag and a status message.

### Use cases

- Check whether a known Toutiao video post is still available before you process it.
- Validate a stored list of Toutiao post IDs and flag the ones that return a `delete` value.
- Test an `aweme_id` before you call a richer video endpoint for the same post.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/toutiao/web/video-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7431543350882206242"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Post ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "delete": 1
  },
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data` | Object that holds the result for the requested post. |
| `data.delete` | Deletion flag for the post. The sample shows `1` for the requested ID, which suggests the post was removed. The response does not define the values, so check against a post you know is live. |
| `message` | Status text for the call. The sample returns `success`. |

### Notes

- Pass the post ID as a string in `aweme_id`, for example `7431543350882206242`.
- A `success` message does not mean the post has full details. The sample response returned only `data.delete`.
- To get more video fields, try [Toutiao Video Information](/apis/toutiao/app/video-info).
- For article posts, use [Toutiao Article Details (Web)](/apis/toutiao/web/article-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Toutiao Article Details (Web)](/apis/toutiao/web/article-info): Returns detailed post information and interface action settings for a specified Toutiao article based on its unique post identifier.

---
Machine-readable: [`catalog/models/toutiao/web/video-info.json`](../../../../catalog/models/toutiao/web/video-info.json) · Store page: https://www.sandbase.ai/model/toutiao/web/video-info
