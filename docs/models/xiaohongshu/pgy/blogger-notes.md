# Xiaohongshu (RED) PGY Blogger Notes API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-notes` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Returns notes posted by a specific blogger on the Xiaohongshu Pugongying platform. Supports filtering by note type, content tag, feature tag, and traffic source.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-notes", "advertise_switch": 1, "note_type": 4, "order_type": 1, "page_number": 1, "page_size": 8, "user_id": "5c668b3e0000000012021605"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-notes', {'advertise_switch': 1, 'note_type': 4, 'order_type': 1, 'page_number': 1, 'page_size': 8, 'user_id': '5c668b3e0000000012021605'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-notes", {
  "advertise_switch": 1,
  "note_type": 4,
  "order_type": 1,
  "page_number": 1,
  "page_size": 8,
  "user_id": "5c668b3e0000000012021605"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-notes", sandbase.Params{
	"advertise_switch": 1,
	"note_type": 4,
	"order_type": 1,
	"page_number": 1,
	"page_size": 8,
	"user_id": "5c668b3e0000000012021605",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-notes` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Blogger user ID  |
| `note_type` | integer |  | Note type, 0=all, 1=image, 2=video, 4=image+video one of: `0`, `1`, `2`, `4` |
| `page_size` | integer |  | Page size (1-100) range 1–100 |
| `order_type` | integer |  | Order, 1=most read, 2=most interaction, 3=latest one of: `1`, `2`, `3` |
| `content_tag` | string |  | 按内容类目筛选，如 美妆；取值见博主详情的 contentTags/Filter by content tag default `""` |
| `feature_tag` | string |  | 按内容特征筛选，如 韩系；取值见博主详情的 featureTags/Filter by feature tag default `""` |
| `page_number` | integer |  | Page number, start from 1 range 1–1000 |
| `advertise_switch` | integer |  | Traffic type, 1=all (incl. ads), 0=organic only one of: `0`, `1` |
| `is_third_platform` | integer |  | 1=只看跨域合作笔记 0=不限(默认)/Cross-platform notes only one of: `0`, `1`; default `0` |

## Details

Retrieve notes for a specific creator by supplying their `user_id`. You can sort results by interaction or recency, and filter entries by tags and media formats.

### Use cases

- Review historical content and top-performing posts for a specific creator.
- Filter creator posts by video or image formats to assess creative range.
- Analyze organic versus sponsored post performance across campaign categories.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-notes" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "<user_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Blogger user ID |
| `note_type` | integer | No | Note type, 0=all, 1=image, 2=video, 4=image+video |
| `page_size` | integer | No | Page size (1-100) |
| `order_type` | integer | No | Order, 1=most read, 2=most interaction, 3=latest |
| `content_tag` | string | No | 按内容类目筛选，如 美妆；取值见博主详情的 contentTags/Filter by content tag |
| `feature_tag` | string | No | 按内容特征筛选，如 韩系；取值见博主详情的 featureTags/Filter by feature tag |
| `page_number` | integer | No | Page number, start from 1 |
| `advertise_switch` | integer | No | Traffic type, 1=all (incl. ads), 0=organic only |
| `is_third_platform` | integer | No | 1=只看跨域合作笔记 0=不限(默认)/Cross-platform notes only |

### Notes

- Use `order_type` to sort results by most read (1), most interaction (2), or latest (3).
- Pagination is controlled via `page_number` (starting at 1) and `page_size` (up to 100).
- Filter media formats using `note_type` with 0 for all, 1 for images, 2 for videos, or 4 for mixed.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/model/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Data Summary](/model/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Details](/model/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-notes.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-notes.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-notes
