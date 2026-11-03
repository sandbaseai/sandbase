# WeChat Channels User Videos API: pricing, parameters and code examples

`wechat-channels/v2/user-videos` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Get the videos on a WeChat Channels account's homepage with descriptions, publish time, like, comment, share and favorite counts, and media download info, with cursor pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/user-videos", "raw": false, "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/user-videos', {'raw': False, 'username': 'v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/user-videos", {
  "raw": false,
  "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/user-videos", sandbase.Params{
	"raw": false,
	"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/user-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure (recommended for media download).  |
| `username` | string | yes | WeChat Channels finder username (`v2_…@finder` format), e.g. `v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder` (People's Daily). See `fetch_channel_info` / `fetch_video_detail` /…  |
| `last_buffer` |  |  | Optional pagination cursor (base64). **Leave empty for the first page**; when `up_continue` in the response is truthy, pass the previous page's `last_buffer` to get the next page. (base64 contains `+//=` characters,…  |

## Details

Returns the videos on a WeChat Channels account's homepage, with descriptions, publish time, engagement counts and media download info. It needs the account's finder `username` (`v2_…@finder` format).

### Use cases

- Track new posts from a news outlet or brand account on WeChat Channels.
- Compare likes, comments, shares and favorites across an account's recent videos.
- Collect `media.full_url` and `media.decode_key` values to archive videos.
- Page through an account's full video history with the `last_buffer` cursor.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/user-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder", "raw": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | WeChat Channels finder username (`v2_…@finder` format), e.g. `v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder` (People's Daily). See `fetch_channel_info` / `fetch_video_detail` / `f |
| `last_buffer` | string | No | Optional pagination cursor (base64). **Leave empty for the first page**; when `up_continue` in the response is truthy, pass the previous page's `last_buffer` to get the next page. (base64 contains `+//=` characters, henc |
| `raw` | boolean | No | Optional, default True. True=raw response; False=simplified parsed structure (recommended for media download). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 15,
  "debug_id": "a3070a39",
  "debug_info": "gAAAAABq6ZEqIrCnqzlwmkb-7or2u6AlRThh3a1MrErmnjEn0R2yuDt0CzWBrLW0KNVRZOx3oSJCTZhb…",
  "last_buffer": "EAEYADAAOKLXxZmn65cDQICgvdCOzqEDSIqUiIPD3Yvo0AFIipTAlo+ki+jQAUj1k8yGk8aK6NABSJ2U…",
  "nickname": "人民日报",
  "up_continue": 0,
  "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@…",
  "videos": [
    {
      "comment_count": 0,
      "cover_img_url": "",
      "create_time": 1793691867,
      "description": "一女子在西藏旅游时缺氧突发高原反应，藏族小女孩和众多好心人主动伸出援手。网友：比风景更治愈的是温暖的人心！",
      "fav_count": 2,
      "forward_count": 2,
      "id": "15046577947003718154",
      "like_count": 1,
      "location": {
        "buildingId": "",
        "city": "",
        "commercializationFlag": 0,
        "country": "",
        "flag": 0,
        "floorName": "",
        "latitude": 0,
        "longitude": 0
      },
      "media": {
        "cover_url": "https://wxapp.tc.qq.com/251/20304/stodownload?encfilekey=KGDRibp2wkicKURGKvIbDIm…",
        "cover_url_token": "&token=A…",
        "decode_key": "154800154",
        "duration": 49,
        "file_size": 51921573,
        "full_url": "http://wxapp.tc.qq.com/251/20302/stodownload?encfilekey=rgjNqbibdAo307NHkDDvERQk…",
        "height": 1904,
        "md5": "62b488876989af0d2ab0e7bb08797955"
      },
      "nickname": "人民日报",
      "object_nonce_id": "93982911…"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `nickname` | Display name of the account, for example `人民日报`. |
| `count` | Number of videos returned on this page. |
| `up_continue` | Shows whether more pages exist. `0` means no further page in this response. |
| `last_buffer` | Cursor string. Pass it as `last_buffer` in the next request to get the following page. |
| `videos[].id` | Video ID as a string. |
| `videos[].create_time` | Publish time as a Unix timestamp in seconds. |
| `videos[].description / videos[].title` | Text posted with the video. In this response both hold the same caption. |
| `videos[].like_count / videos[].comment_count / videos[].forward_count / videos[].fav_count` | Likes, comments, shares (forwards) and favorites for the video. |
| `videos[].media.full_url` | Video file URL. Use it with `media.decode_key` for download and decryption. |
| `videos[].media.duration / videos[].media.file_size / videos[].media.height` | Video length, file size and frame height. The response does not state units. |

### Notes

- Leave `last_buffer` empty for the first page. When `up_continue` is truthy, send the previous response's `last_buffer` to get the next page.
- This request used `raw: false`, which returns the simplified structure. The parameter docs recommend it for media download.
- If you only have a public Channel ID (`sph…`), convert it first with [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username).
- To get one video in full, call [WeChat Channels Video Detail](/apis/wechat-channels/v2/video-detail).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels Video Detail](/apis/wechat-channels/v2/video-detail): Get the full detail of a WeChat Channels video: description, author, engagement counts and the media URL with decode key for download.

---
Machine-readable: [`catalog/models/wechat-channels/v2/user-videos.json`](../../../../catalog/models/wechat-channels/v2/user-videos.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/user-videos
