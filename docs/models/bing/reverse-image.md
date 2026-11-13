# Bing Reverse Image Search API: pricing, parameters and code examples

`bing/reverse-image` · data API · Bing · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search Bing Visual Search with an image URL and get visually similar images, pages that contain the image and related searches.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bing/reverse-image", "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/320px-Camponotus_flavomarginatus_ant.jpg"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bing/reverse-image', {'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/320px-Camponotus_flavomarginatus_ant.jpg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bing/reverse-image", {
  "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/320px-Camponotus_flavomarginatus_ant.jpg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bing/reverse-image", sandbase.Params{
	"image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/320px-Camponotus_flavomarginatus_ant.jpg",
})
```

Same call via the path form: `POST /v1/api/bing/reverse-image` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cab` | string |  | Parameter is used to crop the image and perform the reverse search on the cropped part of the image. For example, `0.8` means cropping the bottom, 80% from the top. The minimum and maximum for this coordinate are `0`…  |
| `cal` | string |  | Parameter is used to crop the image and perform the reverse search on the cropped part of the image. For example, `0.3` means cropping 30% from the left. The minimum and maximum for this coordinate are `0` and `1`,…  |
| `car` | string |  | Parameter is used to crop the image and perform the reverse search on the cropped part of the image. For example, `0.8` means cropping the right, 80% from the left. The minimum and maximum for this coordinate are `0`…  |
| `cat` | string |  | Parameter is used to crop the image and perform the reverse search on the cropped part of the image. For example, `0.3` means cropping 30% from the top. The minimum and maximum for this coordinate are `0` and `1`,…  |
| `mkt` | string |  | The market where the results come from (e.g. `en-US`). Typically, `mkt` is the country where the user is making the request from. However, it could be a different country if the user is not located in a country where…  |
| `count` | string |  | Parameter controls the number of results per page. This parameter defaults to `35`. This parameter is only a suggestion and might not reflect the returned results. The minimum and maximum for this parameter are `0` and…  |
| `image_url` | string | yes | Parameter defines the URL for an image to perform the reverse image search. NOTE: The image's width and height must each be 4,000 pixels or less.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `next_page_token` | string |  | Parameter defines the next page token. It is used for retrieving the next page results.  |

## Details

Search Bing Visual Search with an image URL and get visually similar images, pages that contain the image and related searches.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bing/reverse-image" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/320px-Camponotus_flavomarginatus_ant.jpg"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `image_url` | string | Yes | Parameter defines the URL for an image to perform the reverse image search. NOTE: The image's width and height must each be 4,000 pixels or less. |
| `mkt` | string | No | The market where the results come from (e.g. `en-US`). Typically, `mkt` is the country where the user is making the request from. However, it could be a different country if the user is not located in a country where Bing Reverse Image API  |
| `cat` | string | No | Parameter is used to crop the image and perform the reverse search on the cropped part of the image. For example, `0.3` means cropping 30% from the top. The minimum and maximum for this coordinate are `0` and `1`, respectively. |
| `cal` | string | No | Parameter is used to crop the image and perform the reverse search on the cropped part of the image. For example, `0.3` means cropping 30% from the left. The minimum and maximum for this coordinate are `0` and `1`, respectively. |
| `car` | string | No | Parameter is used to crop the image and perform the reverse search on the cropped part of the image. For example, `0.8` means cropping the right, 80% from the left. The minimum and maximum for this coordinate are `0` and `1`, respectively. |
| `cab` | string | No | Parameter is used to crop the image and perform the reverse search on the cropped part of the image. For example, `0.8` means cropping the bottom, 80% from the top. The minimum and maximum for this coordinate are `0` and `1`, respectively. |
| `next_page_token` | string | No | Parameter defines the next page token. It is used for retrieving the next page results. |
| `count` | string | No | Parameter controls the number of results per page. This parameter defaults to `35`. This parameter is only a suggestion and might not reflect the returned results. The minimum and maximum for this parameter are `0` and `150`, respectively. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/bing/reverse-image.json`](../../../catalog/models/bing/reverse-image.json) · Store page: https://www.sandbase.ai/model/bing/reverse-image
