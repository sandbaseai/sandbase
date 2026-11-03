# Weibo User Super Topics API: pricing, parameters and code examples

`weibo/app/user-super-topics` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the list of super topics that a specified Weibo user has joined or participated in, with optional pagination support.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-super-topics", "uid": "8431518763"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-super-topics', {'uid': '8431518763'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-super-topics", {
  "uid": "8431518763"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-super-topics", sandbase.Params{
	"uid": "8431518763",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-super-topics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `page` | integer |  | Page number, starts from 1 (default 1) range 1– |

## Details

Returns the super topics page of a Weibo user as a list of layout items, such as spacers, section cards and feed posts. It needs the user's numeric ID in `uid`. Use `page` to request later pages.

### Use cases

- Read the section cards on a user's super topics page, such as the `精华帖` (essence posts) card, to see which sections the page shows.
- Collect the posts and images that appear in a user's super topics feed.
- Find location tags on posts in a user's super topics feed.
- Page through a user's super topics feed with `page` to build a full list for one account.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-super-topics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "8431518763"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |
| `page` | integer | No | Page number, starts from 1 (default 1) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "__profile_card_server__": {
    "from": "SHANHAI-SERVER"
  },
  "channelInfo": {
    "channelConfig": {
      "selectInfo": {
        "flowId": "2314758431518763",
        "pageDataType": "flow"
      }
    }
  },
  "config": "{}",
  "items": [
    {
      "category": "cell",
      "span": {
        "style": {
          "height": 10
        }
      },
      "type": "span"
    }
  ],
  "loadedInfo": "{}",
  "navInfo": "{}",
  "pageData": "{}",
  "refreshInfo": "{}"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].category` | Kind of layout item. Values seen are `cell` (spacer), `card` (section header card) and `feed` (a post). |
| `items[].data.desc / items[].data.title_extra_text` | Title and side label of a card. In the example the card reads `精华帖` with the extra text `更多` (more). |
| `items[].data.scheme` | App deep link that opens the section, for example `sinaweibo://pageinfo?containerid=_-_soul`. |
| `items[].data.actionlog.cardid / items[].data.actionlog.fid` | Identifiers of the card and of the page flow it belongs to. The `fid` value matches `channelInfo.channelConfig.selectInfo.flowId`. |
| `items[].data.attitudes_count` | Number of attitudes on a feed post. The example post shows `688`. |
| `items[].data.bmiddle_pic` | URL of the medium-size image attached to a feed post. |
| `items[].data.annotations[].place.title / items[].data.annotations[].place.poiid` | Name and ID of the place tagged on a post. The example shows `郑州` with the type `checkin`. |
| `items[].data.ad_marked` | Boolean that shows whether the feed post is marked as an ad. |
| `channelInfo.channelConfig.selectInfo.flowId` | ID of the page flow for this user. The example value is `2314758431518763`. |

### Notes

- `uid` is a string of digits, for example `8431518763`. Pass it as text.
- `page` starts at 1 and defaults to 1. Increase it to read further pages.
- Items of different `category` values are mixed in one `items` list, so check `category` before you read `data`.
- To get profile data for the same `uid`, call [Weibo User Profile Information](/apis/weibo/app/user-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/user-super-topics.json`](../../../../catalog/models/weibo/app/user-super-topics.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-super-topics
