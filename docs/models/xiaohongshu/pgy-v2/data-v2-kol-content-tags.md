# Xiaohongshu PGY Creator Content Tags API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/data-v2-kol-content-tags` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Content category tags of a Xiaohongshu (RedNote) Pugongying creator by user ID, showing which subjects the creator publishes about.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/data-v2-kol-content-tags", "userId": "5c668b3e0000000012021605"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/data-v2-kol-content-tags', {'userId': '5c668b3e0000000012021605'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/data-v2-kol-content-tags", {
  "userId": "5c668b3e0000000012021605"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/data-v2-kol-content-tags", sandbase.Params{
	"userId": "5c668b3e0000000012021605",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/data-v2-kol-content-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | KOL's user ID.  |

## Details

This API returns the content category tags of a Xiaohongshu (RedNote) Pugongying creator. It needs the creator's `userId` and returns a list of tags, each with a `name` such as a topic label.

### Use cases

- Check which subjects a creator publishes about before you shortlist them for a campaign.
- Filter a list of creators by topic, for example keep only those tagged with food or travel.
- Compare the tag lists of several creators to find overlap in subject matter.
- Add content category labels to an internal creator database.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/data-v2-kol-content-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "5c668b3e0000000012021605"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | KOL's user ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "createTime": null,
    "id": null,
    "name": "美食",
    "proTag": null,
    "reason": null,
    "status": null,
    "tagId": null,
    "updateTime": null
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[].name` | Content category label for the creator, for example `美食` (food) or `出行旅游` (travel). Each item in the list is one tag. |
| `[].tagId / [].id / [].proTag` | Tag identifiers and tag type fields. They are `null` in the sample response, so do not rely on them. |
| `[].createTime / [].updateTime` | Tag creation and update times. They are `null` in the sample response. |
| `[].status / [].reason` | Tag status and reason fields. They are `null` in the sample response. |

### Notes

- The response is a plain list of tag objects. Use the `name` value as the tag. The other keys can be `null`.
- The `userId` is a 24-character hex string, for example `5c668b3e0000000012021605`.
- To find a creator's `userId`, use [Xiaohongshu Pugongying Creator Search](/apis/xiaohongshu/pgy-v2/blogger-v2).
- For profile details of the same creator, call [Xiaohongshu Pugongying Creator Profile](/apis/xiaohongshu/pgy-v2/blogger-user-id).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/data-v2-kol-content-tags.json`](../../../../catalog/models/xiaohongshu/pgy-v2/data-v2-kol-content-tags.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/data-v2-kol-content-tags
