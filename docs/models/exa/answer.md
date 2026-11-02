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

Provides answers accompanied by cited web sources based on a submitted `query`. It supports tuning the retrieval mode via `type` and structuring the output with `outputSchema`.

### Use cases

- Retrieve cited answers to factual questions.
- Extract full-text web references alongside synthesized answers.
- Format answers into structured JSON schemas for automated workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/exa/answer" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The question to answer. |
| `text` | boolean | No | Include the full page text of each citation. |
| `type` | string | No | Retrieval mode used to gather sources before answering. |
| `outputSchema` | object | No | JSON Schema for a structured answer output. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "citations": [
    {
      "id": "https://en.wikipedia.org/wiki/_OpenAI",
      "title": "OpenAI",
      "url": "https://en.wikipedia.org/wiki/_OpenAI"
    }
  ]
}
```

### Notes

- The `type` parameter configures retrieval behavior across modes such as auto, fast, instant, deep-lite, deep, or deep-reasoning.
- Set `text` to true to include the complete page text for each returned citation.
- Supply `outputSchema` with a JSON schema to receive structured answer outputs.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/exa/answer.json`](../../../catalog/models/exa/answer.json) · Store page: https://www.sandbase.ai/model/exa/answer
