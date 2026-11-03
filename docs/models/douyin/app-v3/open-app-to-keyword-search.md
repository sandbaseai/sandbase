# Douyin Keyword Search Share Link API: pricing, parameters and code examples

`douyin/app-v3/open-app-to-keyword-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a Douyin short share link that launches the Douyin application directly to search results for a specified query term.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/open-app-to-keyword-search", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/open-app-to-keyword-search', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/open-app-to-keyword-search", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/open-app-to-keyword-search", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/open-app-to-keyword-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Keyword  |

## Details

Returns a Douyin short share link that opens the Douyin app directly on the search results for a keyword. It needs one input, the `keyword` to search for.

### Use cases

- Send mobile users straight to the Douyin search results for a topic from a web page or message.
- Add a Douyin search deep link to a marketing campaign page or a QR code.
- Build a list of tappable links for trending search terms in an external app.
- Check which short link Douyin creates for a given search term.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/open-app-to-keyword-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
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
  "keyword": "人工智能",
  "short_url": "https://v.douyin.com/VLzKnPXaPKo/",
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `short_url` | The Douyin short link. Opening it on a device with the Douyin app launches the search results for the keyword. |
| `keyword` | The search term the link was built for. It echoes the `keyword` you sent. |
| `status` | Result of the call. The value `success` means the link was created. |

### Notes

- Pass the search term in the required `keyword` parameter. Chinese text such as `人工智能` works as shown in the example.
- The `short_url` value is in the form `https://v.douyin.com/<code>/`.
- To shorten a standard Douyin web link instead, use [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url).
- To find terms worth linking to, call [Douyin Hot Search List](/apis/douyin/app-v3/hot-search-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/open-app-to-keyword-search.json`](../../../../catalog/models/douyin/app-v3/open-app-to-keyword-search.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/open-app-to-keyword-search
