# Google Hotels Search API: pricing, parameters and code examples

`google-hotels/search` · data API · Google Hotels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Google Hotels results for a destination and stay dates: hotels, nightly rates, ratings, amenities and offers.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-hotels/search", "q": "Bali Resorts", "check_in_date": "2026-12-15", "check_out_date": "2026-12-16", "adults": 2}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-hotels/search', {'q': 'Bali Resorts', 'check_in_date': '2026-12-15', 'check_out_date': '2026-12-16', 'adults': 2})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-hotels/search", {
  "q": "Bali Resorts",
  "check_in_date": "2026-12-15",
  "check_out_date": "2026-12-16",
  "adults": 2
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-hotels/search", sandbase.Params{
	"q": "Bali Resorts",
	"check_in_date": "2026-12-15",
	"check_out_date": "2026-12-16",
	"adults": 2,
})
```

Same call via the path form: `POST /v1/api/google-hotels/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | q  |
| `adults` | integer | yes | adults  |
| `check_in_date` | string | yes | YYYY-MM-DD  |
| `check_out_date` | string | yes | YYYY-MM-DD  |

## Details

Google Hotels results for a destination and stay dates: hotels, nightly rates, ratings, amenities and offers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-hotels/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "Bali Resorts", "check_in_date": "2026-12-15", "check_out_date": "2026-12-16", "adults": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `adults` | integer | Yes | adults |
| `check_in_date` | string | Yes | YYYY-MM-DD |
| `check_out_date` | string | Yes | YYYY-MM-DD |
| `q` | string | Yes | q |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-hotels/search.json`](../../../catalog/models/google-hotels/search.json) · Store page: https://www.sandbase.ai/model/google-hotels/search
