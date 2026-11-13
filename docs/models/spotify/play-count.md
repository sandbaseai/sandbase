# Spotify Play Count API: pricing, parameters and code examples

`spotify/play-count` · data API · Spotify · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0022 per call · **Modes:** sync

Fetch stream counts and stats for a Spotify track, album, or artist URL.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0022**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "spotify/play-count", "url": "https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('spotify/play-count', {'url': 'https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("spotify/play-count", {
  "url": "https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "spotify/play-count", sandbase.Params{
	"url": "https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT",
})
```

Same call via the path form: `POST /v1/api/spotify/play-count` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Spotify track, album, or artist URL to fetch stream counts for (e.g. https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp).  |

## Details

Fetch stream counts and stats for a Spotify track, album, or artist URL.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "spotify/play-count", "url": "https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Spotify track, album, or artist URL to fetch stream counts for (e.g. https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp). |

### Pricing

Billed at the actual cost of each call: about $0.0022 per result returned, up to $0.0022 per request (about $0.0022 for the request above). A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/spotify/play-count.json`](../../../catalog/models/spotify/play-count.json) · Store page: https://www.sandbase.ai/model/spotify/play-count
