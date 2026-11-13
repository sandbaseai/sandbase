# Spotify Podcast API: pricing, parameters and code examples

`spotify/podcast` · data API · Spotify · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch a Spotify podcast show's name, publisher, description, rating, and topics by show URL or ID.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "spotify/podcast"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('spotify/podcast', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("spotify/podcast", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "spotify/podcast", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/spotify/podcast` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string |  | Spotify podcast show ID (alternative to url).  |
| `url` | string |  | Spotify podcast show URL (e.g. https://open.spotify.com/show/3mliji9352UAk3XnWElnDV).  |

## Details

Fetch a Spotify podcast show's name, publisher, description, rating, and topics by show URL or ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "spotify/podcast", "url": "https://open.spotify.com/show/3mliji9352UAk3XnWElnDV"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | No | Spotify podcast show ID (alternative to url). |
| `url` | string | No | Spotify podcast show URL (e.g. https://open.spotify.com/show/3mliji9352UAk3XnWElnDV). |

### Pricing

Billed at the actual cost of each call, about $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/spotify/podcast.json`](../../../catalog/models/spotify/podcast.json) · Store page: https://www.sandbase.ai/model/spotify/podcast
