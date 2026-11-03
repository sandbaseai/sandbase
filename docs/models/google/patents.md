# Google Patents API: pricing, parameters and code examples

`google/patents` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Search Google Patents with title, patent number, inventor, assignee, key dates, and PDF link.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/patents", "query": "wireless charging"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/patents', {'query': 'wireless charging'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/patents", {
  "query": "wireless charging"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/patents", sandbase.Params{
	"query": "wireless charging",
})
```

Same call via the path form: `POST /v1/api/google/patents` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | The Google Patents search query.  |

## Details

This API searches Google Patents and returns a list of matching patents. Each result has the title, publication number, inventor, assignee, key dates, and links. It needs one input: a search `query`.

### Use cases

- Find patents on a topic such as wireless charging before starting a new product.
- List the patents a company holds by searching for its name as assignee.
- Track filing and publication dates to see when activity in a technology area picked up.
- Collect PDF links for granted patents to read the full documents.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/patents" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "wireless charging"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The Google Patents search query. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "query": "wireless charging",
    "results": [
      {
        "assignee": "Dongguan Three in a Thousand Electronic Technology Co.,Ltd",
        "filedUtc": 1761004800,
        "image": "",
        "inventor": "Xie Hui",
        "language": "en",
        "link": "https://patents.google.com/patent/EM151206540002S/en",
        "pdfUrl": "",
        "publicationNumber": "EM151206540002S",
        "publishedUtc": 1761523200,
        "snippet": "",
        "title": "Battery chargers; Wireless chargers; Charging stations for mobile devices;"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.results[].title` | Title of the patent or design. It can be cut off with a trailing ellipsis. |
| `data.results[].publicationNumber` | Patent publication number, such as `US11303135B2`. |
| `data.results[].inventor / data.results[].assignee` | Name of the inventor and of the company or person the patent is assigned to. |
| `data.results[].filedUtc / data.results[].publishedUtc` | Filing date and publication date as Unix timestamps in seconds. |
| `data.results[].grantedUtc / data.results[].priorityUtc` | Grant date and priority date as Unix timestamps in seconds. These appear only on some results. |
| `data.results[].link` | URL of the patent page on Google Patents. |
| `data.results[].pdfUrl` | URL of the patent PDF. It is an empty string when no PDF is listed. |
| `data.results[].snippet` | Short text excerpt from the patent. It is cut off and can be empty. |
| `data.results[].image` | URL of a patent image. It is an empty string when none is available. |
| `data.results[].language` | Language code of the result, such as `en`. |

### Notes

- Pass any Google Patents search text in `query`. The response echoes it in `data.query`.
- The request has no pagination parameter, so each call returns one list of results.
- Check that `grantedUtc`, `priorityUtc`, and `pdfUrl` exist and are not empty before you use them.
- To find academic papers on the same topic, try [Google Scholar](/apis/google/scholar).

### Pricing

Billed at the actual cost of each call, about $0.00085 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/patents.json`](../../../catalog/models/google/patents.json) · Store page: https://www.sandbase.ai/model/google/patents
