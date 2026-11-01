# Douyin Hot Video Audience Portrait

`douyin/billboard/hot-user-portrait-list` · api · Douyin

Returns audience persona and demographic data for trending Douyin videos. Look up user portraits by providing a specific work ID and optional display options.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-user-portrait-list", "aweme_id": "7372484719365098803"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-user-portrait-list', {'aweme_id': '7372484719365098803'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-user-portrait-list", {
  "aweme_id": "7372484719365098803"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-user-portrait-list", sandbase.Params{
	"aweme_id": "7372484719365098803",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-user-portrait-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `option` | integer |  | Option  |
| `aweme_id` | string | yes | Work id  |

## Details

Fetch audience demographic information for trending Douyin videos by providing the target `aweme_id` alongside an optional `option` setting.

### Use cases

- Analyze the demographic breakdown of viewers liking trending Douyin videos.
- Evaluate audience personas for competitive research on viral content.
- Assess viewer alignment before planning creator collaborations.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-user-portrait-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7372484719365098803"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Work id |
| `option` | integer | No | Option |

### Notes

- Requires `aweme_id` representing the specific Douyin work ID.
- Use `option` to configure additional query settings.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/model/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/model/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-user-portrait-list.json`](../../../../catalog/models/douyin/billboard/hot-user-portrait-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-user-portrait-list
