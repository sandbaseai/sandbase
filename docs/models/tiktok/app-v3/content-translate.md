# TikTok Content Translation API: pricing, parameters and code examples

`tiktok/app-v3/content-translate` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Translates provided text content into a designated target language. Accepts source text up to 5000 characters and returns the corresponding translated text string.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/content-translate"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/content-translate', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/content-translate", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/content-translate", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/content-translate` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `trg_lang` | string |  | Target language default `"zh-Hans"` |
| `src_content` | string |  | Source content, that is, the content that needs to be translated, the length does not exceed 5000 characters, if it exceeds 5000 characters, only the first 5000 characters will be translated. default `"Hello, welcome!"` |

## Details

Retrieve translated text strings by passing the source text in `src_content` and designating the destination language code in `trg_lang`.

### Use cases

- Translate TikTok post captions and descriptions into a target language.
- Localize user comments for multilingual analysis workflows.
- Convert video text content into different regional languages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/content-translate" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `trg_lang` | string | No | Target language |
| `src_content` | string | No | Source content, that is, the content that needs to be translated, the length does not exceed 5000 characters, if it exceeds 5000 characters, only the first 500… |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "translated_content_list": [
    {
      "src_content": "Hello, welcome!",
      "translated_content": "您好，欢迎！"
    }
  ]
}
```

### Notes

- The `src_content` parameter supports up to 5000 characters; input exceeding this limit is truncated to the first 5000 characters.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Creator Search Insights](/model/tiktok/app-v3/creator-search-insights): Get TikTok Creator Search Insights: trending search queries with popularity scores, trend history and video counts, including content-gap topics, by category a…

---
Machine-readable: [`catalog/models/tiktok/app-v3/content-translate.json`](../../../../catalog/models/tiktok/app-v3/content-translate.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/content-translate
