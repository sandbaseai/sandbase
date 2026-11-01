# TikTok Hashtag Videos

`tiktok/hashtag-videos` · api · TikTok

List recent TikTok videos for a hashtag (creator, caption, views, likes, shares).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/hashtag-videos", "hashtag": "cooking"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/hashtag-videos', {'hashtag': 'cooking'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/hashtag-videos", {
  "hashtag": "cooking"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/hashtag-videos", sandbase.Params{
	"hashtag": "cooking",
})
```

Same call via the path form: `POST /v1/api/tiktok/hashtag-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results to return (1-20, default 20). range 1–20 |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of videos.  |
| `hashtag` | string | yes | TikTok hashtag to fetch videos for, without the # prefix (e.g. booktok).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `playCount`, and it is served only by a source that returns every…  |

## Details

List recent TikTok videos for a hashtag (creator, caption, views, likes, shares).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/hashtag-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "hashtag": "cooking"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag` | string | Yes | TikTok hashtag to fetch videos for, without the # prefix (e.g. booktok). |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of videos. |
| `limit` | integer | No | Maximum number of results to return (1-20, default 20). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `playCount`, and it is served only by a source that returns every one  |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/hashtag-videos.json`](../../../catalog/models/tiktok/hashtag-videos.json) · Store page: https://www.sandbase.ai/model/tiktok/hashtag-videos
