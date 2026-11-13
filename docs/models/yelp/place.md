# Yelp Place API: pricing, parameters and code examples

`yelp/place` · data API · Yelp · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get a Yelp business by place ID or alias with rating, review count, categories, hours, address, phone, website, amenities and menu.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yelp/place", "place_id": "arabica-brooklyn"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yelp/place', {'place_id': 'arabica-brooklyn'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yelp/place", {
  "place_id": "arabica-brooklyn"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yelp/place", sandbase.Params{
	"place_id": "arabica-brooklyn",
})
```

Same call via the path form: `POST /v1/api/yelp/place` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `place_id` | string | yes | Parameter defines the Yelp ID of a place. Each place has two unique IDs (e.g. `ED7A7vDdg8yLNKJTSVHHmg` and `arabica-brooklyn`) and you can use either of them as a value of the `place_id`. To extract the IDs of a place…  |
| `full_menu` | string |  | Set parameter to `true` to scrape business full menu when available. It defaults to `false`. When the parameter `full_menu` is set to `true`, but the business queried doesn't have a full menu page, then `place_results`…  |
| `menu_name` | string |  | Parameter defines the name of which Full Menu to scrape when more than one Full Menu is available. It can only be used in combination with `full_menu` parameter.  |
| `yelp_domain` | string |  | Parameter defines the Yelp domain to use. It defaults to `yelp.com`. Head to the Yelp domains for a full list of supported Yelp domains.  |
| `business_alert` | string |  | Set parameter to `true` to include business alert information when available. It defaults to `false`. Business alerts are temporarily unavailable. With this parameter, `place_results` are returned without…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get a Yelp business by place ID or alias with rating, review count, categories, hours, address, phone, website, amenities and menu.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yelp/place" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"place_id": "arabica-brooklyn"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `place_id` | string | Yes | Parameter defines the Yelp ID of a place. Each place has two unique IDs (e.g. `ED7A7vDdg8yLNKJTSVHHmg` and `arabica-brooklyn`) and you can use either of them as a value of the `place_id`. To extract the IDs of a place you can use our Yelp S |
| `yelp_domain` | string | No | Parameter defines the Yelp domain to use. It defaults to `yelp.com`. Head to the Yelp domains for a full list of supported Yelp domains. |
| `business_alert` | string | No | Set parameter to `true` to include business alert information when available. It defaults to `false`. Business alerts are temporarily unavailable. With this parameter, `place_results` are returned without `business_alert`. |
| `full_menu` | string | No | Set parameter to `true` to scrape business full menu when available. It defaults to `false`. When the parameter `full_menu` is set to `true`, but the business queried doesn't have a full menu page, then `place_results` will be returned inst |
| `menu_name` | string | No | Parameter defines the name of which Full Menu to scrape when more than one Full Menu is available. It can only be used in combination with `full_menu` parameter. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yelp/place.json`](../../../catalog/models/yelp/place.json) · Store page: https://www.sandbase.ai/model/yelp/place
