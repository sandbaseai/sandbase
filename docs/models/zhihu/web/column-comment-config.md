# Zhihu Column Comment Configuration API: pricing, parameters and code examples

`zhihu/web/column-comment-config` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comment settings and options for a Zhihu column article based on the provided article identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/column-comment-config", "article_id": "669214677"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/column-comment-config', {'article_id': '669214677'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/column-comment-config", {
  "article_id": "669214677"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/column-comment-config", sandbase.Params{
	"article_id": "669214677",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/column-comment-config` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `article_id` | string | yes | Article ID  |

## Details

Returns the comment box settings for a Zhihu column article. It shows whether replies are allowed, which emoji and picture options are available, and which extra toggles appear. It needs the numeric `article_id` of the article.

### Use cases

- Check whether the comment area of a column article is closed before you plan to collect its comments.
- Read the placeholder text to see why a comment box is disabled.
- Check which emoji, picture and voice options the comment box offers for an article.
- List the extra toggles shown next to the comment box, such as syncing a comment to Zhihu pins.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/column-comment-config" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"article_id": "669214677"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `article_id` | string | Yes | Article ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attached_info": "",
  "can_reply": false,
  "can_segment_reply": false,
  "comment_identities": [],
  "dialog": null,
  "disable_emoticon": false,
  "disable_picture": false,
  "is_anonymous": false,
  "permission": {
    "emoji": {
      "have": true,
      "is_vip_privilege": false,
      "toast": "会员或 Lv.4 以上可解锁"
    },
    "picture": {
      "have": true,
      "is_vip_privilege": true,
      "toast": "会员或 Lv.7 以上可解锁"
    },
    "voice": {
      "have": false,
      "is_vip_privilege": false,
      "toast": ""
    }
  },
  "picture_max_count": 1,
  "place_holder": "评论区已关闭",
  "place_holder_strategy": "normal"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `place_holder` | Text shown in the comment input box. In this response it is `评论区已关闭`, which means the comment area is closed. |
| `can_reply / can_segment_reply` | Flags that show whether replies to the article, and replies to a segment of it, are allowed. Both are `false` in this response. |
| `disable_emoticon / disable_picture` | Flags that show whether emoji or pictures are turned off for comments on this article. |
| `is_anonymous` | Flag that shows whether the comment is posted anonymously. |
| `permission.emoji.have / permission.picture.have / permission.voice.have` | Whether each input type is available in the comment box. Voice is `false` in this response. |
| `permission.picture.is_vip_privilege` | Flag that shows whether picture comments are a member privilege. It is `true` in this response. |
| `permission.emoji.toast / permission.picture.toast` | Message shown to users who cannot use the feature yet. It names the membership or level needed to use it. |
| `picture_max_count` | Maximum number of pictures allowed in one comment. The value is `1` in this response. |
| `setting[].id / setting[].title` | Identifier and display label of an extra option in the comment box. The sample shows `publish_sync_pin` with the title `同步到想法`. |
| `setting[].disable / setting[].selected` | Whether the option is switched off for the user and whether it is selected. |

### Notes

- `article_id` is the numeric ID of a column article, such as `669214677`. Get it from [Zhihu Column Articles](/apis/zhihu/web/column-articles) or [Zhihu Column Article Detail](/apis/zhihu/web/column-article-detail).
- The response has no comment list. Fields such as `comment_identities` can be empty and `dialog` can be `null`.
- The text in `place_holder`, `toast` and `title` comes back in Chinese.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/column-comment-config.json`](../../../../catalog/models/zhihu/web/column-comment-config.json) · Store page: https://www.sandbase.ai/model/zhihu/web/column-comment-config
