# Douyin Multi Search API: pricing, parameters and code examples

`douyin/search/multi-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns multi-type search results across videos, users, music, and hashtags on Douyin. Supports filtering by keyword, sort order, content type, duration, and post date.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/multi-search"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/multi-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/multi-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/multi-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/multi-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) default `0` |
| `keyword` | string |  | Search keyword, e.g., "Artificial Intelligence" default `"猫咪"` |
| `backtrace` | string |  | Backtrace for pagination, obtained from the last response default `""` |
| `search_id` | string |  | Search ID used for pagination default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type filter default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Returns Douyin search results for a keyword as a list of result cards, mostly videos, plus pagination state and suggested search words. The main input is `keyword`. Optional filters cover sort order, content type, video duration and publish time.

### Use cases

- Pull the top video cards for a keyword such as `猫咪` to see what Douyin ranks first.
- Collect the suggested search words returned for a keyword to find related topics.
- Page through results with `cursor`, `search_id` and `backtrace` to build a larger set of videos for one keyword.
- Narrow results by duration or post date with `filter_duration` and `publish_time` to study recent or short videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/multi-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `backtrace` | string | No | Backtrace for pagination, obtained from the last response |
| `content_type` | string | No | Content type filter |
| `cursor` | integer | No | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) |
| `filter_duration` | string | No | Video duration filter |
| `keyword` | string | No | Search keyword, e.g., "Artificial Intelligence" |
| `publish_time` | string | No | Publish time filter |
| `search_id` | string | No | Search ID used for pagination |
| `sort_type` | string | No | Sorting method |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  13270
]
```

### Response fields

| Field | Meaning |
|---|---|
| `business_config.business_data[].card_id` | Type of each result card. The sample value `douyin.doctype_aweme_video` marks a video card. |
| `business_config.business_data[].data.aweme_info` | Video details for a video card. It includes the video author, an `authentication_token` and the other video metadata. |
| `business_config.business_data[].data.aweme_info.author` | Profile data of the account that posted the video, including avatar images with `url_list` links. |
| `business_config.business_data[].log.search_result_id` | ID of the search result, which matches the video ID used in `pitaya_common_feature.doc_feature[].search_result_id`. |
| `business_config.has_more` | Shows whether more results exist. The sample value is `1`. |
| `business_config.next_page.cursor` | Cursor value to send as `cursor` when you request the next page. |
| `business_config.next_page.search_id` | Search ID to send as `search_id` when you request the next page. |
| `business_config.backtrace` | Pagination token to send as `backtrace` when you request the next page. |
| `business_config.extra.guide_search_words[].word` | Suggested related search word, such as `视频`, `图片` or `头像`. |
| `business_config.extra.impression_server_log.query` | The keyword the search ran for. |

### Notes

- For the first page, send `cursor` as `0` and leave `search_id` and `backtrace` empty.
- For the next page, copy `business_config.next_page.cursor`, `business_config.next_page.search_id` and `business_config.backtrace` into `cursor`, `search_id` and `backtrace`.
- The response is a JSON array. The search data is in the second element, under `business_config`.
- To search one content type only, try [Douyin Video Search](/apis/douyin/search/video-search-v2), [Douyin User Search (V2)](/apis/douyin/search/user-search-v2) or [Douyin Music Search](/apis/douyin/search/music-search).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/multi-search.json`](../../../../catalog/models/douyin/search/multi-search.json) · Store page: https://www.sandbase.ai/model/douyin/search/multi-search
