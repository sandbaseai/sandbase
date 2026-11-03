# Bilibili Creator View and Like Statistics API: pricing, parameters and code examples

`bilibili/web/user-up-stat` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns total video view and like counts for a specified Bilibili creator account. Lookup requires the user unique identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/user-up-stat", "uid": "178360345"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/user-up-stat', {'uid': '178360345'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/user-up-stat", {
  "uid": "178360345"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/user-up-stat", sandbase.Params{
	"uid": "178360345",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/user-up-stat` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User UID  |

## Details

Returns total video views, article views, and total likes for one Bilibili creator account. It needs the creator's numeric `uid` as input.

### Use cases

- Compare total video views and likes across several Bilibili creators before picking partners.
- Record the `archive.view` and `likes` totals on a schedule to chart growth for one account.
- Add creator-level view and like totals to a dashboard next to profile and follower data.
- Screen a list of creator accounts by total reach before pulling their individual videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/user-up-stat" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "178360345"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User UID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "archive": {
    "enable_vt": 0,
    "view": 49024,
    "vt": 0
  },
  "article": {
    "view": 0
  },
  "likes": 640
}
```

### Response fields

| Field | Meaning |
|---|---|
| `archive.view` | Total view count across the creator's videos. |
| `likes` | Total like count for the creator account. |
| `article.view` | Total view count across the creator's articles. It is `0` for this account. |
| `archive.enable_vt` | Flag next to the video totals. The value is `0` here. The key name does not say more, so treat it as an on/off flag. |
| `archive.vt` | Extra counter in the `archive` object. It is `0` here and the response does not explain it. |

### Notes

- Pass the creator's numeric ID as a string in `uid`, for example `178360345`.
- The response has no name or follower fields. Call [Bilibili User Profile](/apis/bilibili/web/user-profile) for profile details and [Bilibili User Relation Statistics](/apis/bilibili/web/user-relation-stat) for relation counts.
- If you only have a profile link or name, use [Bilibili User ID Extraction](/apis/bilibili/web/get-user-id) to find the `uid`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/user-up-stat.json`](../../../../catalog/models/bilibili/web/user-up-stat.json) · Store page: https://www.sandbase.ai/model/bilibili/web/user-up-stat
