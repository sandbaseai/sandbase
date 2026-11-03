# Douyin Xingtu Creator Visibility Status API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-check-author-display` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get whether a specified creator can be displayed in Douyin Creator Marketplace (Xingtu) for the selected content channel. Use it to check creator availability before building a campaign shortlist.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-check-author-display", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-check-author-display', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-check-author-display", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-check-author-display", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-check-author-display` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

This API checks whether one creator can be displayed in Douyin Creator Marketplace (Xingtu) for a chosen content channel. It needs the creator's `oAuthorId` and optionally a `platform` value. It returns a `can_receive` flag with a few headline counts for the creator.

### Use cases

- Check a creator's `can_receive` flag before adding them to a campaign shortlist.
- Filter a list of candidate creator IDs down to those who can take orders on a given channel.
- Compare `follower` and `release_videos_cnt` for a creator at a glance before you request full profile data.
- Re-check a creator on `SHORT_VIDEO` and then on `LIVE_STREAMING` to see which channels they are available on.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-check-author-display" \
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
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "can_receive": true,
  "follower": 188406844,
  "link_cnt": 584605303,
  "release_videos_cnt": 1305
}
```

### Response fields

| Field | Meaning |
|---|---|
| `can_receive` | Boolean flag for the check. `true` means the creator can be displayed for the selected channel. |
| `follower` | Follower count of the creator. The sample value is 188406844. |
| `link_cnt` | A count of link-related activity for the creator. The sample value is 584605303. The response does not explain it further. |
| `release_videos_cnt` | Number of videos the creator has released. The sample value is 1305. |
| `base_resp.status_code` | Status code of the call. `0` is the value in this successful response. |
| `base_resp.status_message` | Status text. It is an empty string when the call succeeds. |

### Notes

- Set `platform` to one of `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT` or `SHORT_DRAMA`. The default is `SHORT_VIDEO`.
- Get `oAuthorId` from [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square). It is a numeric string such as `6870161898013196295`.
- Call [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info) next to get full details for a creator who passes the check.

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-check-author-display.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-check-author-display.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-check-author-display
