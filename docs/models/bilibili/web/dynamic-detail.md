# Bilibili Dynamic Detail API: pricing, parameters and code examples

`bilibili/web/dynamic-detail` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specified Bilibili dynamic post, such as image, text, or article dynamics, using its unique dynamic ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/dynamic-detail", "dynamic_id": "1172584638000922630"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/dynamic-detail', {'dynamic_id': '1172584638000922630'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/dynamic-detail", {
  "dynamic_id": "1172584638000922630"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/dynamic-detail", sandbase.Params{
	"dynamic_id": "1172584638000922630",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/dynamic-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `dynamic_id` | string | yes | Dynamic id  |

## Details

Returns the structure of one Bilibili dynamic post, such as a text, image, or article post. It needs the post's `dynamic_id` and returns basic info plus a list of content modules, such as the author and the content paragraphs.

### Use cases

- Read the author avatar URL and `mid` for a known dynamic post.
- Check the comment type and comment ID of a post before you fetch its comments.
- Store the module layout of a dynamic post for later analysis.
- Check whether a post is fans-only or editable.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/dynamic-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"dynamic_id": "1172584638000922630"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `dynamic_id` | string | Yes | Dynamic id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "item": {
      "basic": {
        "aigc": false,
        "article_type": 0,
        "comment_id_str": "385887198",
        "comment_type": 11,
        "editable": false,
        "is_only_fans": false,
        "like_icon": {
          "action_url": "",
          "end_url": "",
          "id": "0",
          "start_url": ""
        },
        "open_app_extra": ""
      },
      "id_str": "1172584638000922630",
      "modules": [
        {
          "module_author": null,
          "module_blocked": null,
          "module_bottom": null,
          "module_collection": null,
          "module_content": null,
          "module_copyright": null,
          "module_dispute": null,
          "module_extend": null
        }
      ],
      "type": 0
    }
  },
  "message": "0",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.item.id_str` | The dynamic ID as a string. It matches the `dynamic_id` you sent. |
| `data.item.type` | Numeric type code of the dynamic. The response gives `0` for this post and does not label the codes. |
| `data.item.basic.comment_id_str / data.item.basic.comment_type` | The ID and type code used to identify the comment area of this post. In this response they are `385887198` and `11`. |
| `data.item.basic.is_only_fans` | Boolean flag. `true` marks a fans-only post. |
| `data.item.basic.editable` | Boolean flag. It shows whether the post can be edited. |
| `data.item.basic.aigc` | Boolean flag. It is `false` for this post. |
| `data.item.modules[].module_author.face` | URL of the author's avatar image. |
| `data.item.modules[].module_author.avatar.mid` | The author's numeric user ID, as a string. |
| `data.item.modules[].module_content.paragraphs[]` | List of content paragraphs. Each item has `align` and `format` plus fields such as `heading`, `list`, and `link_card`. Fields that do not apply are `null`. |
| `data.item.modules[]` | List of modules. Each item holds one named module, such as `module_author` or `module_content`. Modules that do not apply to the item are `null`. |

### Notes

- Each entry in `data.item.modules[]` fills only one module key, so loop over the list and skip `null` values.
- `dynamic_id` is a long numeric string. Send it as a string.
- For a newer response layout, try [Bilibili Dynamic Details (V2)](/apis/bilibili/web/dynamic-detail-v2).
- To find dynamic IDs for a user, call [Bilibili User Dynamics](/apis/bilibili/web/user-dynamic).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/dynamic-detail.json`](../../../../catalog/models/bilibili/web/dynamic-detail.json) · Store page: https://www.sandbase.ai/model/bilibili/web/dynamic-detail
