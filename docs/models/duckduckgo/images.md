# DuckDuckGo Images API: pricing, parameters and code examples

`duckduckgo/images` · data API · DuckDuckGo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search DuckDuckGo Images by keyword with size, color, type and layout filters, returning image URLs, thumbnails, titles and sources.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "duckduckgo/images", "q": "mountain lake"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('duckduckgo/images', {'q': 'mountain lake'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("duckduckgo/images", {
  "q": "mountain lake"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "duckduckgo/images", sandbase.Params{
	"q": "mountain lake",
})
```

Same call via the path form: `POST /v1/api/duckduckgo/images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the query you want to search. You can use anything that you would use in a regular DuckDuckGo Images search. (e.g., `site:`) Parameter length can not exceed 500 characters.  |
| `df` | string |  | Parameter defines results filtered by date. It can be set to: `d` - Past day `w` - Past week `m` - Past month `y` - Past year  |
| `kl` | string |  | Parameter defines the region to use for the DuckDuckGo Images search. Region code examples: `us-en` (default) for the United States, `uk-en` for United Kingdom, or `fr-fr` for France. Head to the DuckDuckGo regions for…  |
| `safe` | string |  | Parameter defines the level of filtering for adult content. It can be set to `1` (Strict), `-1` (Moderate - default), or `-2` (Off).  |
| `size` | string |  | Parameter defines results filtered by image size. It can be set to: `Small` - Small `Medium` - Medium `Large` - Large `Wallpaper` - Wallpaper  |
| `color` | string |  | Parameter defines results filtered by image color. It can be set to: `color` - Color only `Monochrome` - Black and white `Red` - Red `Orange` - Orange `Yellow` - Yellow `Green` - Green `Blue` - Blue `Purple` - Purple…  |
| `start` | string |  | Parameter defines the result offset. It skips the given number of results. DuckDuckGo Images returns up to 100 `images_results` per page, so the next page starts at `100`. The next page can be found in the the API JSON…  |
| `layout` | string |  | Parameter defines results filtered by image layout. It can be set to: `Square` - Square `Tall` - Tall `Wide` - Wide  |
| `license` | string |  | Parameter defines results filtered by image license. It can be set to: `Any` - All Creative Commons `Public` - Public domain `Share` - Free to share and use `ShareCommercially` - Free to share and use commercially…  |
| `image_type` | string |  | Parameter defines results filtered by image type. It can be set to: `photo` - Photograph `clipart` - Clipart `gif` - Animated GIF `transparent` - Transparent `line` - Line drawing  |
| `hide_ai_images` | string |  | Parameter defines whether to hide AI-generated images, like DuckDuckGo's *Hide AI images* setting. It can be set to `true` or `false` (default).  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search DuckDuckGo Images by keyword with size, color, type and layout filters, returning image URLs, thumbnails, titles and sources.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/duckduckgo/images" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "mountain lake"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the query you want to search. You can use anything that you would use in a regular DuckDuckGo Images search. (e.g., `site:`) Parameter length can not exceed 500 characters. |
| `kl` | string | No | Parameter defines the region to use for the DuckDuckGo Images search. Region code examples: `us-en` (default) for the United States, `uk-en` for United Kingdom, or `fr-fr` for France. Head to the DuckDuckGo regions for a full list of suppor |
| `safe` | string | No | Parameter defines the level of filtering for adult content. It can be set to `1` (Strict), `-1` (Moderate - default), or `-2` (Off). |
| `df` | string | No | Parameter defines results filtered by date. It can be set to: `d` - Past day `w` - Past week `m` - Past month `y` - Past year |
| `size` | string | No | Parameter defines results filtered by image size. It can be set to: `Small` - Small `Medium` - Medium `Large` - Large `Wallpaper` - Wallpaper |
| `color` | string | No | Parameter defines results filtered by image color. It can be set to: `color` - Color only `Monochrome` - Black and white `Red` - Red `Orange` - Orange `Yellow` - Yellow `Green` - Green `Blue` - Blue `Purple` - Purple `Pink` - Pink `Brown` - |
| `image_type` | string | No | Parameter defines results filtered by image type. It can be set to: `photo` - Photograph `clipart` - Clipart `gif` - Animated GIF `transparent` - Transparent `line` - Line drawing |
| `layout` | string | No | Parameter defines results filtered by image layout. It can be set to: `Square` - Square `Tall` - Tall `Wide` - Wide |
| `license` | string | No | Parameter defines results filtered by image license. It can be set to: `Any` - All Creative Commons `Public` - Public domain `Share` - Free to share and use `ShareCommercially` - Free to share and use commercially `Modify` - Free to modify, |
| `hide_ai_images` | string | No | Parameter defines whether to hide AI-generated images, like DuckDuckGo's *Hide AI images* setting. It can be set to `true` or `false` (default). |
| `start` | string | No | Parameter defines the result offset. It skips the given number of results. DuckDuckGo Images returns up to 100 `images_results` per page, so the next page starts at `100`. The next page can be found in the the API JSON response: `the API_pa |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/duckduckgo/images.json`](../../../catalog/models/duckduckgo/images.json) · Store page: https://www.sandbase.ai/model/duckduckgo/images
