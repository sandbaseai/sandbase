# Nextdoor Business API: pricing, parameters and code examples

`nextdoor/business` · data API · Nextdoor · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00242 per call · **Modes:** sync

Fetch one Nextdoor business page by its slug, with phone, email, website, and street address.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00242**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nextdoor/business", "pageSlug": "radiant-plumbing-air-conditioning-austin-tx"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nextdoor/business', {'pageSlug': 'radiant-plumbing-air-conditioning-austin-tx'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nextdoor/business", {
  "pageSlug": "radiant-plumbing-air-conditioning-austin-tx"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nextdoor/business", sandbase.Params{
	"pageSlug": "radiant-plumbing-air-conditioning-austin-tx",
})
```

Same call via the path form: `POST /v1/api/nextdoor/business` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of records to return. A business page resolves to one record, so this is always 1. range 1–1 |
| `market` | string |  | Nextdoor market the page belongs to: "us" (nextdoor.com), "gb" (nextdoor.co.uk), or "ca" (ca.nextdoor.com). Defaults to "us". one of: `us`, `gb`, `ca` |
| `pageSlug` | string | yes | Slug of the Nextdoor business page, the last path segment of its /pages/ URL, e.g. "radiant-plumbing-air-conditioning-austin-tx".  |

## Details

Fetch one Nextdoor business page by its slug, with phone, email, website, and street address.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "nextdoor/business", "pageSlug": "radiant-plumbing-air-conditioning-austin-tx"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `pageSlug` | string | Yes | Slug of the Nextdoor business page, the last path segment of its /pages/ URL, e.g. "radiant-plumbing-air-conditioning-austin-tx". |
| `limit` | integer | No | Maximum number of records to return. A business page resolves to one record, so this is always 1. |
| `market` | string | No | Nextdoor market the page belongs to: "us" (nextdoor.com), "gb" (nextdoor.co.uk), or "ca" (ca.nextdoor.com). Defaults to "us". One of: `us`, `gb`, `ca`. |

### Pricing

Billed at the actual cost of each call: about $0.00242 per result returned, up to $0.00792 per request (about $0.00242 for the request above). A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/nextdoor/business.json`](../../../catalog/models/nextdoor/business.json) · Store page: https://www.sandbase.ai/model/nextdoor/business
