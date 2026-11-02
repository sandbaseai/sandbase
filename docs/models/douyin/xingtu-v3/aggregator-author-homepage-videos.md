# Douyin Xingtu Creator Homepage Videos API: pricing, parameters and code examples

`douyin/xingtu-v3/aggregator-author-homepage-videos` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.069444 per call · **Modes:** sync

List a Douyin Creator Marketplace (Xingtu) creator's homepage videos with keyword, video-type, assignment, date, and page filters. Use it to review relevant content before campaign selection.

## Pricing

- **$0.069444 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/aggregator-author-homepage-videos", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/aggregator-author-homepage-videos', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/aggregator-author-homepage-videos", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/aggregator-author-homepage-videos", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/aggregator-author-homepage-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starting from 1. default `1` |
| `endDate` | string |  | End publish date in yyyyMMdd format. The filter ends at 23:59:59 in Asia/Shanghai.  |
| `keyword` | string |  | Keyword used to search creator homepage videos.  |
| `oAuthorId` | string | yes | Author's unique Xingtu ID.  |
| `startDate` | string |  | Start publish date in yyyyMMdd format. The filter starts at 00:00:00 in Asia/Shanghai.  |
| `videoType` | string |  | Homepage video type filter. one of: `ALL`, `PERSONAL`, `XINGTU`; default `"ALL"` |
| `onlyAssign` | boolean |  | Whether to include only assigned videos. Xingtu usually shows this option when `videoType` is `XINGTU`. default `false` |

## Details

List a Douyin Creator Marketplace (Xingtu) creator's homepage videos with keyword, video-type, assignment, date, and page filters. Use it to review relevant content before campaign selection.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/aggregator-author-homepage-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique Xingtu ID. |
| `page` | integer | No | Page number, starting from 1. |
| `keyword` | string | No | Keyword used to search creator homepage videos. |
| `videoType` | string | No | Homepage video type filter. |
| `onlyAssign` | boolean | No | Whether to include only assigned videos. Xingtu usually shows this option when `videoType` is `XINGTU`. |
| `startDate` | string | No | Start publish date in yyyyMMdd format. The filter starts at 00:00:00 in Asia/Shanghai. |
| `endDate` | string | No | End publish date in yyyyMMdd format. The filter ends at 23:59:59 in Asia/Shanghai. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/aggregator-author-homepage-videos.json`](../../../../catalog/models/douyin/xingtu-v3/aggregator-author-homepage-videos.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/aggregator-author-homepage-videos
