# Twitch Live Streams API: pricing, parameters and code examples

`twitch/live-streams` · data API · Twitch · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get currently live streams, optionally filtered by game/category. Returns streams sorted by relevance or viewer count with broadcaster info, game details, and tags. Supports pagination via cursor.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitch/live-streams"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitch/live-streams', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitch/live-streams", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitch/live-streams", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/twitch/live-streams` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort order for streams. default `"RELEVANCE"` |
| `limit` | integer |  | Number of streams to return (1-100) default `30` |
| `category` | string |  | Game/category slug (e.g., 'just-chatting', 'fortnite', 'league-of-legends'). If omitted or empty, returns top streams across all categories.  |

## Details

Get currently live streams, optionally filtered by game/category. Returns streams sorted by relevance or viewer count with broadcaster info, game details, and tags. Supports pagination via cursor.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "twitch/live-streams", "sort": "RELEVANCE", "limit": 5, "category": "just-chatting"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | No | Game/category slug (e.g., 'just-chatting', 'fortnite', 'league-of-legends'). If omitted or empty, returns top streams across all categories. |
| `limit` | integer | No | Number of streams to return (1-100) |
| `sort` | string | No | Sort order for streams. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitch/live-streams.json`](../../../catalog/models/twitch/live-streams.json) · Store page: https://www.sandbase.ai/model/twitch/live-streams
