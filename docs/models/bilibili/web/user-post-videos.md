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

Returns the videos posted on a Bilibili user's homepage, one page at a time. It needs the user's numeric `uid` and accepts optional `pn` and `order` parameters.

### Use cases

- List all videos a Bilibili creator has uploaded.
- Check a tracked account for new uploads by sorting by post date and reading the newest entries.
- Collect `bvid` values for a creator's videos, then request details or comments for each one.
- Count how many videos a user has posted using the page total.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/user-post-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "178360345"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User UID |
| `order` | string | No | Order method |
| `pn` | integer | No | Page number |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "episodic_button": {
      "text": "播放全部",
      "uri": "//www.bilibili.com/medialist/play/178360345?from=space"
    },
    "gaia_data": null,
    "gaia_res_type": 0,
    "is_risk": false,
    "list": {
      "slist": [],
      "tlist": null,
      "vlist": [
        {
          "aid": 117346609990524,
          "attribute": 16384,
          "author": "Azulsolitan",
          "bvid": "BV1RMaq65EAH",
          "comment": 0,
          "copyright": "3",
          "created": 1790567470,
          "description": ""
        }
      ]
    },
    "page": {
      "count": 6,
      "pn": 1,
      "ps": 25
    }
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.list.vlist[]` | The videos on the requested page. Each item is one posted video. |
| `data.list.vlist[].bvid / data.list.vlist[].aid` | The two identifiers of a video. `bvid` is the string form that starts with `BV`, and `aid` is the numeric form. |
| `data.list.vlist[].author` | The display name of the user who posted the video. |
| `data.list.vlist[].created` | The post time of the video as a Unix timestamp in seconds. |
| `data.list.vlist[].comment` | The comment count of the video. |
| `data.list.vlist[].description` | The text description of the video. It can be an empty string. |
| `data.list.vlist[].copyright` | The copyright type code of the video, returned as a string such as `1` or `3`. |
| `data.page.count` | The total number of videos for this user. |
| `data.page.pn / data.page.ps` | The current page number and the page size. In this response `pn` is `1` and `ps` is `25`. |
| `data.episodic_button.uri` | A link to play all of the user's videos in order. |

### Notes

- Pass `uid` as a string. The example value is `178360345`.
- Use `pn` to move through pages. Compare `data.page.count` with `data.page.ps` to see how many pages exist.
- `order` defaults to `pubdate`.
- To look up one video from the list, pass its `bvid` to [Bilibili Video Details](/apis/bilibili/web/one-video). To get a user's profile, use [Bilibili User Profile](/apis/bilibili/web/user-profile).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/user-post-videos.json`](../../../../catalog/models/bilibili/web/user-post-videos.json) · Store page: https://www.sandbase.ai/model/bilibili/web/user-post-videos
