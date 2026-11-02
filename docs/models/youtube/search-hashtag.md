# YouTube Hashtag Search API: pricing, parameters and code examples

`youtube/search-hashtag` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Search YouTube videos by hashtag with cursor pagination (title, channel, views, length, publish time).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/search-hashtag", "hashtag": "funny"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/search-hashtag', {'hashtag': 'funny'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/search-hashtag", {
  "hashtag": "funny"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/search-hashtag", sandbase.Params{
	"hashtag": "funny",
})
```

Same call via the path form: `POST /v1/api/youtube/search-hashtag` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | string |  | Content filter. Only "all" is served: no source we buy returns a Shorts row with the channel and publish time this endpoint requires. one of: `all` |
| `cursor` | string |  | Continuation token from a previous response for pagination.  |
| `hashtag` | string | yes | Hashtag to search for (without the leading #).  |

## Details

Search YouTube videos by hashtag with cursor pagination (title, channel, views, length, publish time).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/search-hashtag" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashtag": "funny"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag` | string | Yes | Hashtag to search for (without the leading #). |
| `cursor` | string | No | Continuation token from a previous response for pagination. |
| `type` | string | No | Content filter. Only "all" is served: no source we buy returns a Shorts row with the channel and publish time this endpoint requires. One of: `all`. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/youtube/search-hashtag.json`](../../../catalog/models/youtube/search-hashtag.json) · Store page: https://www.sandbase.ai/model/youtube/search-hashtag
