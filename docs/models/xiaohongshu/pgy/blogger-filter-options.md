# Xiaohongshu PGY blogger filter options API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-filter-options` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get PGY blogger filter options on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-filter-options"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-filter-options', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-filter-options", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-filter-options", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-filter-options` with the body above minus `model`.

## Details

Returns the filter options that the Xiaohongshu PGY blogger search uses. It covers activity campaigns, region trees, audience groups and industry tags. The request takes no input.

### Use cases

- Build a filter form for a blogger search tool with the same region and audience choices that PGY shows.
- Look up the code behind a region, audience or industry tag label before you filter bloggers.
- Track which PGY blogger campaigns are listed and when they start and end.
- Map industry tag ids to their Chinese labels when you read other PGY data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-filter-options" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "activities": [
      {
        "activityLabel": "平台优选",
        "activityName": "双11博主团",
        "buttonLink": "https://doc.weixin.qq.com/sheet/e3_AX0A8QY2AP0CNt7iNjy4dS0qoo0aa?scode=ANAAyQcbA…",
        "buttonName": "见具体规则",
        "code": "6adb6413e4b078c833452df1",
        "content": "活动期间合作平台推荐博主，有机会享受流量激励扶持",
        "endTime": "11/15/26 11:59 PM",
        "kolDownloadStatus": 0,
        "priority": 3,
        "show": false,
        "startTime": "10/23/26 12:00 AM"
      }
    ],
    "areas": [
      {
        "children": [
          {
            "children": [
              {
                "children": null,
                "code": "东城区",
                "level": 0,
                "name": "东城区"
              }
            ],
            "code": "北京",
            "level": 0,
            "name": "北京"
          }
        ],
        "code": "中国",
        "level": 0,
        "name": "中国"
      }
    ],
    "audience20": [
      {
        "children": [
          {
            "children": null,
            "disabled": false,
            "label": "挑战极限者",
            "value": "挑战极限者"
          }
        ],
        "disabled": false,
        "label": "自在户外",
        "value": "自在户外"
      }
    ],
    "automotiveIndustryTag": [
      {
        "children": [
          {
            "children": [
              {
                "children": [
                  {
                    "children": null,
                    "disabled": false,
                    "label": "环清-新装除甲醛",
                    "value": "19347660"
                  }
                ],
                "disabled": false,
                "label": "场景",
                "value": "6ae964ad1f150517da6dfecf"
              }
            ],
            "disabled": false,
            "label": "家用清洁",
            "value": "6ae964ad1f150517da6dfece"
          }
        ],
        "disabled": false,
        "label": "日化家清",
        "value": "6ae964ad1f150517da6dfecd"
      }
    ],
    "consumerBehavior": [
      {
        "children": [
          {
            "children": [
              {
                "children": [
                  {
                    "children": [
                      {
                        "children": [],
                        "disabled": false,
                        "label": "保时捷911",
                        "value": "保时捷911"
                      }
                    ],
                    "disabled": false,
                    "label": "Porsche",
                    "value": "Porsche"
                  }
                ],
                "disabled": false,
                "label": "预估车主作者",
                "value": "预估车主作者"
              }
            ],
            "disabled": false,
            "label": "汽车",
            "value": "汽车"
          }
        ],
        "disabled": false,
        "label": "内容行为预估",
        "value": "内容行为预估"
      }
    ],
    "contentScenes": [
      {
        "children": [
          {
            "children": [
              {
                "children": [
                  {
                    "label": "政策",
                    "tooltip": "",
                    "value": "696e2a28f057cb1c2dda6727"
                  }
                ],
                "label": "选车攻略",
                "tooltip": "",
                "value": "696e2a28f057cb1c2dda6726"
              }
            ],
            "label": "理性决策",
            "tooltip": "",
            "value": "696e2a28f057cb1c2dda6725"
          }
        ],
        "label": "汽车",
        "showNew": true,
        "tooltip": "",
        "value": "696e2a28f057cb1c2dda6724"
      }
    ],
    "contentTags": [
      {
        "taxonomy1Tag": "美妆",
        "taxonomy2Tags": [
          "整体妆容"
        ]
      }
    ],
    "contentTheme": [
      {
        "children": [
          {
            "children": null,
            "disabled": false,
            "label": "沉浸式开车",
            "value": "69786d48f02b11619e76b96a"
          }
        ],
        "disabled": false,
        "label": "汽车特色",
        "value": "69786d48f02b11619e76b969"
      }
    ],
    "fansAreas": [
      {
        "children": [
          {
            "children": [
              {
                "children": null,
                "code": "安庆",
                "level": 3,
                "name": "安庆"
              }
            ],
            "code": "安徽",
            "level": 2,
            "name": "安徽"
          }
        ],
        "code": "中国",
        "level": 1,
        "name": "中国"
      }
    ],
    "featureTags": [
      {
        "id": 1,
        "orderId": null,
        "taxonomy1Tag": "形式",
        "taxonomy2Tag": null,
        "taxonomy2Tags": [
          "vlog"
        ],
        "taxonomy3Tags": null
      }
    ],
    "industryTags": [
      {
        "id": 0,
        "orderId": 1,
        "taxonomy1Tag": "美妆个护",
        "taxonomy2Tag": null,
        "taxonomy2Tags": [
          "美妆"
        ],
        "taxonomy3Tags": null
      }
    ],
    "market": [
      {
        "children": [
          {
            "children": [
              {
                "children": null,
                "hover": "选取近30天合作笔记CPM对比同行表现优秀的作者",
                "name": "成本",
                "type": "estimateAllCpm"
              }
            ],
            "hover": null,
            "name": "曝光表现",
            "type": "impPerformance"
          }
        ],
        "hover": null,
        "name": "曝光",
        "type": "imp"
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.activities[].activityName` | Name of a PGY blogger campaign, such as `双11博主团`. |
| `data.activities[].startTime / data.activities[].endTime` | Start and end of the campaign. Values are strings like `10/23/26 12:00 AM`. |
| `data.activities[].code` | Identifier of the campaign. |
| `data.activities[].content / data.activities[].buttonLink` | Short campaign description and the link to its rules page. |
| `data.areas[].name / data.areas[].code` | Region name and its code. For regions in China the code equals the name, for example `北京`. |
| `data.areas[].children[]` | Child regions nested under a country or region. They go from country to province to city to district. The value is `null` at the lowest level. |
| `data.audience20[].label / data.audience20[].value` | Audience group name and its filter value. Each group has `children` with finer audience types. |
| `data.automotiveIndustryTag[].label / data.automotiveIndustryTag[].value` | Industry tag name and its id. Tags nest several levels deep, for example from industry to category to tag. |
| `data.automotiveIndustryTag[].children[].children[].value` | Id of a deeper tag. Leaf tags use numeric id strings like `19347660`. |

### Notes

- Send an empty JSON object `{}`. The API has no parameters.
- Leaf nodes have `children` set to `null`. Items with `disabled` set to `true` are not selectable.
- Use the returned `value` or `code` as the filter value when you search bloggers with [Xiaohongshu (RED) PGY Blogger Search](/apis/xiaohongshu/pgy/blogger-list).
- Activity items carry a `show` flag and a `priority` number.

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-filter-options.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-filter-options.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-filter-options
