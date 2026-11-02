# Xiaohongshu (RED) Blogger Core Data API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-core-data` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-core-data", "user_id": "60b137080000000001000301"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-core-data', {'user_id': '60b137080000000001000301'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-core-data", {
  "user_id": "60b137080000000001000301"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-core-data", sandbase.Params{
	"user_id": "60b137080000000001000301",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-core-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Blogger user ID  |
| `date_type` | integer |  | Date range (~1=7d, 2=30d, 3=90d) range 1–12 |
| `note_type` | integer |  | Note type, 1=image, 2=video, 3=all (default) one of: `1`, `2`, `3` |
| `advertise_switch` | integer |  | Traffic type, 1=all (incl. ads), 0=organic only one of: `0`, `1` |

## Details

Retrieve daily performance metrics and summary statistics for a creator using `user_id`. You can refine the returned dataset with `date_type`, `note_type`, and `advertise_switch`.

### Use cases

- Track daily performance trends for specific Xiaohongshu creators.
- Compare organic versus paid traffic metrics across blogger content.
- Filter creator engagement metrics across image and video formats.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-core-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "60b137080000000001000301"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Blogger user ID |
| `date_type` | integer | No | Date range (~1=7d, 2=30d, 3=90d) |
| `note_type` | integer | No | Note type, 1=image, 2=video, 3=all (default) |
| `advertise_switch` | integer | No | Traffic type, 1=all (incl. ads), 0=organic only |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "dailyData": [
      {
        "dateKey": "2026-09-06",
        "thirdUserNum": 0
      }
    ]
  }
}
```

### Notes

- Set `date_type` to 1 for 7 days, 2 for 30 days, or 3 for 90 days.
- Configure `note_type` as 1 for images, 2 for video, or 3 for all notes.
- Use `advertise_switch` to toggle between organic traffic only (0) and all traffic including ads (1).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) PGY Blogger Data Summary](/model/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Details](/model/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.
- [Xiaohongshu (RED) PGY Blogger Fan History](/model/xiaohongshu/pgy/blogger-fans-history): Returns historical follower growth counts for a Xiaohongshu Pugongying blogger over time based on user ID and a selected date range.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-core-data.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-core-data.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-core-data
