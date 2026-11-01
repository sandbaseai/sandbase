# Douyin Web Series Videos

`douyin/web/series-aweme` · api · Douyin

Returns a paginated list of series videos from the Douyin web platform. Results can be filtered by content subtype, page number, and page size.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/series-aweme", "content_type": 1, "count": 1, "offset": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/series-aweme', {'content_type': 1, 'count': 1, 'offset': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/series-aweme", {
  "content_type": 1,
  "count": 1,
  "offset": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/series-aweme", sandbase.Params{
	"content_type": 1,
	"count": 1,
	"offset": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/web/series-aweme` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer | yes | Number per page, default is 16  |
| `offset` | integer | yes | Page number, default is 0  |
| `content_type` | integer | yes | Subtype, default is 0  |

## Details

Retrieve series videos on the Douyin web platform by specifying the `content_type`, `offset`, and `count` parameters.

### Use cases

- Retrieve episodic video content from Douyin series.
- Paginate through available series videos on the web platform.
- Filter series video items by content subtype.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/series-aweme" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"content_type": "<content_type>", "count": "<count>", "offset": "<offset>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | Yes | Number per page, default is 16 |
| `offset` | integer | Yes | Page number, default is 0 |
| `content_type` | integer | Yes | Subtype, default is 0 |

### Notes

- `count` sets the number of videos per page and defaults to 16.
- `offset` specifies the page offset and defaults to 0.
- `content_type` indicates the series subtype and defaults to 0.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/series-aweme.json`](../../../../catalog/models/douyin/web/series-aweme.json) · Store page: https://www.sandbase.ai/model/douyin/web/series-aweme
