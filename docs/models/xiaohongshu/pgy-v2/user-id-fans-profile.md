# Xiaohongshu Pugongying Follower Distribution API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/user-id-fans-profile` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Xiaohongshu Pugongying follower profile data for a known creator. Use it to review a creator's audience profile during campaign planning.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/user-id-fans-profile", "userId": "5a73c5fa4eacab4c4ccc9778"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/user-id-fans-profile', {'userId': '5a73c5fa4eacab4c4ccc9778'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/user-id-fans-profile", {
  "userId": "5a73c5fa4eacab4c4ccc9778"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/user-id-fans-profile", sandbase.Params{
	"userId": "5a73c5fa4eacab4c4ccc9778",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/user-id-fans-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | KOL's user ID.  |

## Details

Returns the follower profile of one Xiaohongshu Pugongying creator: age, gender, city, province, device and interest breakdowns. It needs the creator's `userId`.

### Use cases

- Check whether a creator's audience matches the target age group of a campaign.
- Compare the share of female and male followers before booking a creator.
- Find the top provinces and cities of a creator's followers to plan regional promotions.
- Review follower device brands and interests to judge product fit.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/user-id-fans-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "5a73c5fa4eacab4c4ccc9778"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | KOL's user ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ages": [
    {
      "group": "<18",
      "percent": 0.15892918714077067
    }
  ],
  "cities": [
    {
      "name": "上海",
      "percent": 0.02496880709359685
    }
  ],
  "dateKey": "2026-11-02",
  "devices": [
    {
      "desc": "苹果",
      "name": "apple inc.",
      "percent": 0.42812300727342967
    }
  ],
  "gender": {
    "female": 0.9059612909155316,
    "male": 0.09403870908446832
  },
  "interests": [
    {
      "name": "娱乐",
      "percent": 0.1204139831281711
    }
  ],
  "provinces": [
    {
      "name": "广东",
      "percent": 0.10229585835775959
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `ages[].group / ages[].percent` | An age bucket such as `18-24` and the share of followers in it. |
| `gender.female / gender.male` | Share of followers by gender. The two values add up to 1. |
| `cities[].name / cities[].percent` | A follower city and the share of followers who live there. |
| `provinces[].name / provinces[].percent` | A follower province and the share of followers who live there. |
| `interests[].name / interests[].percent` | An interest category of the followers, such as food, and its share. |
| `devices[].name / devices[].desc / devices[].percent` | Device brand as a raw name and a short label, with the share of followers using it. |
| `dateKey` | Date string for the profile snapshot, in `YYYY-MM-DD` format. |

### Notes

- `percent` and gender values are fractions between 0 and 1. For example, `0.39` means 39%.
- City, province, interest and device labels are mostly Chinese text, as returned by the platform.
- To find a creator's `userId`, use [Xiaohongshu Pugongying Creator Search](/apis/xiaohongshu/pgy-v2/blogger-v2).
- For headline follower numbers, call [Xiaohongshu Pugongying Follower Summary](/apis/xiaohongshu/pgy-v2/data-v3-fans-summary). For change over time, call [Xiaohongshu Pugongying Follower Growth History](/apis/xiaohongshu/pgy-v2/user-id-fans-overall-new-history).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/user-id-fans-profile.json`](../../../../catalog/models/xiaohongshu/pgy-v2/user-id-fans-profile.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/user-id-fans-profile
