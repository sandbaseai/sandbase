# TikTok Livestream Homepage Recommendations API: pricing, parameters and code examples

`tiktok/web/live-recommend` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended livestreams from the TikTok homepage for a specified category tag. Requires selecting a category tag to retrieve relevant active broadcast recommendations.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/live-recommend", "related_live_tag": "test"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/live-recommend', {'related_live_tag': 'test'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/live-recommend", {
  "related_live_tag": "test"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/live-recommend", sandbase.Params{
	"related_live_tag": "test",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/live-recommend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `related_live_tag` | string | yes | Related live tag (live category). The available values are not fixed; call `/fetch_live_recommend_tabs` first to get the currently available tag list, then pick one to pass in.  |

## Details

Retrieve a list of recommended livestreams from the TikTok homepage based on `related_live_tag`.

### Use cases

- Browse recommended livestreams under a specific category tag.
- Display curated TikTok broadcasts on an external dashboard.
- Monitor active broadcast recommendations across diverse categories.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/live-recommend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"related_live_tag": "VALORANT"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `related_live_tag` | string | Yes | Related live tag (live category). |

### Notes

- Call `/fetch_live_recommend_tabs` first to retrieve currently available values for `related_live_tag`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/live-recommend.json`](../../../../catalog/models/tiktok/web/live-recommend.json) · Store page: https://www.sandbase.ai/model/tiktok/web/live-recommend
