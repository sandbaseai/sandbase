# Kuaishou Web Hot List API: pricing, parameters and code examples

`kuaishou/web/hot-list-v1` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the current trending hot list from Kuaishou Web. It delivers trending topics and popular content rankings directly from the platform.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/hot-list-v1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/hot-list-v1', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/hot-list-v1", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/hot-list-v1", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/web/hot-list-v1` with the body above minus `model`.

## Details

Returns the current Kuaishou Web hot list as an array of ranked trending topics. Each item has a name, a rank, a heat value and linked video IDs. The API takes no input parameters.

### Use cases

- Snapshot the top trending topics on Kuaishou at a set time each day.
- Compare `hotValue` across topics to see which trends draw the most attention.
- Collect `photoIds` for each topic to fetch the related videos in a later call.
- Flag pinned or rising topics through `tagType` and `iconUrl`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/hot-list-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "__typename": "VisionHotRankItem",
    "hotValue": null,
    "iconUrl": "https://p66.a.yximgs.com/udata/pkg/nebula-app/rank_tag_rising3x.png",
    "id": "让互联网更好造福人民造福世界",
    "name": "让互联网更好造福人民造福世界",
    "photoIds": {
      "json": [
        "3xmtwfbf6h99thk"
      ],
      "type": "json"
    },
    "poster": "http://v23-3.kwaicdn.com/upic/2026/11/02/07/BMjAyNjExMDIwNzQ4NDdfMTMxMjExOTkyNV8…",
    "rank": 0,
    "tagType": "置顶",
    "viewCount": null
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[].name` | Title of the trending topic. In the sample, `id` holds the same text. |
| `[].rank` | Position in the list. The first item is `0`. |
| `[].hotValue` | Heat value as a display string, such as `1188.2万`. It is `null` for the pinned item. |
| `[].tagType` | Label for the item, such as `置顶` (pinned). It is `null` when the item has no label. |
| `[].iconUrl` | URL of a tag icon image. It is `null` when the item has no icon. |
| `[].photoIds.json[]` | IDs of the videos or photo posts linked to the topic. |
| `[].poster` | URL of a cover image for the topic. |
| `[].viewCount` | View count for the topic. It is `null` in the sample items. |
| `[].id` | Identifier of the topic. In the sample it is the same text as `name`. |

### Notes

- Send an empty JSON object `{}` as the request body. The API has no parameters and no pagination.
- Use the values in `photoIds.json` with [Kuaishou Single Video Details](/apis/kuaishou/web/one-video) to load each linked video.
- For another trending view, call [Kuaishou Web Hot List (V2)](/apis/kuaishou/web/hot-list-v2).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Web Share Short URL](/apis/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List (V2)](/apis/kuaishou/web/hot-list-v2): Returns current trending search rankings and hot topics on Kuaishou web.

---
Machine-readable: [`catalog/models/kuaishou/web/hot-list-v1.json`](../../../../catalog/models/kuaishou/web/hot-list-v1.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/hot-list-v1
