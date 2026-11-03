# CoinGecko Coin Data by Token Address API: pricing, parameters and code examples

`coingecko/coins-contract` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Get all the metadata (image, websites, socials, description, contract address, etc.) and market data (price, ATH, exchange tickers, etc.) of a coin from the CoinGecko coin page based on an asset platform and a.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-contract", "contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "id": "ethereum"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-contract', {'contract_address': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', 'id': 'ethereum'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-contract", {
  "contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
  "id": "ethereum"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-contract", sandbase.Params{
	"contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
	"id": "ethereum",
})
```

Same call via the path form: `POST /v1/api/coingecko/coins-contract` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Asset platform ID. *refers to [`/asset_platforms`](/reference/asset-platforms-list). default `"ethereum"` |
| `contract_address` | string | yes | The contract address of token. default `"0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"` |

## Details

Returns the CoinGecko page data for one coin, found by its token contract address on a given asset platform. It needs `contract_address` and the asset platform `id`, and returns metadata such as links, categories and images, plus market data.

### Use cases

- Resolve a token contract address to its CoinGecko coin `id` so you can call other coin endpoints.
- List every chain where a stablecoin is deployed, with the contract address on each chain.
- Pull the homepage, block explorer, GitHub and whitepaper links for a token to build a token profile page.
- Show a token's icon, name and category tags in a wallet or portfolio app.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-contract" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "id": "ethereum"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `contract_address` | string | Yes | The contract address of token. |
| `id` | string | Yes | Asset platform ID. *refers to [`/asset_platforms`](/reference/asset-platforms-list). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "additional_notices": [],
  "asset_platform_id": "ethereum",
  "block_time_in_minutes": 0,
  "categories": [
    "Stablecoins"
  ],
  "contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
  "country_origin": "US",
  "description": {
    "ar": "",
    "bg": "",
    "cs": "",
    "da": "",
    "de": "",
    "el": "",
    "en": "USDC is a fully collateralized US dollar stablecoin. USDC is the bridge between …",
    "es": "",
    "fi": "",
    "fr": "",
    "he": "",
    "hi": ""
  },
  "detail_platforms": {
    "algorand": {
      "contract_address": "31566704",
      "decimal_place": 5
    },
    "aptos": {
      "contract_address": "0xbae207659db88bea0cbead6da0ed00aac12edcdda169e591cd41c94180b46f3b",
      "decimal_place": 6,
      "geckoterminal_url": "https://www.geckoterminal.com/aptos/tokens/0xbae207659db88bea0cbead6da0ed00aac12…"
    },
    "arbitrum-one": {
      "contract_address": "0xaf88d065e77c8cc2239327c5edb3a432268e5831",
      "decimal_place": 6,
      "geckoterminal_url": "https://www.geckoterminal.com/arbitrum/tokens/0xaf88d065e77c8cc2239327c5edb3a432…"
    },
    "arc": {
      "contract_address": "0x3600000000000000000000000000000000000000",
      "decimal_place": 6,
      "geckoterminal_url": "https://www.geckoterminal.com/arc/tokens/0x3600000000000000000000000000000000000…"
    },
    "avalanche": {
      "contract_address": "0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e",
      "decimal_place": 6,
      "geckoterminal_url": "https://www.geckoterminal.com/avax/tokens/0xb97ef9ef8734c71904d8002f8b6bc66dd9c4…"
    },
    "base": {
      "contract_address": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
      "decimal_place": 6,
      "geckoterminal_url": "https://www.geckoterminal.com/base/tokens/0x833589fcd6edb6e08f4c7c32d4f71b54bda0…"
    },
    "celo": {
      "contract_address": "0xceba9300f2b948710d2653dd7b07f33a8b32118c",
      "decimal_place": 6,
      "geckoterminal_url": "https://www.geckoterminal.com/celo/tokens/0xceba9300f2b948710d2653dd7b07f33a8b32…"
    },
    "cronos": {
      "contract_address": "0x3d7f2c478aafdb65542bcb44bceec05849999d2d",
      "decimal_place": 6,
      "geckoterminal_url": "https://www.geckoterminal.com/cro/tokens/0x3d7f2c478aafdb65542bcb44bceec05849999…"
    },
    "ethereum": {
      "contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
      "decimal_place": 6,
      "geckoterminal_url": "https://www.geckoterminal.com/eth/tokens/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606e…"
    },
    "hedera-hashgraph": {
      "contract_address": "0.0.456858",
      "decimal_place": 6,
      "geckoterminal_url": "https://www.geckoterminal.com/hedera-hashgraph/tokens/0.0.456858"
    },
    "hyperevm": {
      "contract_address": "0xb88339cb7199b77e23db6e890353e22632ba630f",
      "decimal_place": 6,
      "geckoterminal_url": "https://www.geckoterminal.com/hyperevm/tokens/0xb88339cb7199b77e23db6e890353e226…"
    },
    "hyperliquid": {
      "contract_address": "0x6d1e7cde53ba9467b783cb7c530ce054",
      "decimal_place": 8
    }
  },
  "genesis_date": null,
  "has_supply_breakdown": false,
  "hashing_algorithm": null,
  "id": "usd-coin"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | The CoinGecko coin ID for the token, for example `usd-coin`. Use it with the other CoinGecko coin APIs. |
| `asset_platform_id / contract_address` | The asset platform and contract address that matched your request. |
| `categories` | List of CoinGecko category names the coin belongs to, such as `Stablecoins`. |
| `detail_platforms.ethereum.contract_address / detail_platforms.ethereum.decimal_place` | The token's contract address and decimal places on one chain. Every other chain key under `detail_platforms`, such as `solana` or `base`, has the same shape. |
| `detail_platforms.ethereum.geckoterminal_url` | Link to the token page on GeckoTerminal for that chain. Some chains, such as `algorand`, do not have this field. |
| `description.en` | English description of the coin. Most other language keys are empty strings. |
| `image.large / image.small / image.thumb` | URLs of the coin logo in three sizes. |
| `links.homepage / links.blockchain_site / links.repos_url.github / links.whitepaper` | Official website, block explorer pages, GitHub repositories and whitepaper link for the coin. |
| `market_cap_rank` | The coin's rank by market cap. |
| `market_data.ath / market_data.ath_change_percentage` | The all-time high value of the coin and the percent change from that high. Both are keyed by currency code, such as `eur` or `btc`. |

### Notes

- Set `id` to an asset platform ID such as `ethereum`. The `detail_platforms` keys in the response show the ID format for other chains, for example `polygon-pos` and `arbitrum-one`.
- The `contract_address` format depends on the chain. It can be a 0x hex string, a mixed-case Solana string like `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`, or a Hedera style ID like `0.0.456858`.
- Call [CoinGecko Coin Historical Chart Data by Token Address](/apis/coingecko/coins-contract-market-chart) for chart data of the same token.
- Call [CoinGecko Coin Data by ID](/apis/coingecko/coins) with the returned `id` to fetch the same kind of coin page data without a contract address.

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/coins-contract.json`](../../../catalog/models/coingecko/coins-contract.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-contract
