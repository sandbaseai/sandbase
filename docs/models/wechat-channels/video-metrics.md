# WeChat Channels Video Metrics API: pricing, parameters and code examples

`wechat-channels/video-metrics` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get interaction metrics for a WeChat Channels video by object ID with optional continuation-buffer input. Use it to review engagement for known video content.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/video-metrics", "objectId": "15042116979764234697"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/video-metrics', {'objectId': '15042116979764234697'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/video-metrics", {
  "objectId": "15042116979764234697"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/video-metrics", sandbase.Params{
	"objectId": "15042116979764234697",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/video-metrics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `objectId` | string | yes | WeChat Channels video object id used to fetch interaction metrics.  |
| `last_buffer` | string |  | Pagination buffer returned by the previous WeChat Channels metrics response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.  |
| `objectNonceId` | string |  | Optional WeChat Channels object nonce id.  |

## Details

Returns interaction counts for one WeChat Channels video, plus its title and the name of the account that posted it. It needs the video `objectId`. You can also pass `objectNonceId`.

### Use cases

- Track likes, shares and comments on a known video to see how it performs.
- Compare `like_count` and `forward_count` across several videos from one creator.
- Pull the title and creator name for a video when you only have its object ID.
- Log the counts at different times to see how engagement grows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/video-metrics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"objectId": "15042116979764234697", "objectNonceId": "13454967799950666727_0_0_4_32_0_45d03c48-d38a-11f1-8fe5-9b7987977b23"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `objectId` | string | Yes | WeChat Channels video object id used to fetch interaction metrics. |
| `last_buffer` | string | No | Pagination buffer returned by the previous WeChat Channels metrics response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body. |
| `objectNonceId` | string | No | Optional WeChat Channels object nonce id. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count_info": {
    "comment_count": 984,
    "fav_count": 6927,
    "forward_count": 64934,
    "like_count": 4917,
    "version_data": {
      "data_version": 1793691946,
      "overwrite": false
    }
  },
  "nickname": "讲AI的老程",
  "object_id": "15042116979764234697",
  "title": "马斯克峰会8个颠覆性预言 3年5年10年 全部都会成真吗#ai #人工智能 #马斯克 #机器人 #人形机器人 #大模型 #agi #经济 #就业 #ai编程 #…",
  "username": "v2_060000231003b20faec8c6e48d1cc7d0c704ed37b077c63a30935687f6c94777ccc8aadbd72c@…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count_info.like_count` | Number of likes on the video. |
| `count_info.comment_count` | Number of comments on the video. |
| `count_info.fav_count` | Number of times viewers marked the video as a favorite. |
| `count_info.forward_count` | Number of times the video was forwarded. |
| `count_info.version_data.data_version / count_info.version_data.overwrite` | Version number of the count data and an `overwrite` flag. The response does not explain how to use them. |
| `object_id` | ID of the video. It matches the `objectId` you sent. |
| `title` | Video title text, including its hashtags. |
| `nickname` | Display name of the account that posted the video. |
| `username` | Internal account ID of the poster. It ends in `@finder`. |

### Notes

- Only `objectId` is required. `objectNonceId` is optional.
- `last_buffer` is for continuation. Leave it empty on the first call. For this POST endpoint, send it in an `application/x-www-form-urlencoded` form body.
- The sample response did not include a continuation buffer, so you may not need `last_buffer` for a single video.
- To find `objectId` values for an account, call [WeChat Channels Account Videos](/apis/wechat-channels/account-videos) or [WeChat Channels Video Search](/apis/wechat-channels/search-video).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/video-metrics.json`](../../../catalog/models/wechat-channels/video-metrics.json) · Store page: https://www.sandbase.ai/model/wechat-channels/video-metrics
