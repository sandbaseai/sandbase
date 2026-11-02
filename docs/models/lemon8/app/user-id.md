# Lemon8 User ID from Share Link API: pricing, parameters and code examples

`lemon8/app/user-id` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns a Lemon8 user ID extracted from a user profile share link. Input supports long or short sharing URLs copied from the web or app.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/user-id", "share_text": "https://www.lemon8-app.com/lemon8cars?region=us"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/user-id', {'share_text': 'https://www.lemon8-app.com/lemon8cars?region=us'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/user-id", {
  "share_text": "https://www.lemon8-app.com/lemon8cars?region=us"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/user-id", sandbase.Params{
	"share_text": "https://www.lemon8-app.com/lemon8cars?region=us",
})
```

Same call via the path form: `POST /v1/api/lemon8/app/user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `share_text` | string | yes | Share link, supports long links and short links, can be obtained and copied from the share button on the web and APP.  |

## Details

Look up a Lemon8 account identifier using the `share_text` parameter. This endpoint resolves shared profile links into the underlying user ID.

### Use cases

- Resolve shared Lemon8 profile URLs into stable user identifiers.
- Map user links copied from the Lemon8 mobile app to user IDs.
- Automate profile identification from Lemon8 web share links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_text": "https://www.lemon8-app.com/lemon8cars?region=us"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_text` | string | Yes | Share link, supports long links and short links, can be obtained and copied from the share button on the web and APP. |

### Notes

- The `share_text` parameter accepts both long links and short links copied from the Lemon8 app or web interface.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Lemon8 Discover Page Banners](/model/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/model/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/model/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.

---
Machine-readable: [`catalog/models/lemon8/app/user-id.json`](../../../../catalog/models/lemon8/app/user-id.json) · Store page: https://www.sandbase.ai/model/lemon8/app/user-id
