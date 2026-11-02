# Xiaohongshu (RED) PGY Blogger Note Rates API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-notes-rate` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Returns overall note performance metrics from a creator's data overview on Pugongying. Supports filtering by date range, note format, and advertising traffic.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-notes-rate", "user_id": "60b137080000000001000301"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-notes-rate', {'user_id': '60b137080000000001000301'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-notes-rate", {
  "user_id": "60b137080000000001000301"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-notes-rate", sandbase.Params{
	"user_id": "60b137080000000001000301",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-notes-rate` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Blogger user ID  |
| `date_type` | integer |  | Date range (~1=7d, 2=30d, 3=90d) range 1–12 |
| `note_type` | integer |  | Note type, 1=image, 2=video, 3=all (default) one of: `1`, `2`, `3` |
| `advertise_switch` | integer |  | Traffic type, 1=all (incl. ads), 0=organic only one of: `0`, `1` |

## Details

Retrieve aggregated note performance statistics for a specific creator using `user_id`. Optional parameters filter metrics by date window, note format, and traffic source.

### Use cases

- Evaluate creator engagement rates across image and video formats.
- Compare organic note performance against sponsored campaign traffic.
- Assess creator content delivery trends over 7, 30, or 90 days.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-notes-rate" \
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

### Notes

- Use `date_type` to set the analysis window: 1 for 7 days, 2 for 30 days, or 3 for 90 days.
- `note_type` filters by format: 1 for image, 2 for video, or 3 for all notes.
- `advertise_switch` controls whether traffic includes advertising (1) or organic views only (0).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/model/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Data Summary](/model/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Details](/model/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-notes-rate.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-notes-rate.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-notes-rate
