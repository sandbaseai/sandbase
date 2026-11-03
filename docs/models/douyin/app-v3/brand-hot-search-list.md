# Douyin Brand Hot Search List API: pricing, parameters and code examples

`douyin/app-v3/brand-hot-search-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the current Douyin brand hot search list and category data. Use it to track trending brand searches and popular brand rankings across the platform.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/brand-hot-search-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/brand-hot-search-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/brand-hot-search-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/brand-hot-search-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/brand-hot-search-list` with the body above minus `model`.

## Details

Returns the current Douyin brand hot search page data: a banner image and a list of brand categories. It needs no input, so you send an empty JSON object `{}`.

### Use cases

- Read the list of brand categories and their `id` values to build a category picker for brand ranking tools.
- Pull the category list on a schedule to detect when Douyin adds or renames a brand category.
- Collect the `id` of each category, then request the ranking for that category in the detail API.
- Save the banner image for the brand hot search page in a reporting dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/brand-hot-search-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "banner_url": {
    "uri": "daa7000a0f0d6a308320",
    "url_list": [
      "https://p26-sign.douyinpic.com/obj/daa7000a0f0d6a308320?x-expires=1793775600&x-s…"
    ]
  },
  "category_list": [
    {
      "id": 10,
      "name": "汽车"
    }
  ],
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611031531328768F9FF39F8485A71CE",
    "now": 1793691092000
  },
  "log_pb": {
    "impr_id": "202611031531328768F9FF39F8485A71CE"
  },
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `category_list[].id` | Numeric ID of a brand category, for example `10`. Use it as the category input in the detail API. |
| `category_list[].name` | Category name as shown on Douyin, in Chinese. Examples in the response are `汽车`, `手机` and `美妆`. |
| `banner_url.uri` | Identifier of the banner image. |
| `banner_url.url_list[]` | Image URLs for the banner. They are signed links and contain an `x-expires` value. |
| `status_code / status_msg` | Result status of the call. `status_code` is `0` and `status_msg` is empty in the sample response. |
| `extra.now` | Server time in the response, as a 13-digit number that looks like a Unix time in milliseconds. |
| `extra.logid / log_pb.impr_id` | Request tracking IDs. In the sample response both hold the same value. |

### Notes

- The request takes no parameters. Send `{}` as the body.
- To get the brand ranking for one category, pass a `category_list[].id` value to [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail).
- Banner URLs are signed and include an `x-expires` query value, so download the image soon after you fetch it.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.
- [Douyin Video Share QR Code](/apis/douyin/app-v3/generate-video-share-qrcode): Returns a Douyin share QR code for a designated target.

---
Machine-readable: [`catalog/models/douyin/app-v3/brand-hot-search-list.json`](../../../../catalog/models/douyin/app-v3/brand-hot-search-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/brand-hot-search-list
