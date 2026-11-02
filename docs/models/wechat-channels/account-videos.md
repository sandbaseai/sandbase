# WeChat Channels Account Videos API: pricing, parameters and code examples

`wechat-channels/account-videos` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.069444 per call · **Modes:** sync

Get a paginated WeChat Channels account feed by v2Name with continuation-buffer support. Use it to browse videos and other feed entries published by a known creator account.

## Pricing

- **$0.069444 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/account-videos", "v2Name": "v2_060000231003b20faec8c7e48d1dc6d5c802e83db0770775bb566d2b495e6aae711d6d56bd04@finder"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/account-videos', {'v2Name': 'v2_060000231003b20faec8c7e48d1dc6d5c802e83db0770775bb566d2b495e6aae711d6d56bd04@finder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/account-videos", {
  "v2Name": "v2_060000231003b20faec8c7e48d1dc6d5c802e83db0770775bb566d2b495e6aae711d6d56bd04@finder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/account-videos", sandbase.Params{
	"v2Name": "v2_060000231003b20faec8c7e48d1dc6d5c802e83db0770775bb566d2b495e6aae711d6d56bd04@finder",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/account-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `v2Name` | string | yes | WeChat Channels account unique id, usually ending with @finder.  |
| `last_buffer` | string |  | Pagination buffer returned by the previous WeChat Channels account videos response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.  |

## Details

Get a paginated WeChat Channels account feed by v2Name with continuation-buffer support. Use it to browse videos and other feed entries published by a known creator account.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/account-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"v2Name": "v2_060000231003b20faec8c7e48d1dc6d5c802e83db0770775bb566d2b495e6aae711d6d56bd04@finder"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `v2Name` | string | Yes | WeChat Channels account unique id, usually ending with @finder. |
| `last_buffer` | string | No | Pagination buffer returned by the previous WeChat Channels account videos response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/account-videos.json`](../../../catalog/models/wechat-channels/account-videos.json) · Store page: https://www.sandbase.ai/model/wechat-channels/account-videos
