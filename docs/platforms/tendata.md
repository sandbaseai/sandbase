# Tendata API: 12 endpoints with pricing and code examples

Call 12 Tendata endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`tendata/company/search`](../models/tendata/company/search.md) | Fuzzy-match a company name to trade company IDs, optionally filtered by ISO3 country code, for use in other customs trade queries. | from $0 per run, depending on parameters |
| [`tendata/trade/destination-countries`](../models/tendata/trade/destination-countries.md) | Break down the customs records that match a trade query by destination country, with weight, USD value and shipment count for each country. | about $0.016 per call |
| [`tendata/trade/exporter-names`](../models/tendata/trade/exporter-names.md) | List the names of exporters that match a customs trade query, without aggregates, as a low-cost way to build a supplier list. | about $0.0016 per call |
| [`tendata/trade/exporters`](../models/tendata/trade/exporters.md) | Rank exporters that match a customs trade query (HS code, product, countries, ports, date window), with aggregated weight, USD value and… | about $0.019 per call |
| [`tendata/trade/exporters-summary`](../models/tendata/trade/exporters-summary.md) | Get one aggregate summary of the exporters that match a customs trade query: exporter count, total weight, USD value and shipments. | about $0.064 per call |
| [`tendata/trade/hs-codes`](../models/tendata/trade/hs-codes.md) | Break down the customs records that match a trade query by HS code, with weight, USD value and shipment count for each code. | about $0.016 per call |
| [`tendata/trade/importer-names`](../models/tendata/trade/importer-names.md) | List the names of importers that match a customs trade query, without aggregates, as a low-cost way to build a prospect list. | about $0.0016 per call |
| [`tendata/trade/importers`](../models/tendata/trade/importers.md) | Rank importers that match a customs trade query (HS code, product, countries, ports, date window), with aggregated weight, USD value and… | about $0.019 per call |
| [`tendata/trade/importers-summary`](../models/tendata/trade/importers-summary.md) | Get one aggregate summary of the importers that match a customs trade query: importer count, total weight, USD value and shipments. | about $0.064 per call |
| [`tendata/trade/origin-countries`](../models/tendata/trade/origin-countries.md) | Break down the customs records that match a trade query by country of origin, with weight, USD value and shipment count for each country. | about $0.016 per call |
| [`tendata/trade/record-count`](../models/tendata/trade/record-count.md) | Count the customs records that match a trade query before paying for rows, to check that filters are narrow enough. | from $0 per run, depending on parameters |
| [`tendata/trade/volume-trend`](../models/tendata/trade/volume-trend.md) | Get the weight, USD value and shipment count of the customs records that match a trade query for each month or year in the date window. | about $0.019 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tendata/company/search", "name": "apple", "pageNo": 1, "pageSize": 3}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
