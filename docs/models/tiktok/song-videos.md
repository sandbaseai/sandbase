# TikTok Song Videos API: pricing, parameters and code examples

`tiktok/song-videos` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0006 per call · **Modes:** sync

List TikTok videos that use a given song or sound (with descriptions, authors, and engagement stats).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0006**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/song-videos", "clipId": "7439295283975702544"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/song-videos', {'clipId': '7439295283975702544'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/song-videos", {
  "clipId": "7439295283975702544"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/song-videos", sandbase.Params{
	"clipId": "7439295283975702544",
})
```

Same call via the path form: `POST /v1/api/tiktok/song-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `clipId` | string | yes | The song ID found in TikTok music URLs (e.g. 7439295283975702544).  |
| `cursor` | string |  | Pagination cursor for retrieving the next page of results.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor`, and it is served only by a source that returns every…  |

## Details

List TikTok videos that use a given song or sound (with descriptions, authors, and engagement stats).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/song-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"clipId": "7439295283975702544"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `clipId` | string | Yes | The song ID found in TikTok music URLs (e.g. 7439295283975702544). |
| `cursor` | string | No | Pagination cursor for retrieving the next page of results. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor`, and it is served only by a source that returns every one |

### Pricing

Billed at the actual cost of each call, usually $0.0006 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/song-videos.json`](../../../catalog/models/tiktok/song-videos.json) · Store page: https://www.sandbase.ai/model/tiktok/song-videos
