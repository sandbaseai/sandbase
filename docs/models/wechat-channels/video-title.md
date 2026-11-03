# WeChat Channels Video Title API: pricing, parameters and code examples

`wechat-channels/video-title` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get lightweight title information for a WeChat Channels video by object ID and optional nonce ID. Use it to identify known video content without requesting downloadable media.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/video-title", "objectId": "14941130915890399732"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/video-title', {'objectId': '14941130915890399732'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/video-title", {
  "objectId": "14941130915890399732"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/video-title", sandbase.Params{
	"objectId": "14941130915890399732",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/video-title` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `objectId` | string | yes | WeChat Channels video object id.  |
| `objectNonceId` | string |  | Optional WeChat Channels object nonce id. Supplying it can improve lookup accuracy.  |

## Details

Returns the title, the posting account's name and username, and a media type code for one WeChat Channels video. It needs the video `objectId`, and you can add `objectNonceId` as an optional second input.

### Use cases

- Check which video an `objectId` from a saved list or log points to.
- Show the title and account name next to a stored video ID in a dashboard.
- Pull hashtags such as `#早安中国` from a video title for topic tagging.
- Match a video to its posting account by `username` before fetching more account data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/video-title" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"objectId": "14941130915890399732"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `objectId` | string | Yes | WeChat Channels video object id. |
| `objectNonceId` | string | No | Optional WeChat Channels object nonce id. Supplying it can improve lookup accuracy. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "media_type": 4,
  "nickname": "人民日报",
  "title": "6月11日，星期四。花开如瀑，金波荡漾。微风轻拂，芬芳满怀。愿您岁月安然，惬意从容。#早安中国",
  "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title` | The video title text as posted. It can include hashtags, like `#早安中国` in the sample. |
| `nickname` | Display name of the account that posted the video. The sample shows `人民日报`. |
| `username` | Internal username of the posting account. It ends in `@finder`. |
| `media_type` | Numeric code for the media type. The sample returns `4`. The response does not say what each code means. |

### Notes

- Only `objectId` is required. Add `objectNonceId` if you have it, since it can improve lookup accuracy.
- This API returns title data only. For download links or engagement counts, call [WeChat Channels Video Download URL](/apis/wechat-channels/video-download-url) or [WeChat Channels Video Metrics](/apis/wechat-channels/video-metrics).
- For fuller video data, use [WeChat Channels Video Detail](/apis/wechat-channels/v2/video-detail).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/video-title.json`](../../../catalog/models/wechat-channels/video-title.json) · Store page: https://www.sandbase.ai/model/wechat-channels/video-title
