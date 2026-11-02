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
  -d '{"model": "firecrawl/batch/scrape", "urls": "<urls>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('firecrawl/batch/scrape', {'urls': '<urls>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("firecrawl/batch/scrape", {
  "urls": "<urls>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "firecrawl/batch/scrape", sandbase.Params{
	"urls": "<urls>",
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

Scrape a list of URLs in one job and get clean markdown and metadata for each page. It runs asynchronously: submit the job, then poll for the result.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/firecrawl/batch/scrape" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://example.com"], "formats": ["markdown"]}'
```

The call returns a run `id` with status `pending`. Poll `GET https://api.sandbase.ai/v1/run/{id}` until the status is `completed`; the job result is in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `urls` | array | Yes | URLs to scrape. |
| `formats` | array | No | Output formats for each page, e.g. `["markdown"]`. |

### Example response

Real result for the request above, trimmed to the main fields.

```json
{
  "status": "completed",
  "total": 1,
  "completed": 1,
  "data": [
    {
      "markdown": "This domain is for use in documentation examples without needing permission. …",
      "metadata": {
        "title": "Example Domain",
        "sourceURL": "https://example.com",
        "statusCode": 200,
        "language": "en"
      }
    }
  ]
}
```

### Pricing

$0.0075 per URL in `urls`, with a minimum of one URL per job. Failed jobs are not charged.

---
Machine-readable: [`catalog/models/firecrawl/batch/scrape.json`](../../../../catalog/models/firecrawl/batch/scrape.json) · Store page: https://www.sandbase.ai/model/firecrawl/batch/scrape
