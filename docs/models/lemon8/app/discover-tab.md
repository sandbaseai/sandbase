# Lemon8 Discover Page Content API: pricing, parameters and code examples

`lemon8/app/discover-tab` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the main content featured on the Lemon8 discover tab. Retrieve trending recommendations and highlighted posts directly from the app feed.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/discover-tab"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/discover-tab', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/discover-tab", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/discover-tab", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/lemon8/app/discover-tab` with the body above minus `model`.

## Details

Returns the content featured on the Lemon8 discover tab as a list in `data`, plus paging flags and impression IDs. It needs no input parameters.

### Use cases

- Pull the current discover feed to see which posts Lemon8 recommends.
- Check the discover tab on a schedule to track which featured content appears over time.
- Collect post entries from the feed, then look up each one with a post details call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/discover-tab" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [],
  "has_more": false,
  "impr_id": "0",
  "session_impr_id": "0"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data` | List of featured discover tab items. The sample response returns an empty list, so check its length before reading items. |
| `has_more` | Boolean flag that shows whether more items are available after this response. It is `false` in the sample response. |
| `impr_id` | Impression ID string for this response. The sample value is `"0"`. |
| `session_impr_id` | Impression ID string for the session. The sample value is `"0"`. |

### Notes

- The request body is an empty object: send `{}`.
- The `data` list can come back empty, so handle that case in your code.
- To get full details for a post found in the feed, call [Lemon8 Post Details](/apis/lemon8/app/post-detail).
- For promotional banners on the same page, use [Lemon8 Discover Page Banners](/apis/lemon8/app/discover-banners).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Lemon8 Discover Page Banners](/apis/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Editor Picks](/apis/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.
- [Lemon8 Hot Search Keywords](/apis/lemon8/app/hot-search-keywords): Returns trending search keywords and topics currently popular on Lemon8.

---
Machine-readable: [`catalog/models/lemon8/app/discover-tab.json`](../../../../catalog/models/lemon8/app/discover-tab.json) · Store page: https://www.sandbase.ai/model/lemon8/app/discover-tab
