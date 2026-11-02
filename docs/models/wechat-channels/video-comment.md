# WeChat Channels Video Comments API: pricing, parameters and code examples

`wechat-channels/video-comment` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.020833 per call · **Modes:** sync

Get first-level comments for a WeChat Channels video by object ID with continuation-buffer pagination. Use it to review audience discussion on known video content.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/video-comment", "objectId": "15042116979764234697"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/video-comment', {'objectId': '15042116979764234697'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/video-comment", {
  "objectId": "15042116979764234697"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/video-comment", sandbase.Params{
	"objectId": "15042116979764234697",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/video-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `objectId` | string | yes | WeChat Channels video object id used to fetch first-level comments. If you only have the exportId returned by a video search result, first call the Export Id Conversion (V1) endpoint at…  |
| `last_buffer` | string |  | Pagination buffer returned by the previous first-level WeChat Channels comment response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.  |
| `objectNonceId` | string |  | Optional WeChat Channels object nonce id.  |

## Details

Get first-level comments for a WeChat Channels video by object ID with continuation-buffer pagination. Use it to review audience discussion on known video content.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/video-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"objectId": "15042116979764234697", "objectNonceId": "13454967799950666727_0_0_4_32_0_45d03c48-d38a-11f1-8fe5-9b7987977b23"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `objectId` | string | Yes | WeChat Channels video object id used to fetch first-level comments. If you only have the exportId returned by a video search result, first call the Export Id Conversion (V1) endpoint at /api/weixin-channels/convert-export-id/v1 to convert it to an objectId. |
| `objectNonceId` | string | No | Optional WeChat Channels object nonce id. |
| `last_buffer` | string | No | Pagination buffer returned by the previous first-level WeChat Channels comment response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/video-comment.json`](../../../catalog/models/wechat-channels/video-comment.json) · Store page: https://www.sandbase.ai/model/wechat-channels/video-comment
