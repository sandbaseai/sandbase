# Similarweb Website Top Geographies API: pricing, parameters and code examples

`similarweb/website-top-geographies` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.225 per call · **Modes:** sync

Get the countries a website's traffic comes from, with share and visits for each country.

## Pricing

- Depends on parameters ().

Formula: `0.225 * Math.max(1.0, Math.min(10.0, (output.data?.data?.countries != nil ? len(output.data.data.countries) : 10) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/website-top-geographies", "domain": "cnn.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/website-top-geographies', {'domain': 'cnn.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/website-top-geographies", {
  "domain": "cnn.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/website-top-geographies", sandbase.Params{
	"domain": "cnn.com",
})
```

Same call via the path form: `POST /v1/api/similarweb/website-top-geographies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `month` | string |  | Complete month in YYYY-MM.  |
| `domain` | string | yes | Bare website hostname without scheme, path, port, or credentials.  |

## Details

Returns the countries that send traffic to a website, with each country's share of traffic and visit count. It needs a bare `domain` such as `cnn.com` and can take a `month` in `YYYY-MM` format.

### Use cases

- Check which countries make up most of a news site's audience.
- Compare the US share of visits for two competing websites.
- Find smaller markets, such as India, where a site already gets traffic.
- Feed country-level visit counts into a market sizing report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/website-top-geographies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "cnn.com", "month": "2026-09"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | Bare website hostname without scheme, path, port, or credentials. |
| `month` | string | No | Complete month in YYYY-MM. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "countries": [
      {
        "country_code": "us",
        "country_name": "United States",
        "rank": null,
        "share": 0.8111012961668697,
        "visits": 153021200.49451894
      }
    ]
  },
  "meta": {
    "country": "ww",
    "end_date": "2026-09",
    "granularity": "monthly",
    "request_id": "imc_c30995d6af7ed527de005aaf6c0822d71f6c0fc719e2f31a4cb27ddb09d08ee5",
    "retrieved_at": "2026-11-03T07:43:23.793583227Z",
    "source": "similarweb",
    "start_date": "2026-09"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.countries[]` | List of countries that send traffic to the domain. Each item is one country. |
| `data.countries[].country_code` | Lowercase two-letter country code, for example `us`. |
| `data.countries[].country_name` | English name of the country. |
| `data.countries[].share` | Fraction of the site's traffic from this country. A value of `0.81` means about 81 percent. |
| `data.countries[].visits` | Number of visits from this country. The value is a decimal, so round it for display. |
| `data.countries[].rank` | Country rank value. It is `null` in this response. |
| `meta.start_date / meta.end_date` | First and last month covered by the data, in `YYYY-MM` format. |
| `meta.granularity` | Time step of the data. The value here is `monthly`. |
| `meta.country` | Country scope of the request. The value `ww` is used here for all countries combined. |

### Notes

- `month` is optional. Use a complete month in `YYYY-MM` format, such as `2026-09`.
- Pass the hostname only. Leave out the scheme, path, port, and credentials.
- The response has no pagination parameters. The pricing section says up to 10 countries come back.
- For more on a site's traffic over time, call [Similarweb Website Traffic Trend](/apis/similarweb/website-traffic-trend).

### Pricing

Billed at the actual cost of each call, about $0.225 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/website-top-geographies.json`](../../../catalog/models/similarweb/website-top-geographies.json) · Store page: https://www.sandbase.ai/model/similarweb/website-top-geographies
