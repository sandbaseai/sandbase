# DataForSEO Google Dataset Search Results API: pricing, parameters and code examples

`dataforseo/v3/serp/google/dataset_search/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Google Dataset Search results for a keyword: dataset titles, providers, formats and last-modified dates.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/dataset_search/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/dataset_search/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/dataset_search/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/dataset_search/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/dataset_search/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns Google Dataset Search results for a keyword. Each result is a dataset with its description, authors, providers, file formats and licenses. The API needs a `keyword`, and you can add `location_code` and `language_code`.

### Use cases

- Find open datasets on a topic such as climate before starting a research project.
- Check which licenses and file formats datasets on a topic use.
- Track which authors and organizations publish datasets for a keyword.
- Build a list of dataset IDs and descriptions to review or catalog.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/dataset_search/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "climate", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query. |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "serp",
        "device": "desktop",
        "function": "live",
        "keyword": "climate",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "google"
      },
      "id": "11030829-1614-0139-0000-90b8dd2033f2",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://datasetsearch.research.google.com/search?query=climate&hl=en",
          "datetime": "2026-11-03 08:29:23 +00:00",
          "item_types": [
            "dataset"
          ],
          "items": [
            {
              "area_covered": [
                "Europe"
              ],
              "authors": [
                {
                  "domain": null,
                  "name": "ECMWF",
                  "type": "authors_element",
                  "url": null
                }
              ],
              "dataset_description": {
                "links": null,
                "text": "This dataset provides the derived climate indicators developed for the European …"
              },
              "dataset_id": "L2cvMTFudzljbDltdg==",
              "dataset_providers": [
                {
                  "domain": null,
                  "title": "European Centre for Medium-Range Weather Forecasts",
                  "type": "dataset_providers_element",
                  "url": null
                }
              ],
              "formats": [
                {
                  "format": "netcdf-4",
                  "size": 4,
                  "type": "formats_element"
                }
              ],
              "image_url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRnuGxAndms337mhnT-hA9uTjmI…",
              "licenses": [
                {
                  "domain": "creativecommons.org",
                  "title": "Attribution 4.0 (CC BY 4.0)",
                  "type": "licenses_element",
                  "url": "https://creativecommons.org/licenses/by/4.0/"
                }
              ]
            }
          ],
          "items_count": 20,
          "keyword": "climate",
          "language_code": "en",
          "se_domain": "datasetsearch.research.google.com"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "2.2526 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "2.3482 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].dataset_id` | Identifier of the dataset in the results. |
| `tasks[].result[].items[].dataset_description.text` | Short description of the dataset. The text can be cut off. |
| `tasks[].result[].items[].authors[].name` | Name of the author or authors. One entry can hold several names separated by semicolons. |
| `tasks[].result[].items[].dataset_providers[].title` | Name of the organization that provides the dataset. The field is `null` for some datasets. |
| `tasks[].result[].items[].area_covered` | List of places the dataset covers, such as a region or country. |
| `tasks[].result[].items[].formats[].format / tasks[].result[].items[].formats[].size` | File format of the dataset, for example `netcdf-4`, and its `size` when one is given. Both can be `null`. |
| `tasks[].result[].items[].licenses[].title / tasks[].result[].items[].licenses[].url` | License name and a link to the license text. The field is `null` when no license is listed. |
| `tasks[].result[].items_count` | Number of dataset items in the result. |
| `tasks[].result[].check_url` | Google Dataset Search URL for the same query. |

### Notes

- Set `location_code` to a code such as `2840` for the United States, and `language_code` to a code such as `en`.
- Many fields are `null` for some datasets, so check each one before you use it.
- Results are in `tasks[].result`, and `tasks[].result[].items[]` holds the datasets.

### Pricing

Billed at the actual cost of each call, about $0.002 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/dataset_search/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/dataset_search/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/dataset_search/live/advanced
