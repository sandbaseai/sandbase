# Bilibili App User Info API: pricing, parameters and code examples

`bilibili/app/user-info` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns account profile details and uploaded video archives for a specified Bilibili creator using their unique user identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/user-info", "user_id": "203680252"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/user-info', {'user_id': '203680252'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/user-info", {
  "user_id": "203680252"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/user-info", sandbase.Params{
	"user_id": "203680252",
})
```

Same call via the path form: `POST /v1/api/bilibili/app/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User ID (required)  |

## Details

Returns the profile card and the uploaded video list for one Bilibili creator. It needs the creator's numeric `user_id`.

### Use cases

- Pull a creator's profile card, follow count and badges into a talent database.
- List a creator's latest uploads with their `bvid` and publish time to track posting activity.
- Check the total number of uploaded videos and articles for a creator before a deeper crawl.
- Collect cover images and author names of recent videos for a creator dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "203680252"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID (required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "ad_container_path": "bilibili://mall/smallshop?msource=cps_productTab_203680252&from=cps_productTab_2…",
    "ad_shop_type": 2,
    "ad_source_content_v2": {
      "ad_content": {
        "extra": {
          "card": {
            "button": {
              "jump_url": "bilibili://mall/web?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetailshop…",
              "text": "",
              "type": 1
            },
            "card_type": 33,
            "covers": [
              {
                "url": "https://i0.hdslb.com/bfs/kfptfe/floor/6a4b179b4e8a6069468f9b32e4d4ebcaf6a7b628.p…"
              }
            ],
            "jump_url": "bilibili://mall/web?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetailshop…",
            "title": "小店"
          },
          "sales_type": 12,
          "upzone_entrance_report_id": "203680252",
          "upzone_entrance_type": 1
        }
      }
    },
    "archive": {
      "count": 1967,
      "episodic_button": {
        "text": "播放全部",
        "uri": "bilibili://music/playlist/spacepage/203680252?desc=1&offset=0&oid=0&order=time&p…"
      },
      "item": [
        {
          "author": "AYCS2",
          "bvid": "BV1oY4u6REdF",
          "cover": "http://i0.hdslb.com/bfs/archive/c80f8c142e993379aa9ac7cd7520cfc219d1f0e3.jpg",
          "cover_icon": "",
          "cover_left_icon": "",
          "cover_left_text": "",
          "ctime": 1793671323,
          "danmaku": 60
        }
      ],
      "order": [
        {
          "title": "最新发布",
          "value": "pubdate"
        }
      ]
    },
    "article": {
      "count": 1,
      "item": [
        {
          "act_id": 0,
          "apply_time": "",
          "attributes": 148,
          "authenMark": null,
          "author": {
            "face": "https://i1.hdslb.com/bfs/face/cf421068a26ce754e95a46e7cee101b5b04dbb02.jpg",
            "mid": 203680252,
            "name": "AYCS2",
            "nameplate": {
              "condition": "所有自制视频总播放数>=100万，数据次日更新",
              "image": "https://i0.hdslb.com/bfs/face/27a952195555e64508310e366b3e38bd4cd143fc.png",
              "image_small": "https://i1.hdslb.com/bfs/face/0497be49e08357bf05bca56e33a0637a273a7610.png",
              "level": "稀有勋章",
              "name": "知名偶像",
              "nid": 8
            },
            "official_verify": {
              "desc": "bilibili 知名游戏UP主",
              "type": 0
            },
            "pendant": {
              "expire": 0,
              "image": "",
              "name": "",
              "pid": 0
            },
            "vip": {
              "avatar_subscript": 1,
              "due_date": 0,
              "label": {
                "label_theme": "annual_vip",
                "path": "http://i0.hdslb.com/bfs/vip/label_annual.png",
                "text": "年度大会员"
              },
              "nickname_color": "#FB7299",
              "status": 1,
              "theme_type": 0,
              "type": 2,
              "vip_pay_type": 0
            }
          },
          "banner_url": "",
          "categories": [
            {
              "id": 3,
              "name": "生活",
              "parent_id": 0
            }
          ],
          "category": {
            "id": 15,
            "name": "日常",
            "parent_id": 3
          }
        }
      ],
      "lists": [],
      "lists_count": 0
    },
    "audios": {
      "count": 0,
      "item": []
    },
    "card": {
      "DisplayRank": "",
      "achieve": {
        "achieve_url": "https://www.bilibili.com/h5/achieve?navhide=1&mid=203680252",
        "image": "https://i1.hdslb.com/bfs/face/0497be49e08357bf05bca56e33a0637a273a7610.png",
        "is_default": false
      },
      "approve": false,
      "article": 0,
      "attention": 307,
      "attentions": null,
      "avatar": {
        "container_size": {
          "height": 1.5,
          "width": 1.5
        },
        "fallback_layers": {
          "is_critical_group": true,
          "layers": [
            {
              "general_spec": {
                "pos_spec": {
                  "axis_x": 0.75,
                  "axis_y": 0.75,
                  "coordinate_pos": 2
                },
                "render_spec": {
                  "opacity": 1
                },
                "size_spec": {
                  "height": 1.05,
                  "width": 1.05
                }
              },
              "layer_config": {
                "is_critical": true,
                "tags": {
                  "AVATAR_LAYER": {}
                }
              },
              "resource": {
                "res_native_draw": {
                  "draw_src": {
                    "draw": {
                      "color_config": {
                        "day": {
                          "argb": "#FFFFFFFF"
                        },
                        "is_dark_mode_aware": true,
                        "night": {
                          "argb": "#FF17181A"
                        }
                      },
                      "draw_type": 1,
                      "fill_mode": 1
                    },
                    "src_type": 3
                  }
                },
                "res_type": 5
              },
              "visible": true
            }
          ]
        },
        "layers": [
          {
            "is_critical_group": true,
            "layers": [
              {
                "general_spec": {
                  "pos_spec": {
                    "axis_x": 0.75,
                    "axis_y": 0.75,
                    "coordinate_pos": 2
                  },
                  "render_spec": {
                    "opacity": 1
                  },
                  "size_spec": {
                    "height": 1.05,
                    "width": 1.05
                  }
                },
                "layer_config": {
                  "is_critical": true,
                  "tags": {
                    "AVATAR_LAYER": {}
                  }
                },
                "resource": {
                  "res_native_draw": {
                    "draw_src": {
                      "draw": {
                        "color_config": {
                          "day": {
                            "argb": "#FFFFFFFF"
                          },
                          "is_dark_mode_aware": true,
                          "night": {
                            "argb": "#FF17181A"
                          }
                        },
                        "draw_type": 1,
                        "fill_mode": 1
                      },
                      "src_type": 3
                    }
                  },
                  "res_type": 5
                },
                "visible": true
              }
            ]
          }
        ],
        "mid": "203680252"
      },
      "birthday": "",
      "control": 0,
      "description": "",
      "digital_id": "",
      "digital_type": -2
    },
    "cheese": {
      "count": 0,
      "item": []
    },
    "coin_archive": {
      "count": 12,
      "item": [
        {
          "author": "BML制作指挥部 等联合创作",
          "cover": "http://i2.hdslb.com/bfs/archive/765d98a7cb2679a819b69050677cbb995081bc64.jpg",
          "cover_icon": "",
          "cover_left_icon": "",
          "cover_left_text": "",
          "ctime": 1783857977,
          "danmaku": 902,
          "duration": 250
        }
      ]
    },
    "comic": {
      "count": 0,
      "item": []
    },
    "default_tab": "video",
    "digital_button": null
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.archive.count` | Total number of uploaded video archives for this creator. |
| `data.archive.item[].bvid` | The BV ID of the video. Use it to identify the video in other Bilibili APIs. |
| `data.archive.item[].author / data.archive.item[].cover` | The creator name shown on the video and the URL of its cover image. |
| `data.archive.item[].ctime` | Timestamp of the video. The value looks like a Unix time in seconds. |
| `data.archive.item[].danmaku` | Danmaku (on-screen comment) count shown for the video. |
| `data.archive.order[].title / data.archive.order[].value` | Sort options for the video list. The `value` entries are `pubdate` and `click`. |
| `data.article.count` | Number of articles the creator has published. |
| `data.article.item[].author.name / data.article.item[].author.mid` | Display name and numeric user ID of the article author. |
| `data.article.item[].author.official_verify.desc` | Verification text on the account, such as the official creator title. |
| `data.card.attention` | Count shown in the profile card's `attention` field, which is the number of accounts this user follows. |

### Notes

- Pass the creator's numeric ID as `user_id`, for example `203680252`. If you only have a profile link, use [Bilibili User ID Extraction](/apis/bilibili/web/get-user-id) to get it.
- The `data.archive.item[]` list in this response holds a short page of videos. For the full video list, call [Bilibili User Videos](/apis/bilibili/app/user-videos).
- Use the `bvid` value from `data.archive.item[]` with [Bilibili App Single Video Details](/apis/bilibili/app/one-video) to get details of one video.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili App Bangumi Tab](/apis/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/apis/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/apis/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.

---
Machine-readable: [`catalog/models/bilibili/app/user-info.json`](../../../../catalog/models/bilibili/app/user-info.json) · Store page: https://www.sandbase.ai/model/bilibili/app/user-info
