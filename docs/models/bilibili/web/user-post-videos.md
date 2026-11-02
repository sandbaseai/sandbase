# Bilibili User Post Videos API: pricing, parameters and code examples

`bilibili/web/user-post-videos` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns videos posted on a Bilibili user's homepage. Query by user identifier with options to control sorting order and page number.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/user-post-videos", "order": "pubdate", "pn": 1, "uid": "178360345"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/user-post-videos', {'order': 'pubdate', 'pn': 1, 'uid': '178360345'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/user-post-videos", {
  "order": "pubdate",
  "pn": 1,
  "uid": "178360345"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/user-post-videos", sandbase.Params{
	"order": "pubdate",
	"pn": 1,
	"uid": "178360345",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/user-post-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pn` | integer |  | Page number default `1` |
| `uid` | string | yes | User UID  |
| `order` | string |  | Order method default `"pubdate"` |

## Details

Fetch video lists from a creator's Bilibili homepage by supplying `uid`. You can also specify pagination with `pn` and sort results using `order`.

### Use cases

- Browse video uploads from a specific Bilibili creator.
- Monitor new content posted by tracked Bilibili accounts.
- Sort a user's uploaded videos by post date.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/user-post-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "178360345"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User UID |
| `pn` | integer | No | Page number |
| `order` | string | No | Order method |

### Notes

- Use `uid` to specify the target Bilibili user identifier.
- Use `pn` for page navigation and `order` to set the result sort method.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/user-post-videos.json`](../../../../catalog/models/bilibili/web/user-post-videos.json) · Store page: https://www.sandbase.ai/model/bilibili/web/user-post-videos
