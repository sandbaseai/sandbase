# Douyin Xingtu Creator Channel Metrics API: pricing, parameters and code examples

`douyin/xingtu-v3/author-author-platform-channel-info-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) channel information for a specified creator and content format. Use it to compare a creator's short-video, live, image-text, or short-drama presence.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/author-author-platform-channel-info-v2", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/author-author-platform-channel-info-v2', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/author-author-platform-channel-info-v2", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/author-author-platform-channel-info-v2", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/author-author-platform-channel-info-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns channel information for one creator on Douyin Creator Marketplace (Xingtu), for a chosen content format. It needs the creator's `oAuthorId`, and `platform` is optional. In the sample call, the response held a status block and the creator's self introduction.

### Use cases

- Read a creator's self introduction text before shortlisting them for a campaign.
- Check whether a call for a given `oAuthorId` succeeds before running deeper creator lookups.
- Request each `platform` value in turn to compare a creator's short-video, live, image-text, and short-drama channel data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/author-author-platform-channel-info-v2" \
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
    "status_message": "Success"
  },
  "self_intro": "我用心，你放心"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `base_resp.status_code` | Result code of the call. `0` means the call succeeded. |
| `base_resp.status_message` | Text status for the call. The sample shows `Success`. |
| `self_intro` | The creator's self-written introduction or slogan, as plain Chinese text. The sample value is `我用心，你放心`. |

### Notes

- `oAuthorId` is the creator's Xingtu author ID, a numeric string such as `6870161898013196295`. Find it with [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- `platform` accepts `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, or `SHORT_DRAMA`. It defaults to `SHORT_VIDEO`.
- For the creator's profile details, call [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/author-author-platform-channel-info-v2.json`](../../../../catalog/models/douyin/xingtu-v3/author-author-platform-channel-info-v2.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/author-author-platform-channel-info-v2
