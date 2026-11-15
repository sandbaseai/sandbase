# Yellow Pages Business Details API: pricing, parameters and code examples

`yellowpages/business-details` · data API · Yellow Pages · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Fetch comprehensive details for a specific business by its YellowPages URL path. Returns name, contact info, hours of operation, categories, description, neighborhoods, amenities, social links, and payment methods. Optionally checks the business website for POS technology signals.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yellowpages/business-details", "url": "https://www.yellowpages.com/new-york-ny/mip/rr-plumbing-roto-rooter-574238364"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yellowpages/business-details', {'url': 'https://www.yellowpages.com/new-york-ny/mip/rr-plumbing-roto-rooter-574238364'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yellowpages/business-details", {
  "url": "https://www.yellowpages.com/new-york-ny/mip/rr-plumbing-roto-rooter-574238364"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yellowpages/business-details", sandbase.Params{
	"url": "https://www.yellowpages.com/new-york-ny/mip/rr-plumbing-roto-rooter-574238364",
})
```

Same call via the path form: `POST /v1/api/yellowpages/business-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full YellowPages business URL or path (e.g., 'https://www.yellowpages.com/new-york-ny/mip/rr-plumbing-roto-rooter-574238364' or '/new-york-ny/mip/rr-plumbing-roto-rooter-574238364')  |
| `check_pos` | boolean |  | When true, also checks the business website for POS technology stack signals. one of: `False`, `True`; default `false` |

## Details

Fetch comprehensive details for a specific business by its YellowPages URL path. Returns name, contact info, hours of operation, categories, description, neighborhoods, amenities, social links, and payment methods. Optionally checks the business website for POS technology signals.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "yellowpages/business-details", "url": "https://www.yellowpages.com/new-york-ny/mip/rr-plumbing-roto-rooter-574238364", "check_pos": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full YellowPages business URL or path (e.g., 'https://www.yellowpages.com/new-york-ny/mip/rr-plumbing-roto-rooter-574238364' or '/new-york-ny/mip/rr-plumbing-roto-rooter-574238364') |
| `check_pos` | boolean | No | When true, also checks the business website for POS technology stack signals. One of: `False`, `True`. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yellowpages/business-details.json`](../../../catalog/models/yellowpages/business-details.json) · Store page: https://www.sandbase.ai/model/yellowpages/business-details
