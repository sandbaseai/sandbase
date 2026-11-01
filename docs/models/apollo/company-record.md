# Apollo Get Complete Organization Info

`apollo/company-record` · api · Apollo

The complete Apollo record for one company, by Apollo organization id (not by domain).

## Pricing

- **$0.01975 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apollo/company-record", "id": "5d0a0fbff6512580bf33a120"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apollo/company-record', {'id': '5d0a0fbff6512580bf33a120'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apollo/company-record", {
  "id": "5d0a0fbff6512580bf33a120"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apollo/company-record", sandbase.Params{
	"id": "5d0a0fbff6512580bf33a120",
})
```

Same call via the path form: `POST /v1/api/apollo/company-record` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The Apollo ID for the organization that you want to research. To find organization IDs, call the Organization Search endpoint and identify the organizaton_id value for the organization. Example: 5e66b6381e05b4008c8331b8  |

## Details

The complete Apollo record for one company, by Apollo organization id (not by domain).

The response is the official Apollo API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/company-record" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "5d0a0fbff6512580bf33a120"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | The Apollo ID for the organization that you want to research. To find organization IDs, call the Organization Search endpoint and identify the organizaton_id va |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apollo/company-record.json`](../../../catalog/models/apollo/company-record.json) · Store page: https://www.sandbase.ai/model/apollo/company-record
