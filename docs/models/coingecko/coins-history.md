# CoinGecko Coin Historical Data by ID API: pricing, parameters and code examples

`coingecko/coins-history` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get the historical data (price, market cap, 24hrs volume, ...) at a given date for a coin based on a particular coin ID

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-history", "id": "bitcoin", "date": "30-12-2024"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-history', {'id': 'bitcoin', 'date': '30-12-2024'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-history", {
  "id": "bitcoin",
  "date": "30-12-2024"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-history", sandbase.Params{
	"id": "bitcoin",
	"date": "30-12-2024",
})
```

Same call via the path form: `POST /v1/api/coingecko/coins-history` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list). default `"bitcoin"` |
| `date` | string | yes | The date of data snapshot. Format: `YYYY-MM-DD` default `"2025-12-30"` |
| `localization` | boolean |  | Include all the localized languages in response. Default: true  |

## Details

Returns a snapshot of one coin on a given date. The snapshot holds the coin's value, market cap and trading volume in many fiat and crypto currencies. It needs a CoinGecko coin `id` and a `date`.

### Use cases

- Look up the `eur` value of `bitcoin` on a past date for tax or accounting records.
- Compare the market cap of a coin across fiat and crypto currencies on one day.
- Build a daily history table by calling the API once per date.
- Show localized coin names in a multi-language app using the `localization` object.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-history" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "bitcoin", "date": "30-12-2024"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date` | string | Yes | The date of data snapshot. Format: `YYYY-MM-DD` |
| `id` | string | Yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list). |
| `localization` | boolean | No | Include all the localized languages in response. Default: true |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "id": "bitcoin",
  "image": {
    "small": "https://coin-images.coingecko.com/coins/images/1/small/bitcoin.png?1696501400",
    "thumb": "https://coin-images.coingecko.com/coins/images/1/thumb/bitcoin.png?1696501400"
  },
  "localization": {
    "ar": "Bitcoin (بيتكوين)",
    "bg": "биткойн",
    "cs": "Bitcoin",
    "da": "Bitcoin",
    "de": "Bitcoin",
    "el": "Bitcoin",
    "en": "Bitcoin",
    "es": "Bitcoin",
    "fi": "Bitcoin",
    "fr": "Bitcoin",
    "he": "Bitcoin",
    "hi": "Bitcoin"
  },
  "market_data": {
    "current_price": {
      "aed": 343305.7658195852,
      "ars": 96363245.77150266,
      "aud": 150320.68900219753,
      "bch": 210.85675489002864,
      "bdt": 11162633.882111557,
      "bhd": 35238.609915637775,
      "bits": 1000000,
      "bmd": 93467.14705911094,
      "bnb": 133.14575872653612,
      "brl": 577477.4213900111,
      "btc": 1,
      "cad": 134136.57208747132
    },
    "market_cap": {
      "aed": 6804244126051.13,
      "ars": 1909898155781462.5,
      "aud": 2979322711709.64,
      "bch": 4179134109.4243608,
      "bdt": 221240927434734.72,
      "bhd": 698421431857.6024,
      "bits": 19803021000000,
      "bmd": 1852498121717.9175,
      "bnb": 2638919403.4094796,
      "brl": 11445474395221.982,
      "btc": 19803021,
      "cad": 2658557104439.818
    },
    "total_volume": {
      "aed": 108819726243.11224,
      "ars": 30544846806515.348,
      "aud": 47648067275.66459,
      "bch": 66836553.964847304,
      "bdt": 3538288267030.821,
      "bhd": 11169797498.31152,
      "bits": 316902868429.7276,
      "bmd": 29626852702.037895,
      "bnb": 42204024.68471026,
      "brl": 183046546734.27097,
      "btc": 316902.8684297276,
      "cad": 42518088849.74863
    }
  },
  "name": "Bitcoin",
  "public_interest_stats": {
    "alexa_rank": null,
    "bing_matches": null
  },
  "symbol": "btc"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id / symbol / name` | The coin ID, ticker symbol and display name. In the example, these are `bitcoin`, `btc` and `Bitcoin`. |
| `market_data.current_price.eur / market_data.current_price.jpy` | The value of one coin on the requested date, keyed by currency code. Keys such as `btc`, `eth` and `bnb` give the same value in crypto. |
| `market_data.market_cap.eur / market_data.market_cap.jpy` | The coin market cap on that date, keyed by currency code. |
| `market_data.total_volume.eur / market_data.total_volume.jpy` | The trading volume on that date, keyed by currency code. |
| `localization.en / localization.ja / localization.zh` | The coin name in each language, keyed by language code. This object appears when `localization` is true or left at its default. |
| `image.small / image.thumb` | URLs of the coin image in two sizes. |
| `public_interest_stats.alexa_rank / public_interest_stats.bing_matches` | Public interest counters. They are `null` in this response. |

### Notes

- Get the coin `id` from [CoinGecko Coins List (ID Map)](/apis/coingecko/coins-list).
- The schema describes `date` as `YYYY-MM-DD`, but the request example uses `30-12-2024`. Check which format your call accepts.
- Set `localization` to `false` to leave out the language names.
- For a range of dates in one call, use [CoinGecko Coin Historical Chart Data within Time Range by ID](/apis/coingecko/coins-market-chart-range).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/coins-history.json`](../../../catalog/models/coingecko/coins-history.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-history
