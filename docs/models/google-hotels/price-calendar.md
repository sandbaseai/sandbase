# Google Hotels Price Calendar API: pricing, parameters and code examples

`google-hotels/price-calendar` · data API · Google Hotels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get the nightly price of a hotel on Google Hotels for each date in a range, by property token and guest count.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-hotels/price-calendar", "property_token": "CgsIlOPW65yHnZPwARAB", "start_date": "2026-12-10", "end_date": "2026-12-20"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-hotels/price-calendar', {'property_token': 'CgsIlOPW65yHnZPwARAB', 'start_date': '2026-12-10', 'end_date': '2026-12-20'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-hotels/price-calendar", {
  "property_token": "CgsIlOPW65yHnZPwARAB",
  "start_date": "2026-12-10",
  "end_date": "2026-12-20"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-hotels/price-calendar", sandbase.Params{
	"property_token": "CgsIlOPW65yHnZPwARAB",
	"start_date": "2026-12-10",
	"end_date": "2026-12-20",
})
```

Same call via the path form: `POST /v1/api/google-hotels/price-calendar` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Parameter defines the country to use for the Google Hotels search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries page for a…  |
| `hl` | string |  | Parameter defines the language to use for the Google Hotels search. It's a two-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French). Head to the Google languages page for a full list of…  |
| `adults` | string |  | Parameter defines the number of adults. Default to `2`.  |
| `children` | string |  | Parameter defines the number of children. Default to `0`.  |
| `currency` | string |  | Parameter defines the currency of the returned prices. Default to `USD`. Head to the Google Travel Currencies page for a full list of supported currency codes.  |
| `end_date` | string | yes | Parameter defines the last date of the price calendar. It can't be more than 3 years from now. The format is **YYYY-MM-DD**. e.g. `2027-01-11`  |
| `start_date` | string | yes | Parameter defines the first date of the price calendar. Each date has the best price of a 1-night stay starting that day. The format is **YYYY-MM-DD**. e.g. `2026-11-13`  |
| `children_ages` | string |  | Parameter defines the ages of children. The age range is from `1` to `17`, with children who haven't reached 1 year old being considered as `1`. Example for single child only: `5` Example for multiple children…  |
| `property_token` | string | yes | Parameter defines the specific property. You can find `property_token` from Google Hotels API.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get the nightly price of a hotel on Google Hotels for each date in a range, by property token and guest count.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-hotels/price-calendar" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"property_token": "CgsIlOPW65yHnZPwARAB", "start_date": "2026-12-10", "end_date": "2026-12-20"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `property_token` | string | Yes | Parameter defines the specific property. You can find `property_token` from Google Hotels API. |
| `start_date` | string | Yes | Parameter defines the first date of the price calendar. Each date has the best price of a 1-night stay starting that day. The format is **YYYY-MM-DD**. e.g. `2026-11-13` |
| `end_date` | string | Yes | Parameter defines the last date of the price calendar. It can't be more than 3 years from now. The format is **YYYY-MM-DD**. e.g. `2027-01-11` |
| `adults` | string | No | Parameter defines the number of adults. Default to `2`. |
| `children` | string | No | Parameter defines the number of children. Default to `0`. |
| `children_ages` | string | No | Parameter defines the ages of children. The age range is from `1` to `17`, with children who haven't reached 1 year old being considered as `1`. Example for single child only: `5` Example for multiple children (separated by comma `,`): `5,8 |
| `gl` | string | No | Parameter defines the country to use for the Google Hotels search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries page for a full list of supporte |
| `hl` | string | No | Parameter defines the language to use for the Google Hotels search. It's a two-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French). Head to the Google languages page for a full list of supported Google langu |
| `currency` | string | No | Parameter defines the currency of the returned prices. Default to `USD`. Head to the Google Travel Currencies page for a full list of supported currency codes. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-hotels/price-calendar.json`](../../../catalog/models/google-hotels/price-calendar.json) · Store page: https://www.sandbase.ai/model/google-hotels/price-calendar
