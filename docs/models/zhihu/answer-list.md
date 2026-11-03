# Zhihu Answer List API: pricing, parameters and code examples

`zhihu/answer-list` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get answers for a Zhihu question with sorting and pagination controls. Use it to browse responses to a known question and continue through additional answer pages.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/answer-list", "questionId": "19550225"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/answer-list', {'questionId': '19550225'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/answer-list", {
  "questionId": "19550225"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/answer-list", sandbase.Params{
	"questionId": "19550225",
})
```

Same call via the path form: `POST /v1/api/zhihu/answer-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order` | string |  | Sorting criteria for answers. one of: `_default`, `_updated`; default `"_updated"` |
| `cursor` | string |  | Pagination cursor from previous result.  |
| `offset` | integer |  | Start offset, begins with 0. default `0` |
| `sessionId` | string |  | Session ID from previous result.  |
| `questionId` | string | yes | Question ID  |

## Details

This API returns a page of answers for a Zhihu question. It needs the `questionId` of the question. You can sort the answers with `order` and continue to the next page with `cursor`, `offset` and `sessionId`.

### Use cases

- Collect the answers to a known Zhihu question for text analysis.
- Track newly updated answers on a question by sorting with `_updated`.
- Build a list of answer authors for a topic, including their follower counts and headlines.
- Page through all answers of a popular question and store each one.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/answer-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"questionId": "19550225"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `questionId` | string | Yes | Question ID |
| `cursor` | string | No | Pagination cursor from previous result. |
| `offset` | integer | No | Start offset, begins with 0. |
| `order` | string | No | Sorting criteria for answers. |
| `sessionId` | string | No | Session ID from previous result. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ad_info": {
    "ad": {
      "ad_verb": "",
      "brand": {
        "id": 0,
        "logo": "https://pic2.zhimg.com/v2-6fe322be1641f689e87bda83a4b359ee_xl.png?source=d6434ca…",
        "name": "知乎 · 盐选会员"
      },
      "category": 1,
      "click_tracks": [
        "https://sugar.zhihu.com/plutus_adreaper?bn=0&ft=8&btm=1&pdi=1536546700469087&s=0…"
      ],
      "close_track": "https://sugar.zhihu.com/plutus_adreaper?ed=CjEEfR4wM30qEmRRATYqBEYnWn8Bbm4iKxV_X…",
      "close_tracks": [
        "https://sugar.zhihu.com/plutus_adreaper?ed=CjEEfR4wM30qEmRRATYqBEYnWn8Bbm4iKxV_X…"
      ],
      "conversion_tracks": [
        "https://sugar.zhihu.com/plutus_adreaper?pf=4&atp=0&pty=1&anis=0&qmls=0&nt=0&pdi=…"
      ],
      "creatives": [
        {
          "app_promotion_url": "",
          "brand": {
            "id": 0,
            "logo": "https://pic2.zhimg.com/v2-6fe322be1641f689e87bda83a4b359ee_xl.png?source=d6434ca…",
            "name": "知乎 · 盐选会员"
          },
          "cta": {
            "value": "查看详情"
          },
          "description": "「厚地高天，堪叹古今情不尽；痴男怨女，可怜风月债难偿。」 本期长篇专题精选那些让人又爱又恨的极致拉扯。",
          "footer": {
            "value": ""
          },
          "image": "",
          "landing_url": "https://www.zhihu.com/render/zda-page/changpian02zhihu?spu=biz%3D0%26ci%3D389804…",
          "title": "盐选长篇专题：「恨海情天」必吃榜！"
        }
      ],
      "debug_tracks": [
        "https://sugar.zhihu.com/plutus_adreaper?ar=3898041&pdi=1536546700469087&ri=de68f…"
      ],
      "display_advertising_tag": true,
      "download_silent": false,
      "experiment_info": "{}"
    },
    "adjson": "{\"ads\":[{\"id\":3826269,\"ad_zone_id\":236,\"template\":\"web_word\",\"impression_tracks\"…",
    "position": 3
  },
  "data": [
    {
      "cursor": "50858d0153c20155399960038c647bfd",
      "is_jump_native": false,
      "position": 0,
      "skip_count": false,
      "target": {
        "admin_closed_comment": false,
        "allow_segment_interaction": 1,
        "annotation_action": null,
        "answer_type": "normal",
        "attached_info": "ogETCAQQAxiS69/Wor7jkh0gkaCpCZICLgoJODAzMzQyMDQ4EhMyMTAwMjQwODcyNDc4NjAyNjQyGAQi…",
        "author": {
          "avatar_url": "https://picx.zhimg.com/v2-16ca5aba7366c47a58b1f7fd910a83ba_l.jpg?source=1def8aca",
          "avatar_url_template": "https://pic1.zhimg.com/v2-16ca5aba7366c47a58b1f7fd910a83ba.jpg?source=1def8aca",
          "badge": [],
          "badge_v2": {
            "detail_badges": [],
            "icon": "",
            "merged_badges": [],
            "night_icon": "",
            "title": ""
          },
          "exposed_medal": {
            "avatar_url": "",
            "description": "",
            "medal_id": "0",
            "medal_name": ""
          },
          "follower_count": 5,
          "gender": 0,
          "headline": "人文历史建筑景点美食…"
        },
        "business_type": "normal",
        "can_comment": {
          "reason": "",
          "status": true
        }
      },
      "target_type": "answer",
      "type": "question_feed_card"
    }
  ],
  "finished_reading_filtered_count": 0,
  "paging": {
    "is_end": false,
    "need_force_login": false,
    "next": "https://www.zhihu.com/api/v4/questions/19550225/feeds?cursor=50858d0153c2015508e…",
    "page": 1
  },
  "session": {
    "id": "1793692119110262585"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One answer card in the list. Each card holds the answer in `target`. |
| `data[].cursor` | Cursor value for this card. It marks the position of the answer in the list. |
| `data[].target_type / data[].type` | Kind of item. In this response `target_type` is `answer` and `type` is `question_feed_card`. |
| `data[].target.answer_type` | Type of answer, for example `normal`. |
| `data[].target.author.headline` | The author's profile headline. |
| `data[].target.author.follower_count` | Number of followers the answer author has. |
| `data[].target.author.exposed_medal.medal_name` | Name of the medal shown on the author's profile. It is empty when the author shows no medal. |
| `data[].target.can_comment.status` | `true` when comments are allowed on the answer. |
| `paging.is_end` | `true` when there are no more pages. |
| `paging.next` | URL of the next page. It contains the `cursor` value for the next request. |
| `session.id` | Session ID for this listing. Send it back as `sessionId` when you request the next page. |
| `ad_info.ad` | An advertisement placed in the feed. It is not an answer. Skip it when you process answers. |

### Notes

- Take `questionId` from a Zhihu question URL. In `https://www.zhihu.com/question/19550225` the ID is `19550225`.
- To get the next page, pass the `cursor` value from `paging.next` and the `session.id` value as `sessionId`. Stop when `paging.is_end` is `true`.
- `order` accepts `_default` or `_updated`. The default is `_updated`.
- For full details of one answer, call [Zhihu Answer Details](/apis/zhihu/web/answer-detail). For the question itself, call [Zhihu Question Detail](/apis/zhihu/web/question-detail).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/zhihu/answer-list.json`](../../../catalog/models/zhihu/answer-list.json) · Store page: https://www.sandbase.ai/model/zhihu/answer-list
