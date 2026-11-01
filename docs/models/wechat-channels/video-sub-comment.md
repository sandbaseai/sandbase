# WeChat Channels Video Sub Comments

`wechat-channels/video-sub-comment` · api · WeChat Channels

Get replies under a first-level WeChat Channels video comment using the video and root-comment IDs. Use it to continue a threaded comment discussion with buffer pagination.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/video-sub-comment", "objectId": "15042116979764234697", "rootCommentId": "15042242325261781458"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/video-sub-comment', {'objectId': '15042116979764234697', 'rootCommentId': '15042242325261781458'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/video-sub-comment", {
  "objectId": "15042116979764234697",
  "rootCommentId": "15042242325261781458"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/video-sub-comment", sandbase.Params{
	"objectId": "15042116979764234697",
	"rootCommentId": "15042242325261781458",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/video-sub-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `objectId` | string | yes | WeChat Channels video object id used to fetch second-level comment replies.  |
| `last_buffer` | string |  | Pagination buffer for WeChat Channels second-level comment replies. Use the first-level comment's last_buffer for the first reply page when present. For this POST endpoint, send it in an…  |
| `rootCommentId` | string | yes | Root first-level comment id returned by the WeChat Channels video comments endpoint.  |

## Details

Get replies under a first-level WeChat Channels video comment using the video and root-comment IDs. Use it to continue a threaded comment discussion with buffer pagination.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/video-sub-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"objectId": "15042116979764234697", "rootCommentId": "15042242325261781458"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `objectId` | string | Yes | WeChat Channels video object id used to fetch second-level comment replies. |
| `rootCommentId` | string | Yes | Root first-level comment id returned by the WeChat Channels video comments endpoint. |
| `last_buffer` | string | No | Pagination buffer for WeChat Channels second-level comment replies. Use the first-level comment's last_buffer for the first reply page when present. For this POST endpoint, send it in an application/x-www-form-urlencoded form body. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/video-sub-comment.json`](../../../catalog/models/wechat-channels/video-sub-comment.json) · Store page: https://www.sandbase.ai/model/wechat-channels/video-sub-comment
