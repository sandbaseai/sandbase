# Xiaohongshu User Search API: pricing, parameters and code examples

`xiaohongshu/search-user` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Search Xiaohongshu (RedNote) users by keyword with page-based pagination. Use it to support creator discovery, account research, and finding profiles related to a topic, name, or brand term.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/search-user", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/search-user', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/search-user", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/search-user", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/search-user` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `keyword` | string | yes | Search keyword.  |

## Details

This API returns Xiaohongshu (RedNote) user accounts that match a search keyword. It needs one input, `keyword`, and accepts an optional `page` number for more results.

### Use cases

- Find creator accounts that post about a topic such as food by searching a topic keyword.
- Check whether a brand name or person name matches existing Xiaohongshu accounts.
- Build a shortlist of profiles with their follower counts shown in `sub_title` for outreach research.
- Collect user IDs from search results to look up each profile in more detail.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/search-user" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "美食"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `page` | integer | No | Page number for pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "filters": [
    {
      "filter_tags": [
        {
          "icon_tail_url": "",
          "icon_tail_url_night": "",
          "icon_url": "",
          "icon_url_night": "",
          "id": "all",
          "name": "不限",
          "need_location_info": false,
          "origin_text": ""
        }
      ],
      "group_show_type": 0,
      "id": "fans_count",
      "invisible": true,
      "name": "粉丝数量",
      "type": "single",
      "word_request_id": "5c1334adfe1832dc352490d37357c71a"
    }
  ],
  "users": [
    {
      "desc": "小红书号：d10686543",
      "followed": false,
      "id": "5f956ca30000000001006e76",
      "image": "https://sns-avatar-qc.xhscdn.com/avatar/5fe98a2e6a06fb6dec28c1d4.jpg?imageView2/…",
      "link": "xhsdiscover://1/user/user.5f956ca30000000001006e76",
      "name": "美食",
      "reason": "",
      "red_id": "d10686543",
      "red_official_verified": false,
      "red_official_verify_type": 0,
      "self": false,
      "show_red_official_verify_icon": false
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `users[]` | List of user accounts that match the keyword. Each item is one profile. |
| `users[].id` | Internal user ID of the account. It also appears inside the `link` value. |
| `users[].red_id` | The public Xiaohongshu ID of the account. The same number appears in `desc` after the label 小红书号. |
| `users[].name` | Display name of the account. |
| `users[].sub_title` | Short follower label as shown in the app, for example `粉丝 6万`. It is display text, not a number. |
| `users[].image` | URL of the account avatar image. |
| `users[].link` | App deep link that opens the user profile in the Xiaohongshu app. |
| `users[].red_official_verified / users[].red_official_verify_type / users[].show_red_official_verify_icon` | Flags for official verification. The `false` and `0` values in the sample mean the account is not verified. |
| `users[].followed / users[].self` | Whether the account is already followed, and whether it is the calling account itself. |
| `filters[].id / filters[].name / filters[].filter_tags[]` | Filter groups the app offers, such as `fans_count` and `user_type`. Each tag has an `id` and a display `name`. |

### Notes

- Send `page` to get the next set of results. It starts at 1 and the sample request used the default.
- Follower counts come as text such as `粉丝 4.2万`, so parse them if you need numbers.
- User IDs in `users[].id` are 24-character hex strings. Use them with [Xiaohongshu (RED) User Information](/apis/xiaohongshu/app-v2/user-info) or [Xiaohongshu (RED) User Posted Notes](/apis/xiaohongshu/app-v2/user-posted-notes) for more detail.
- The `filters` list describes filter options only. This API has no filter parameters.

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/search-user.json`](../../../catalog/models/xiaohongshu/search-user.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/search-user
