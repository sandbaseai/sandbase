# Exa Question Answering API: pricing, parameters and code examples

`exa/answer` · data API · Exa · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0075 per call (free daily quota) · **Modes:** sync

Returns direct answers and cited web sources for a given query. Supports custom retrieval modes, optional full page text, and structured schema definitions.

## Pricing

- **$0.0075 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "exa/answer", "query": "Which manufacturers had the top three global EV sales in 2025?"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('exa/answer', {'query': 'Which manufacturers had the top three global EV sales in 2025?'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("exa/answer", {
  "query": "Which manufacturers had the top three global EV sales in 2025?"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "exa/answer", sandbase.Params{
	"query": "Which manufacturers had the top three global EV sales in 2025?",
})
```

Same call via the path form: `POST /v1/api/exa/answer` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `text` | boolean |  | Include the full page text of each citation.  |
| `type` | string |  | Retrieval mode used to gather sources before answering. one of: `auto`, `fast`, `instant`, `deep-lite`, `deep`, `deep-reasoning` |
| `query` | string | yes | The question to answer.  |
| `outputSchema` | object |  | JSON Schema for a structured answer output.  |

## Details

Ask a question and get a short answer grounded in live web search, with the sources Exa used as citations (title, URL, publish date). Optionally return a structured answer that follows your JSON Schema.

### Use cases

- Answer factual questions in an agent with cited sources.
- Extract structured facts with `outputSchema`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/exa/answer" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The question to answer. |
| `outputSchema` | object | No | JSON Schema for a structured answer output. |
| `text` | boolean | No | Include the full page text of each citation. |
| `type` | string | No | Retrieval mode used to gather sources before answering. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "answer": "OpenAI is an American artificial intelligence public benefit corporation based i…",
  "citations": [
    {
      "author": "Unauthorized hacks",
      "id": "https://en.wikipedia.org/wiki/OpenAI",
      "publishedDate": "2026-10-27T00:00:00.000Z",
      "title": "OpenAI",
      "url": "https://en.wikipedia.org/wiki/OpenAI"
    }
  ],
  "requestId": "f07f69f06d8753ed462b91b73130a835"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `answer` | The answer text, or an object when `outputSchema` is set. |
| `citations[]` | Sources: `title`, `url`, `publishedDate`, `author`, and `text` when requested. |

### Notes

- Set `text: true` to include each citation's page text, for example to verify the answer.

### Pricing

$0.0075 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/exa/answer.json`](../../../catalog/models/exa/answer.json) · Store page: https://www.sandbase.ai/model/exa/answer
