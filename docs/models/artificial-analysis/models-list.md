# Artificial Analysis Models List API: pricing, parameters and code examples

`artificial-analysis/models-list` · data API · Artificial Analysis · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

Get a list of all LLM models (one row per model variant, e.g. each effort level) with slug, display name, the release it belongs to (releaseSlug and a release object), deprecation flag, release date, and creator.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "artificial-analysis/models-list"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('artificial-analysis/models-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("artificial-analysis/models-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "artificial-analysis/models-list", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/artificial-analysis/models-list` with the body above minus `model`.

## Details

Returns a list of LLM models tracked on Artificial Analysis, with one row per model variant such as each effort level. Each row has a slug, display name, release, release date, deprecation flag and creator. The API takes no input.

### Use cases

- Build a catalog of LLM model slugs to use as keys in other lookups.
- Group model variants by release to see all effort levels of one model.
- Track new LLM releases by sorting rows on `releaseDate`.
- List every model from one creator, such as Google, Anthropic or OpenAI.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/artificial-analysis/models-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "creators": [
      {
        "logo": "/img/logos/google.svg",
        "name": "Google",
        "slug": "google"
      }
    ],
    "models": [
      {
        "creator": {
          "logo": "/img/logos/google.svg",
          "name": "Google",
          "slug": "google"
        },
        "deprecated": false,
        "name": "Gemini 4 Carbon (High)",
        "release": {
          "name": "Gemini 4 Carbon",
          "slug": "gemini-4-carbon"
        },
        "releaseDate": "2026-10-28",
        "releaseSlug": "gemini-4-carbon",
        "slug": "gemini-4-carbon"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.models[].slug` | Unique ID of the model variant, for example `gemini-4-carbon-medium`. |
| `data.models[].name` | Display name of the variant. The effort level is shown in brackets, for example `Gemini 4 Carbon (High)`. |
| `data.models[].releaseSlug / data.models[].release.slug` | Slug of the release the variant belongs to. Variants of the same release share this value. |
| `data.models[].release.name` | Display name of the release, without the effort level. |
| `data.models[].releaseDate` | Release date in `YYYY-MM-DD` format. |
| `data.models[].deprecated` | Boolean. `true` if the model is marked as deprecated. |
| `data.models[].creator.name / data.models[].creator.slug` | Name and slug of the company that created the model. |
| `data.models[].creator.logo` | Relative path to the creator logo image. |
| `data.creators[]` | List of creators with `name`, `slug` and `logo`. Use it as a lookup table for creator filters. |

### Notes

- The request body is empty (`{}`). The response is not paginated in this example.
- The `slug` of a variant can equal its `releaseSlug` (for example `gemini-4-carbon`), so use `slug` to tell variants apart.
- To find a model by name, try [Artificial Analysis Search Models](/apis/artificial-analysis/search-models).
- For cost data, see [Artificial Analysis Cost Per Task](/apis/artificial-analysis/cost-per-task).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/artificial-analysis/models-list.json`](../../../catalog/models/artificial-analysis/models-list.json) · Store page: https://www.sandbase.ai/model/artificial-analysis/models-list
