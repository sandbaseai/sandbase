# Bing Copilot Answer API: pricing, parameters and code examples

`bing/copilot` · data API · Bing · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Bing Copilot's conversational answer to a prompt, with the text blocks and cited references.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bing/copilot", "q": "what is the capital of france"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bing/copilot', {'q': 'what is the capital of france'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bing/copilot", {
  "q": "what is the capital of france"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bing/copilot", sandbase.Params{
	"q": "what is the capital of france",
})
```

Same call via the path form: `POST /v1/api/bing/copilot` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | conversational prompt; param name not independently confirmed  |

## Details

This API returns Bing Copilot's answer to a conversational prompt. It gives a short summary line, the full answer as typed text blocks, and the web pages cited as sources. It needs one input, the prompt text in `q`.

### Use cases

- Add a short sourced answer to a search box or chatbot in your own app.
- Collect the cited pages for a question to build a reading list or check where a claim comes from.
- Render the answer with its own headings and paragraphs by looping over the text blocks.
- Compare how Copilot answers different phrasings of the same question.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bing/copilot" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "what is the capital of france"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | conversational prompt; param name not independently confirmed |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "header": "The capital of France is Paris, the country’s political, cultural, and economic …",
  "references": [
    {
      "index": 0,
      "link": "https://en.wikipedia.org/wiki/Paris",
      "snippet": "As the capital of France, Paris is the seat of France's national government. For…",
      "source": "Wikipedia",
      "title": "Paris - Wikipedia"
    }
  ],
  "search_information": {},
  "text_blocks": [
    {
      "snippet": "Paris is not only the administrative capital of France but also one of the most …",
      "snippet_highlighted_words": [
        "Paris"
      ],
      "type": "paragraph"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `header` | A one-sentence summary answer to the prompt. |
| `text_blocks[].type` | The kind of block, such as `paragraph` or `heading`. Use it to decide how to render each block. |
| `text_blocks[].snippet` | The text of the block. The value may be cut short in long answers. |
| `text_blocks[].level` | The heading level. It appears on blocks where `type` is `heading`. |
| `text_blocks[].snippet_highlighted_words` | Words in the paragraph that Copilot highlighted, such as names and titles. |
| `references[].index` | Position of the cited source in the list, starting at `0`. |
| `references[].title / references[].link` | The title and URL of the cited web page. |
| `references[].snippet` | An excerpt from the cited page. |
| `references[].source` | The name or domain of the site that hosts the cited page. |

### Notes

- Send the prompt as `q`. It is the only parameter and it is required.
- The result is in `outputs[0].data`.
- `search_information` came back as an empty object for the sample request, so do not rely on it.
- To find images or videos on the same topic, call [Bing Images Search](/apis/bing/images) or [Bing Videos Search](/apis/bing/videos).

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/bing/copilot.json`](../../../catalog/models/bing/copilot.json) · Store page: https://www.sandbase.ai/model/bing/copilot
