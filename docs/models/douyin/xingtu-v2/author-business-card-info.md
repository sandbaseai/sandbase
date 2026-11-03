# Douyin Xingtu Author Business Card Info API: pricing, parameters and code examples

`douyin/xingtu-v2/author-business-card-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns business card details for a Douyin Xingtu creator based on the specified author ID. Useful for reviewing creator profile summaries and business contact information.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-business-card-info", "o_author_id": "7589271892177518598"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-business-card-info', {'o_author_id': '7589271892177518598'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-business-card-info", {
  "o_author_id": "7589271892177518598"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-business-card-info", sandbase.Params{
	"o_author_id": "7589271892177518598",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-business-card-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `o_author_id` | string | yes | Creator/author ID  |

## Details

Returns the business card of a Douyin Xingtu creator, including profile summary, follower count, city, and contact details. It needs one input, the creator's Xingtu author ID in `o_author_id`.

### Use cases

- Check a creator's follower count and credit score before you shortlist them for a brand campaign.
- See whether a creator shows a WeChat contact and whether an email or phone is listed.
- Match a Xingtu creator to their public Douyin ID using `unique_id` and `short_id`.
- Check whether a creator belongs to an MCN through the `mcn_info` object.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-business-card-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7589271892177518598"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator/author ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "card_info": {
    "author_avatar_frame_icon": 0,
    "avatar_uri": "https://p26.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-i-0813c000-ce_oYEL…",
    "city": "长春",
    "contact_status": 1,
    "cooperation_brand": "",
    "credit_score": "100",
    "email": "",
    "follower": "320991",
    "has_wechat": true,
    "lark_nick_name": "",
    "mcn_info": {},
    "nick_name": "芯科技Lady"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `card_info.nick_name` | Display name of the creator. |
| `card_info.follower` | Follower count, returned as a string. |
| `card_info.credit_score` | Creator credit score, returned as a string. The sample value is `100`. |
| `card_info.city` | City listed on the creator's card. |
| `card_info.unique_id / card_info.short_id` | Douyin IDs for the creator. Use them to match the creator to a Douyin account. |
| `card_info.wechat / card_info.has_wechat / card_info.show_wechat` | The WeChat account on the card, a flag for whether the creator has one, and a display setting for it. |
| `card_info.phone / card_info.email` | Contact phone and email. The phone is partly masked in the sample, and the email can be an empty string. |
| `card_info.contact_status / card_info.privacy_status` | Numeric status flags for contact availability and privacy settings on the card. |
| `card_info.mcn_info` | MCN details for the creator. It is an empty object when none is returned. |
| `card_info.avatar_uri` | URL of the creator's avatar image. |

### Notes

- Get the creator ID from a search call such as [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v2/search-creator).
- If you only have a Douyin ID, convert it with [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id).
- For more profile data on the same creator, call [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info).
- Empty strings in fields like `email`, `self_intro` and `cooperation_brand` mean the card has no value for them.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Content Hot Keywords](/apis/douyin/xingtu-v2/author-content-hot-keywords): Returns trending content keywords for a Douyin creator.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-business-card-info.json`](../../../../catalog/models/douyin/xingtu-v2/author-business-card-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-business-card-info
