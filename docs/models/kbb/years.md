# Kelley Blue Book Years API: pricing, parameters and code examples

`kbb/years` · data API · Kelley Blue Book · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retrieve all available vehicle model years from Kelley Blue Book in one round trip. Returns an array of integer years in descending order, from the newest model year the site currently lists (one year beyond the next.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kbb/years"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kbb/years', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kbb/years", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kbb/years", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/kbb/years` with the body above minus `model`.

## Details

Returns the list of vehicle model years that Kelley Blue Book currently lists, newest first. The call needs no input.

### Use cases

- Fill a model year dropdown in a car search form.
- Check the newest model year Kelley Blue Book lists before you run other vehicle lookups.
- Validate a user-supplied model year against the years the site supports.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kbb/years" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "years": [
      2028
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `status` | Result of the call. The value is `success` when the request worked. |
| `data.years[]` | Model years as integers, sorted from newest to oldest. The first item is the newest model year listed. |

### Notes

- Send an empty JSON object `{}` as the request body. The API has no parameters.
- The API runs asynchronously. Poll the run endpoint until `status` is `completed`, then read `outputs[0].data`.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/kbb/years.json`](../../../catalog/models/kbb/years.json) · Store page: https://www.sandbase.ai/model/kbb/years
