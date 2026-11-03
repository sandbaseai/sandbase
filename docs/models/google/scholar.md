# Google Scholar API: pricing, parameters and code examples

`google/scholar` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Search Google Scholar for academic papers with title, authors, citation count, and PDF link.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/scholar", "query": "attention is all you need"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/scholar', {'query': 'attention is all you need'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/scholar", {
  "query": "attention is all you need"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/scholar", sandbase.Params{
	"query": "attention is all you need",
})
```

Same call via the path form: `POST /v1/api/google/scholar` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | The Google Scholar search query.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `year`, and it is served only by a source that returns every one of…  |

## Details

This API searches Google Scholar and returns a list of matching academic papers. Each result has a title, a citation count, a link, a PDF link when one exists, and a short text snippet. It needs one input, a search `query`.

### Use cases

- Find the most cited papers for a topic or a paper title.
- Collect direct PDF links for a reading list.
- Track how many times a known paper has been cited by repeating the same search.
- Match a paper title to its venue and author string from the `publicationInfo` text.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/scholar" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "attention is all you need"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The Google Scholar search query. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `year`, and it is served only by a source that returns every one of th |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "query": "attention is all you need",
    "results": [
      {
        "citedBy": 279724,
        "id": "5Gohgn6QFikJ",
        "link": "https://proceedings.neurips.cc/paper_files/paper/7181-attention-is",
        "pdfUrl": "https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd05…",
        "publicationInfo": "A Vaswani, N Shazeer, N Parmar… - Advances in neural …, 2017 - proceedings.neuri…",
        "snippet": "… to attend to all positions in the decoder up to and including that position. W…",
        "title": "Attention is all you need"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.query` | The search text the request used. |
| `data.results[].title` | Title of the paper. |
| `data.results[].citedBy` | Number of citations shown for the paper. |
| `data.results[].link` | URL of the page for the paper, such as a publisher or proceedings page. |
| `data.results[].pdfUrl` | Direct URL of a PDF. It is an empty string when no PDF was found. |
| `data.results[].publicationInfo` | One text line with the authors, venue, year and source site. The authors list can be cut short with an ellipsis. |
| `data.results[].snippet` | Short excerpt of text from the paper that matches the query. Some results do not have it. |
| `data.results[].id` | Result ID from Google Scholar, a short string such as `5Gohgn6QFikJ`. |
| `found` | `true` when the search returned results. |

### Notes

- Pass `requireFields` with `year` to make sure the serving source can return a year field. This can change the price of the call.
- The publication year is visible inside `publicationInfo` in the response above, as part of the text line.
- Check that `pdfUrl` is not empty before you use it.
- The request has no pagination parameter. It takes only `query` and `requireFields`.

### Pricing

Billed at the actual cost of each call, about $0.00085 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/scholar.json`](../../../catalog/models/google/scholar.json) · Store page: https://www.sandbase.ai/model/google/scholar
