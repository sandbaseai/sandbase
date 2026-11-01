# TikTok Trending Feed

`tiktok/trending-feed` · api · TikTok

Sample TikTok's For You feed as served to a viewer in one country (caption, views, likes, comments, author). Returns a rotating sample, not a ranked chart.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/trending-feed", "region": "US"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/trending-feed', {'region': 'US'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/trending-feed", {
  "region": "US"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/trending-feed", sandbase.Params{
	"region": "US",
})
```

Same call via the path form: `POST /v1/api/tiktok/trending-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `trim` | string |  | Set to true to return a simplified response.  |
| `region` | string | yes | 2-letter country code for the proxy location (e.g. "US").  |

## Details

Sample TikTok's For You feed as served to a viewer in one country (caption, views, likes, comments, author). Returns a rotating sample, not a ranked chart.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/trending-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"region": "US"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `region` | string | Yes | 2-letter country code for the proxy location (e.g. "US"). |
| `trim` | string | No | Set to true to return a simplified response. |

### Pricing

Billed at the actual cost of each call, usually $0.0008 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/trending-feed.json`](../../../catalog/models/tiktok/trending-feed.json) · Store page: https://www.sandbase.ai/model/tiktok/trending-feed
