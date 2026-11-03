# Yandex Videos Search API: pricing, parameters and code examples

`yandex/videos` · data API · Yandex · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Yandex Videos results for a keyword: titles, thumbnails, durations and source sites.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yandex/videos", "text": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yandex/videos', {'text': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yandex/videos", {
  "text": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yandex/videos", sandbase.Params{
	"text": "coffee",
})
```

Same call via the path form: `POST /v1/api/yandex/videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `text` | string | yes | text  |

## Details

This API returns Yandex Videos search results for a keyword. Each result has a description, a rank position and a thumbnail URL. It needs one input, the search text in `text`.

### Use cases

- Check which videos Yandex ranks first for a keyword such as `coffee`.
- Collect video descriptions for a topic to study how creators word their content.
- Download thumbnail URLs to build a visual overview of a topic.
- Compare the video results for several keywords by running one call per keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yandex/videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "coffee"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `text` | string | Yes | text |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "search_information": {
    "within": null
  },
  "videos_results": [
    {
      "description": "In this video Jimmy is teaching us how to make the 3 most popular milk coffees w…",
      "position": 1,
      "thumbnail": "https://avatars.mds.yandex.net/get-vthumb/1650686/4b503447f957aa8cc8e5b3f605be6a…"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `videos_results[]` | List of video results for the keyword, in ranked order. |
| `videos_results[].position` | Rank of the video in the results. The first result has `position` 1. |
| `videos_results[].description` | Text snippet describing the video. Long descriptions are cut and end with an ellipsis. |
| `videos_results[].thumbnail` | URL of the video preview image. The URL ends in `564x318_1`, which suggests a 564 by 318 pixel image. |
| `search_information.within` | Extra search information. It is `null` in this response. |

### Notes

- Pass the search keyword in the `text` parameter. It is the only parameter and it is required.
- The response in this example has no title, duration or source site fields, even though the API description mentions them. Rely on `description`, `position` and `thumbnail`.
- For image results on the same keyword, call [Yandex Images Search](/apis/yandex/images).

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yandex/videos.json`](../../../catalog/models/yandex/videos.json) · Store page: https://www.sandbase.ai/model/yandex/videos
