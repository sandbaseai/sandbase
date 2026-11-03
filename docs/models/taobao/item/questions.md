# Taobao Product Questions API: pricing, parameters and code examples

`taobao/item/questions` · data API · Taobao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get buyer questions and answers for a Taobao or Tmall product by item ID, page by page.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "taobao/item/questions", "itemId": "672400567264"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('taobao/item/questions', {'itemId': '672400567264'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("taobao/item/questions", {
  "itemId": "672400567264"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "taobao/item/questions", sandbase.Params{
	"itemId": "672400567264",
})
```

Same call via the path form: `POST /v1/api/taobao/item/questions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `itemId` | string | yes | Unique product identifier on Taobao/Tmall (item ID).  |

## Details

This API returns the buyer questions and answers posted for a Taobao or Tmall product. It needs the product `itemId` and returns one page of questions at a time, along with product info and the total question count.

### Use cases

- Find the most common buyer concerns about a phone case, such as yellowing or dust, before you write a listing.
- Collect real buyer answers to track what customers say about a competitor's product.
- Rank the question tags by `count` to see which product features buyers ask about most.
- Export questions and answers for a product to build an FAQ dataset.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/taobao/item/questions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "672400567264"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | Unique product identifier on Taobao/Tmall (item ID). |
| `page` | integer | No | Page number for pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "balaVersion": "3.0",
  "dataSuccess": "true",
  "experienceFlag": "false",
  "item": {
    "buyerCount": null,
    "itemPic": "https://gw.alicdn.com/tfscom/tuitui/i1/1659916565/O1CN01AahvcyWAMwC2vH2e_!!46116…",
    "itemTitle": "图拉斯C1新款iPhone18手机壳适用苹果17ProMax透明16新14Pro磁吸外壳高级保护13pm套14防摔12超薄全包无毒p",
    "itemUrl": "https://a.m.taobao.com/i672400567264.htm",
    "questionCount": "3050",
    "tags": {
      "list": [
        {
          "count": "162",
          "keyword": "发黄",
          "propertyId": "100003264"
        }
      ]
    }
  },
  "list": [
    [
      {
        "cardType": "2",
        "clusterId": "587432526622",
        "clusterName": null,
        "feedType": "200",
        "gmtCreate": "1793345025000",
        "gmtModified": "1793637360000",
        "id": "587432526622",
        "similarCount": null,
        "similarFeeds": null,
        "subFeeds": [
          {
            "answerType": "1",
            "elements": [],
            "feedType": "151",
            "gmtCreate": "1793346523000",
            "gmtModified": null,
            "id": "587172635816",
            "title": "手机壳倒是还好，就是太光滑了，溜手，摔了好几次了。",
            "user": {
              "userLogo": "https://wwc.alicdn.com/avatar/getAvatar.do?type=sns&width=64&height=64&userIdStr…",
              "userNick": "娜***",
              "userScore": null,
              "userUrl": "https://h5.m.taobao.com/account/index.html?userId=Xm9IOmv0MF9zMHlevFIYOmc0vC8YOm…"
            }
          }
        ],
        "subFeedsCount": "4",
        "targetUrl": "https://web.m.taobao.com/app/mtb/ask-everyone/detail?disableNav=YES&from=answer&…"
      }
    ]
  ],
  "pagination": {
    "direction": "1",
    "hasMore": "true",
    "pageNum": "2",
    "pageSize": "10"
  },
  "questionStatus": {
    "closeQuestion": "false"
  },
  "questionWords": [],
  "success": "true",
  "total": "3050"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `total / item.questionCount` | Total number of questions for the product. Both values are strings. |
| `item.itemTitle / item.itemUrl / item.itemPic` | Title, mobile page link and main image of the product. |
| `item.tags.list[].keyword / item.tags.list[].count` | A keyword buyers mention in their questions and the number of questions that match it. |
| `list[][].id` | ID of the question. |
| `list[][].title` | Text of the question. |
| `list[][].gmtCreate / list[][].gmtModified` | Time the question was created and last modified, as millisecond timestamps in a string. |
| `list[][].subFeedsCount` | Number of answers attached to the question. This can be higher than the number of answers in `subFeeds`. |
| `list[][].subFeeds[].title` | Text of an answer to the question. |
| `list[][].subFeeds[].user.userNick` | Masked nickname of the person who wrote the answer. |
| `list[][].targetUrl` | Link to the question detail page on Taobao. |

### Notes

- Use `page` to move through results. The `pagination` object shows `pageNum`, `pageSize` and `hasMore`. Keep requesting the next page while `hasMore` is `true`.
- Each entry of `list` is itself an array that holds the question object.
- To get the `itemId`, use the number in the product link, such as `672400567264` in `https://a.m.taobao.com/i672400567264.htm`. You can also find items with [Taobao Product Search](/apis/taobao/search/items).
- For buyer reviews of the same product, call [Taobao Product Reviews](/apis/taobao/item/reviews). For price and specs, call [Taobao Product Details](/apis/taobao/item/detail).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/taobao/item/questions.json`](../../../../catalog/models/taobao/item/questions.json) · Store page: https://www.sandbase.ai/model/taobao/item/questions
