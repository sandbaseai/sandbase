# Pipixia Home Short Drama Feed API: pricing, parameters and code examples

`pipixia/app/home-short-drama-feed` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns short drama and novel recommendations from the Pipixia home feed. Supports pagination to browse through items sequentially.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/home-short-drama-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/home-short-drama-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/home-short-drama-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/home-short-drama-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/pipixia/app/home-short-drama-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default is 1, add 1 for each page. default `1` |

## Details

Returns short drama and novel recommendations from the Pipixia home feed, grouped into feed cells such as a popular titles shelf. The only input is an optional `page` number, which defaults to 1.

### Use cases

- Pull the current list of popular short dramas and novels shown on the Pipixia home feed.
- Rank titles by their `hot` value to see which ones lead a feed shelf.
- Group recommended titles by `category` to see which genres appear most often.
- Collect `book_id` values to track which titles appear on the feed from one page to the next.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/home-short-drama-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number, default is 1, add 1 for each page. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": [
    {
      "cell_id": "2040003",
      "cell_name": "大家都在看",
      "cell_type": 204,
      "channel_id": "94349610839",
      "feed_data": {
        "book_data": [
          {
            "book_data": {
              "book_id": "7663434332274428952",
              "book_name": "重回千禧我靠赶海养活家人",
              "book_type": "0",
              "category": "种田",
              "category_tags": [
                {
                  "CategoryId": 23,
                  "CategoryName": "种田",
                  "Dim": "",
                  "Gender": 0,
                  "category_schema_url": null
                }
              ],
              "creation_status": "0",
              "genre": "205",
              "highlight_category_tag": null
            },
            "category_v2": [],
            "hot": 22732164,
            "toutiao_click_rate": "0"
          }
        ],
        "has_more": true,
        "is_recommend": true
      },
      "show_num": 0,
      "visible_refresh": 0
    }
  ],
  "extra": {
    "enable_grey": "0"
  },
  "log_id": "20261103154147BACA29F5B15BF0D5667D",
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].cell_name` | Display name of the feed cell, for example `大家都在看`. Use it to tell shelves apart. |
| `data[].cell_id / data[].cell_type` | Identifier and numeric type of the feed cell. Some cells, such as `自动播大卡`, have no `feed_data`. |
| `data[].feed_data.book_data[].book_data.book_id` | ID of the drama or novel, returned as a string. |
| `data[].feed_data.book_data[].book_data.book_name` | Title of the drama or novel. |
| `data[].feed_data.book_data[].book_data.category` | Main category of the title, for example `种田` or `武侠`. |
| `data[].feed_data.book_data[].book_data.category_tags[].CategoryName` | Name of each category tag on the title. `CategoryId` holds the matching numeric ID. |
| `data[].feed_data.book_data[].hot` | Numeric hot value of the title. Higher values appear first in this response. |
| `data[].feed_data.book_data[].book_data.creation_status` | Creation status code of the title, returned as a string such as `0` or `1`. |
| `data[].feed_data.has_more` | Is `true` when the cell has more items to load. |
| `log_id` | Identifier of this response. |

### Notes

- Send `page` as an integer. Start at 1 and add 1 for each further page.
- Not every item in `data` carries `feed_data`, so check that it exists before reading `book_data`.
- IDs such as `book_id` are long numeric strings. Keep them as strings in your code.
- To browse regular posts instead of dramas, call [Pipixia App Home Feed](/apis/pipixia/app/home-feed).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/home-short-drama-feed.json`](../../../../catalog/models/pipixia/app/home-short-drama-feed.json) · Store page: https://www.sandbase.ai/model/pipixia/app/home-short-drama-feed
