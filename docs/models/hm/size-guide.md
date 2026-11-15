# H&M Size Guide API: pricing, parameters and code examples

`hm/size-guide` · data API · H&M · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Return the H&M size guide shown on a product page: measurement tables (chest, waist, hip, inside leg, etc.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hm/size-guide", "article_code": "1353272003"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hm/size-guide', {'article_code': '1353272003'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hm/size-guide", {
  "article_code": "1353272003"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hm/size-guide", sandbase.Params{
	"article_code": "1353272003",
})
```

Same call via the path form: `POST /v1/api/hm/size-guide` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `locale` | string |  | Storefront locale in <language>_<country> form controlling the language and size systems of the guide. Verified values: 'en_us' (US sizes, inch and cm) and 'ko_kr' (Korean text and KR sizes). Other H&M storefront… default `"en_us"` |
| `article_code` | string | yes | 10-digit H&M article code (e.g. '1347416001'); one code per call. Use hits[*].id from search_products or article_code from the Korean listing endpoints.  |

## Details

Return the H&M size guide shown on a product page: measurement tables (chest, waist, hip, inside leg, etc.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "hm/size-guide", "article_code": "1353272003"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `article_code` | string | Yes | 10-digit H&M article code (e.g. '1347416001'); one code per call. Use hits[*].id from search_products or article_code from the Korean listing endpoints. |
| `locale` | string | No | Storefront locale in <language>_<country> form controlling the language and size systems of the guide. Verified values: 'en_us' (US sizes, inch and cm) and 'ko_kr' (Korean text and KR sizes). Other H&M storefront locales |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hm/size-guide.json`](../../../catalog/models/hm/size-guide.json) · Store page: https://www.sandbase.ai/model/hm/size-guide
