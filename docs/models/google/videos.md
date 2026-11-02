# Google Videos API: pricing, parameters and code examples

`google/videos` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Search Google for video results (YouTube and others) with title, link, thumbnail, and source.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/videos", "query": "lofi hip hop"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/videos', {'query': 'lofi hip hop'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/videos", {
  "query": "lofi hip hop"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/videos", sandbase.Params{
	"query": "lofi hip hop",
})
```

Same call via the path form: `POST /v1/api/google/videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Two-letter country code for result localization (e.g. us, gb, de). default `"us"` |
| `hl` | string |  | Two-letter interface and results language code (e.g. en, es, de). default `"en"` |
| `query` | string | yes | The video search query.  |
| `location` | string |  | Fine-grained location for result localization, given as a canonical Google location string (e.g. 'New York, United States', 'London, United Kingdom'). More specific than the country-level gl.  |
| `timeframe` | string |  | Restrict results to a recent time window: 1h, 1d, 7d, 1y, or all. Default all (no time restriction). one of: `1h`, `1d`, `7d`, `1y`, `all` |
| `autocorrect` | boolean |  | Toggle Google spelling autocorrect (default true). Set false to search the exact query without correction.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `source`, and it is served only by a source that returns every one…  |

## Details

Search Google for video results (YouTube and others) with title, link, thumbnail, and source.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"gl": "us", "hl": "en", "query": "lofi hip hop"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The video search query. |
| `autocorrect` | boolean | No | Toggle Google spelling autocorrect (default true). Set false to search the exact query without correction. |
| `gl` | string | No | Two-letter country code for result localization (e.g. us, gb, de). Default `"us"`. |
| `hl` | string | No | Two-letter interface and results language code (e.g. en, es, de). Default `"en"`. |
| `location` | string | No | Fine-grained location for result localization, given as a canonical Google location string (e.g. 'New York, United States', 'London, United Kingdom'). More specific than the country-level gl. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `source`, and it is served only by a source that returns every one of  |
| `timeframe` | string | No | Restrict results to a recent time window: 1h, 1d, 7d, 1y, or all. Default all (no time restriction). One of: `1h`, `1d`, `7d`, `1y`, `all`. |

### Pricing

Billed at the actual cost of each call, usually $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/google/videos.json`](../../../catalog/models/google/videos.json) · Store page: https://www.sandbase.ai/model/google/videos
