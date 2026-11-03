# TikTok Tag Detail API: pricing, parameters and code examples

`tiktok/web/tag-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves detail information for a specified TikTok hashtag via the web platform based on the provided tag name parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/tag-detail", "tag_name": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/tag-detail', {'tag_name': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/tag-detail", {
  "tag_name": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/tag-detail", sandbase.Params{
	"tag_name": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/tag-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tag_name` | string | yes | Tag name  |

## Details

Returns detail data for one TikTok hashtag, including its ID, title, and view and video counts. It needs one input: the hashtag name in `tag_name`, without the `#` sign.

### Use cases

- Track how many views and videos a hashtag such as `openai` has gathered.
- Convert a hashtag name into its numeric challenge ID for use in other tools.
- Check whether a hashtag is marked as commercial before using it in a campaign.
- Read the share title and description TikTok shows for a hashtag page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/tag-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tag_name": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag_name` | string | Yes | Tag name |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "challengeInfo": {
    "challenge": {
      "coverLarger": "",
      "coverMedium": "",
      "coverThumb": "",
      "desc": "",
      "id": "72988465",
      "isCommerce": false,
      "profileLarger": "",
      "profileMedium": "",
      "profileThumb": "",
      "stats": {
        "videoCount": 0,
        "viewCount": 9100000000
      },
      "title": "openai"
    },
    "challengeAnnouncement": {
      "body": "",
      "title": ""
    },
    "stats": {
      "videoCount": 0,
      "viewCount": 9100000000
    },
    "statsV2": {
      "videoCount": "377014",
      "viewCount": "9077075330"
    }
  },
  "cookie": "tt_chain…",
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103154429F2959E7F1D151604ED12",
    "now": 1793691870000
  },
  "log_pb": {
    "impr_id": "20261103154429F2959E7F1D151604ED12"
  },
  "shareMeta": {
    "desc": "Watch awesome short videos created with trending hashtag #openai",
    "title": "#openai on TikTok"
  },
  "statusCode": 0,
  "status_code": 0,
  "status_msg": "",
  "tt_chain_token": "0k5cdiqY…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `challengeInfo.challenge.id` | Numeric ID of the hashtag (challenge) as a string. |
| `challengeInfo.challenge.title` | The hashtag name, shown without the `#` sign. |
| `challengeInfo.challenge.isCommerce` | Boolean flag that shows whether the hashtag is marked as commercial. |
| `challengeInfo.challenge.desc` | Hashtag description text. It is an empty string for this tag. |
| `challengeInfo.statsV2.viewCount / challengeInfo.statsV2.videoCount` | Total views and total videos for the hashtag, returned as numeric strings. Prefer these over the `stats` fields, because `stats.videoCount` is `0` in this response. |
| `challengeInfo.stats.viewCount / challengeInfo.stats.videoCount` | The same counts as plain numbers. `viewCount` looks rounded, and `videoCount` is `0` here. |
| `challengeInfo.challenge.coverLarger / coverMedium / coverThumb` | Cover image URLs in three sizes. They are empty strings for this tag. |
| `shareMeta.title / shareMeta.desc` | Title and description text TikTok uses when someone shares the hashtag page. |
| `statusCode / status_msg` | Request status. `0` in `statusCode` means the call worked, and `status_msg` holds a message if there is one. |

### Notes

- Pass the hashtag name as plain text in `tag_name`, for example `openai`.
- Use `challengeInfo.statsV2` for counts, since the values in `challengeInfo.stats` can be `0` or rounded.
- To list videos under a hashtag, call [TikTok Tag Posts](/apis/tiktok/web/tag-post).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/tag-detail.json`](../../../../catalog/models/tiktok/web/tag-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/web/tag-detail
