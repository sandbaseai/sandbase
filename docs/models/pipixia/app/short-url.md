# Pipixia Short URL Conversion API: pricing, parameters and code examples

`pipixia/app/short-url` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a shortened link for a specified web address. Takes an original web link as input and converts it into a Pipixia-compatible short URL format.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/short-url", "original_url": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/short-url', {'original_url': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/short-url", {
  "original_url": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/short-url", sandbase.Params{
	"original_url": "example",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/short-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `original_url` | string | yes | Original URL, can be any link.  |

## Details

Returns a Pipixia short URL for a web address you send. It needs one input, `original_url`, which can be any link.

### Use cases

- Shorten a Pipixia post link such as `https://h5.pipix.com/item/7385813877985909043` before sharing it in a message or caption.
- Convert external web addresses into the `https://h5.pipix.com/s/` short format.
- Batch-generate compact links for a list of posts in a campaign report or share sheet.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/short-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"original_url": "https://h5.pipix.com/item/7385813877985909043"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `original_url` | string | Yes | Original URL, can be any link. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "short_url": "https://h5.pipix.com/s/rFYPVXgqO3o/"
  },
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691714055
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.short_url` | The shortened link for the `original_url` you sent. It uses the `https://h5.pipix.com/s/<code>/` format. |
| `status_code` | Result code of the call. `0` means the call succeeded. |
| `message` | Short status text. It reads `success` when the call works. |
| `prompt` | Extra prompt text. It is an empty string in the sample response. |
| `time` | Numeric timestamp in the response. The sample value `1793691714055` has 13 digits. |

### Notes

- Send `original_url` as a full address that starts with `https://`. A Pipixia post link has the form `https://h5.pipix.com/item/<post id>`.
- Read the result from `data.short_url`. Check that `status_code` is `0` before you use it.
- To look up the post behind a link, call [Pipixia Post Detail](/apis/pipixia/app/post-detail) with the post ID from the `/item/` path.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/short-url.json`](../../../../catalog/models/pipixia/app/short-url.json) · Store page: https://www.sandbase.ai/model/pipixia/app/short-url
