# Tavily URL Content Extraction

`tavily/extract` · api · Tavily

Extracts clean text content from specified web pages using their URLs. Supports basic or advanced extraction depth and optional image inclusion.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tavily/extract", "urls": ["https://static.sandbase.ai/examples/de3a14cf-48e2-4dd0-9ef9-4c4c1da485c8/input/2f4290fd-6946-4f6b-8cbe-5b3366e41080.com"]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tavily/extract', {'urls': ['https://static.sandbase.ai/examples/de3a14cf-48e2-4dd0-9ef9-4c4c1da485c8/input/2f4290fd-6946-4f6b-8cbe-5b3366e41080.com']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tavily/extract", {
  "urls": [
    "https://static.sandbase.ai/examples/de3a14cf-48e2-4dd0-9ef9-4c4c1da485c8/input/2f4290fd-6946-4f6b-8cbe-5b3366e41080.com"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tavily/extract", sandbase.Params{
	"urls": []any{"https://static.sandbase.ai/examples/de3a14cf-48e2-4dd0-9ef9-4c4c1da485c8/input/2f4290fd-6946-4f6b-8cbe-5b3366e41080.com"},
})
```

Same call via the path form: `POST /v1/api/tavily/extract` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `urls` | array | yes | URLs to extract content from.  |
| `extract_depth` | string |  | Depth of content extraction. one of: `basic`, `advanced` |
| `include_images` | boolean |  | Include images found on the pages.  |

## Details

Retrieves clean web page content for a list of target addresses supplied via `urls`. Set `extract_depth` to adjust extraction detail or toggle `include_images` to return page images.

### Use cases

- Extract readable web page text for downstream analysis.
- Retrieve article text and images from specific web addresses.
- Gather clean webpage data using basic or advanced extraction depths.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tavily/extract" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"urls": "<urls>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `urls` | array | Yes | URLs to extract content from. |
| `extract_depth` | string | No | Depth of content extraction. |
| `include_images` | boolean | No | Include images found on the pages. |

### Notes

- Set `extract_depth` to either basic or advanced to control parsing depth.
- Toggle `include_images` to true to return images identified on the pages.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tavily/extract.json`](../../../catalog/models/tavily/extract.json) · Store page: https://www.sandbase.ai/model/tavily/extract
