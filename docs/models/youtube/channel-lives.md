# YouTube Channel Live Streams API: pricing, parameters and code examples

`youtube/channel-lives` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List a YouTube channel's live and past-live streams by handle or channel ID with cursor pagination (title, views, length, publish time).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/channel-lives"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/channel-lives', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/channel-lives", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/channel-lives", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/channel-lives` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Continuation token from a previous response for pagination.  |
| `handle` | string |  | YouTube channel handle.  |
| `channelId` | string |  | YouTube channel ID.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `lengthText`, and it is served only by a source that returns every…  |

## Details

List a YouTube channel's live and past-live streams by handle or channel ID with cursor pagination (title, views, length, publish time).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/channel-lives" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "@IShowSpeed"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channelId` | string | No | YouTube channel ID. |
| `cursor` | string | No | Continuation token from a previous response for pagination. |
| `handle` | string | No | YouTube channel handle. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `lengthText`, and it is served only by a source that returns every one |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/youtube/channel-lives.json`](../../../catalog/models/youtube/channel-lives.json) · Store page: https://www.sandbase.ai/model/youtube/channel-lives
