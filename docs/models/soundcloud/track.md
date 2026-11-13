# SoundCloud Track API: pricing, parameters and code examples

`soundcloud/track` · data API · SoundCloud · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Get a SoundCloud track by artist and track slug with title, duration, plays, likes, reposts, comments, genre, artwork and upload date.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "soundcloud/track", "artist": "forss", "track": "flickermood"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('soundcloud/track', {'artist': 'forss', 'track': 'flickermood'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("soundcloud/track", {
  "artist": "forss",
  "track": "flickermood"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "soundcloud/track", sandbase.Params{
	"artist": "forss",
	"track": "flickermood",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/soundcloud/track` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `track` | string | yes | Track slug from the SoundCloud URL.  |
| `artist` | string | yes | SoundCloud artist name from the track URL.  |
| `timeout` | number |  | Seconds the data source may spend before giving up (max 50, default 50). A timed-out call is not billed. default `50`; range –50 |

## Details

Get a SoundCloud track by artist and track slug with title, duration, plays, likes, reposts, comments, genre, artwork and upload date.

---
Machine-readable: [`catalog/models/soundcloud/track.json`](../../../catalog/models/soundcloud/track.json) · Store page: https://www.sandbase.ai/model/soundcloud/track
