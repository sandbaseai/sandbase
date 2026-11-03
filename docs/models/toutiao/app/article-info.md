# Toutiao Article Details (App) API: pricing, parameters and code examples

`toutiao/app/article-info` · data API · Toutiao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns details and interface settings for a specified Toutiao post. Provide the post ID to inspect article properties and action settings.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/app/article-info", "group_id": "7450114952884503059"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('toutiao/app/article-info', {'group_id': '7450114952884503059'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("toutiao/app/article-info", {
  "group_id": "7450114952884503059"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "toutiao/app/article-info", sandbase.Params{
	"group_id": "7450114952884503059",
})
```

Same call via the path form: `POST /v1/api/toutiao/app/article-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `group_id` | string | yes | Post ID, can be obtained from the link  |

## Details

Returns details for one Toutiao article: engagement counts, the publishing account, share links, and the action bar settings. It needs the article's `group_id`.

### Use cases

- Track the read, like, comment and share counts of a single Toutiao article.
- Identify which media account published an article and check its follower count and verification status.
- Get the share URL, share title and source article URL for a post.
- Check whether commenting, liking or burying is disabled on an article.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/toutiao/app/article-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"group_id": "7450114952884503059"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `group_id` | string | Yes | Post ID, can be obtained from the link |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "ab_path": "0f35e2858fb36f23fab49cc74e768cf5",
    "ban_bury": 0,
    "ban_comment": 0,
    "ban_digg": 0,
    "bury_count": 0,
    "comment_count": 1,
    "content_hash": "e6b66251",
    "context": "{\"entity_info\":{\"1140837504906020782\":{\"baike\":{\"button_title\":\"查看百科\",\"descripti…",
    "danmaku_count": 0,
    "dataType": 0,
    "detail_show_flags": 0,
    "digg_count": 3
  },
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.group_id` | Numeric ID of the article. `data.itemCell.articleBase.gidStr` holds the same ID as a string. |
| `data.share_info.title` | Article title, with the " - 今日头条" suffix. |
| `data.source` | Name of the account that published the article. |
| `data.url` | Link to the original article on the publisher's site. |
| `data.read_count / data.digg_count / data.comment_count / data.repin_count` | Counts of reads, likes, comments and saves (repins) for the article. |
| `data.itemCell.itemCounter.shareCount / data.itemCell.itemCounter.forwardCount` | Counts of shares and forwards for the article. `readCount`, `diggCount` and `commentCount` in the same object repeat the main counts. |
| `data.user_info.name / data.user_info.fans_count / data.user_info.user_verified` | Publisher account name, follower count, and whether the account is verified. `data.user_info.user_auth_info` holds the verification label as a JSON string. |
| `data.user_info.media_id / data.user_info.user_id` | Numeric IDs of the publishing media account and its user. |
| `data.ban_comment / data.ban_digg / data.ban_bury` | Flags for whether comments, likes and buries are disabled. `0` means not disabled. |
| `data.itemCell.actionCtrl.actionBar.actionSettingList[]` | Action bar buttons for the article. Each entry has an `actionType` and a `styleSetting.text` label such as share, comment or like. |
| `data.h5_extra.audio_info.audioDuration` | Length of the audio version of the article. `audioWatchCount` shows how many times the audio was played. |

### Notes

- Take `group_id` from the Toutiao post link. It is the long number after `/group/` or `/article/`, for example `7450114952884503059`.
- `data.itemCell` and `data.h5_extra.itemCell` contain the same article data, and `data.user_info` and `data.media_info` contain the same account data.
- To read comments on the article, call [Toutiao Post Comments](/apis/toutiao/app/comments). For the publisher's profile, use [Toutiao User Profile](/apis/toutiao/app/user-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Toutiao Post Comments](/apis/toutiao/app/comments): Returns user comments and interaction metrics for a specific Toutiao post.
- [Toutiao Profile User ID](/apis/toutiao/app/user-id): Resolves a Toutiao user profile URL into numeric and secure user identifiers.
- [Toutiao User Profile](/apis/toutiao/app/user-info): Get a Toutiao (Jinri Toutiao) user profile by user ID: name, bio, avatar, follower, following and like counts, and content tabs.

---
Machine-readable: [`catalog/models/toutiao/app/article-info.json`](../../../../catalog/models/toutiao/app/article-info.json) · Store page: https://www.sandbase.ai/model/toutiao/app/article-info
