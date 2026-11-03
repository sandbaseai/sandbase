# WeChat Channels Video Detail API: pricing, parameters and code examples

`wechat-channels/v2/video-detail` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Get the full detail of a WeChat Channels video: description, author, engagement counts and the media URL with decode key for download. Look up by object ID, export ID or share URL.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/video-detail", "object_id": "15026240326408735234", "raw": false}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/video-detail', {'object_id': '15026240326408735234', 'raw': False})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/video-detail", {
  "object_id": "15026240326408735234",
  "raw": false
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/video-detail", sandbase.Params{
	"object_id": "15026240326408735234",
	"raw": false,
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure (recommended for media download).  |
| `export_id` |  |  | Second priority, optional. `exportId` from search results (must start with `export/`). Search results often only carry `exportId` without a plain object_id — pass export_id directly in that case (it expires, use it…  |
| `object_id` |  |  | Highest priority, optional. Video objectId (numeric), e.g. `14941130915890399732`. Obtainable from the video `id` of `fetch_user_videos` / `fetch_collection_videos`.  |
| `share_url` |  |  | Last, optional. Channels share URL (`https://weixin.qq.com/sph/…`), e.g. `https://weixin.qq.com/sph/AH3sCoIPhH`. Used only when both object_id and export_id are empty.  |
| `object_nonce_id` |  |  | Optional. `feedNonceId` (numeric) from search results, pairs with the above to improve hit rate.  |

## Details

Get a WeChat Channels (视频号) video by its `object_id`, `export_id` or share link: title, description, author, publish time and like, comment, forward, favorite and read counts.

### Use cases

- Track engagement of WeChat Channels videos.
- Identify the account behind a shared Channels video.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"object_id": "15026240326408735234", "raw": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `export_id` | string | No | Second priority, optional. `exportId` from search results (must start with `export/`). Search results often only carry `exportId` without a plain object_id — pass export_id directly in that case (it expires, use it soon) |
| `object_id` | string | No | Highest priority, optional. Video objectId (numeric), e.g. `14941130915890399732`. Obtainable from the video `id` of `fetch_user_videos` / `fetch_collection_videos`. |
| `object_nonce_id` | string | No | Optional. `feedNonceId` (numeric) from search results, pairs with the above to improve hit rate. |
| `raw` | boolean | No | Optional, default True. True=raw response; False=simplified parsed structure (recommended for media download). |
| `share_url` | string | No | Last, optional. Channels share URL (`https://weixin.qq.com/sph/…`), e.g. `https://weixin.qq.com/sph/AH3sCoIPhH`. Used only when both object_id and export_id are empty. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "id": "15026240326408735234",
  "title": "18岁生日当天，无证醉驾被查。小伙一听要拘留，脱口而出：“能不能让我爸去……”@安徽警方 \n",
  "description": "18岁生日当天，无证醉驾被查。小伙一听要拘留，脱口而出：“能不能让我爸去……”@安徽警方 \n",
  "nickname": "人民日报",
  "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@…",
  "create_time": 1791267433,
  "like_count": 7273,
  "comment_count": 41,
  "forward_count": 14324,
  "fav_count": 17302,
  "read_count": 0,
  "object_nonce_id": "2216029447755799692"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | Video `object_id`. |
| `title / description` | Title and description. |
| `nickname / username` | Account display name and internal username. |
| `create_time` | Publish time, Unix seconds. |
| `like_count / comment_count / forward_count / fav_count / read_count` | Engagement counts. |
| `object_nonce_id` | Nonce needed together with `object_id` by the comment APIs. |

### Notes

- Pass one identifier: `object_id` takes priority, then `export_id`, then `share_url`.
- Set `raw: true` to get the unprocessed upstream payload.

### Pricing

$0.01 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels User Videos](/apis/wechat-channels/v2/user-videos): Get the videos on a WeChat Channels account's homepage with descriptions, publish time, like, comment, share and favorite counts, and media download info, with…

---
Machine-readable: [`catalog/models/wechat-channels/v2/video-detail.json`](../../../../catalog/models/wechat-channels/v2/video-detail.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/video-detail
