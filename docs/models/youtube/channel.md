# YouTube Channel

`youtube/channel` · api · YouTube

Fetch a YouTube channel's stats (subscribers, video count, total views, description) and the links on its About page, by handle or channel ID.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00045**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/channel"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/channel', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/channel", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/channel", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/channel` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string |  | YouTube channel handle.  |
| `channelId` | string |  | YouTube channel ID (UC...). Pass it directly when you have it: some sources accept only the ID and otherwise look up the handle first, which adds a step.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `views`, and it is served only by a source that returns every one of…  |

## Details

Fetch a YouTube channel's stats (subscribers, video count, total views, description) and the links on its About page, by handle or channel ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/channel" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "@mkbhd"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channelId` | string | No | YouTube channel ID (UC...). Pass it directly when you have it: some sources accept only the ID and otherwise look up the handle first, which adds a step. |
| `handle` | string | No | YouTube channel handle. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `views`, and it is served only by a source that returns every one of t |

### Pricing

Billed at the actual cost of each call, usually $0.00045 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/youtube/channel.json`](../../../catalog/models/youtube/channel.json) · Store page: https://www.sandbase.ai/model/youtube/channel
