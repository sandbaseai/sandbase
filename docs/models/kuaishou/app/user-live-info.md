# Kuaishou User Broadcast Details API: pricing, parameters and code examples

`kuaishou/app/user-live-info` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns broadcast information and stream status for a specified Kuaishou account. Requests target a creator profile using the unique user identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/user-live-info", "user_id": "3795214411"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/user-live-info', {'user_id': '3795214411'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/user-live-info", {
  "user_id": "3795214411"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/user-live-info", sandbase.Params{
	"user_id": "3795214411",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/user-live-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | 用户ID/User ID  |

## Details

This API returns the live status and a short activity summary for one Kuaishou account. It needs the numeric `user_id` of the creator.

### Use cases

- Check whether a Kuaishou creator is streaming right now using the `isLive` flag.
- Track how many videos a creator has posted by reading `photoCount` on a schedule.
- Filter a list of creator IDs down to the ones that are live before you fetch more data.
- Confirm that a lookup for a `user_id` succeeded by reading the `result` value.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/user-live-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3795214411"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "debug_id": "36c5a730",
  "debug_info": "gAAAAABq6Y77fQhzwkkN1X2BZxqssPoHtERg4092vXpG5Nv1xPwYXM2t_9PpgPb6KX17A8Jcs-2zGXeJ…",
  "dynamicIconV2": {
    "isLive": false,
    "photoCount": 683,
    "result": 1,
    "type": 3
  },
  "host-name": "public-bjmt-c56-kce-node76.idchb1az4.hb1.kwaidc.com",
  "llsid": 2010206515696162481,
  "result": 1,
  "shieldNextPhoto": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `dynamicIconV2.isLive` | Shows whether the account is broadcasting right now. In the sample it is `false`. |
| `dynamicIconV2.photoCount` | Number of posts counted for the account. The sample shows `683`. |
| `dynamicIconV2.type` | Numeric type code for the profile icon state. The sample shows `3`. The response does not explain what each code means. |
| `dynamicIconV2.result / result` | Result codes for the icon block and the whole request. The sample shows `1` for both. |
| `shieldNextPhoto` | Boolean flag in the response. The sample shows `false`. The response does not explain its effect. |
| `llsid` | Large numeric ID attached to this response. It looks like a request or session identifier. |
| `debug_id / debug_info / host-name` | Diagnostic values for the request and the server that handled it. Most integrations can ignore them. |

### Notes

- Pass `user_id` as a string, for example `3795214411`.
- If you only have a username or profile link, call [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id) first to get the ID.
- To see past streams for the same account, call [Kuaishou User Broadcast Replay](/apis/kuaishou/web/user-live-replay).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/user-live-info.json`](../../../../catalog/models/kuaishou/app/user-live-info.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/user-live-info
