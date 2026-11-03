# Douyin Account Fan Interest Topics API: pricing, parameters and code examples

`douyin/billboard/hot-account-fans-interest-topic-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the top ten topics that an account's followers were interested in over the last three days based on a specified user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-account-fans-interest-topic-list", "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-account-fans-interest-topic-list', {'sec_uid': 'MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-account-fans-interest-topic-list", {
  "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-account-fans-interest-topic-list", sandbase.Params{
	"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-account-fans-interest-topic-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_uid` | string | yes | User sec_id  |

## Details

Returns up to ten topics (hashtags) that followers of a Douyin account were interested in over the last three days. It needs one input, the account's `sec_uid`.

### Use cases

- Pick hashtags for new videos that match what a creator's followers already watch.
- Compare the topic mix of two creators by running the same call for each `sec_uid`.
- Track which interest topics gain or lose heat day by day using the `trends` values.
- Check the overall size of a topic before deciding whether to join it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-account-fans-interest-topic-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": [
    {
      "challenge_base_info": {
        "avg_play_cnt": 126318,
        "challenge_id": "1609320153042948",
        "challenge_name": "theshy",
        "challenge_type": 1,
        "cover_url": "https://p26-sign.douyinpic.com/aweme/200x200/image-cut-tos/a612fcb74474ed514f978…",
        "create_time": 1534767297,
        "fancy_qrcode": "https://p11-sign.douyinpic.com/aweme-qrcode/SEWOcX7703835840601917194~c5_200x200…",
        "play_cnt": 60937251819
      },
      "challenge_data": {
        "challenge_id": 1609320153042948,
        "comment_cnt": 97727,
        "hot_score": 1169147,
        "like_cnt": 897683,
        "plav_avg": 3538.751681000782,
        "play_cnt": 67890951,
        "publish_cnt": 19185
      },
      "trends": [
        {
          "datetime": 1785686400,
          "value": 878729
        }
      ]
    }
  ],
  "extra": {
    "now": 1793691105000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].challenge_base_info.challenge_name` | Name of the topic or hashtag. |
| `data[].challenge_base_info.challenge_id` | ID of the topic, returned as a string. |
| `data[].challenge_base_info.play_cnt / data[].challenge_base_info.avg_play_cnt` | Play count figures for the topic. `play_cnt` is the larger total and `avg_play_cnt` is a per-item average. |
| `data[].challenge_base_info.challenge_type` | Numeric type code of the topic. Values seen are `0`, `1` and `2`. The response does not explain what each code means. |
| `data[].challenge_base_info.create_time` | Unix timestamp in seconds for when the topic was created. |
| `data[].challenge_base_info.cover_url / data[].challenge_base_info.fancy_qrcode` | Links to the topic cover image and a QR code image. |
| `data[].challenge_data.hot_score` | Heat score for the topic. It is `0` when no recent data is returned for that topic. |
| `data[].challenge_data.publish_cnt / play_cnt / like_cnt / comment_cnt` | Recent activity counts for the topic: videos published, plays, likes and comments. All are `0` when no recent data is returned. |
| `data[].trends[].datetime / data[].trends[].value` | One point per day in the topic trend. `datetime` is a Unix timestamp in seconds. The list is empty for some topics. |

### Notes

- Send `sec_uid` as a string. Use the same account ID format shown in the example, which starts with `MS4w`.
- The `data` list has no pagination parameters. The request takes only `sec_uid`.
- Some topics return `0` in every `challenge_data` field and an empty `trends` list. Use `challenge_base_info` for those topics.
- To see which accounts the same followers like, call [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list). For search terms, call [Douyin Account Fan Interest Search Terms](/apis/douyin/billboard/hot-account-fans-interest-search-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-account-fans-interest-topic-list.json`](../../../../catalog/models/douyin/billboard/hot-account-fans-interest-topic-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-account-fans-interest-topic-list
