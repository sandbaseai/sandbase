# Google Maps API: 1 endpoints with pricing and code examples

Call 1 Google Maps endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`google-maps/photo-metadata`](../models/google-maps/photo-metadata.md) | Contributor, place, coordinates, type and date of one Google Maps photo by its data ID. | $0.00015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-maps/photo-metadata", "data_id": "CIABIhAAQr6KrxiC_knILBjf2RxL"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
