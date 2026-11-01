# YouTube Playlist

`youtube/playlist` · api · YouTube

List every video in a YouTube playlist (title, length, and channel per video plus playlist owner and totals).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/playlist", "playlistId": "PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/playlist', {'playlistId': 'PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/playlist", {
  "playlistId": "PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/playlist", sandbase.Params{
	"playlistId": "PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj",
})
```

Same call via the path form: `POST /v1/api/youtube/playlist` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `playlistId` | string | yes | The playlist ID: the "list" parameter in a playlist URL (e.g. "PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi").  |

## Details

List every video in a YouTube playlist (title, length, and channel per video plus playlist owner and totals).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/playlist" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"playlistId": "PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `playlistId` | string | Yes | The playlist ID: the "list" parameter in a playlist URL (e.g. "PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi"). |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/youtube/playlist.json`](../../../catalog/models/youtube/playlist.json) · Store page: https://www.sandbase.ai/model/youtube/playlist
