# Tavily URL Content Extraction API: pricing, parameters and code examples

`tavily/extract` · data API · Tavily · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

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

Returns the page title and images for each URL you send, with a list of URLs that could not be extracted. It needs a `urls` array with one or more web page addresses.

### Use cases

- Pull the title of a list of known pages to check what each URL points to.
- Collect the images found on specific pages by setting `include_images` to `true`.
- Find which URLs in a batch could not be extracted by reading `failed_results`.
- Run a batch of pages from a search or site crawl through one extraction call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tavily/extract" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://en.wikipedia.org/wiki/Artificial_intelligence"]}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `urls` | array | Yes | URLs to extract content from. |
| `extract_depth` | string | No | Depth of content extraction. |
| `include_images` | boolean | No | Include images found on the pages. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "failed_results": [],
  "request_id": "f594f392-10f6-4a3f-9d7c-ac020a617625",
  "response_time": 0.03,
  "results": [
    {
      "images": [],
      "title": "Artificial intelligence - Wikipedia",
      "url": "https://en.wikipedia.org/wiki/Artificial_intelligence"
    }
  ],
  "usage": {
    "credits": 1
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results[]` | One entry per URL that was extracted successfully. |
| `results[].url` | The page address that was extracted. Use it to match each result to the URL you sent. |
| `results[].title` | The title of the page, for example `Artificial intelligence - Wikipedia`. |
| `results[].images` | List of images found on the page. It is empty in this response, where `include_images` was not set. |
| `failed_results` | List of URLs that could not be extracted. It is empty when every URL worked. |
| `request_id` | Unique ID of the request, as a UUID. |
| `response_time` | Time taken for the request. The value is a number such as `0.03`. |
| `usage.credits` | Number of credits recorded for the call, such as `1`. |

### Notes

- Pass several addresses in the `urls` array to extract them in one call. Check both `results` and `failed_results` for each one.
- Set `extract_depth` to `basic` or `advanced`. Set `include_images` to `true` to fill `results[].images`.
- To find URLs to extract, call [Tavily Search](/apis/tavily/search) or [Tavily Site Map](/apis/tavily/map).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/tavily/extract.json`](../../../catalog/models/tavily/extract.json) · Store page: https://www.sandbase.ai/model/tavily/extract
