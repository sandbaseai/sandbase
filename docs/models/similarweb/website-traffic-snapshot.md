# Similarweb Website Traffic Snapshot

`similarweb/website-traffic-snapshot` · api · Similarweb

Get a one-month snapshot of a website's traffic: visits, visit duration, pages per visit and bounce rate.

## Pricing

- **$0.3 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/website-traffic-snapshot", "domain": "cnn.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/website-traffic-snapshot', {'domain': 'cnn.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/website-traffic-snapshot", {
  "domain": "cnn.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/website-traffic-snapshot", sandbase.Params{
	"domain": "cnn.com",
})
```

Same call via the path form: `POST /v1/api/similarweb/website-traffic-snapshot` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `month` | string |  | Complete month in YYYY-MM.  |
| `domain` | string | yes | Bare website hostname without scheme, path, port, or credentials.  |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |

## Details

Get a one-month snapshot of a website's traffic: visits, visit duration, pages per visit and bounce rate.

The response is the official Similarweb API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/website-traffic-snapshot" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "cnn.com"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `domain` | string | Yes | Bare website hostname without scheme, path, port, or credentials. |
| `month` | string | No | Complete month in YYYY-MM. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/website-traffic-snapshot.json`](../../../catalog/models/similarweb/website-traffic-snapshot.json) · Store page: https://www.sandbase.ai/model/similarweb/website-traffic-snapshot
