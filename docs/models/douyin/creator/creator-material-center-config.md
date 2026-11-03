# Douyin Material Center Configuration API: pricing, parameters and code examples

`douyin/creator/creator-material-center-config` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns configuration details and settings for the Douyin material center. Provides system parameters and feature availability for account asset workflows.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-material-center-config"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-material-center-config', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-material-center-config", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-material-center-config", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-material-center-config` with the body above minus `model`.

## Details

Returns the lookup lists used by the Douyin creator material center: city codes, province and city lists, and tag codes for hot spots and hot words. It takes no input parameters. Send an empty JSON object as the request body.

### Use cases

- Map numeric city codes to city names before you read material center billboard data.
- Build a province and city picker that shows only cities with a billboard.
- Translate hot word tag codes into names such as 美食 (food) or 旅行 (travel) in a trend dashboard.
- Cache the hot spot tag groups to filter hot spot results by category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-material-center-config" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "city_code_list": [
    {
      "code": 110000,
      "name": "北京"
    }
  ],
  "hot_spot_tag_list": [
    {
      "code": [
        1004
      ],
      "name": "站内玩法"
    }
  ],
  "hot_word_tag_list": [
    {
      "code": 333,
      "name": "美食"
    }
  ],
  "province_list": [
    {
      "city_list": [
        {
          "code": 1817993,
          "has_billboard": true,
          "name": "安庆"
        }
      ],
      "province": "安徽"
    }
  ],
  "status_code": 0,
  "status_msg": "",
  "tag_list": [
    {
      "code": 333,
      "name": "美食"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `city_code_list[].code / city_code_list[].name` | Numeric code and name of a city, such as `110000` for 北京. This list is separate from the city codes in `province_list`. |
| `province_list[].province` | Name of a province or municipality, such as 安徽. |
| `province_list[].city_list[].code / province_list[].city_list[].name` | Numeric code and name of a city inside the province. |
| `province_list[].city_list[].has_billboard` | `true` if the city has a billboard, `false` if it does not. |
| `hot_spot_tag_list[].name` | Name of a hot spot tag group, such as 娱乐 (entertainment) or 话题互动. |
| `hot_spot_tag_list[].code` | List of numeric codes that belong to the hot spot tag group. |
| `hot_word_tag_list[].code / hot_word_tag_list[].name` | Numeric code and name of a hot word tag, such as `333` for 美食. |
| `tag_list[].code / tag_list[].name` | Numeric code and name of a general tag. The sample entries match the hot word tags. |
| `status_code / status_msg` | Result status of the call. `status_code` is `0` and `status_msg` is empty in the sample response. |

### Notes

- This API needs no parameters. Send `{}` as the body.
- City codes in `city_code_list` (for example `110000`) differ from those in `province_list[].city_list[]` (for example `1816670` for 北京), so match codes within the same list.
- Names are returned in Chinese.
- For ranked data, call [Douyin Creator Material Center Billboard](/apis/douyin/creator/creator-material-center-billboard) or [Douyin Creator Hot Spot Billboard](/apis/douyin/creator/creator-hot-spot-billboard).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-material-center-config.json`](../../../../catalog/models/douyin/creator/creator-material-center-config.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-material-center-config
