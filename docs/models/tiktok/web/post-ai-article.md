# TikTok AI-generated article of a single video API: pricing, parameters and code examples

`tiktok/web/post-ai-article` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get AI-generated article of a single video on TikTok. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/post-ai-article", "itemId": "7651935877744168194"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/post-ai-article', {'itemId': '7651935877744168194'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/post-ai-article", {
  "itemId": "7651935877744168194"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/post-ai-article", sandbase.Params{
	"itemId": "7651935877744168194",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/post-ai-article` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | Video id  |

## Details

Returns an AI-generated article for a single TikTok video, with a title, a short description and SEO keywords. It needs the video id as `itemId`.

### Use cases

- Turn a video into a written summary for a blog or newsletter.
- Pull the suggested keywords of a video to study how it is described for search.
- Collect titles and descriptions of many videos to review their topics in bulk.
- Check how a product review video, such as a skincare or sunscreen review, is summarized in text.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/post-ai-article" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "7651935877744168194"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611030744269003827AA4F970017CAA",
    "now": 1793691867000
  },
  "itemCustomTDK": {
    "article": "The world of sunscreens can be overwhelming, with countless options available, e…",
    "desc": "Discover my genuine thoughts on the new Supergoop Unseen Sunscreen SPF50 and why…",
    "keywords": [
      "Supergoop unseen sunscreen review"
    ],
    "title": "Supergoop Unseen Sunscreen SPF50 Review: A Surprising Find"
  },
  "log_pb": {
    "impr_id": "202611030744269003827AA4F970017CAA"
  },
  "statusCode": 0,
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `itemCustomTDK.title` | AI-generated title for the video. |
| `itemCustomTDK.article` | Body text of the AI-generated article about the video. Long articles are returned as one string. |
| `itemCustomTDK.desc` | Short description of the video. It can include the hashtags from the video caption. |
| `itemCustomTDK.keywords[]` | List of suggested keywords for the video. Some entries start with a space, so trim them before use. |
| `status_code / statusCode` | Result code of the request. `0` in this response. |
| `status_msg` | Status message. It is an empty string in this response. |
| `extra.fatal_item_ids[]` | List of video ids that failed to load. It is empty in this response. |
| `extra.now` | Time of the response as a number, such as `1793691867000`. |
| `log_pb.impr_id / extra.logid` | Request tracking ids. Both hold the same value in this response. |

### Notes

- Pass the video id as `itemId`. It is a numeric string such as `7651935877744168194`.
- If you only have a video link, call [TikTok Video ID from URL](/apis/tiktok/web/aweme-id) first to get the id.
- To see stats, author and media for the same video, call [TikTok Video Detail](/apis/tiktok/web/post-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/tiktok/web/post-ai-article.json`](../../../../catalog/models/tiktok/web/post-ai-article.json) · Store page: https://www.sandbase.ai/model/tiktok/web/post-ai-article
