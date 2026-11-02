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

Converts long links into shortened URLs using `original_url`. Useful for sharing clean links across social workflows.

### Use cases

- Convert long content links into compact URLs for easy sharing.
- Transform external addresses into Pipixia short link format.
- Prepare streamlined links for mobile app distribution.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/short-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"original_url": "<original_url>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `original_url` | string | Yes | Original URL, can be any link. |

### Notes

- The `original_url` parameter is required and accepts any web address.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hashtag Details](/model/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/model/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/model/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/short-url.json`](../../../../catalog/models/pipixia/app/short-url.json) · Store page: https://www.sandbase.ai/model/pipixia/app/short-url
