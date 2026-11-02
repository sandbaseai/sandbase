# Douyin Live Room Gift User Ranking API: pricing, parameters and code examples

`douyin/web/live-gift-ranking` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Retrieves the contributor gift ranking for a specific Douyin live stream room. Query by room ID and leaderboard type to inspect top gift givers.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/live-gift-ranking", "rank_type": 30, "room_id": "7356585666190461731"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/live-gift-ranking', {'rank_type': 30, 'room_id': '7356585666190461731'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/live-gift-ranking", {
  "rank_type": 30,
  "room_id": "7356585666190461731"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/live-gift-ranking", sandbase.Params{
	"rank_type": 30,
	"room_id": "7356585666190461731",
})
```

Same call via the path form: `POST /v1/api/douyin/web/live-gift-ranking` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Room room_id  |
| `rank_type` | integer |  | Leaderboard type, default is 30, no need to modify. default `30` |

## Details

Fetch the user gift ranking list for a Douyin live stream room using `room_id`. You can also configure the leaderboard format via `rank_type`.

### Use cases

- Identify top gift contributors during a Douyin live broadcast.
- Monitor audience engagement and supporter rankings for live rooms.
- Track live gifting activity for creator performance analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/live-gift-ranking" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "7356585666190461731"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Room room_id |
| `rank_type` | integer | No | Leaderboard type, default is 30, no need to modify. |

### Notes

- `rank_type` specifies the leaderboard type and defaults to 30.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/live-gift-ranking.json`](../../../../catalog/models/douyin/web/live-gift-ranking.json) · Store page: https://www.sandbase.ai/model/douyin/web/live-gift-ranking
