# TikTok Video API: pricing, parameters and code examples

`tiktok/video` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0004 per call · **Modes:** sync

Fetch a single TikTok video by URL with its caption and engagement counts (views, likes, comments, shares, saves).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0004**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/video"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/video', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/video", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/video", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string |  | TikTok video ID, the numeric run at the end of a video URL. Use it when a listing SKU handed you an id and no URL.  |
| `url` | string |  | Full TikTok video URL.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `views`, and it is served only by a source that returns every one of…  |

## Details

Fetch a single TikTok video by URL with its caption and engagement counts (views, likes, comments, shares, saves).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@mrbeast/video/7654638524729216287?_r=1&u_code=elgjf3ff8cajhk&preview_pb=0&sharer_language=en&_d=elh6737j6kjl71&share_item_id=7654638524729216287&source=h5_m"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | No | TikTok video ID, the numeric run at the end of a video URL. Use it when a listing SKU handed you an id and no URL. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `views`, and it is served only by a source that returns every one of t |
| `url` | string | No | Full TikTok video URL. |

### Pricing

Billed at the actual cost of each call, usually $0.0004 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/video.json`](../../../catalog/models/tiktok/video.json) · Store page: https://www.sandbase.ai/model/tiktok/video
