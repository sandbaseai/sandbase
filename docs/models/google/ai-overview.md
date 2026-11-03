# Google AI Overview API: pricing, parameters and code examples

`google/ai-overview` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0015 per call · **Modes:** sync

Ask Google Search a prompt and receive the AI Overview it generated for that scrape, with every source Google listed. Google regenerates the overview per search, so the same prompt can return different wording and a different source list.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0015**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/ai-overview", "prompt": "How does photosynthesis work?"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/ai-overview', {'prompt': 'How does photosynthesis work?'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/ai-overview", {
  "prompt": "How does photosynthesis work?"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/ai-overview", sandbase.Params{
	"prompt": "How does photosynthesis work?",
})
```

Same call via the path form: `POST /v1/api/google/ai-overview` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The question or prompt to answer with a Google AI Overview.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `scrapedAt`, and it is served only by a source that returns every…  |

## Details

This API returns the Google AI Overview for a prompt you send. The response has the answer text in plain and Markdown form, plus the list of sources Google cited. It needs one input, `prompt`.

### Use cases

- Track how Google words its AI answer for a question your brand or topic appears in.
- Collect the cited source URLs to see which sites Google credits for a given question.
- Compare AI Overview answers for several phrasings of the same question.
- Store the answer text with its `scrapedAt` time to keep a record of how an answer changed.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/ai-overview" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "How does photosynthesis work?"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `prompt` | string | Yes | The question or prompt to answer with a Google AI Overview. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `scrapedAt`, and it is served only by a source that returns every one  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "answer": "Photosynthesis is the process by which plants, algae, and cyanobacteria convert …",
    "answerMarkdown": "Photosynthesis is the process by which plants, algae, and cyanobacteria convert …",
    "citations": [
      {
        "index": 1,
        "title": "Photosynthesis",
        "url": "https://www.youtube.com/watch?v=g78utcLQrJ4&t=4"
      }
    ],
    "language": "en",
    "prompt": "How does photosynthesis work?",
    "scrapedAt": "2026-11-03 07:34:35 UTC"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.answer` | The AI Overview as plain text. It may include extra text after the main answer. |
| `data.answerMarkdown` | The same AI Overview formatted as Markdown. |
| `data.citations[].index` | The position of the source in the citation list, starting at 1. |
| `data.citations[].title / data.citations[].url` | The title and link of a source Google listed for the overview. |
| `data.prompt` | The prompt that was searched, echoed back. |
| `data.language` | Language code of the overview, such as `en`. |
| `data.scrapedAt` | The time of the scrape, in the format `2026-11-03 07:34:35 UTC`. |
| `found` | `true` when an AI Overview was returned for the prompt. |

### Notes

- Send `scrapedAt` in `requireFields` if your request must get that field. This can route the call to a dearer source and raise the price.
- Google regenerates the overview on each search, so repeat calls with the same `prompt` can return different text and different `citations`.
- For a conversational Google answer to the same kind of question, try [Google AI Mode](/apis/google/ai-mode).

### Pricing

Billed at the actual cost of each call, about $0.0015 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/ai-overview.json`](../../../catalog/models/google/ai-overview.json) · Store page: https://www.sandbase.ai/model/google/ai-overview
