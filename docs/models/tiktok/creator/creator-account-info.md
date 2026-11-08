# TikTok Creator Account Info API: pricing, parameters and code examples

`tiktok/creator/creator-account-info` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call · **Modes:** sync

Returns basic profile details for a TikTok Shop creator account, including username, avatar URLs, account ID, region, partner bindings, and permissions.

## Pricing

- **$0.001 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/creator-account-info"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/creator-account-info', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/creator-account-info", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/creator-account-info", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/creator/creator-account-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `proxy` |  |  | Optional HTTP proxy address, can be omitted if not used  |
| `cookie` | string | yes | Cookie string of your own logged-in TikTok Shop creator account (from your browser session on the TikTok Shop / Seller Center site). Sent to the upstream for this request only and never stored by SandBase.  |

## Details

Retrieves TikTok Shop creator account details such as username, avatar, and permissions. You can optionally route requests through an HTTP proxy via `proxy`.

### Use cases

- Verify TikTok Shop creator account status and permissions.
- Display creator profile details such as username and avatar in a dashboard.
- Check partner binding information for authorized creator workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/creator/creator-account-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cookie": "<YOUR_TIKTOK_SHOP_COOKIE>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cookie` | string | Yes | Cookie string of your own logged-in TikTok Shop creator account. Used for this request only and never stored |
| `proxy` | string | No | Optional HTTP proxy address, can be omitted if not used |

### Notes

- Requires `cookie` from your own TikTok Shop creator account. The data returned belongs to that account; this API cannot look up other creators. SandBase forwards the cookie for this synchronous request only and does not store it in call history or logs, so async mode and retries are not supported.
- Pass an optional HTTP proxy address in `proxy` if routing through a proxy server.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/tiktok/creator/creator-account-info.json`](../../../../catalog/models/tiktok/creator/creator-account-info.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/creator-account-info
