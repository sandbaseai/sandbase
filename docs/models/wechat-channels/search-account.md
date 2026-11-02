# WeChat Channels Account Search API: pricing, parameters and code examples

`wechat-channels/search-account` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.071429 per call · **Modes:** sync

Looks up a specific WeChat Channels account identity by keyword. Use it to resolve a creator name or account term to the identifier required by account-video queries.

## Pricing

- **$0.071429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/search-account", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/search-account', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/search-account", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/search-account", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/search-account` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword used to resolve a WeChat Channels account id.  |

## Details

Looks up a specific WeChat Channels account identity by keyword. Use it to resolve a creator name or account term to the identifier required by account-video queries.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/search-account" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword used to resolve a WeChat Channels account id. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/search-account.json`](../../../catalog/models/wechat-channels/search-account.json) · Store page: https://www.sandbase.ai/model/wechat-channels/search-account
