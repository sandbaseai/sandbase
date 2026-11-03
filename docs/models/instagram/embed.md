# Instagram Profile Embed API: pricing, parameters and code examples

`instagram/embed` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch the public embed HTML for an Instagram profile by handle.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/embed", "handle": "nasa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/embed', {'handle': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/embed", {
  "handle": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/embed", sandbase.Params{
	"handle": "nasa",
})
```

Same call via the path form: `POST /v1/api/instagram/embed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | Instagram username without the leading @.  |

## Details

Returns the public embed page for an Instagram profile as a single HTML string. It needs one input, the `handle` of the account without the leading @.

### Use cases

- Render a profile card for an Instagram account inside your own page or dashboard.
- Parse the returned HTML to pull public profile details that the embed page shows.
- Check whether a handle resolves to a public embed page before you run deeper lookups.
- Archive a snapshot of how an account's embed page looked on a given day.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/embed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "nasa"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Instagram username without the leading @. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "html": "<!DOCTYPE html><html class=\"_9dls _ar44\" lang=\"en\" dir=\"ltr\"><head><link data-de…"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.html` | The full HTML document of the profile's embed page, returned as one string. Parse it or render it in an iframe. |
| `found` | `true` when the embed page was returned for the handle. A handle with no result returns `found: false`. |

### Notes

- Pass `handle` without the leading @, for example `nasa`.
- The response is raw HTML, not structured JSON. For structured profile fields such as counts and bio, call [Instagram Profile](/apis/instagram/profile) or [Instagram Basic Profile](/apis/instagram/basic-profile).
- To list an account's posts, use [Instagram User Posts (V1)](/apis/instagram/v1/user-posts).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/embed.json`](../../../catalog/models/instagram/embed.json) · Store page: https://www.sandbase.ai/model/instagram/embed
