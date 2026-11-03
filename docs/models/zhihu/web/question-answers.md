# Zhihu Question Answers API: pricing, parameters and code examples

`zhihu/web/question-answers` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of answers for a specified Zhihu question. Supports pagination through cursor or offset parameters and sorting by time or default rank.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/question-answers", "limit": 20, "question_id": "2089412797440455404"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/question-answers', {'limit': 20, 'question_id': '2089412797440455404'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/question-answers", {
  "limit": 20,
  "question_id": "2089412797440455404"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/question-answers", sandbase.Params{
	"limit": 20,
	"question_id": "2089412797440455404",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/question-answers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of answers per page, default 5  |
| `order` | string |  | Sort order, default=default sort, updated=sort by time  |
| `cursor` | string |  | Pagination cursor for next page, extracted from response fields  |
| `offset` | integer |  | Offset, default 0  |
| `session_id` | string |  | Session ID for pagination state, extracted from response fields  |
| `question_id` | string | yes | Question ID  |

## Details

Returns a page of answers for one Zhihu question, with each answer's author details and a cursor for the next page. It needs a `question_id`, and you can sort by default rank or by update time.

### Use cases

- Collect the top answers to a Zhihu question and list the authors who wrote them.
- Compare the follower counts and credentials of the people answering a question.
- Page through all answers to a question in time order with `order` set to `updated`.
- Find answer IDs to pass to an answer detail lookup.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/question-answers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"question_id": "19550225"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `question_id` | string | Yes | Question ID |
| `cursor` | string | No | Pagination cursor for next page, extracted from response fields |
| `limit` | integer | No | Number of answers per page, default 5 |
| `offset` | integer | No | Offset, default 0 |
| `order` | string | No | Sort order, default=default sort, updated=sort by time |
| `session_id` | string | No | Session ID for pagination state, extracted from response fields |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ad_info": {
    "ad": {
      "ad_verb": "",
      "brand": {
        "id": 0,
        "logo": "https://pic1.zhimg.com/v2-6dc7efaea43f291bbafdc2b7a9eabfb7_xl.jpg?source=d6434ca…",
        "name": "知乎日报"
      },
      "category": 1,
      "click_tracks": [
        "https://sugar.zhihu.com/plutus_adreaper?qetl=0&idi=100010063&bn=0&pty=1&qmls=0&r…"
      ],
      "close_track": "https://sugar.zhihu.com/plutus_adreaper?pdi=1585291053080156&qetl=0&di=tower&qma…",
      "close_tracks": [
        "https://sugar.zhihu.com/plutus_adreaper?pdi=1585291053080156&qetl=0&di=tower&qma…"
      ],
      "conversion_tracks": [
        "https://sugar.zhihu.com/plutus_adreaper?ft=8&qmag=3&anis=0&di=tower&ri=0d727a67-…"
      ],
      "creatives": [
        {
          "app_promotion_url": "",
          "brand": {
            "id": 0,
            "logo": "https://pic1.zhimg.com/v2-6dc7efaea43f291bbafdc2b7a9eabfb7_xl.jpg?source=d6434ca…",
            "name": "知乎日报"
          },
          "cta": {
            "value": "查看详情"
          },
          "description": "有没有哪一刻，你突然读懂了那句「今月曾经照古人」？或许是站在应县木塔下抬头的那一刻，是站在安岳茗山寺凝望的那一刻。这个秋天，想邀请你一起出发——走过古建、石窟、…",
          "footer": {
            "value": ""
          },
          "image": "",
          "landing_url": "https://www.zhihu.com/parker/campaign/2085797272877523769?zh_hide_nav_bar=true&s…",
          "title": "带着今天的问题 走近一座古建 一处古迹"
        }
      ],
      "debug_tracks": [
        "https://sugar.zhihu.com/plutus_adreaper?rui=0d727a67-b463-4c9b-985a-ca0458530b1e…"
      ],
      "download_silent": false,
      "experiment_info": "{}",
      "id": 3809965
    },
    "adjson": "{\"ads\":[{\"id\":3809965,\"ad_zone_id\":236,\"template\":\"web_word\",\"impression_tracks\"…",
    "position": 3
  },
  "data": [
    {
      "cursor": "c49443398f92ae92f26a14c9ce1cdaad",
      "is_jump_native": false,
      "position": 0,
      "skip_count": false,
      "target": {
        "admin_closed_comment": false,
        "allow_segment_interaction": 1,
        "annotation_action": null,
        "answer_type": "normal",
        "attached_info": "ogETCAQQAxj369CgzOng0RsgkaCpCZICLgoJNzY0MTM3NTA4EhMxOTkxNTc5ODI1OTU4MzAzMjIzGAQi…",
        "author": {
          "avatar_url": "https://pic1.zhimg.com/v2-bfe6200c1c029aa5b8281ea360a74e23_l.jpg?source=1def8aca",
          "avatar_url_template": "https://pica.zhimg.com/v2-bfe6200c1c029aa5b8281ea360a74e23.jpg?source=1def8aca",
          "badge": [
            {
              "description": "上海交通大学 材料科学与工程博士",
              "topics": [],
              "type": "identity"
            }
          ],
          "badge_v2": {
            "detail_badges": [
              {
                "description": "新知答主",
                "detail_type": "zhihu_yearly_answerer",
                "icon": "https://picx.zhimg.com/v2-4a07bc69c4bb04444721f35b32125c75_l.png?source=32738c0c",
                "night_icon": "https://picx.zhimg.com/v2-4a07bc69c4bb04444721f35b32125c75_l.png?source=32738c0c",
                "sources": [
                  {
                    "avatar_path": "",
                    "avatar_url": "",
                    "description": "",
                    "id": "2024",
                    "name": "",
                    "priority": 2024,
                    "token": "",
                    "type": "year"
                  }
                ],
                "title": "年度新知答主",
                "type": "reward",
                "url": "https://www.zhihu.com/question/510340037"
              }
            ],
            "icon": "https://pic1.zhimg.com/v2-27bfcba90e66db79ce8768ab807e017e_l.png?source=32738c0c",
            "merged_badges": [
              {
                "description": "新知答主",
                "detail_type": "best",
                "icon": "",
                "night_icon": "",
                "sources": [],
                "title": "年度新知答主",
                "type": "best",
                "url": "https://www.zhihu.com/question/510340037"
              }
            ],
            "night_icon": "https://pic1.zhimg.com/v2-27bfcba90e66db79ce8768ab807e017e_l.png?source=32738c0c",
            "title": "新知答主"
          },
          "exposed_medal": {
            "avatar_url": "https://picx.zhimg.com/v2-f8f0ec3b12c813410945335044af18bd_l.png?source=1def8aca",
            "description": "",
            "medal_avatar_frame": "",
            "medal_id": "2062582789959169574",
            "medal_name": "高考 2026",
            "mini_avatar_url": "https://picx.zhimg.com/v2-f8f0ec3b12c813410945335044af18bd_r.png?source=1def8aca"
          },
          "follower_count": 31313,
          "gender": 1,
          "headline": "高校教师·研究生导师·多本SCI期刊编辑编委。讲论文写作、研究生培养、学术避坑的落地方法。新书《科研全攻略》筹备中，关注我，把读研读博讲成能上手的事。\n（公众号…"
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
    "next": "https://www.zhihu.com/api/v4/questions/19550225/feeds?cursor=c49443398f92ae92f2b…",
    "page": 1
  },
  "session": {
    "id": "1793692133874449509"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One feed item per answer. The `target_type` value is `answer` and the answer itself sits under `target`. |
| `data[].cursor` | Cursor string for this item. Pass it as `cursor` to continue from this position. |
| `data[].target.answer_type` | Type of the answer, for example `normal`. |
| `data[].target.can_comment.status` | Whether commenting is open on the answer. `reason` is empty when comments are allowed. |
| `data[].target.author.headline` | Short bio line the answerer set on their profile. |
| `data[].target.author.follower_count` | Number of followers the answer's author has. |
| `data[].target.author.badge[].description` | Verified identity text for the author, such as a school and degree. The list is empty when the author has no badge. |
| `data[].target.author.badge_v2.detail_badges[]` | Detailed badges of the author, with `title`, `description` and `type` such as `identity` or `reward`. |
| `data[].target.author.exposed_medal.medal_name` | Name of the medal the author shows on their profile. It is empty when no medal is shown. |
| `paging.is_end / paging.page / paging.next` | Whether this is the last page, the current page number, and the URL of the next page. The `next` URL contains the `cursor` for the following request. |
| `session.id` | Session ID for this paging run. Pass it as `session_id` on later requests. |

### Notes

- The `question_id` is the number at the end of a Zhihu question URL, such as `19550225`. [Zhihu Question Detail](/apis/zhihu/web/question-detail) returns details for the same question.
- To get the next page, send the `cursor` from `paging.next` (or from the last item in `data`) together with `session.id` as `session_id`. Stop when `paging.is_end` is `true`.
- The response also carries an `ad_info` block with an ad entry. You can ignore it when you only need answers.
- To read one answer in full, call [Zhihu Answer Details](/apis/zhihu/web/answer-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/question-answers.json`](../../../../catalog/models/zhihu/web/question-answers.json) · Store page: https://www.sandbase.ai/model/zhihu/web/question-answers
