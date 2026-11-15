# Channel3 Image Search API: pricing, parameters and code examples

`channel3/image-search` · data API · Channel3 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007 per call · **Modes:** async

Find products across retailers that match an image URL, with offers.

## Pricing

- **$0.007 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "channel3/image-search", "image_url": "<image_url>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('channel3/image-search', {'image_url': '<image_url>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("channel3/image-search", {
  "image_url": "<image_url>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "channel3/image-search", sandbase.Params{
	"image_url": "<image_url>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/channel3/image-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` |  |  | Products per page, 1-30. Channel3 default: 20.  |
| `config` | object |  |   |
| `filters` | object |  |   |
| `segment` |  |  | Image segmentation. Omit to search the whole image; "AUTO" crops the main product; an object name (e.g. "shoe", "mug") crops that object.  |
| `image_url` | string | yes | Publicly accessible HTTP/HTTPS URL of a product image to search by. Required on every page, including with page_token. Base64 and data: URLs are not accepted.  |
| `page_token` |  |  | next_page_token from a previous image search's output, to fetch the next page.  |

## Details

Find products across retailers that match an image URL, with offers.

---
Machine-readable: [`catalog/models/channel3/image-search.json`](../../../catalog/models/channel3/image-search.json) · Store page: https://www.sandbase.ai/model/channel3/image-search
