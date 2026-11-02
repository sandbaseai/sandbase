# TikTok Profile Unique IDs API: pricing, parameters and code examples

`tiktok/web/all-unique-id` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers. Accepts a list of profile URLs in the request payload.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/all-unique-id", "body": ["<body>"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/all-unique-id', {'body': ['<body>']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/all-unique-id", {
  "body": [
    "<body>"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/all-unique-id", sandbase.Params{
	"body": []any{"<body>"},
})
```

Same call via the path form: `POST /v1/api/tiktok/web/all-unique-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `body` | array | yes | User homepage link  |

## Details

Retrieves unique identifiers for TikTok users based on their profile URLs provided in the `body` parameter.

### Use cases

- Batch resolve TikTok homepage links to profile unique IDs.
- Map profile URLs to TikTok internal identifiers for downstream data workflows.
- Extract profile identifiers from lists of TikTok creator links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/all-unique-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"body": "<body>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | array | Yes | User homepage link |

### Notes

- Provide TikTok user homepage links as an array in `body`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Video ID from URL](/model/tiktok/web/aweme-id): Extracts and returns the unique single video ID from a provided TikTok video link.

---
Machine-readable: [`catalog/models/tiktok/web/all-unique-id.json`](../../../../catalog/models/tiktok/web/all-unique-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/all-unique-id
