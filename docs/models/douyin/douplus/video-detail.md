# Douyin Douplus Video Detail API: pricing, parameters and code examples

`douyin/douplus/video-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Douyin video details using a direct video ID or a shared link. Input video identifiers or share text containing short links to inspect video metadata.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/douplus/video-detail", "video": "7651708301280906538"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/douplus/video-detail', {'video': '7651708301280906538'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/douplus/video-detail", {
  "video": "7651708301280906538"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/douplus/video-detail", sandbase.Params{
	"video": "7651708301280906538",
})
```

Same call via the path form: `POST /v1/api/douyin/douplus/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | Video ID, or share link/text (required). e.g. `7651708301280906538`, or a share caption containing a v.douyin.com link  |

## Details

Look up a Douyin video in the DOU+ promotion tool by video ID or share link: caption, publish time, author with follower count, and like, comment and share counts.

### Use cases

- Check a video before buying DOU+ promotion for it.
- Get basic stats for a video from a share link.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/douplus/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video": "7651708301280906538"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `video` | string | Yes | Video ID, or share link/text (required). e.g. `7651708301280906538`, or a share caption containing a v.douyin.com link |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "itemList": [
      {
        "AwemeInfo": {
          "AwemeId": "7651708301280906538",
          "Desc": "观看major下来，理性讨论下战队排名 #csgo茄子 #茄子cs解说 #科隆major #csgo",
          "CreateTime": "1781552198000",
          "Author": {
            "Nickname": "csgo茄子",
            "FollowerCount": 9757566
          },
          "Statistics": {
            "DiggCount": 49974,
            "CommentCount": 2195,
            "ShareCount": 687
          }
        }
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.itemList[].AwemeInfo.AwemeId / Desc` | Video ID and caption. |
| `AwemeInfo.CreateTime` | Publish time, Unix milliseconds. |
| `AwemeInfo.Author` | `Nickname`, `FollowerCount`, `SecUid`. |
| `AwemeInfo.Statistics` | `DiggCount`, `CommentCount`, `ShareCount`. |

### Notes

- `video` accepts a numeric video ID or a share link.

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin DOU+ Promotable Items](/apis/douyin/douplus/promotable-item-list): Returns the promotable video item list for a Douyin account on the DOU+ promotion page.
- [Douyin DOU+ User Search](/apis/douyin/douplus/search-user): Searches for Douyin users in the DOU+ delivery context using a Douyin ID or nickname.
- [Douyin DOU+ Talent Categories](/apis/douyin/douplus/talent-categories): Returns the Douyin DOU+ talent category directory.

---
Machine-readable: [`catalog/models/douyin/douplus/video-detail.json`](../../../../catalog/models/douyin/douplus/video-detail.json) · Store page: https://www.sandbase.ai/model/douyin/douplus/video-detail
