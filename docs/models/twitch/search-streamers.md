# Twitch Search Streamers API: pricing, parameters and code examples

`twitch/search-streamers` · data API · Twitch · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Search for Twitch channels/streamers by query. Returns matching channels with live status, follower counts, and current stream info. Searches across channel names, stream titles, and game names.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitch/search-streamers", "query": "valorant"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitch/search-streamers', {'query': 'valorant'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitch/search-streamers", {
  "query": "valorant"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitch/search-streamers", sandbase.Params{
	"query": "valorant",
})
```

Same call via the path form: `POST /v1/api/twitch/search-streamers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query (channel name, game name, or keywords)  |

## Details

Search for Twitch channels/streamers by query. Returns matching channels with live status, follower counts, and current stream info. Searches across channel names, stream titles, and game names.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "twitch/search-streamers", "query": "valorant"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query (channel name, game name, or keywords) |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitch/search-streamers.json`](../../../catalog/models/twitch/search-streamers.json) · Store page: https://www.sandbase.ai/model/twitch/search-streamers
