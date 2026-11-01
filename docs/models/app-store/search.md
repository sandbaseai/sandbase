# App Store Search

`app-store/search` · api · App Store

Search iPhone, iPad, and Mac apps or developers on the Apple App Store by storefront.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "app-store/search", "term": "software"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('app-store/search', {'term': 'software'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("app-store/search", {
  "term": "software"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "app-store/search", sandbase.Params{
	"term": "software",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/app-store/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `num` | integer |  | Maximum results after filtering, 1-200. Default 10. range 1–200 |
| `lang` | string |  | Language-region code, such as 'en-us' or 'fr-fr'. Default 'en-us'.  |
| `term` | string | yes | Search term, 1-2,048 UTF-8 bytes (at most 4,096 bytes URL-encoded).  |
| `device` | string |  | 'mobile' for iPhone apps, 'tablet' for iPad apps, 'desktop' for Mac apps. Default 'mobile'. one of: `mobile`, `tablet`, `desktop` |
| `country` | string |  | Two-letter Apple storefront country, such as 'us' or 'gb' ('uk' is accepted). Default 'us'.  |
| `property` | string |  | 'developer' matches developer names instead of app names, ignoring case. one of: `developer` |
| `category_id` | integer |  | Filter results by a native genre identifier. range 1–2147483647 |
| `disallow_explicit` | boolean |  | Exclude explicit results.  |

## Details

Search iPhone, iPad, and Mac apps or developers on the Apple App Store by storefront.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/app-store/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"term": "software"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `term` | string | Yes | Search term, 1-2,048 UTF-8 bytes (at most 4,096 bytes URL-encoded). |
| `category_id` | integer | No | Filter results by a native genre identifier. |
| `country` | string | No | Two-letter Apple storefront country, such as 'us' or 'gb' ('uk' is accepted). Default 'us'. |
| `device` | string | No | 'mobile' for iPhone apps, 'tablet' for iPad apps, 'desktop' for Mac apps. Default 'mobile'. One of: `mobile`, `tablet`, `desktop`. |
| `disallow_explicit` | boolean | No | Exclude explicit results. |
| `lang` | string | No | Language-region code, such as 'en-us' or 'fr-fr'. Default 'en-us'. |
| `num` | integer | No | Maximum results after filtering, 1-200. Default 10. |
| `property` | string | No | 'developer' matches developer names instead of app names, ignoring case. One of: `developer`. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/app-store/search.json`](../../../catalog/models/app-store/search.json) · Store page: https://www.sandbase.ai/model/app-store/search
