# Kuaishou Music Ranking API: pricing, parameters and code examples

`kuaishou/app/music-ranking` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns ranked music tracks on Kuaishou, including track IDs, titles, hot counts, and audio URLs. Supports filtering by chart type and cursor pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/music-ranking"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/music-ranking', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/music-ranking", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/music-ranking", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/music-ranking` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Page size, default 20, range 1-50 default `20` |
| `tab_id` | integer |  | 100002=hot songs (default), 100063=Pi-plan ranking default `100002` |
| `pcursor` | string |  | Cursor, empty for first page default `""` |

## Details

Retrieve music chart leaderboards on Kuaishou by specifying `tab_id` for different rankings, with pagination managed via `pcursor` and `count`.

### Use cases

- Track trending songs and popular background audio across Kuaishou.
- Identify viral music tracks for social media content planning.
- Retrieve audio URLs and track metadata for platform music rankings.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/music-ranking" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Page size, default 20, range 1-50 |
| `tab_id` | integer | No | 100002=hot songs (default), 100063=Pi-plan ranking |
| `pcursor` | string | No | Cursor, empty for first page |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "musics": [
    {
      "audioType": 1,
      "copyrightTimeLimit": 60,
      "duration": 320,
      "finalStatus": 0,
      "hotCount": "1902.1万",
      "id": "5xak4hqnwe7ecw9",
      "name": "我不难过",
      "snippetDuration": 60,
      "type": 4,
      "url": "https://v1-plat-fdl.wsukwai.com/ksc2/pUMOAetCwmckeNtMnU5XWhK1n-Cof_zoeJdTw0B4qvO…"
    }
  ]
}
```

### Notes

- Set `tab_id` to 100002 for hot songs or 100063 for Pi-plan rankings.
- Use `count` to specify the page size between 1 and 50 tracks.
- Pass an empty string to `pcursor` for the initial page, then use subsequent cursor values for pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/music-ranking.json`](../../../../catalog/models/kuaishou/app/music-ranking.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/music-ranking
