# WeChat Account Search API: pricing, parameters and code examples

`wechat-search/search-account` · data API · WeChat Search · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.055556 per call · **Modes:** sync

Search WeChat Official Accounts by keyword with page-number pagination and one result per page. Use it to find an account by name or related term before profile or article lookup.

## Pricing

- **$0.055556 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-search/search-account", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-search/search-account', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-search/search-account", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-search/search-account", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/wechat-search/search-account` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number starting from 1 for WeChat Official Account profile search. default `1` |
| `keyword` | string | yes | Search keyword for WeChat Official Account profiles.  |

## Details

Search WeChat Official Accounts by keyword with page-number pagination and one result per page. Use it to find an account by name or related term before profile or article lookup.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-search/search-account" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword for WeChat Official Account profiles. |
| `page` | integer | No | Page number starting from 1 for WeChat Official Account profile search. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/wechat-search/search-account.json`](../../../catalog/models/wechat-search/search-account.json) · Store page: https://www.sandbase.ai/model/wechat-search/search-account
