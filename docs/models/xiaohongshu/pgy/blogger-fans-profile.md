# Xiaohongshu (RED) PGY Blogger Fan Profile API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-fans-profile` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns demographic distributions for a blogger's follower base, including gender, age, region, interests, and device types, filtered by user ID.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-fans-profile", "user_id": "60b137080000000001000301"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-fans-profile', {'user_id': '60b137080000000001000301'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-fans-profile", {
  "user_id": "60b137080000000001000301"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-fans-profile", sandbase.Params{
	"user_id": "60b137080000000001000301",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-fans-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Blogger user ID  |

## Details

Returns the follower demographic breakdown for one Xiaohongshu (RED) blogger on the PGY platform. It covers gender, age, city, province, interest and device shares. The only input is the blogger's `user_id`.

### Use cases

- Check whether a blogger's followers match the age and gender of your target buyers before you book a campaign.
- Compare the top provinces and cities of a blogger's audience against your sales regions.
- Pick bloggers whose followers mostly use a given phone brand, such as Apple or Huawei.
- Match a blogger's top follower interests to your product category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-fans-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "60b137080000000001000301"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Blogger user ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "ages": [
      {
        "group": "<18",
        "percent": 0.030148218227688428
      }
    ],
    "cities": [
      {
        "name": "北京",
        "percent": 0.05891793379212795
      }
    ],
    "dateKey": "2026-11-02",
    "devices": [
      {
        "desc": "苹果",
        "name": "apple inc.",
        "percent": 0.43350383631713557
      }
    ],
    "gender": {
      "female": 0.42393566698202456,
      "male": 0.5760643330179754
    },
    "interests": [
      {
        "name": "生活记录",
        "percent": 0.08384622079649869
      }
    ],
    "provinces": [
      {
        "name": "广东",
        "percent": 0.12422816418681827
      }
    ]
  },
  "guid": null,
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.gender.female / data.gender.male` | Share of followers by gender. The two values add up to 1. |
| `data.ages[].group` | Age bucket label, for example `<18`, `18-24` or `25-34`. |
| `data.ages[].percent` | Share of followers in that age bucket, as a fraction between 0 and 1. |
| `data.provinces[].name / data.cities[].name` | Province or city name of the followers, in Chinese. |
| `data.provinces[].percent / data.cities[].percent` | Share of followers located in that province or city, as a fraction between 0 and 1. |
| `data.interests[].name` | Interest category of the followers, in Chinese, such as `生活记录` (life records). |
| `data.interests[].percent` | Share of followers tied to that interest, as a fraction between 0 and 1. |
| `data.devices[].name / data.devices[].desc` | Device brand. `name` is the English brand key and `desc` is the Chinese label. |
| `data.devices[].percent` | Share of followers using that device brand, as a fraction between 0 and 1. |
| `data.dateKey` | Date string in `YYYY-MM-DD` format attached to this profile. |

### Notes

- All `percent` values and gender values are fractions, so `0.36` means 36%.
- Lists such as `ages`, `cities` and `devices` come back as arrays of items with a `percent` value.
- Find a blogger's `user_id` with [Xiaohongshu (RED) PGY Blogger Search](/apis/xiaohongshu/pgy/blogger-list).
- For follower counts over time, call [Xiaohongshu (RED) PGY Blogger Fan History](/apis/xiaohongshu/pgy/blogger-fans-history).

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/apis/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Data Summary](/apis/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Details](/apis/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-fans-profile.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-fans-profile.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-fans-profile
