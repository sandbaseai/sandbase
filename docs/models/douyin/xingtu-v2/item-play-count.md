# Douyin Video Play Count

`douyin/xingtu-v2/item-play-count` · api · Douyin

Get the play count (watch_cnt) of a Douyin video from XingTu, plus video details such as author, cover, duration and publish time.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/item-play-count", "item_id": "7630036460159111515", "need_cover_url": true, "platform_source": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/item-play-count', {'item_id': '7630036460159111515', 'need_cover_url': True, 'platform_source': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/item-play-count", {
  "item_id": "7630036460159111515",
  "need_cover_url": true,
  "platform_source": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/item-play-count", sandbase.Params{
	"item_id": "7630036460159111515",
	"need_cover_url": true,
	"platform_source": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/item-play-count` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video (item) ID  |
| `need_cover_url` | boolean |  | Whether to return cover URL, default true default `true` |
| `platform_source` | integer |  | Platform source, default 1 default `1` |

## Details

Pass a Douyin video ID and get its play count from XingTu, which Douyin does not show publicly, together with basic video details.

### Use cases

- Verify real views of sponsored videos.
- Track play counts for campaign reporting.
- Compare views with likes to spot anomalies.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/item-play-count" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7630036460159111515"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video (item) ID |
| `need_cover_url` | boolean | No | Whether to return cover URL, default true |
| `platform_source` | integer | No | Platform source, default 1 |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "item_id": "7630036460159111515",
  "watch_cnt": 12644412
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Get Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Get creator audience profile distribution.
- [Get Author Base Info](/model/douyin/xingtu-v2/author-base-info): Get creator/author base information.
- [Get Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Get creator/author business card information.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/item-play-count.json`](../../../../catalog/models/douyin/xingtu-v2/item-play-count.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/item-play-count
