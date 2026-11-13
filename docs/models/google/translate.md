# Google Translate API: pricing, parameters and code examples

`google/translate` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Translate text with Google Translate between a source and target language code and get the translation with detected language.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/translate", "text": "Hello, how are you?", "from": "en", "to": "zh-CN"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/translate', {'text': 'Hello, how are you?', 'from': 'en', 'to': 'zh-CN'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/translate", {
  "text": "Hello, how are you?",
  "from": "en",
  "to": "zh-CN"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/translate", sandbase.Params{
	"text": "Hello, how are you?",
	"from": "en",
	"to": "zh-CN",
})
```

Same call via the path form: `POST /v1/api/google/translate` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `to` | string | yes | Parameter defines the language you want to translate the text into. It's a two or three-letter language code, optionally followed by a region or script code (e.g., `es` for Spanish, `pt-PT` for Portuguese (Portugal),…  |
| `from` | string | yes | Parameter defines the language of the text you want to translate. It's a two or three-letter language code, optionally followed by a region or script code (e.g., `es` for Spanish, `pt-PT` for Portuguese (Portugal), or…  |
| `text` | string | yes | Parameter defines the text you want to translate. Its length can't exceed 5,000 characters, emojis and some rare characters count as two.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Translate text with Google Translate between a source and target language code and get the translation with detected language.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/translate" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello, how are you?", "from": "en", "to": "zh-CN"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `text` | string | Yes | Parameter defines the text you want to translate. Its length can't exceed 5,000 characters, emojis and some rare characters count as two. |
| `from` | string | Yes | Parameter defines the language of the text you want to translate. It's a two or three-letter language code, optionally followed by a region or script code (e.g., `es` for Spanish, `pt-PT` for Portuguese (Portugal), or `zh-CN` for Chinese (S |
| `to` | string | Yes | Parameter defines the language you want to translate the text into. It's a two or three-letter language code, optionally followed by a region or script code (e.g., `es` for Spanish, `pt-PT` for Portuguese (Portugal), or `zh-CN` for Chinese  |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/translate.json`](../../../catalog/models/google/translate.json) · Store page: https://www.sandbase.ai/model/google/translate
