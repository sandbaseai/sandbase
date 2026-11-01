# Zhihu Pin Detail

`zhihu/web/pin-detail` · api · Zhihu

Retrieves the full content and details of a single Zhihu pin using its unique pin identifier. Returns parsed text blocks, links, and formatting metadata.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/pin-detail", "pin_id": "2050290260991534603"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/pin-detail', {'pin_id': '2050290260991534603'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/pin-detail", {
  "pin_id": "2050290260991534603"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/pin-detail", sandbase.Params{
	"pin_id": "2050290260991534603",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/pin-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pin_id` | string | yes | Pin ID  |

## Details

Retrieves complete details for a specific Zhihu pin by supplying its `pin_id`. The response includes text sections, formatting attributes, and link types.

### Use cases

- Retrieve full text and links from a Zhihu pin.
- Display Zhihu pin content within external monitoring dashboards.
- Archive pin discussions and educational posts for research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/pin-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"pin_id": "2050290260991534603"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `pin_id` | string | Yes | Pin ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "content": [
    {
      "content": "普通人学AI，建议死磕这10个油管博主 | ① Andrej Karpathy｜AI界传奇人物主要分享：大模型原理、GPT训练过程、神经网络、AI未来趋势② Jeff Su｜AI…",
      "fold_type": "raw",
      "own_text": "普通人学AI，建议死磕这10个油管博主 | ① Andrej Karpathy｜AI界传奇人物主要分享：大模型原理、GPT训练过程、神经网络、AI未来趋势② Jeff Su｜AI…",
      "text_link_type": "internal",
      "type": "text"
    }
  ]
}
```

### Notes

- Provide the unique post identifier in `pin_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/pin-detail.json`](../../../../catalog/models/zhihu/web/pin-detail.json) · Store page: https://www.sandbase.ai/model/zhihu/web/pin-detail
