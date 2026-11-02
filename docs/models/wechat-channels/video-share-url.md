# WeChat Channels Video Share URL API: pricing, parameters and code examples

`wechat-channels/video-share-url` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.027778 per call · **Modes:** sync

Generates a share link for a WeChat Channels video identified by objectId. Use it to share a known Channels video or obtain its link for a subsequent lookup.

## Pricing

- **$0.027778 per call** (USD)

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

Generates a share link for a WeChat Channels video identified by objectId. Use it to share a known Channels video or obtain its link for a subsequent lookup.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/video-share-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"objectId": "14941130915890399732"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `objectId` | string | Yes | WeChat Channels video objectId as a numeric string of up to 32 digits. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/video-share-url.json`](../../../catalog/models/wechat-channels/video-share-url.json) · Store page: https://www.sandbase.ai/model/wechat-channels/video-share-url
