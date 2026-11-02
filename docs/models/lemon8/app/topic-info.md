# Lemon8 Topic Information API: pricing, parameters and code examples

`lemon8/app/topic-info` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information and background visual assets for a specific Lemon8 topic using its unique forum identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/topic-info", "forum_id": "7174447913778593798"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/topic-info', {'forum_id': '7174447913778593798'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/topic-info", {
  "forum_id": "7174447913778593798"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/topic-info", sandbase.Params{
	"forum_id": "7174447913778593798",
})
```

Same call via the path form: `POST /v1/api/lemon8/app/topic-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `forum_id` | string | yes | Topic ID, can be obtained from the following interfaces: Get information of specified post: `lemon8/app/post-detail`; Get Editor's Picks of discover page: `lemon8/app/discover-tab-information-tabs`; search hashtags:…  |

## Details

Look up metadata and background assets for a Lemon8 topic by providing its unique `forum_id`.

### Use cases

- Display header imagery and details on custom topic pages.
- Inspect Lemon8 topic metadata for content discovery.
- Enrich hashtag analysis with forum background information.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/topic-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"forum_id": "7174447913778593798"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `forum_id` | string | Yes | Topic ID, can be obtained from the following interfaces: Get information of specified post: `lemon8/app/post-detail`; Get Editor's Picks of discover page: `lem… |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "background": {
      "url_list": [
        {
          "url": "https://p16-lemon8-va-sign.tiktokcdn-us.com/tos-maliva-i-tej9nj120t-us/4b46d07e1…"
        }
      ]
    }
  }
}
```

### Notes

- Obtain `forum_id` via post detail, discover tabs, or hashtag search endpoints.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Lemon8 Discover Page Banners](/model/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/model/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/model/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.

---
Machine-readable: [`catalog/models/lemon8/app/topic-info.json`](../../../../catalog/models/lemon8/app/topic-info.json) · Store page: https://www.sandbase.ai/model/lemon8/app/topic-info
