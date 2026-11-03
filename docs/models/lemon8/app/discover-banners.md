# Lemon8 Discover Page Banners API: pricing, parameters and code examples

`lemon8/app/discover-banners` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the current promotional and featured banners displayed on the Lemon8 discover page. Applications can use this data to inspect active platform campaigns and highlighted topics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/discover-banners"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/discover-banners', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/discover-banners", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/discover-banners", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/lemon8/app/discover-banners` with the body above minus `model`.

## Details

Returns the banners currently shown on the Lemon8 discover page. Each banner has a title, a click link, and image URLs. The request takes no input parameters.

### Use cases

- Show the current Lemon8 campaign banners in an external dashboard.
- Log banner titles over time to see which campaigns Lemon8 promotes.
- Download banner images to archive how the discover page looked on a given day.
- Extract the campaign page links to find which landing pages Lemon8 is promoting.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/discover-banners" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "banners": [
      {
        "banner_click_url": "sslocal://webview?url=https%3A%2F%2Fv.lemon8-app.com%2Foxygen%2Fpage%2Frelease%2…",
        "collection_banner_url": {
          "height": 1,
          "uri": "tos-alisg-i-sdweummd6v-sg/ec242ef821a849909b6fedabb9185281",
          "url_list": [
            {
              "url": "https://p16-lemon8-cross-sign.tiktokcdn-us.com/tos-alisg-i-sdweummd6v-sg/ec242ef…"
            }
          ],
          "width": 1
        },
        "id": "26051",
        "profile_banner_url": {
          "height": 1,
          "uri": "tos-alisg-i-sdweummd6v-sg/0fc8e0e164d94b179c3c431ab60ceddb",
          "url_list": [
            {
              "url": "https://p16-lemon8-cross-sign.tiktokcdn-us.com/tos-alisg-i-sdweummd6v-sg/0fc8e0e…"
            }
          ],
          "width": 1
        },
        "title": "Meet the ingredients behind the glow!"
      }
    ]
  },
  "message": "success",
  "result_status": 0,
  "server_time": "1793691389.99"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.banners[]` | List of banners on the discover page. Each item is one banner. |
| `data.banners[].id` | Banner ID as a string, such as `26051`. |
| `data.banners[].title` | Display title of the banner, for example a campaign or topic headline. |
| `data.banners[].banner_click_url` | Link opened when a user taps the banner. It uses the `sslocal://webview?url=` format, with the target page URL-encoded inside the `url` value. |
| `data.banners[].profile_banner_url` | Banner image for the profile placement. Contains `url_list[].url`, `uri`, `width` and `height`. |
| `data.banners[].collection_banner_url` | Banner image for the collection placement. Has the same structure as `profile_banner_url`. Some banners do not include it. |
| `data.banners[].banner_image` | Main banner image object with `url_list[].url`, `uri`, `width` and `height`. Only some banners include it. |
| `data.banners[].profile_banner_url.url_list[].url` | Direct image URL (WebP) for the profile banner. Other image objects use the same `url_list[].url` path. |
| `server_time` | Server timestamp as a string of Unix seconds with decimals. |

### Notes

- The request body is an empty object `{}`. No parameters are needed.
- Image fields differ between banners. Check that `banner_image` or `collection_banner_url` exists before you read it. One banner returns `collection_banner_uri` as an empty string instead of an image object.
- The `width` and `height` values in the image objects are `1` in this response, so do not use them as real image sizes.
- For other discover page data, call [Lemon8 Discover Page Content](/apis/lemon8/app/discover-tab) or [Lemon8 Hot Search Keywords](/apis/lemon8/app/hot-search-keywords).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Lemon8 Discover Page Content](/apis/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/apis/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.
- [Lemon8 Hot Search Keywords](/apis/lemon8/app/hot-search-keywords): Returns trending search keywords and topics currently popular on Lemon8.

---
Machine-readable: [`catalog/models/lemon8/app/discover-banners.json`](../../../../catalog/models/lemon8/app/discover-banners.json) · Store page: https://www.sandbase.ai/model/lemon8/app/discover-banners
