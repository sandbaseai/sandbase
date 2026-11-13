# Foreplay Brands by Domain API: pricing, parameters and code examples

`foreplay/brands-by-domain` · data API · Foreplay · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0175 per call · **Modes:** sync

Find the advertiser brands Foreplay tracks for a website domain, with brand ID, name, logo and ad counts, to use in brand ad lookups.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0175**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "foreplay/brands-by-domain", "domain": "nike.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('foreplay/brands-by-domain', {'domain': 'nike.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("foreplay/brands-by-domain", {
  "domain": "nike.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "foreplay/brands-by-domain", sandbase.Params{
	"domain": "nike.com",
})
```

Same call via the path form: `POST /v1/api/foreplay/brands-by-domain` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of results (1-20). Each returned item is billed at about $0.0175, so this caps the cost of one call. default `10`; range –20 |
| `order` | string |  | Order of results: 'most_ranked' (default) or 'least_ranked'. Sorts brands by relevance ranking. default `"most_ranked"` |
| `domain` | string | yes | Domain name to search for. This can be a full URL (e.g., 'https://example.com') or just the domain (e.g., 'example.com'). The system will automatically format and clean the domain. This endpoint looks up candidate…  |

## Details

Find the advertiser brands Foreplay tracks for a website domain, with brand ID, name, logo and ad counts, to use in brand ad lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/foreplay/brands-by-domain" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "nike.com", "limit": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | Domain name to search for. This can be a full URL (e.g., 'https://example.com') or just the domain (e.g., 'example.com'). The system will automatically format and clean the domain. This endpoint looks up candidate brands |
| `limit` | integer | No | Pagination limit (max 10). Controls the number of brands returned per request. |
| `order` | string | No | Order of results: 'most_ranked' (default) or 'least_ranked'. Sorts brands by relevance ranking. |

### Pricing

Billed at the actual upstream cost of each call (about $0.0175 for the request above). Failed calls are not charged.

---
Machine-readable: [`catalog/models/foreplay/brands-by-domain.json`](../../../catalog/models/foreplay/brands-by-domain.json) · Store page: https://www.sandbase.ai/model/foreplay/brands-by-domain
