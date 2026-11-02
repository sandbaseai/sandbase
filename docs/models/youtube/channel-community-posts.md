# YouTube Channel Community Posts API: pricing, parameters and code examples

`youtube/channel-community-posts` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List a YouTube channel's community posts by handle or channel ID with cursor pagination (text, likes, image, publish time).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/channel-community-posts"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/channel-community-posts', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/channel-community-posts", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/channel-community-posts", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/channel-community-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Continuation token from a previous response for pagination.  |
| `handle` | string |  | YouTube channel handle.  |
| `channelId` | string |  | YouTube channel ID.  |

## Details

List a YouTube channel's community posts by handle or channel ID with cursor pagination (text, likes, image, publish time).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/channel-community-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "@MrBeast"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channelId` | string | No | YouTube channel ID. |
| `cursor` | string | No | Continuation token from a previous response for pagination. |
| `handle` | string | No | YouTube channel handle. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/youtube/channel-community-posts.json`](../../../catalog/models/youtube/channel-community-posts.json) · Store page: https://www.sandbase.ai/model/youtube/channel-community-posts
