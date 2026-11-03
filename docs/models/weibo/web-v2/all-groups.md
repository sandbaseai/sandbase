# Weibo All Groups Information API: pricing, parameters and code examples

`weibo/web-v2/all-groups` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves complete group information on the Weibo platform. Returns details for both default system groups and user-defined custom groups.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/all-groups"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/all-groups', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/all-groups", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/all-groups", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/all-groups` with the body above minus `model`.

## Details

Returns the follow-group structure of the Weibo account behind the request: default system groups, the user's own groups, and subscription groups. It needs no input. Send an empty JSON object `{}`.

### Use cases

- List the group names and IDs of an account before building a group management screen.
- Check which system groups exist, such as all follows and mutual follows, and how each one is configured.
- Read the `gid` of a group to use it as a reference when working with that group elsewhere.
- Compare group layouts to see whether a custom group section or subscription section is empty.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/all-groups" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "feed_default": 1,
  "fetch_hot": "1",
  "groups": [
    {
      "group": [
        {
          "ad_scene": 1,
          "count": 0,
          "frequency": 0,
          "gid": "100012069624559340",
          "navigation_title": "关注",
          "sysgroup": 2,
          "title": "全部关注",
          "type": "1"
        }
      ],
      "group_type": 0,
      "title": "默认分组"
    }
  ],
  "is_new_segment": "1",
  "ok": 1,
  "total_number": 67,
  "trans_param": "0_1793691982"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `groups[]` | Sections of groups. Each section has a `title` such as the default groups, my groups, or subscription groups, and a `group` list. |
| `groups[].title / groups[].group_type` | Name and type code of the section. |
| `groups[].group[].gid` | ID of one group. It is a numeric string. |
| `groups[].group[].title` | Display name of the group, for example the all-follows group or the mutual-follows group. Some entries have no `title`. |
| `groups[].group[].type` | Type code of the group, returned as a string. |
| `groups[].group[].sysgroup` | Flag set on each group shown in the response. All items in the sample carry the value `2`. |
| `groups[].group[].settings.remind / groups[].group[].settings.priority` | Reminder and priority settings of a group. Present only on some groups. |
| `groups[].group[].apipath` | Timeline path attached to a group, for example `statuses/friends/timeline`. Present only on some groups. |
| `total_number` | Total number reported for the groups, `67` in the sample. |
| `ok` | Status flag. `1` means the call succeeded. |

### Notes

- This endpoint takes no parameters. Send `{}` as the body.
- The `groups` list can contain empty sections, such as a subscription section with `group` set to `[]`.
- Group IDs in `gid` are strings. Keep them as strings to avoid losing digits.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/all-groups.json`](../../../../catalog/models/weibo/web-v2/all-groups.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/all-groups
