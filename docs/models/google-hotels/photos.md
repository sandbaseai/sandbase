# Google Hotels Photos API: pricing, parameters and code examples

`google-hotels/photos` · data API · Google Hotels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get photos of a hotel on Google Hotels by property token, with image URLs, categories and paging.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-hotels/photos", "property_token": "CgsIlOPW65yHnZPwARAB"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-hotels/photos', {'property_token': 'CgsIlOPW65yHnZPwARAB'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-hotels/photos", {
  "property_token": "CgsIlOPW65yHnZPwARAB"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-hotels/photos", sandbase.Params{
	"property_token": "CgsIlOPW65yHnZPwARAB",
})
```

Same call via the path form: `POST /v1/api/google-hotels/photos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `property_token` | string | yes | Parameter defines unique identifier used to identify a Google Property. You can find `property_token` from Google Hotels Properties API.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `next_page_token` | string |  | Parameter defines the next page token needed to retrieve the next batch of photos of a particular section.  |

## Details

Get photos of a hotel on Google Hotels by property token, with image URLs, categories and paging.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-hotels/photos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"property_token": "CgsIlOPW65yHnZPwARAB"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `property_token` | string | Yes | Parameter defines unique identifier used to identify a Google Property. You can find `property_token` from Google Hotels Properties API. |
| `next_page_token` | string | No | Parameter defines the next page token needed to retrieve the next batch of photos of a particular section. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-hotels/photos.json`](../../../catalog/models/google-hotels/photos.json) · Store page: https://www.sandbase.ai/model/google-hotels/photos
