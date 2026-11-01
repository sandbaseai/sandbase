# DataForSEO Website Screenshot

`dataforseo/v3/on_page/page_screenshot` · api · DataForSEO

Capture a full-page or viewport screenshot of any URL in desktop, mobile or tablet view. Options for custom screen size, language, user agent and dismissing cookie pop-ups.

## Pricing

- **$0.004 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/on_page/page_screenshot", "accept_language": "en", "browser_preset": "desktop", "disable_cookie_popup": true, "full_page_screenshot": false, "url": "https://static.sandbase.ai/examples/46031d8f-5e94-4e1f-be8d-c5fa08a87c0d/input/5de63a4b-cc40-4bad-b86c-d9afc7795d54.md"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/on_page/page_screenshot', {'accept_language': 'en', 'browser_preset': 'desktop', 'disable_cookie_popup': True, 'full_page_screenshot': False, 'url': 'https://static.sandbase.ai/examples/46031d8f-5e94-4e1f-be8d-c5fa08a87c0d/input/5de63a4b-cc40-4bad-b86c-d9afc7795d54.md'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/on_page/page_screenshot", {
  "accept_language": "en",
  "browser_preset": "desktop",
  "disable_cookie_popup": true,
  "full_page_screenshot": false,
  "url": "https://static.sandbase.ai/examples/46031d8f-5e94-4e1f-be8d-c5fa08a87c0d/input/5de63a4b-cc40-4bad-b86c-d9afc7795d54.md"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/on_page/page_screenshot", sandbase.Params{
	"accept_language": "en",
	"browser_preset": "desktop",
	"disable_cookie_popup": true,
	"full_page_screenshot": false,
	"url": "https://static.sandbase.ai/examples/46031d8f-5e94-4e1f-be8d-c5fa08a87c0d/input/5de63a4b-cc40-4bad-b86c-d9afc7795d54.md",
})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/on_page/page_screenshot` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | page url required field absolute URL of the page to capture a screenshot of example: https://dataforseo.com/apis  |
| `switch_pool` | boolean |  | switch proxy pool optional field if true, additional proxy pools will be used to obtain the requested data  |
| `browser_preset` | string |  | preset for browser screen parameters optional field possible values: desktop, mobile, tablet desktop: 1920x1080, scale 1 mobile: 390x844, scale 3 tablet: 1024x1366, scale 2  |
| `accept_language` | string |  | language header for accessing the website optional field all locale formats are supported (xx, xx-XX, xxx-XX, etc.) Note: if you do not specify this parameter, some websites may deny access  |
| `ip_pool_for_scan` | string |  | proxy pool location optional field possible values: us, de  |
| `custom_user_agent` | string |  | custom user agent optional field custom user agent for crawling a website default value: Mozilla/5.0 (compatible; RSiteAuditor)  |
| `browser_screen_width` | integer |  | browser screen width in pixels optional field minimum value: 240 maximum value: 9999 if set, browser_preset is ignored  |
| `disable_cookie_popup` | boolean |  | disable the cookie popup optional field set to true to dismiss cookie consent dialogs default value: false  |
| `full_page_screenshot` | boolean |  | take a screenshot of the full page optional field set to false to capture only the visible viewport default value: true  |
| `browser_screen_height` | integer |  | browser screen height in pixels optional field minimum value: 240 maximum value: 9999 if set, browser_preset is ignored  |
| `browser_screen_scale_factor` | number |  | browser screen scale factor optional field minimum value: 0.5 maximum value: 3 if set, browser_preset is ignored  |

## Details

Pass a URL and get back a hosted screenshot image of the rendered page. Choose a device preset or exact screen size, and capture the full page or only the visible viewport.

### Use cases

- Generate thumbnails and previews of web pages.
- Visually monitor competitor landing pages or SERP features.
- Archive how a page looked at a point in time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/on_page/page_screenshot" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://dataforseo.com/apis"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | page url required field absolute URL of the page to capture a screenshot of example: https://dataforseo.com/apis |
| `switch_pool` | boolean | No | switch proxy pool optional field if true, additional proxy pools will be used to obtain the requested data |
| `browser_preset` | string | No | preset for browser screen parameters optional field possible values: desktop, mobile, tablet desktop: 1920x1080, scale … |
| `accept_language` | string | No | language header for accessing the website optional field all locale formats are supported (xx, xx-XX, xxx-XX, etc.) Not… |
| `ip_pool_for_scan` | string | No | proxy pool location optional field possible values: us, de |
| `custom_user_agent` | string | No | custom user agent optional field custom user agent for crawling a website default value: Mozilla/5.0 (compatible; RSite… |
| `browser_screen_width` | integer | No | browser screen width in pixels optional field minimum value: 240 maximum value: 9999 if set, browser_preset is ignored |
| `disable_cookie_popup` | boolean | No | disable the cookie popup optional field set to true to dismiss cookie consent dialogs default value: false |
| `full_page_screenshot` | boolean | No | take a screenshot of the full page optional field set to false to capture only the visible viewport default value: true |
| `browser_screen_height` | integer | No | browser screen height in pixels optional field minimum value: 240 maximum value: 9999 if set, browser_preset is ignored |
| `browser_screen_scale_factor` | number | No | browser screen scale factor optional field minimum value: 0.5 maximum value: 3 if set, browser_preset is ignored |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "status_code": 20000,
  "tasks": [
    {
      "status_message": "Ok.",
      "data": {
        "api": "on_page",
        "function": "page_screenshot",
        "url": "https://dataforseo.com/apis"
      },
      "result": [
        {
          "crawl_progress": "finished",
          "items_count": 1,
          "items": [
            {
              "image": "https://api.dataforseo.com/cdn/screenshot/10060902-2190-0444-0000-91f534c360ca"
            }
          ]
        }
      ]
    }
  ]
}
```

### Notes

- `browser_preset`: `desktop` (1920×1080), `mobile` (390×844) or `tablet`.
- Set `disable_cookie_popup` to `true` to hide consent banners.

### Pricing

Flat price per call. Failed calls are not charged.

### Related APIs

- [DataForSEO Google Ads Keyword Search Volume](/model/dataforseo/v3/keywords_data/google_ads/search_volume/live): Get Google Ads search volume, CPC, competition and 12-month trend for up to 1,000 keywords per request, by location and language.
- [DataForSEO Google Trends](/model/dataforseo/v3/keywords_data/google_trends/explore/live): Get Google Trends interest over time for up to 5 keywords by location, language and time range, with weekly values on a 0–100 scale.
- [DataForSEO Google SERP (Advanced)](/model/dataforseo/v3/serp/google/organic/live/advanced): Get live Google organic search results for any keyword, location and language, including AI Overviews, featured snippets, People Also Ask and other SERP featur…

---
Machine-readable: [`catalog/models/dataforseo/v3/on_page/page_screenshot.json`](../../../../../catalog/models/dataforseo/v3/on_page/page_screenshot.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/on_page/page_screenshot
