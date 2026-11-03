# Douyin XingTu kolId by Douyin ID API: pricing, parameters and code examples

`douyin/xingtu-v2/xingtu-kolid-by-unique-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns Xingtu author profile details and platform identifiers matching a specified Douyin unique identifier.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/xingtu-kolid-by-unique-id", "unique_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/xingtu-kolid-by-unique-id', {'unique_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/xingtu-kolid-by-unique-id", {
  "unique_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/xingtu-kolid-by-unique-id", sandbase.Params{
	"unique_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/xingtu-kolid-by-unique-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `unique_id` | string | yes | Douyin unique_id  |

## Details

Returns the Xingtu author record that matches a Douyin `unique_id`. The response has the Xingtu author `id`, the `core_user_id`, the nickname, the avatar URL and a content tag. The only input is `unique_id`.

### Use cases

- Convert a Douyin `unique_id` into the Xingtu author `id` before calling other Xingtu author APIs.
- Check the `tag` and `nick_name` of a creator before adding them to a campaign list.
- Match a list of Douyin handles to Xingtu authors and store the `core_user_id` for each one.
- Get the avatar URL of a Xingtu author for a creator roster.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/xingtu-kolid-by-unique-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"unique_id": "dyczxzs"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `unique_id` | string | Yes | Douyin unique_id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "avatar_uri": "https://p11.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_3beaaeb52…",
  "base_resp": {
    "status_code": 0,
    "status_message": "Success"
  },
  "core_user_id": "92769419069",
  "finish_rate_ovr": 0,
  "hot_list_ranks": [],
  "id": "6870164585236660237",
  "nick_name": "抖音作者助手",
  "tag": "教育培训"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | Xingtu author ID as a string. Use this value as the author ID in other Xingtu author APIs. |
| `core_user_id` | Core user ID of the account, returned as a string. |
| `nick_name` | Display name of the creator. |
| `tag` | Content category label of the creator. The example value is `教育培训` (education and training). |
| `avatar_uri` | URL of the creator's avatar image. |
| `finish_rate_ovr` | Numeric completion rate value. It is `0` in the example response, and the response does not state its unit. |
| `hot_list_ranks` | List of hot list rankings for the creator. It is empty in the example response. |
| `base_resp.status_code / base_resp.status_message` | Result status of the lookup. `0` and `Success` mean the call worked. |

### Notes

- `unique_id` is the Douyin account ID, for example `dyczxzs`.
- `id` and `core_user_id` are long numeric values returned as strings. Keep them as strings to avoid rounding.
- Pass the returned `id` to [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info) for fuller profile data.
- Use [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info) to get business card details for the same author.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/xingtu-kolid-by-unique-id.json`](../../../../catalog/models/douyin/xingtu-v2/xingtu-kolid-by-unique-id.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/xingtu-kolid-by-unique-id
