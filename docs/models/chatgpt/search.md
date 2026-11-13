# ChatGPT Search API: pricing, parameters and code examples

`chatgpt/search` · data API · ChatGPT · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0018 per call · **Modes:** sync

Ask ChatGPT a web-grounded question and receive an answer with source citations. ChatGPT composes each answer per request, so the same prompt returns different wording and a different source set.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0018**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "chatgpt/search", "prompt": "What are the best practices for home composting?"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('chatgpt/search', {'prompt': 'What are the best practices for home composting?'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("chatgpt/search", {
  "prompt": "What are the best practices for home composting?"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "chatgpt/search", sandbase.Params{
	"prompt": "What are the best practices for home composting?",
})
```

Same call via the path form: `POST /v1/api/chatgpt/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Question or research prompt for ChatGPT to answer using web search.  |
| `country` | string |  | ISO-3166 alpha-2 country to ask from, e.g. US, GB, DE. ChatGPT localizes both the pages it retrieves and the answer it writes, so this is the difference between what a US buyer and a UK buyer are told. default `"US"` |
| `webSearch` | string |  | Whether to insist ChatGPT browses the web. force instructs it to search and is the default; auto lets ChatGPT decide, which is cheaper and answers from memory roughly half the time. Check webSearchTriggered for what… one of: `force`, `auto`; default `"force"` |
| `requireAds` | boolean |  | Serve only from a source that can return sponsored placements shown with the answer. One source currently qualifies, so the request cannot fall back when it is unavailable. default `false` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `cited` or `ads`, and it is served only by a source that returns…  |
| `requirePlaces` | boolean |  | Serve only from a source that can return places shown with the answer. Leaving this off still returns places whenever the source that answered can. Turning it on selects the single source that guarantees them, which… default `false` |
| `requireEntities` | boolean |  | Serve only from a source that can return brands and other named entities recognized in the answer. One source currently qualifies, so the request cannot fall back when it is unavailable. default `false` |
| `requireShoppingCards` | boolean |  | Serve only from a source that can return shopping cards shown with the answer. Leaving this off still returns shopping cards whenever the source that answered can. Turning it on selects the single source that… default `false` |

## Details

Ask ChatGPT a web-grounded question and receive an answer with source citations. ChatGPT composes each answer per request, so the same prompt returns different wording and a different source set.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "chatgpt/search", "prompt": "What are the best practices for home composting?"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `prompt` | string | Yes | Question or research prompt for ChatGPT to answer using web search. |
| `country` | string | No | ISO-3166 alpha-2 country to ask from, e.g. US, GB, DE. ChatGPT localizes both the pages it retrieves and the answer it writes, so this is the difference between what a US buyer and a UK buyer are told. Default `"US"`. |
| `requireAds` | boolean | No | Serve only from a source that can return sponsored placements shown with the answer. One source currently qualifies, so the request cannot fall back when it is unavailable. Default `false`. |
| `requireEntities` | boolean | No | Serve only from a source that can return brands and other named entities recognized in the answer. One source currently qualifies, so the request cannot fall back when it is unavailable. Default `false`. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `cited` or `ads`, and it is served only by a source that returns every |
| `requirePlaces` | boolean | No | Serve only from a source that can return places shown with the answer. Leaving this off still returns places whenever the source that answered can. Turning it on selects the single source that guarantees them, which cost |
| `requireShoppingCards` | boolean | No | Serve only from a source that can return shopping cards shown with the answer. Leaving this off still returns shopping cards whenever the source that answered can. Turning it on selects the single source that guarantees  |
| `webSearch` | string | No | Whether to insist ChatGPT browses the web. force instructs it to search and is the default; auto lets ChatGPT decide, which is cheaper and answers from memory roughly half the time. Check webSearchTriggered for what actu |

### Pricing

Billed at the actual cost of each call, about $0.0018 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/chatgpt/search.json`](../../../catalog/models/chatgpt/search.json) · Store page: https://www.sandbase.ai/model/chatgpt/search
