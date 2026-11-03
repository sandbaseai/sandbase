# WeChat MP Search Suggestions API: pricing, parameters and code examples

`wechat-mp/search-suggestions` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.114286 per call · **Modes:** sync

Get WeChat search suggestions for a keyword, optionally scoped by a supported business type. Use it to expand or refine a query before a targeted WeChat search.

## Pricing

- **$0.114286 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/search-suggestions", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/search-suggestions', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/search-suggestions", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/search-suggestions", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/search-suggestions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Keyword used to fetch WeChat search suggestions.  |
| `businessType` | string |  | WeChat search business type used to scope suggestion results. one of: `ALL`, `ACCOUNT`, `ARTICLE`, `CHANNEL`, `MOMENTS`, `LIVE`, `EMOJI`, `AUDIO`, `BOOK`, `WECHAT_INDEX`, `NEWS`, `MINI_PROGRAM` …; default `"ALL"` |

## Details

Returns a list of WeChat search suggestion words for a keyword. It needs a `keyword` and accepts an optional `businessType` to scope the suggestions to one WeChat search area, such as `ARTICLE` or `MINI_PROGRAM`.

### Use cases

- Expand a seed topic like `人工智能` into longer related search phrases for content research.
- Compare suggestions across `businessType` values such as `ARTICLE`, `ACCOUNT` and `MINI_PROGRAM` to see how the same keyword is searched in each area.
- Build a keyword list for a targeted WeChat search by collecting suggestions for many seed words.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/search-suggestions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword used to fetch WeChat search suggestions. |
| `businessType` | string | No | WeChat search business type used to scope suggestion results. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "sug_words": [
      "人工智能"
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data` | Object that wraps the suggestion result. |
| `data.sug_words` | List of suggested search phrases for the keyword, in the order the API returns them. |
| `data.sug_words[]` | One suggested phrase as a plain string. In the sample, the first item repeats the keyword and the next items are longer related phrases such as `人工智能训练师`. |

### Notes

- Set `businessType` to one of `ALL`, `ACCOUNT`, `ARTICLE`, `CHANNEL`, `MOMENTS`, `LIVE`, `EMOJI`, `AUDIO`, `BOOK`, `WECHAT_INDEX`, `NEWS`, `MINI_PROGRAM` or `ENCYCLOPEDIA`. The default is `ALL`.
- The request has no pagination parameters.
- To search the WeChat Index for a chosen phrase, call [WeChat MP WeChat Index Search](/apis/wechat-mp/search-wechat-index).

### Pricing

$0.114286 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-mp/search-suggestions.json`](../../../catalog/models/wechat-mp/search-suggestions.json) · Store page: https://www.sandbase.ai/model/wechat-mp/search-suggestions
