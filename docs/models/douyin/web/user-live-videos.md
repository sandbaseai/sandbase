# Douyin User Webcast Video Records API: pricing, parameters and code examples

`douyin/web/user-live-videos` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Retrieves user broadcast video data from Douyin Web using a specific room identifier. Input the webcast ID to look up associated room records.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-live-videos", "webcast_id": "153857447459"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-live-videos', {'webcast_id': '153857447459'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-live-videos", {
  "webcast_id": "153857447459"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-live-videos", sandbase.Params{
	"webcast_id": "153857447459",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-live-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `webcast_id` | string | yes | Room webcast_id  |

## Details

Fetches user broadcast video data from Douyin Web for a target stream. Provide the room identifier in `webcast_id` to view matching video data.

### Use cases

- Retrieve broadcast video records for a specific Douyin room.
- Monitor user stream video data using a webcast identifier.
- Extract room-level video details and media from Douyin Web.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-live-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"webcast_id": "<webcast_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `webcast_id` | string | Yes | Room webcast_id |

### Notes

- Requires `webcast_id` representing the webcast room identifier.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-live-videos.json`](../../../../catalog/models/douyin/web/user-live-videos.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-live-videos
