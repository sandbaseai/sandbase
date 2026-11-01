# Weibo User Album

`weibo/app/user-album` · api · Weibo

Returns the photo and media album content of a specified Weibo user. Supports cursor-based pagination using the since_id parameter.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-album", "uid": "<uid>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-album', {'uid': '<uid>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-album", {
  "uid": "<uid>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-album", sandbase.Params{
	"uid": "<uid>",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-album` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `since_id` |  |  | Pagination cursor, don't pass for first request, use returned since_id for subsequent requests  |

## Details

Retrieve album media content for a specific Weibo account using `uid`. Supports cursor-based pagination via `since_id` to cycle through pages.

### Use cases

- Inspect photo and media albums belonging to a specified Weibo user.
- Extract media assets from a creator profile for digital archiving.
- Browse historical profile images chronologically using cursor pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-album" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "<uid>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |
| `since_id` | string | No | Pagination cursor, don't pass for first request, use returned since_id for subsequent requests |

### Notes

- Requires `uid` to identify the target Weibo account.
- Do not pass `since_id` on the initial request; use the returned value for subsequent requests.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo App AI Smart Search](/model/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/model/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/model/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/user-album.json`](../../../../catalog/models/weibo/app/user-album.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-album
