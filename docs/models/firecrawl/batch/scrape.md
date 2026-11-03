# Firecrawl Batch Scrape API: pricing, parameters and code examples

`firecrawl/batch/scrape` · data API · Firecrawl · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.0075 per run, depending on parameters · **Modes:** async

Scrape multiple URLs in a single batch job. Submit a list of URLs and poll for results as each page completes.

## Pricing

- Depends on parameters (`params.urls`).

| parameters | USD |
|---|---|
| defaults | 0.0075 |

Formula: `Math.max(1.0, len(params.urls ?? []) * 1.0) * 0.0075`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "firecrawl/batch/scrape", "urls": ["https://example.com"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('firecrawl/batch/scrape', {'urls': ['https://example.com']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("firecrawl/batch/scrape", {
  "urls": [
    "https://example.com"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "firecrawl/batch/scrape", sandbase.Params{
	"urls": []any{"https://example.com"},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/firecrawl/batch/scrape` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `urls` | array | yes | List of URLs to scrape.  |
| `formats` | array |  | Output formats for each page.  |

## Details

Scrapes a list of web pages in one batch job and returns the content of each page in the formats you pick, such as `markdown`. It needs a `urls` array and takes an optional `formats` array.

### Use cases

- Pull the text of many articles or docs pages as `markdown` in one call to feed a search index or an LLM.
- Collect the `links` of a set of known pages to see where each one points.
- Save `html` or `rawHtml` snapshots of a fixed list of pages for later comparison.
- Check the language and content type of many pages at once.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/firecrawl/batch/scrape" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://example.com"], "formats": ["markdown"]}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `urls` | array | Yes | List of URLs to scrape. |
| `formats` | array | No | Output formats for each page. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "completed": 1,
  "completedAt": "2026-11-03T07:33:32.124Z",
  "createdAt": "2026-11-03T07:33:31.624Z",
  "creditsUsed": 1,
  "data": [
    {
      "markdown": "This domain is for use in documentation examples without needing permission. Thi…",
      "metadata": {
        "cacheState": "hit",
        "cachedAt": "2026-11-03T07:33:19.669Z",
        "contentType": "text/html; charset=utf-8",
        "creditsUsed": 1,
        "favicon": "data:,",
        "language": "en",
        "proxyUsed": "basic",
        "scrapeId": "01a1a053-d76c-72e9-abc3-54d02183e9e6"
      }
    }
  ],
  "duration": 0.5,
  "expiresAt": "2026-11-04T07:33:41.000Z",
  "status": "completed",
  "success": true,
  "total": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `status / success` | Job state. `completed` with `success` set to `true` means the batch finished. |
| `total / completed` | Number of URLs submitted and number of pages finished so far. Compare them while polling. |
| `data[].markdown` | Page content as markdown. It appears when `markdown` is in `formats`. |
| `data[].metadata.scrapeId` | Unique ID of the scrape for this page. |
| `data[].metadata.language / contentType` | Language code detected for the page and the content type of the response. |
| `data[].metadata.cacheState / cachedAt` | Whether the page came from cache (`hit` in the example) and the time it was cached. |
| `data[].metadata.proxyUsed` | Type of proxy used for the fetch, such as `basic`. |
| `creditsUsed / data[].metadata.creditsUsed` | Credits used by the whole job and by each page. |
| `createdAt / completedAt / expiresAt` | ISO 8601 UTC timestamps for job creation, job completion, and when the job result expires. |
| `duration` | Duration value for the job, `0.5` in the example. |

### Notes

- The call is asynchronous. It returns a run `id` with status `pending`. Poll `GET https://api.sandbase.ai/v1/run/{id}` until the status is `completed`, then read the result from `outputs[0].data`.
- Allowed `formats` values are `markdown`, `html`, `rawHtml`, `links` and `screenshot`.
- Each item in `data` matches one URL. Check `completed` against `total` to see how many pages are done.
- The result has an `expiresAt` time, so save the data you need before then.

### Pricing

Billed at the actual cost of each call, about $0.0075 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/firecrawl/batch/scrape.json`](../../../../catalog/models/firecrawl/batch/scrape.json) · Store page: https://www.sandbase.ai/model/firecrawl/batch/scrape
