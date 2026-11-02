# WeChat MP Account Basic Info API: pricing, parameters and code examples

`wechat-mp/account-basic-info` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.142857 per call · **Modes:** sync

Get basic profile information for a WeChat Official Account by account name. Use it to identify or enrich a known account before article, ownership, or publishing research.

## Pricing

- **$0.142857 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/account-basic-info", "name": "人民日报"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/account-basic-info', {'name': '人民日报'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/account-basic-info", {
  "name": "人民日报"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/account-basic-info", sandbase.Params{
	"name": "人民日报",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/account-basic-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `name` | string | yes | WeChat Official Account name used to fetch basic profile information.  |

## Details

Get basic profile information for a WeChat Official Account by account name. Use it to identify or enrich a known account before article, ownership, or publishing research.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/account-basic-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "人民日报"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | WeChat Official Account name used to fetch basic profile information. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/wechat-mp/account-basic-info.json`](../../../catalog/models/wechat-mp/account-basic-info.json) · Store page: https://www.sandbase.ai/model/wechat-mp/account-basic-info
