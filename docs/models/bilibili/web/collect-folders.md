# Bilibili User Collection Folders API: pricing, parameters and code examples

`bilibili/web/collect-folders` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the collection folders owned by a specific Bilibili user. Supply the user identifier via `uid` to inspect their public collection folders.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/collect-folders", "uid": "178360345"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/collect-folders', {'uid': '178360345'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/collect-folders", {
  "uid": "178360345"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/collect-folders", sandbase.Params{
	"uid": "178360345",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/collect-folders` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User UID  |

## Details

Returns the public collection folders owned by a Bilibili user, with each folder's title, ID and item count. It needs one input, the user's numeric UID passed as `uid`.

### Use cases

- List all collection folders a Bilibili creator has made and compare their sizes.
- Find the folder ID to fetch the videos inside a specific folder.
- Track whether a user adds or removes collection folders by comparing `data.count` over time.
- Build a profile view that shows a user's saved-video topics by folder title.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/collect-folders" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "178360345"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User UID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "count": 4,
    "list": [
      {
        "attr": 22,
        "fav_state": 0,
        "fid": 28851128,
        "id": 2885112845,
        "is_kid_playlist": false,
        "kid_playlist_desc": "",
        "media_count": 14,
        "mid": 178360345,
        "title": "好抽象"
      }
    ],
    "season": null
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of collection folders returned for the user. |
| `data.list[].title` | Name of the collection folder, as set by the user. |
| `data.list[].media_count` | Number of items in the folder. |
| `data.list[].fid / data.list[].id` | Folder identifiers. `id` looks like `fid` followed by the last two digits of the owner's `mid`, so use the exact value you need for follow-up calls. |
| `data.list[].mid` | Numeric UID of the user who owns the folder. It matches the `uid` you sent. |
| `data.list[].attr` | Numeric attribute value for the folder. The response does not explain its bit meanings. |
| `data.list[].fav_state` | Numeric state flag for the folder. It is `0` for all folders in this response. |
| `data.list[].is_kid_playlist / data.list[].kid_playlist_desc` | Flag and description text for kid playlists. In this response the flag is `false` and the description is empty. |
| `data.season` | Season collection data. It is `null` for this user. |

### Notes

- Pass the user's numeric UID as a string in `uid`. If you only have a profile link, use [Bilibili User ID Extraction](/apis/bilibili/web/get-user-id) to get the UID.
- To see the videos inside a folder, call [Bilibili User Collection Folder Videos](/apis/bilibili/web/user-collection-videos) with a folder ID from `data.list[]`.
- The request has no pagination parameters. The response returns the folders in `data.list` along with a total in `data.count`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili Comprehensive Popular Videos](/apis/bilibili/web/com-popular): Returns a comprehensive list of trending videos on Bilibili, including video metadata, author details, and engagement statistics across pages.

---
Machine-readable: [`catalog/models/bilibili/web/collect-folders.json`](../../../../catalog/models/bilibili/web/collect-folders.json) · Store page: https://www.sandbase.ai/model/bilibili/web/collect-folders
