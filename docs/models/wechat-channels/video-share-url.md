# WeChat Channels Video Share URL API: pricing, parameters and code examples

`wechat-channels/video-share-url` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Generates a share link for a WeChat Channels video identified by objectId. Use it to share a known Channels video or obtain its link for a subsequent lookup.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/video-share-url", "objectId": "14941130915890399732"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/video-share-url', {'objectId': '14941130915890399732'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/video-share-url", {
  "objectId": "14941130915890399732"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/video-share-url", sandbase.Params{
	"objectId": "14941130915890399732",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/video-share-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `objectId` | string | yes | WeChat Channels video objectId as a numeric string of up to 32 digits.  |

## Details

Returns a share link for a WeChat Channels video. It needs the video's `objectId`, a numeric string of up to 32 digits.

### Use cases

- Build a shareable link for a Channels video when you only store its `objectId`.
- Add a clickable video link to a report or dashboard that tracks Channels content.
- Check that an `objectId` resolves to a share link before you run other lookups on it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/video-share-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"objectId": "14941130915890399732"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `objectId` | string | Yes | WeChat Channels video objectId as a numeric string of up to 32 digits. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "baseResponse": {
    "errMsg": {
      "pbRequestMsgInfo": null,
      "string": ""
    },
    "pbRequestMsgInfo": null,
    "ret": 0
  },
  "debug_id": "0d40f417",
  "debug_info": "gAAAAABq6ZEtz42gcdCDHhDLWar9xy2VgLbbYPFgPXOAEtdZkXrXcdwRuKMG5f15jimcUeQld7nEBFAJ…",
  "feedH5Url": "https://weixin.qq.com/sph/Aci4tPzBEf",
  "pbRequestMsgInfo": null,
  "urlList": [
    {
      "feedH5Url": "https://weixin.qq.com/sph/Aci4tPzBEf",
      "objectId": 14941130915890399732,
      "pbRequestMsgInfo": null
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `feedH5Url` | The share link for the video. It is a `weixin.qq.com/sph/` URL. The same value appears in `urlList[].feedH5Url`. |
| `urlList[].feedH5Url` | Share link for each requested video. The list holds one entry for the `objectId` you sent. |
| `urlList[].objectId` | The video `objectId` that the link belongs to. It comes back as a number here, so large values may lose precision in some JSON parsers. |
| `baseResponse.ret` | Status code of the call. The sample returns `0`. |
| `baseResponse.errMsg.string` | Error message text. It is an empty string in the sample response. |
| `debug_id / debug_info` | Debug values attached to the response. You do not need them to use the link. |

### Notes

- Send `objectId` as a string, as in the request example. Read `urlList[].objectId` with a big-number safe parser, or match on the string you sent.
- A newer version of this endpoint is available as [WeChat Channels Video Share URL](/apis/wechat-channels/v2/video-share-url).
- To get video details for the same `objectId`, call [WeChat Channels Video Detail](/apis/wechat-channels/v2/video-detail).

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/video-share-url.json`](../../../catalog/models/wechat-channels/video-share-url.json) · Store page: https://www.sandbase.ai/model/wechat-channels/video-share-url
