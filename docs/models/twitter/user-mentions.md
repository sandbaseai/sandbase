# X (Twitter) User Mentions API: pricing, parameters and code examples

`twitter/user-mentions` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.003 per call · **Modes:** sync

Recent tweets that mention a user by username, with optional time range and cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.003**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/user-mentions", "userName": "NASA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/user-mentions', {'userName': 'NASA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/user-mentions", {
  "userName": "NASA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/user-mentions", sandbase.Params{
	"userName": "NASA",
})
```

Same call via the path form: `POST /v1/api/twitter/user-mentions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | The cursor to paginate through the results. First page is empty.  |
| `userName` | string | yes | The user screen name to get mentions for.  |
| `sinceTime` | integer |  | On or after a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. range 0–9223372036854776000 |
| `untilTime` | integer |  | Before a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. range 0–9223372036854776000 |

## Details

Returns recent tweets that mention a given X (Twitter) user. Each tweet includes its text, author, engagement counts, reply context and the users it mentions. The only required input is `userName`, the screen name without the @ sign.

### Use cases

- Track public replies and mentions of a brand or agency account such as `NASA`.
- Collect mention text for sentiment or topic analysis over a chosen time window.
- Find high-view posts that tag an account so a team can respond to them.
- Build a feed of links shared in tweets that mention a user, using `entities.urls`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/user-mentions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userName": "NASA"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userName` | string | Yes | The user screen name to get mentions for. |
| `cursor` | string | No | The cursor to paginate through the results. First page is empty. |
| `sinceTime` | integer | No | On or after a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. |
| `untilTime` | integer | No | Before a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "has_next_page": true,
  "msg": "success",
  "next_cursor": "DAADDAABCgABHWLxy4mbQVkKAAIdYutU-ZuRPQAIAAIAAAACCAADAAAAAAgABAAAAAAKAAUdYvROi0An…",
  "status": "success",
  "tweets": [
    {
      "article": null,
      "author": {
        "affiliatesHighlightedLabel": {},
        "automatedBy": null,
        "canDm": true,
        "canMediaTag": true,
        "coverPicture": "",
        "createdAt": "Sun Oct 03 21:27:35 +0000 2021",
        "description": "",
        "entities": {
          "description": {
            "urls": []
          },
          "url": {}
        }
      },
      "bookmarkCount": 0,
      "card": {
        "binding_values": [
          {
            "key": "photo_image_full_size_large",
            "value": {
              "image_value": {
                "height": 419,
                "url": "https://pbs.twimg.com/card_img/2117520633382965248/Mw80kojC?format=jpg&name=800x…",
                "width": 800
              }
            }
          }
        ],
        "card_platform": {
          "platform": {
            "audience": {
              "name": "production"
            },
            "device": {
              "name": "iPhone",
              "version": "13"
            }
          }
        },
        "name": "summary_large_image",
        "url": "https://t.co/FZqZ4fF9Ta",
        "user_refs_results": []
      },
      "communityInfo": null,
      "conversationId": "2116999144376340883",
      "createdAt": "Tue Nov 03 07:33:54 +0000 2026",
      "displayTextRange": [
        6
      ],
      "entities": {
        "urls": [
          {
            "display_url": "tiktok.com/t/ZPLuYSyTT/",
            "expanded_url": "https://www.tiktok.com/t/ZPLuYSyTT/",
            "indices": [
              6
            ],
            "url": "https://t.co/FZqZ4fF9Ta"
          }
        ],
        "user_mentions": [
          {
            "id_str": "11348282",
            "indices": [
              0
            ],
            "name": "NASA",
            "screen_name": "NASA"
          }
        ]
      },
      "extendedEntities": {},
      "id": "2117520631306862937",
      "inReplyToId": "2117516836212462064"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tweets[]` | List of tweets that mention the requested user, newest first in the sample. |
| `tweets[].id / tweets[].url / tweets[].twitterUrl` | Tweet ID and the links to the tweet on x.com and twitter.com. |
| `tweets[].text` | Full text of the tweet, including the leading @mentions and shortened t.co links. |
| `tweets[].createdAt` | Time the tweet was posted, as a string like `Tue Nov 03 07:33:54 +0000 2026`. |
| `tweets[].likeCount / tweets[].replyCount / tweets[].retweetCount / tweets[].quoteCount / tweets[].bookmarkCount / tweets[].viewCount` | Engagement counts for the tweet. |
| `tweets[].isReply / tweets[].inReplyToId / tweets[].inReplyToUsername` | Shows whether the tweet is a reply, and gives the ID and username of the tweet or user it answers. |
| `tweets[].conversationId` | ID of the first tweet in the conversation thread this tweet belongs to. |
| `tweets[].entities.user_mentions[]` | Users mentioned in the tweet, with `id_str`, `name` and `screen_name`. |
| `tweets[].entities.urls[]` | Links in the tweet, with the short `url`, the `expanded_url` and the `display_url`. |
| `has_next_page / next_cursor` | `has_next_page` says whether more results exist. `next_cursor` is the value to send as `cursor` for the next page. |

### Notes

- Pass `userName` as the plain screen name, for example `NASA`.
- For the first page, leave `cursor` empty. For the next page, send the `next_cursor` value as `cursor` while `has_next_page` is `true`.
- Use `sinceTime` (on or after) and `untilTime` (before) as unix timestamps in seconds to limit the time range.
- To read a full conversation for a tweet, pass its `id` to [Twitter Post Comments](/apis/twitter/post-comments) or [X / Twitter Tweet Thread](/apis/twitter/thread).

### Pricing

Billed at the actual cost of each call, about $0.003 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/user-mentions.json`](../../../catalog/models/twitter/user-mentions.json) · Store page: https://www.sandbase.ai/model/twitter/user-mentions
