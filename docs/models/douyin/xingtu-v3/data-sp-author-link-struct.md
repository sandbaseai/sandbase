# Douyin Xingtu Creator Link Structure API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-author-link-struct` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) creator-link structure data for a specified creator and content channel. Use it to compare creator link structures during performance research.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-link-struct", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-link-struct', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-link-struct", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-link-struct", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-link-struct` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns the link structure for one creator on Douyin Creator Marketplace (Xingtu). It needs the creator's `oAuthorId` and can take a `platform` value to pick the content channel.

### Use cases

- Compare how a creator's link stages split between steps 1 to 4 before booking a campaign.
- Check the creator's link type label, such as `种草`, to match a creator to a seeding goal.
- Rank several candidate creators by their step proportions and the `relative_ratio` value in step 5.
- Run the same creator across `SHORT_VIDEO` and `LIVE_STREAMING` to see how the structure differs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-link-struct" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `platform` | string | No | Platform type. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "author_link_type": "种草",
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "link_struct": {
    "1": {
      "proportion": 0.16304054463905537,
      "value": 95314367
    },
    "2": {
      "proportion": 0.5087374275836838,
      "value": 297410598
    },
    "3": {
      "proportion": 0.32822010340197,
      "value": 191879213
    },
    "4": {
      "proportion": 1.9243752908618417e-06,
      "value": 1125
    },
    "5": {
      "rank_percent": 0,
      "relative_ratio": -0.0208,
      "value": 584605303
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `author_link_type` | Text label for the creator's link type. The sample value is `种草`. |
| `link_struct` | Object keyed by step number from `1` to `5`. Each key holds the numbers for that step. |
| `link_struct.1 / link_struct.2 / link_struct.3 / link_struct.4` | Each step has a `value` count and a `proportion`. In the sample the `proportion` values of steps 1 to 4 add up to about 1. |
| `link_struct.1.proportion / link_struct.2.proportion / link_struct.3.proportion / link_struct.4.proportion` | Share of the total that each step holds, as a decimal between 0 and 1. In the sample, step 2 is the largest at about 0.51. |
| `link_struct.1.value / link_struct.2.value / link_struct.3.value / link_struct.4.value` | Raw count for each step. In the sample, step 2 is 297410598 and step 4 is 1125. |
| `link_struct.5.value` | Count for step 5. In the sample it equals the sum of the values in steps 1 to 3. |
| `link_struct.5.relative_ratio` | Relative ratio for step 5. The sample value is `-0.0208`, a negative number. |
| `link_struct.5.rank_percent` | Rank percent for step 5. The sample value is `0`. |
| `base_resp.status_code / base_resp.status_message` | Call status. `0` with an empty message means the call succeeded. |

### Notes

- Pass `platform` as one of `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT` or `SHORT_DRAMA`. It defaults to `SHORT_VIDEO`.
- Find an `oAuthorId` with [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- For the related link metrics of the same creator, call [Douyin Xingtu Creator Link Metrics](/apis/douyin/xingtu-v3/data-sp-author-link-info).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-link-struct.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-link-struct.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-link-struct
