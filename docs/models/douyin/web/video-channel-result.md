# Douyin Video Channel Feed

`douyin/web/video-channel-result` · api · Douyin

Returns video listings from a specific Douyin channel page. Requires a channel tag ID and supports pagination through count and refresh index parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/video-channel-result", "tag_id": 2027}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/video-channel-result', {'tag_id': 2027})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/video-channel-result", {
  "tag_id": 2027
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/video-channel-result", sandbase.Params{
	"tag_id": 2027,
})
```

Same call via the path form: `POST /v1/api/douyin/web/video-channel-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number  |
| `tag_id` | integer | yes | Tag id, get from the URL  |
| `refresh_index` | integer |  | Refresh index  |

## Details

Fetch video content from a Douyin channel by supplying `tag_id`. You can adjust result sizes with `count` and navigate channel results using `refresh_index`.

### Use cases

- Retrieve video lists associated with specific Douyin channel tags.
- Track media content appearing within selected channel feeds.
- Inspect video specifications and available bitrates for channel items.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/video-channel-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tag_id": 2027}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag_id` | integer | Yes | Tag id, get from the URL |
| `count` | integer | No | Number |
| `refresh_index` | integer | No | Refresh index |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_list": [
    {
      "video": {
        "bit_rate": [
          {
            "bit_rate": 1089619,
            "gear_name": "1080_1_1",
            "quality_type": 3
          }
        ]
      }
    }
  ]
}
```

### Notes

- Obtain `tag_id` from the channel URL on Douyin.
- Use `count` to control the number of videos returned.
- Pass `refresh_index` for paginated channel queries.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/video-channel-result.json`](../../../../catalog/models/douyin/web/video-channel-result.json) · Store page: https://www.sandbase.ai/model/douyin/web/video-channel-result
