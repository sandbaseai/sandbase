# Bilibili Dynamic Details (V2) API: pricing, parameters and code examples

`bilibili/web/dynamic-detail-v2` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed data for a specific Bilibili dynamic post using its dynamic ID. Designed for video dynamics, providing author modules and engagement metrics such as comments, shares, and likes.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/dynamic-detail-v2", "dynamic_id": "1172584638000922630"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/dynamic-detail-v2', {'dynamic_id': '1172584638000922630'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/dynamic-detail-v2", {
  "dynamic_id": "1172584638000922630"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/dynamic-detail-v2", sandbase.Params{
	"dynamic_id": "1172584638000922630",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/dynamic-detail-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `dynamic_id` | string | yes | Dynamic id  |

## Details

Returns the details of one Bilibili dynamic post, including the author module, the text description and any attached images. It needs one input, the `dynamic_id` of the post.

### Use cases

- Read the text and publish time of a Bilibili dynamic post from its ID.
- Collect the author name, `mid` and verification title of the account that posted a dynamic.
- Download the image URLs attached to an image dynamic.
- Copy the share link of a dynamic post for use in reports or dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/dynamic-detail-v2" \
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
        "like_icon": {},
        "rid_str": "385887198",
        "rtype": 2
      },
      "id_str": "1172584638000922630",
      "modules": [
        {
          "module_author": {
            "decorate_card": null,
            "more": {
              "three_point_items": [
                {
                  "label": "复制动态地址",
                  "params": {
                    "link": "https://t.bilibili.com/1172584638000922630?share_source=pc_native"
                  },
                  "type": "THREE_POINT_COPY"
                }
              ]
            },
            "pub_text": "2026年02月23日 21:07",
            "pub_ts": 1771852036,
            "relation": null,
            "show_follow": false,
            "user": {
              "face": "https://i2.hdslb.com/bfs/face/6b2ade215ea603b495648875c925172a863d16d4.jpg",
              "face_nft": false,
              "mid": 17819768,
              "name": "电影最TOP",
              "official": {
                "desc": "",
                "role": 1,
                "title": "2025百大UP主、2024百大UP主、知名影视UP主",
                "type": 0
              },
              "pendant": {
                "expire": 0,
                "image": "",
                "image_enhance": "",
                "image_enhance_frame": "",
                "n_pid": 0,
                "name": "",
                "pid": 0
              },
              "vip": {
                "avatar_icon": {
                  "icon_resource": {},
                  "icon_type": 1
                },
                "avatar_subscript": 1,
                "avatar_subscript_url": "",
                "due_date": 1828022400000,
                "label": {
                  "bg_color": "#FB7299",
                  "bg_style": 1,
                  "border_color": "",
                  "img_label_uri_hans": "https://i0.hdslb.com/bfs/activity-plat/static/20220608/e369244d0b14644f5e1a06431…",
                  "img_label_uri_hans_static": "https://i0.hdslb.com/bfs/vip/8d7e624d13d3e134251e4174a7318c19a8edbd71.png",
                  "img_label_uri_hant": "",
                  "img_label_uri_hant_static": "https://i0.hdslb.com/bfs/activity-plat/static/20220614/e369244d0b14644f5e1a06431…",
                  "label_theme": "annual_vip"
                },
                "nickname_color": "#FB7299",
                "role": 3,
                "status": 1
              }
            }
          },
          "module_type": "MODULE_TYPE_AUTHOR"
        }
      ],
      "type": "DYNAMIC_TYPE_DRAW",
      "visible": true
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
| `data.item.type` | The dynamic type, for example `DYNAMIC_TYPE_DRAW` for an image post. |
| `data.item.basic.rid_str / data.item.basic.rtype` | The resource ID of the post content and its numeric resource type. |
| `data.item.modules[].module_type` | Names the module in each list entry. Values seen are `MODULE_TYPE_AUTHOR`, `MODULE_TYPE_DESC` and `MODULE_TYPE_DYNAMIC`. |
| `data.item.modules[].module_author.user.mid / data.item.modules[].module_author.user.name` | The numeric user ID and display name of the author. |
| `data.item.modules[].module_author.pub_ts / data.item.modules[].module_author.pub_text` | The publish time as a Unix timestamp and as formatted text. |
| `data.item.modules[].module_author.user.official.title` | The verification title shown on the author's account. |
| `data.item.modules[].module_desc.text` | The plain text of the post. |
| `data.item.modules[].module_dynamic.dyn_draw.items[].src` | The URL of each attached image. `width`, `height` and `size` sit beside it. |
| `data.item.modules[].module_author.more.three_point_items[].params.link` | The share link of the dynamic, found in the item of type `THREE_POINT_COPY`. |

### Notes

- The `modules` list holds one object per module. Find each one by its `module_type` and do not rely on its position.
- The sample dynamic is an image post (`DYNAMIC_TYPE_DRAW`), so the response has `dyn_draw` and no engagement counts. Other dynamic types may return different modules.
- Pass `dynamic_id` as a string. It is a long number and the response returns it as `id_str`.
- `pub_ts` is a Unix timestamp. `pub_text` shows the same time as text.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/dynamic-detail-v2.json`](../../../../catalog/models/bilibili/web/dynamic-detail-v2.json) · Store page: https://www.sandbase.ai/model/bilibili/web/dynamic-detail-v2
