# TikTok Keyword Search Deep Link API: pricing, parameters and code examples

`tiktok/app-v3/open-app-to-keyword-search` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a TikTok share link that directs users to search results for a specified keyword inside the TikTok mobile application.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/open-app-to-keyword-search", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/open-app-to-keyword-search', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/open-app-to-keyword-search", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/open-app-to-keyword-search", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/open-app-to-keyword-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Keyword  |

## Details

Returns a TikTok short share link that opens the search results for a keyword in the TikTok mobile app. It needs one input: the `keyword` to search for.

### Use cases

- Put a TikTok search link behind a button in a marketing email so readers land on results for your campaign keyword.
- Add a QR code or link on a product page that opens TikTok results for a brand name.
- Build a list of tappable topic links in a web app that send mobile users straight into TikTok search.
- Share a keyword search link in a chat or social post without asking people to type the query.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/open-app-to-keyword-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "keyword": "openai",
  "short_url": "https://www.tiktok.com/t/ZP9ytc66mBWv8-IYMhN/",
  "status": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `keyword` | The keyword you sent. The response echoes it back so you can match the link to the request. |
| `short_url` | The TikTok share link for the keyword search. Opening it on a phone with the app installed should lead to the search results for that keyword. |
| `status` | Status code of the result. The value `0` appears in this successful response. |

### Notes

- Send the search text in the `keyword` parameter. It is the only required input.
- Each call returns a new `short_url` value, so store the link if you want to reuse it.
- To get the search results as data instead of a link, call [TikTok Search](/apis/tiktok/app-v3/general-search-result) or [TikTok Video Keyword Search](/apis/tiktok/app-v3/video-search-result).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/open-app-to-keyword-search.json`](../../../../catalog/models/tiktok/app-v3/open-app-to-keyword-search.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/open-app-to-keyword-search
