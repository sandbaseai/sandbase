# Querit Web Search API: pricing, parameters and code examples

`querit/search` · data API · Querit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0048 per call · **Modes:** sync

Search the web with Querit and get ranked results with title, URL, snippet and optional page content chunks for AI grounding.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0048**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "querit/search", "query": "electric vehicle market share 2026"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('querit/search', {'query': 'electric vehicle market share 2026'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("querit/search", {
  "query": "electric vehicle market share 2026"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "querit/search", sandbase.Params{
	"query": "electric vehicle market share 2026",
})
```

Same call via the path form: `POST /v1/api/querit/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Maximum number of results returned. Default: server default (value unspecified).  |
| `query` | string | yes | Search term. Supports long natural-language descriptions  |
| `filters` | object |  | Filter conditions, see below  |
| `highlights` | boolean |  | Request relevant fragments from the body text. true extracts against the original query at the length the model judges best; the object form takes query and maxCharacters, see below  |
| `needContent` | boolean |  | Whether to return body text. When true, body text lands in each result's sentence field (sentence array) default `false` |
| `chunksPerDoc` | integer |  | Summary chunks per document. Free / PAYG support up to 1; Enterprise up to 3. Deprecated — still available, but migrate to highlights default `1` |
| `contentMaxChars` | integer |  | Optional body-text length limit per result, from 1 to 1,000,000 Unicode code points. Used with needContent: true; omit or send null to return the full available body text without truncation. Default: Full available…  |

## Details

Search the web with Querit and get ranked results with title, URL, snippet and optional page content chunks for AI grounding.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/querit/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "electric vehicle market share 2026"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search term. Supports long natural-language descriptions |
| `chunksPerDoc` | integer | No | Summary chunks per document. Free / PAYG support up to 1; Enterprise up to 3. Deprecated — still available, but migrate to highlights |
| `contentMaxChars` | integer | No | Optional body-text length limit per result, from 1 to 1,000,000 Unicode code points. Used with needContent: true; omit or send null to return the full available body text without truncation. Default: Full available body  |
| `count` | integer | No | Maximum number of results returned. Default: server default (value unspecified). |
| `filters` | object | No | Filter conditions, see below |
| `highlights` | boolean | No | Request relevant fragments from the body text. true extracts against the original query at the length the model judges best; the object form takes query and maxCharacters, see below |
| `needContent` | boolean | No | Whether to return body text. When true, body text lands in each result's sentence field (sentence array) |

### Pricing

Billed at the actual upstream cost of each call (about $0.0048 for the request above). Failed calls are not charged.

---
Machine-readable: [`catalog/models/querit/search.json`](../../../catalog/models/querit/search.json) · Store page: https://www.sandbase.ai/model/querit/search
