# Bilibili User homepage video data V2 API: pricing, parameters and code examples

`bilibili/web/user-post-videos-v2` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get user homepage video data V2 on Bilibili. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/user-post-videos-v2", "uid": "178360345"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/user-post-videos-v2', {'uid': '178360345'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/user-post-videos-v2", {
  "uid": "178360345"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/user-post-videos-v2", sandbase.Params{
	"uid": "178360345",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/user-post-videos-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pn` | integer |  | Page number, no cap default `1` |
| `ps` | integer |  | Page size, max 100 default `30` |
| `uid` | string | yes | Uid  |
| `keyword` | string |  | Keyword, empty returns all  |

## Details

Returns a page of videos posted by one Bilibili user, with title, video IDs, cover image, duration, publish time and view count for each video. It needs the user's numeric `uid`. You can filter by `keyword` and page with `pn` and `ps`.

### Use cases

- List all videos a creator has posted to track their upload history.
- Search one creator's videos for a topic by passing `keyword`.
- Collect `bvid` values to fetch full details for each video.
- Compare view counts across a creator's videos to see which ones performed best.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/user-post-videos-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "178360345", "pn": 1, "ps": 30}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes |  |
| `keyword` | string | No | Keyword, empty returns all |
| `pn` | integer | No | Page number, no cap |
| `ps` | integer | No | Page size, max 100 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "archives": [
      {
        "aid": 117346609990524,
        "bvid": "BV1RMaq65EAH",
        "ctime": 1790567471,
        "duration": 410,
        "enable_vt": 0,
        "interactive_video": false,
        "pic": "http://i0.hdslb.com/bfs/archive/224ab56f95a761db0a9bb5d58406109c37dfa55a.jpg",
        "playback_position": 0,
        "pubdate": 1790567470,
        "stat": {
          "view": 36
        },
        "state": 0,
        "title": "ATM10sky通关纪念"
      }
    ],
    "page": {
      "num": 1,
      "size": 30,
      "total": 6
    }
  },
  "message": "0",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.archives[].bvid / data.archives[].aid` | The two IDs of the video. `bvid` is the string form that starts with `BV`, and `aid` is the numeric form. |
| `data.archives[].title` | Title of the video. |
| `data.archives[].pic` | URL of the cover image. |
| `data.archives[].duration` | Length of the video. The value is a plain integer, for example `410`. |
| `data.archives[].pubdate / data.archives[].ctime` | Unix timestamps in seconds for the video. `pubdate` is the publish time and `ctime` is the creation time. |
| `data.archives[].stat.view` | View count of the video. |
| `data.archives[].upMid` | Numeric ID of the user who posted the video. It matches the `uid` in the request. |
| `data.archives[].interactive_video` | `true` if the video is an interactive video, otherwise `false`. |
| `data.page.num / data.page.size / data.page.total` | Current page number, page size, and a `total` count. In the sample, `total` is `6` for a request with `ps` set to `30`. |

### Notes

- `uid` is the numeric user ID, for example `178360345`. If you only have a profile link, use [Bilibili User ID Extraction](/apis/bilibili/web/get-user-id) to get it.
- Use `pn` for the page number (default `1`) and `ps` for the page size (default `30`, max `100`). Leave `keyword` empty to return all videos.
- To get full details for a video, pass its `bvid` to [Bilibili Video Details](/apis/bilibili/web/one-video).
- The result is returned in `outputs[0].data`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/bilibili/web/user-post-videos-v2.json`](../../../../catalog/models/bilibili/web/user-post-videos-v2.json) · Store page: https://www.sandbase.ai/model/bilibili/web/user-post-videos-v2
