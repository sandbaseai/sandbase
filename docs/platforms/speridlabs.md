# speridlabs models API: 1 endpoints with pricing and code examples

Call 1 speridlabs models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`speridlabs/idol`](../models/speridlabs/idol.md) | Idol by Sperid Labs turns a single image of an object into a 3D Gaussian splat (PLY) with a GLB point-cloud preview. | $0.1 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "speridlabs/idol", "image": "https://static.sandbase.ai/examples/92b467b8-e906-4df4-a912-290fbd4a134d/input/969c0927-46b5-4d95-91ca-8568e6eed33d.png"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
