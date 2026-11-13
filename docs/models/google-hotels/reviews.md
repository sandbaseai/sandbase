# Google Hotels Reviews API: pricing, parameters and code examples

`google-hotels/reviews` · data API · Google Hotels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get guest reviews for a hotel on Google Hotels by property token, with rating, text, date, source and category filters.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-hotels/reviews", "property_token": "CgsIlOPW65yHnZPwARAB"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-hotels/reviews', {'property_token': 'CgsIlOPW65yHnZPwARAB'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-hotels/reviews", {
  "property_token": "CgsIlOPW65yHnZPwARAB"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-hotels/reviews", sandbase.Params{
	"property_token": "CgsIlOPW65yHnZPwARAB",
})
```

Same call via the path form: `POST /v1/api/google-hotels/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `hl` | string |  | Parameter defines the language to use for the Google Hotels search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or…  |
| `sort_by` | string |  | Parameter defines the sorting order of the reviews. Available options: `1` - Most helpful (Default) `2` - Most recent `3` - Highest score `4` - Lowest score  |
| `source_number` | string |  | Parameter filters the reviews based on their originating source. Standard options (always available): `0` - All reviews (Default) `-1` - Google For property-specific source numbers, refer to the `other_reviews` field…  |
| `category_token` | string |  | Parameter is used to get reviews filtered by a specific category. You can find `category_token` from Google Hotels API under `reviews_breakdown`.  |
| `property_token` | string | yes | Parameter defines the specific property. You can find `property_token` from Google Hotels Properties API.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `next_page_token` | string |  | Parameter defines the next page token. It is used for retrieving the next page results.  |

## Details

Get guest reviews for a hotel on Google Hotels by property token, with rating, text, date, source and category filters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-hotels/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"property_token": "CgsIlOPW65yHnZPwARAB"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `property_token` | string | Yes | Parameter defines the specific property. You can find `property_token` from Google Hotels Properties API. |
| `hl` | string | No | Parameter defines the language to use for the Google Hotels search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region code (e. |
| `category_token` | string | No | Parameter is used to get reviews filtered by a specific category. You can find `category_token` from Google Hotels API under `reviews_breakdown`. |
| `sort_by` | string | No | Parameter defines the sorting order of the reviews. Available options: `1` - Most helpful (Default) `2` - Most recent `3` - Highest score `4` - Lowest score |
| `source_number` | string | No | Parameter filters the reviews based on their originating source. Standard options (always available): `0` - All reviews (Default) `-1` - Google For property-specific source numbers, refer to the `other_reviews` field in Google Hotels Proper |
| `next_page_token` | string | No | Parameter defines the next page token. It is used for retrieving the next page results. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-hotels/reviews.json`](../../../catalog/models/google-hotels/reviews.json) · Store page: https://www.sandbase.ai/model/google-hotels/reviews
