# Douyin DOU+ Promotable Items API: pricing, parameters and code examples

`douyin/douplus/promotable-item-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the promotable video item list for a Douyin account on the DOU+ promotion page. Includes item details based on specified promotion targets and optimization objectives.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/douplus/promotable-item-list", "sec_uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/douplus/promotable-item-list', {'sec_uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/douplus/promotable-item-list", {
  "sec_uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/douplus/promotable-item-list", sandbase.Params{
	"sec_uid": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/douplus/promotable-item-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` |  |  | Number of items, default 30  |
| `aim_ids` |  |  | Optional advanced parameter — optimization objective code(s), comma separated.  |
| `sec_uid` | string | yes | sec_uid of the delivery account (required)  |
| `target_id` |  |  | Promotion target (the goal card on the DOU+ page), default 31 (likes & comments).  |

## Details

Retrieve videos eligible for DOU+ promotion for a specified Douyin user using their `sec_uid`. Customize results by item count with `count`, promotion goal via `target_id`, and optimization objective codes via `aim_ids`.

### Use cases

- Identify videos eligible for DOU+ promotion campaigns on a given Douyin account.
- Filter promotable content according to specific optimization goals and targets.
- Track DOU+ delivery candidate items alongside their metadata.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/douplus/promotable-item-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | sec_uid of the delivery account (required) |
| `count` | string | No | Number of items, default 30 |
| `aim_ids` | string | No | Optional advanced parameter — optimization objective code(s), comma separated. |
| `target_id` | string | No | Promotion target (the goal card on the DOU+ page), default 31 (likes & comments). |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "item_info_list": [
    {
      "playlet_type": 0,
      "aweme_info": {
        "aweme_id": "7691250576776709797",
        "create_time": 1790758823000,
        "desc": ". #海俪恩蛋尾巴摇摇#海俪恩美瞳#海俪恩小狗#美瞳推荐",
        "valid_anchor_type": 0
      },
      "item_source": {
        "source_type": 0
      }
    }
  ]
}
```

### Notes

- `sec_uid` is required to identify the delivery account.
- `target_id` defines the promotion goal card and defaults to 31 for likes and comments.
- `count` defines the number of items returned, defaulting to 30.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin DOU+ User Search](/apis/douyin/douplus/search-user): Searches for Douyin users in the DOU+ delivery context using a Douyin ID or nickname.
- [Douyin DOU+ Talent Categories](/apis/douyin/douplus/talent-categories): Returns the Douyin DOU+ talent category directory.
- [Douyin DOU+ Talents by Category](/apis/douyin/douplus/talents-by-category): Returns a list of DOU+ talents filtered by category name or keyword.

---
Machine-readable: [`catalog/models/douyin/douplus/promotable-item-list.json`](../../../../catalog/models/douyin/douplus/promotable-item-list.json) · Store page: https://www.sandbase.ai/model/douyin/douplus/promotable-item-list
