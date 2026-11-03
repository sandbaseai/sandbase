# Toutiao Video Information API: pricing, parameters and code examples

`toutiao/app/video-info` · data API · Toutiao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specified Toutiao video using its post identifier. Useful for retrieving metadata and content status from Toutiao posts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/app/video-info", "group_id": "7431543350882206242"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('toutiao/app/video-info', {'group_id': '7431543350882206242'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("toutiao/app/video-info", {
  "group_id": "7431543350882206242"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "toutiao/app/video-info", sandbase.Params{
	"group_id": "7431543350882206242",
})
```

Same call via the path form: `POST /v1/api/toutiao/app/video-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `group_id` | string | yes | Post ID, can be obtained from the link  |

## Details

Returns information for one Toutiao video post. You send the post ID as `group_id`. The response holds a `data` object for the video, plus an error code and message.

### Use cases

- Check whether a Toutiao video link still resolves to a post.
- Pull video metadata for a post ID taken from a Toutiao link.
- Validate a list of `group_id` values before you call comment or article APIs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/toutiao/app/video-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"group_id": "7431543350882206242"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `group_id` | string | Yes | Post ID, can be obtained from the link |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": null,
  "err_no": 10400,
  "err_tips": "在这个星球中找不到",
  "message": "rpc err"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data` | Holds the video information when the lookup works. It is `null` when the post is not found, as in the sample call for `7431543350882206242`. |
| `err_no` | Numeric error code. The sample call returned `10400`, which came with `data` set to `null`. |
| `err_tips` | Short error text for the failed lookup. The sample call returned `在这个星球中找不到`. |
| `message` | Status message for the call. The sample call returned `rpc err`. |

### Notes

- Take `group_id` from the Toutiao video link. It is a long numeric string, for example `7431543350882206242`.
- Check `err_no` and whether `data` is `null` before you read any video fields.
- To read comments on the same post, call [Toutiao Post Comments](/apis/toutiao/app/comments).
- If this lookup fails, try [Toutiao Specified Video Details](/apis/toutiao/web/video-info) with the same post.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Toutiao Article Details (App)](/apis/toutiao/app/article-info): Returns details and interface settings for a specified Toutiao post.
- [Toutiao Post Comments](/apis/toutiao/app/comments): Returns user comments and interaction metrics for a specific Toutiao post.
- [Toutiao Profile User ID](/apis/toutiao/app/user-id): Resolves a Toutiao user profile URL into numeric and secure user identifiers.

---
Machine-readable: [`catalog/models/toutiao/app/video-info.json`](../../../../catalog/models/toutiao/app/video-info.json) · Store page: https://www.sandbase.ai/model/toutiao/app/video-info
