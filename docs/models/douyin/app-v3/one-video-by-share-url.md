# Douyin Single Video by Share URL API: pricing, parameters and code examples

`douyin/app-v3/one-video-by-share-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed video metadata and playback stream specifications for a specific Douyin post using its public share link.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/one-video-by-share-url", "share_url": "https://static.sandbase.ai/examples/a4f6780e-576a-4cd7-b3b0-ef3f793529c1/input/a037f59a-0a2e-4214-8938-b5c11d2ac95a.bin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/one-video-by-share-url', {'share_url': 'https://static.sandbase.ai/examples/a4f6780e-576a-4cd7-b3b0-ef3f793529c1/input/a037f59a-0a2e-4214-8938-b5c11d2ac95a.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/one-video-by-share-url", {
  "share_url": "https://static.sandbase.ai/examples/a4f6780e-576a-4cd7-b3b0-ef3f793529c1/input/a037f59a-0a2e-4214-8938-b5c11d2ac95a.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/one-video-by-share-url", sandbase.Params{
	"share_url": "https://static.sandbase.ai/examples/a4f6780e-576a-4cd7-b3b0-ef3f793529c1/input/a037f59a-0a2e-4214-8938-b5c11d2ac95a.bin",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/one-video-by-share-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `share_url` | string | yes | Share link  |

## Details

Get a Douyin video's full details straight from a share link (`douyin.com/video/<id>` or a `v.douyin.com` short link copied from the app): caption, stats, author, music and play URLs.

### Use cases

- Handle links pasted by users without parsing them yourself.
- Look up engagement and author for a shared video.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/one-video-by-share-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_url": "https://www.douyin.com/video/7512756548356492544"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_url` | string | Yes | Share link |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_detail": {
    "aweme_id": "7512756548356492544",
    "desc": "#neo浪漫蓝调",
    "create_time": 1749199950,
    "statistics": {
      "digg_count": 190359,
      "comment_count": 1456,
      "collect_count": 10797,
      "share_count": 27894
    },
    "author": {
      "nickname": "栗子味",
      "uid": "3635433641882579",
      "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_sma…",
      "unique_id": "Wuf666"
    },
    "video": {
      "duration": 12634,
      "width": 1024,
      "height": 576,
      "play_addr": {
        "url_list": [
          "https://v9-colds.douyinvod.com/0783179606d7b480c2e57136bba54…"
        ]
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_id` | Video ID. |
| `desc` | Caption with hashtags. |
| `create_time` | Publish time, Unix seconds. |
| `statistics` | `digg_count` (likes), `comment_count`, `collect_count` (saves), `share_count`. |
| `author` | `nickname`, numeric `uid`, `sec_uid` (used by profile APIs) and `unique_id` (抖音号). |
| `video.play_addr.url_list` | Play URLs; signed and temporary. |
| `video.duration` | Length in milliseconds. |

### Notes

- When you already have the `aweme_id`, [Douyin Video Detail](/apis/douyin/web/one-video) takes it directly.

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/one-video-by-share-url.json`](../../../../catalog/models/douyin/app-v3/one-video-by-share-url.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/one-video-by-share-url
