# Lemon8 Post ID from Share Link API: pricing, parameters and code examples

`lemon8/app/item-id` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Resolves a Lemon8 share URL into its canonical post ID. Accepts both long and short sharing links copied from the web platform or mobile app.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/item-id", "share_text": "<share_text>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/item-id', {'share_text': '<share_text>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/item-id", {
  "share_text": "<share_text>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/item-id", sandbase.Params{
	"share_text": "<share_text>",
})
```

Same call via the path form: `POST /v1/api/lemon8/app/item-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `share_text` | string | yes | Share link, supports long links and short links, can be obtained and copied from the share button on the web and APP.  |

## Details

Retrieve a canonical Lemon8 post ID by providing a share link in `share_text`. It resolves both long and short URLs copied from the Lemon8 mobile app or web interface.

### Use cases

- Extract item IDs from shared URLs for downstream Lemon8 queries.
- Convert mobile and web short links into direct Lemon8 post identifiers.
- Automate post tracking workflows from user-submitted share text.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/item-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_text": "<share_text>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_text` | string | Yes | Share link, supports long links and short links, can be obtained and copied from the share button on the web and APP. |

### Notes

- The `share_text` parameter accepts both long and short links copied via the Lemon8 share button.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Lemon8 Discover Page Banners](/model/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/model/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/model/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.

---
Machine-readable: [`catalog/models/lemon8/app/item-id.json`](../../../../catalog/models/lemon8/app/item-id.json) · Store page: https://www.sandbase.ai/model/lemon8/app/item-id
