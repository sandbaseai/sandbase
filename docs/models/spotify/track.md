# Spotify Track API: pricing, parameters and code examples

`spotify/track` · data API · Spotify · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch a Spotify track's play count, popularity, duration, and album details by track URL or ID.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "spotify/track"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('spotify/track', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("spotify/track", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "spotify/track", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/spotify/track` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string |  | Spotify track ID (alternative to url).  |
| `url` | string |  | Spotify track URL (e.g. https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT).  |

## Details

Fetch a Spotify track's play count, popularity, duration, and album details by track URL or ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "spotify/track", "url": "https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | No | Spotify track ID (alternative to url). |
| `url` | string | No | Spotify track URL (e.g. https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT). |

### Pricing

Billed at the actual cost of each call, about $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/spotify/track.json`](../../../catalog/models/spotify/track.json) · Store page: https://www.sandbase.ai/model/spotify/track
