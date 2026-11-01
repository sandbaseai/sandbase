# YouTube Channel Playlists

`youtube/channel-playlists` · api · YouTube

List a YouTube channel's playlists by handle or channel ID with cursor pagination (title, video count, thumbnail).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/channel-playlists"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/channel-playlists', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/channel-playlists", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/channel-playlists", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/channel-playlists` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Continuation token from a previous response for pagination.  |
| `handle` | string |  | YouTube channel handle.  |
| `channelId` | string |  | YouTube channel ID.  |

## Details

List a YouTube channel's playlists by handle or channel ID with cursor pagination (title, video count, thumbnail).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/channel-playlists" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "@veritasium"}'
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
Machine-readable: [`catalog/models/youtube/channel-playlists.json`](../../../catalog/models/youtube/channel-playlists.json) · Store page: https://www.sandbase.ai/model/youtube/channel-playlists
