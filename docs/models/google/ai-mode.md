# Google AI Mode API: pricing, parameters and code examples

`google/ai-mode` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Ask Google AI Mode a prompt and receive the cited answer it generates. AI Mode composes the answer at search time, so repeat calls on one prompt can differ in wording and in which sources are cited.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/ai-mode", "prompt": "What is the Model Context Protocol and who maintains it?"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/ai-mode', {'prompt': 'What is the Model Context Protocol and who maintains it?'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/ai-mode", {
  "prompt": "What is the Model Context Protocol and who maintains it?"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/ai-mode", sandbase.Params{
	"prompt": "What is the Model Context Protocol and who maintains it?",
})
```

Same call via the path form: `POST /v1/api/google/ai-mode` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The question or prompt to answer with Google AI Mode.  |

## Details

Returns the answer Google AI Mode generates for a text prompt, plus the sources it cites. It needs one input, a `prompt` string with the question to answer.

### Use cases

- Check how Google AI Mode describes a brand, product or website and which pages it cites.
- Collect the source pages AI Mode cites for a topic to see which sites it relies on.
- Run the same prompt several times and compare the cited sources to see how the answer changes.
- Feed a question into a research workflow and keep the cited URLs for follow-up checks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/ai-mode" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is the Model Context Protocol and who maintains it?"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `prompt` | string | Yes | The question or prompt to answer with Google AI Mode. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "answer": "The Model Context Protocol (MCP) is an open standard and open-source framework d…",
    "answerMarkdown": "The Model Context Protocol (MCP) is an open standard and open-source framework d…",
    "citations": [
      {
        "title": "Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Model_Context_Protocol"
      }
    ],
    "prompt": "What is the Model Context Protocol and who maintains it?"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.answer` | The generated answer as plain text. |
| `data.answerMarkdown` | The same answer in Markdown. Use it when you want to keep the formatting of the answer. |
| `data.citations[]` | List of sources cited in the answer. |
| `data.citations[].title` | Title of the cited source, such as a site or page name. |
| `data.citations[].url` | Link to the cited page. |
| `data.prompt` | The prompt that the answer was generated for. It repeats the `prompt` you sent. |
| `found` | `true` when AI Mode returned a result for the prompt. |

### Notes

- Send the question in `prompt`. The request takes no other parameters and has no pagination.
- Repeat calls on one prompt can return different wording and different citations.
- The result is returned in `outputs[0].data`.
- For the short summary Google shows above regular search results, use [Google AI Overview](/apis/google/ai-overview).

### Pricing

Billed at the actual cost of each call, about $0.002 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/ai-mode.json`](../../../catalog/models/google/ai-mode.json) · Store page: https://www.sandbase.ai/model/google/ai-mode
