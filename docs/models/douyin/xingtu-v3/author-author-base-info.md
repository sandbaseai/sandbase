# Douyin Xingtu Creator Profile API: pricing, parameters and code examples

`douyin/xingtu-v3/author-author-base-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get the Douyin Creator Marketplace (Xingtu) profile for a specified creator and content channel. Use it to review creator information before shortlisting or campaign outreach.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/author-author-base-info", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/author-author-base-info', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/author-author-base-info", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/author-author-base-info", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/author-author-base-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns the Douyin Xingtu (Creator Marketplace) profile for one creator. It needs the creator's Xingtu author ID in `oAuthorId` and optionally a content channel in `platform`.

### Use cases

- Check a creator's follower count, nickname and MCN before adding them to a campaign shortlist.
- Find which agency (MCN) represents a creator so you know who to contact for outreach.
- Read a creator's content theme labels to judge topic fit for a brand.
- Check whether a creator is active and visible on Xingtu before sending an order.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/author-author-base-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `platform` | string | No | Platform type. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "abandon_sign_result": 0,
  "appeal_id": "0",
  "author_avatar_frame_icon": 0,
  "author_type": 2,
  "avatar_uri": "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-i-0813c000-ce_os7G9…",
  "avg_play": 0,
  "aweme_tags": [],
  "base64_qrcode": "iVBORw0KGgoAAAANSUhEUgAAAWgAAAFoAQAAAABSnlx4AAACYUlEQVR4nO2aS47DQAhEq0a5/5VrFkCb…",
  "base_resp": {
    "status_code": 0,
    "status_message": "Success"
  },
  "category_id": "1",
  "city": "",
  "content_theme_labels": [
    "网球赛事"
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `nick_name` | The creator's display name on Douyin. |
| `id / core_user_id` | `id` is the Xingtu author ID you sent in the request. `core_user_id` is a second numeric ID for the same creator. |
| `follower` | Total follower count of the creator. |
| `content_theme_labels` | List of topic labels that describe the creator's content, in Chinese. |
| `mcn_name / mcn_id / mcn_logo` | Name, ID and logo URL of the MCN agency linked to the creator. |
| `is_star / is_online / is_visible` | Flags for the creator's Xingtu status. `is_visible` was `false` in the sample response. |
| `e_commerce_enable` | Whether the creator has e-commerce enabled. `false` in the sample response. |
| `avatar_uri` | URL of the creator's avatar image. |
| `platform / platform_channel` | Lists of numeric codes for the platforms and channels the creator is on. The response does not label the codes. |
| `create_time / modify_time` | Unix timestamps in seconds, sent as strings. |

### Notes

- Get `oAuthorId` from [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- `platform` accepts `SHORT_VIDEO` (default), `LIVE_STREAMING`, `PICTURE_TEXT` and `SHORT_DRAMA`.
- For performance data, call [Douyin Xingtu Marketing Metrics](/apis/douyin/xingtu-v3/author-author-marketing-info) next.
- For audience details, call [Douyin Xingtu Audience Distribution](/apis/douyin/xingtu-v3/data-sp-author-audience-distribution).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/author-author-base-info.json`](../../../../catalog/models/douyin/xingtu-v3/author-author-base-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/author-author-base-info
