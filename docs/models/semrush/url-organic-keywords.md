# Semrush URL Organic Keywords API: pricing, parameters and code examples

`semrush/url-organic-keywords` · data API · Semrush · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02 per call · **Modes:** sync

Keywords a single URL ranks for in Google organic search, with position, search volume and CPC.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/url-organic-keywords", "database": "us", "url": "https://www.nike.com/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('semrush/url-organic-keywords', {'database': 'us', 'url': 'https://www.nike.com/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("semrush/url-organic-keywords", {
  "database": "us",
  "url": "https://www.nike.com/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "semrush/url-organic-keywords", sandbase.Params{
	"database": "us",
	"url": "https://www.nike.com/",
})
```

Same call via the path form: `POST /v1/api/semrush/url-organic-keywords` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Page URL to analyze.  |
| `database` | string | yes | Regional Semrush database, e.g. "us", "uk", "de".  |

## Details

Keywords a single URL ranks for in Google organic search, with position, search volume and CPC.

The result is returned in `outputs[0].data` as the official Semrush API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/semrush/url-organic-keywords" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"database": "us", "url": "https://www.nike.com/"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `database` | string | Yes | Regional Semrush database, e.g. "us", "uk", "de". |
| `url` | string | Yes | Page URL to analyze. |

### Pricing

Billed at the actual cost of each call, about $0.02 for a typical request; the cost grows with the number of rows returned. Searches with no results are billed at their actual cost. Failed calls are not charged.

---
Machine-readable: [`catalog/models/semrush/url-organic-keywords.json`](../../../catalog/models/semrush/url-organic-keywords.json) · Store page: https://www.sandbase.ai/model/semrush/url-organic-keywords
