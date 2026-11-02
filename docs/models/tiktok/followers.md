# TikTok Followers API: pricing, parameters and code examples

`tiktok/followers` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

List the followers of a TikTok account by username, returning each follower's profile basics.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/followers", "handle": "stoolpresidente"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/followers', {'handle': 'stoolpresidente'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/followers", {
  "handle": "stoolpresidente"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/followers", sandbase.Params{
	"handle": "stoolpresidente",
})
```

Same call via the path form: `POST /v1/api/tiktok/followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor, to fetch the next page of followers.  |
| `handle` | string | yes | TikTok username whose followers to list, without the @ prefix (e.g. stoolpresidente).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `videoCount` or `secUid`, and it is served only by a source that…  |

## Details

List the followers of a TikTok account by username, returning each follower's profile basics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "stoolpresidente"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | TikTok username whose followers to list, without the @ prefix (e.g. stoolpresidente). |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor, to fetch the next page of followers. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `videoCount` or `secUid`, and it is served only by a source that retur |

### Pricing

Billed at the actual cost of each call, usually $0.0008 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/followers.json`](../../../catalog/models/tiktok/followers.json) · Store page: https://www.sandbase.ai/model/tiktok/followers
