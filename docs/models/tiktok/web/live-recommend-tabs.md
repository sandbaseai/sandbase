# TikTok Stream Recommendation Tabs API: pricing, parameters and code examples

`tiktok/web/live-recommend-tabs` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns available recommendation tabs and category tags for TikTok broadcast homepages. Supports pagination via a log identifier cursor.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/live-recommend-tabs"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/live-recommend-tabs', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/live-recommend-tabs", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/live-recommend-tabs", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/live-recommend-tabs` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `logid` | string |  | Pagination cursor. Leave empty for the first page; to load the next page, pass the `logid` value returned by the previous response default `""` |

## Details

Returns the recommendation tabs and category tags shown on the TikTok LIVE homepage, with sub-tabs and viewer counts. It needs no input for the first page and takes an optional `logid` cursor for later pages.

### Use cases

- Track which game categories, such as Gaming sub-tabs, have the most live viewers.
- Build a category menu for an external live-stream dashboard.
- Compare viewer counts across lifestyle tabs like Chats, Outdoors and Talents.
- Collect cover images for each live category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/live-recommend-tabs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `logid` | string | No | Pagination cursor. Leave empty for the first page; to load the next page, pass the `logid` value returned by the previous response |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "is_not_show_tab": false,
      "sub_tabs": [
        {
          "cover_url": "https://p19-common-sign.tiktokcdn.com/tos-alisg-i-agnx3xz2cs-sg/Garena_Free_Fire…",
          "position": 0,
          "rank_type": "hot_game",
          "tab_name": "Garena Free Fire",
          "tab_type": "Garena Free Fire",
          "viewer_count": 71422
        }
      ],
      "tab_name": "Gaming",
      "tab_type": "gaming"
    }
  ],
  "extra": {
    "has_more": true,
    "if_expire": true,
    "now": 1793691866004
  },
  "logid": "20261103154425C6E4DDDF5B9C6943B3EB",
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].tab_name / data[].tab_type` | Display name and internal type of a top-level tab, for example `Gaming` and `gaming`. |
| `data[].is_not_show_tab` | When `true`, the tab is a settings entry and is not shown as a normal tab. Its `sub_tabs` list is empty. |
| `data[].sub_tabs[].tab_name` | Display name of a category inside the tab, such as `Fortnite` or `Chats`. |
| `data[].sub_tabs[].tab_type` | Internal type of the sub-tab. For games it matches the game name. For lifestyle tabs it is a code like `chatting` or `outdoor`. |
| `data[].sub_tabs[].viewer_count` | Viewer count shown for the sub-tab. |
| `data[].sub_tabs[].rank_type` | Ranking label for the sub-tab, such as `hot_game`. It is an empty string when no label applies. |
| `data[].sub_tabs[].cover_url` | Signed URL of the cover image for the sub-tab. |
| `data[].sub_tabs[].position` | Position value of the sub-tab. It is `0` for every item in this response. |
| `extra.has_more` | Shows whether another page is available. |
| `logid` | Cursor value for the next page. Pass it as the `logid` request parameter. |

### Notes

- Leave `logid` empty for the first page. For the next page, send the `logid` value from the previous response.
- Check `extra.has_more` to see if more pages exist.
- `extra.now` is a timestamp in milliseconds, for example `1793691866004`.
- Cover image URLs are signed and contain an `x-expires` parameter, so save the images soon after you fetch them.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/live-recommend-tabs.json`](../../../../catalog/models/tiktok/web/live-recommend-tabs.json) · Store page: https://www.sandbase.ai/model/tiktok/web/live-recommend-tabs
