# WeChat MP Account Historical Articles

`wechat-mp/account-history-articles` · api · WeChat MP

Get historical posts for a WeChat Official Account by username, with cursor pagination and article, video, audio, or image content tabs. Use it to browse an account's publishing history.

## Pricing

- **$0.041667 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/account-history-articles", "username": "worldofai"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/account-history-articles', {'username': 'worldofai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/account-history-articles", {
  "username": "worldofai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/account-history-articles", sandbase.Params{
	"username": "worldofai",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/account-history-articles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | string |  | Base64 pagination cursor. Leave empty for the first page; pass next_offset from the previous response for the next page. Send it in the URL-encoded form body.  |
| `username` | string | yes | WeChat Official Account username with the gh_ prefix.  |
| `itemShowType` | string |  | Content tab. Defaults to ARTICLE. one of: `ARTICLE`, `VIDEO`, `AUDIO`, `IMAGE`; default `"ARTICLE"` |

## Details

Get historical posts for a WeChat Official Account by username, with cursor pagination and article, video, audio, or image content tabs. Use it to browse an account's publishing history.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/account-history-articles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "worldofai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | WeChat Official Account username with the gh_ prefix. |
| `offset` | string | No | Base64 pagination cursor. Leave empty for the first page; pass next_offset from the previous response for the next page. Send it in the URL-encoded form body. |
| `itemShowType` | string | No | Content tab. Defaults to ARTICLE. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/wechat-mp/account-history-articles.json`](../../../catalog/models/wechat-mp/account-history-articles.json) · Store page: https://www.sandbase.ai/model/wechat-mp/account-history-articles
