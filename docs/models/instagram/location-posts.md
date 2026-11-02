# Instagram Location Posts API: pricing, parameters and code examples

`instagram/location-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List public Instagram posts tagged at a location, ranked or most recent, with cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/location-posts", "locationId": "103912118089363"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/location-posts', {'locationId': '103912118089363'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/location-posts", {
  "locationId": "103912118089363"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/location-posts", sandbase.Params{
	"locationId": "103912118089363",
})
```

Same call via the path form: `POST /v1/api/instagram/location-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Order the posts by Instagram's top ranking or by newest first. Defaults to ranked. one of: `ranked`, `recent` |
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor.  |
| `locationId` | string | yes | Instagram location id, as returned by instagram.search_locations.  |

## Details

List public Instagram posts tagged at a location, ranked or most recent, with cursor pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/location-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sort": "recent", "locationId": "103912118089363"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `locationId` | string | Yes | Instagram location id, as returned by instagram.search_locations. |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor. |
| `sort` | string | No | Order the posts by Instagram's top ranking or by newest first. Defaults to ranked. One of: `ranked`, `recent`. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/location-posts.json`](../../../catalog/models/instagram/location-posts.json) · Store page: https://www.sandbase.ai/model/instagram/location-posts
