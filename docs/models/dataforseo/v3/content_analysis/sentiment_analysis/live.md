# DataForSEO Content Sentiment Analysis API: pricing, parameters and code examples

`dataforseo/v3/content_analysis/sentiment_analysis/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024036 per call · **Modes:** sync

Evaluates text content to determine sentiment scores and emotional tone. Returns sentiment classifications and polarity metrics across analyzed web content.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024036**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/content_analysis/sentiment_analysis/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/content_analysis/sentiment_analysis/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/content_analysis/sentiment_analysis/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/content_analysis/sentiment_analysis/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/content_analysis/sentiment_analysis/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |

## Details

This API returns sentiment breakdowns for web content that mentions a keyword. It needs one input, `keyword`, such as a brand name like `nike`. The result shows how mentions split by positive, neutral and negative polarity and by emotion such as `anger`, `happiness` and `love`.

### Use cases

- Compare how many `nike` mentions carry a positive tone versus a negative tone.
- Find which emotions, such as `love` or `anger`, show up most in content about a brand.
- Check which countries and languages produce the most positive or negative content about a brand.
- See which page types, such as news, blogs or ecommerce, carry the most negative mentions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/content_analysis/sentiment_analysis/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "nike"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "content_analysis",
        "function": "sentiment_analysis",
        "keyword": "nike"
      },
      "id": "11030828-2190-0465-0000-137f2de84f4c",
      "path": [
        "v3"
      ],
      "result": [
        {
          "positive_connotation_distribution": {
            "negative": {
              "connotation_types": {
                "negative": 4000000,
                "neutral": 219104,
                "positive": 547208
              },
              "countries": {
                "BR": 72064,
                "DE": 97752,
                "ES": 52080,
                "FR": 79960,
                "GB": 138600,
                "IN": 87808,
                "IR": 65064,
                "NL": 58992
              },
              "languages": {
                "af": 18152,
                "de": 62016,
                "en": 3486040,
                "es": 27704,
                "fr": 33312,
                "it": 15784,
                "ja": 519352,
                "nl": 11400
              },
              "page_categories": [
                {
                  "category": null,
                  "count": 242928
                }
              ],
              "page_types": {
                "blogs": 186456,
                "ecommerce": 2978776,
                "message-boards": 62344,
                "news": 832904,
                "organization": 146432
              },
              "rank": 513,
              "sentiment_connotations": {
                "anger": 88,
                "fun": 4440,
                "happiness": 537232,
                "love": 90176,
                "sadness": 448,
                "share": 26408
              },
              "text_categories": [
                {
                  "category": [
                    10014
                  ],
                  "count": 196608
                }
              ]
            },
            "neutral": {
              "connotation_types": {
                "negative": 686088,
                "neutral": 3994384,
                "positive": 954080
              },
              "countries": {
                "BR": 65544,
                "DE": 87704,
                "FR": 73656,
                "GB": 162192,
                "IN": 89712,
                "IR": 53296,
                "PL": 53456,
                "US": 278840
              },
              "languages": {
                "af": 14008,
                "de": 33128,
                "en": 3435768,
                "es": 5000,
                "it": 20640,
                "ja": 574040,
                "nl": 4912,
                "pl": 22280
              },
              "page_categories": [
                {
                  "category": null,
                  "count": 405392
                }
              ],
              "page_types": {
                "blogs": 355816,
                "ecommerce": 2969944,
                "message-boards": 40472,
                "news": 703232,
                "organization": 268760
              },
              "rank": 496,
              "sentiment_connotations": {
                "anger": 80,
                "fun": 5040,
                "happiness": 408512,
                "love": 95448,
                "sadness": 368,
                "share": 20336
              },
              "text_categories": [
                {
                  "category": null,
                  "count": 204720
                }
              ]
            },
            "positive": {
              "connotation_types": {
                "negative": 494848,
                "neutral": 275248,
                "positive": 4000000
              },
              "countries": {
                "BR": 109600,
                "DE": 104000,
                "ES": 50592,
                "FR": 94784,
                "GB": 110488,
                "IN": 88144,
                "IR": 49496,
                "NL": 65488
              },
              "languages": {
                "af": 20344,
                "de": 69752,
                "en": 2355736,
                "es": 60456,
                "fr": 43640,
                "it": 12472,
                "ja": 1542632,
                "nl": 18472
              },
              "page_categories": [
                {
                  "category": null,
                  "count": 332544
                }
              ],
              "page_types": {
                "blogs": 206856,
                "ecommerce": 2845648,
                "message-boards": 71624,
                "news": 940856,
                "organization": 348848
              },
              "rank": 479,
              "sentiment_connotations": {
                "anger": 48,
                "fun": 14240,
                "happiness": 446256,
                "love": 221856,
                "sadness": 440,
                "share": 14592
              },
              "text_categories": [
                {
                  "category": null,
                  "count": 184504
                }
              ]
            }
          },
          "sentiment_connotation_distribution": {
            "anger": {
              "connotation_types": {
                "negative": 2928,
                "neutral": 920,
                "positive": 1192
              },
              "countries": {
                "AT": 48,
                "AU": 40,
                "BR": 168,
                "DE": 1176,
                "FR": 256,
                "IN": 48,
                "NL": 80,
                "PL": 56
              },
              "languages": {
                "af": 40,
                "de": 1752,
                "en": 1240,
                "es": 32,
                "fr": 432,
                "ja": 288,
                "nl": 104,
                "pl": 32
              },
              "page_categories": [
                {
                  "category": null,
                  "count": 392
                }
              ],
              "page_types": {
                "blogs": 536,
                "ecommerce": 1608,
                "message-boards": 64,
                "news": 1376,
                "organization": 904
              },
              "rank": 227,
              "sentiment_connotations": {
                "anger": 3504,
                "fun": 104,
                "happiness": 360,
                "love": 24,
                "sadness": 104,
                "share": 64
              },
              "text_categories": [
                {
                  "category": [
                    10014
                  ],
                  "count": 320
                }
              ]
            },
            "fun": {
              "connotation_types": {
                "negative": 51808,
                "neutral": 23616,
                "positive": 256520
              },
              "countries": {
                "BE": 4624,
                "BR": 11144,
                "DE": 15584,
                "FR": 12384,
                "GB": 5232,
                "IN": 5520,
                "JP": 5128,
                "NL": 6352
              },
              "languages": {
                "af": 3872,
                "de": 16568,
                "en": 30992,
                "fr": 16848,
                "it": 3024,
                "ja": 230400,
                "nl": 5800,
                "pl": 4136
              },
              "page_categories": [
                {
                  "category": null,
                  "count": 28240
                }
              ],
              "page_types": {
                "blogs": 15656,
                "ecommerce": 197608,
                "message-boards": 1464,
                "news": 68544,
                "organization": 91400
              },
              "rank": 414,
              "sentiment_connotations": {
                "anger": 104,
                "fun": 280352,
                "happiness": 40256,
                "love": 7464,
                "sadness": 120,
                "share": 1192
              },
              "text_categories": [
                {
                  "category": null,
                  "count": 12464
                }
              ]
            },
            "happiness": {
              "connotation_types": {
                "negative": 1908432,
                "neutral": 455192,
                "positive": 1707376
              },
              "countries": {
                "BR": 119232,
                "DE": 104840,
                "ES": 55272,
                "FR": 95224,
                "GB": 97296,
                "IN": 89080,
                "IR": 42008,
                "NL": 68776
              },
              "languages": {
                "af": 38720,
                "br": 17344,
                "de": 95368,
                "en": 1883520,
                "fr": 47472,
                "ja": 2360752,
                "nl": 5000,
                "pl": 12040
              },
              "page_categories": [
                {
                  "category": null,
                  "count": 247632
                }
              ],
              "page_types": {
                "blogs": 100040,
                "ecommerce": 2144328,
                "message-boards": 80752,
                "news": 1703768,
                "organization": 228568
              },
              "rank": 445,
              "sentiment_connotations": {
                "anger": 40,
                "fun": 12664,
                "happiness": 3985864,
                "love": 51520,
                "sadness": 120,
                "share": 16152
              },
              "text_categories": [
                {
                  "category": null,
                  "count": 183000
                }
              ]
            },
            "love": {
              "connotation_types": {
                "negative": 768920,
                "neutral": 264272,
                "positive": 2074936
              },
              "countries": {
                "BR": 145440,
                "DE": 85672,
                "ES": 52240,
                "FR": 123592,
                "GB": 63560,
                "IN": 70200,
                "JP": 56952,
                "NL": 79224
              },
              "languages": {
                "af": 10056,
                "de": 90672,
                "en": 327952,
                "es": 8056,
                "fr": 133688,
                "ja": 3509968,
                "nl": 24360,
                "pl": 11088
              },
              "page_categories": [
                {
                  "category": null,
                  "count": 569168
                }
              ],
              "page_types": {
                "blogs": 104600,
                "ecommerce": 1225960,
                "message-boards": 291200,
                "news": 2388216,
                "organization": 158472
              },
              "rank": 448,
              "sentiment_connotations": {
                "anger": 8,
                "fun": 5216,
                "happiness": 122488,
                "love": 3967352,
                "sadness": 96,
                "share": 2672
              },
              "text_categories": [
                {
                  "category": null,
                  "count": 492848
                }
              ]
            },
            "sadness": {
              "connotation_types": {
                "negative": 10376,
                "neutral": 3536,
                "positive": 9040
              },
              "countries": {
                "BR": 456,
                "DE": 2392,
                "FR": 432,
                "GB": 240,
                "IN": 352,
                "NG": 304,
                "NL": 824,
                "PL": 216
              },
              "languages": {
                "de": 4184,
                "en": 10840,
                "es": 304,
                "fr": 456,
                "ja": 1512,
                "nl": 1296,
                "pl": 360,
                "pt": 368
              },
              "page_categories": [
                {
                  "category": null,
                  "count": 3424
                }
              ],
              "page_types": {
                "blogs": 3344,
                "ecommerce": 11344,
                "message-boards": 216,
                "news": 2648,
                "organization": 4072
              },
              "rank": 354,
              "sentiment_connotations": {
                "anger": 104,
                "fun": 120,
                "happiness": 1304,
                "love": 208,
                "sadness": 17080,
                "share": 224
              },
              "text_categories": [
                {
                  "category": null,
                  "count": 1288
                }
              ]
            },
            "share": {
              "connotation_types": {
                "negative": 498176,
                "neutral": 193944,
                "positive": 316680
              },
              "countries": {
                "AU": 24904,
                "BR": 37664,
                "DE": 15208,
                "ES": 20464,
                "FR": 10280,
                "IN": 11304,
                "MX": 14032,
                "NL": 10584
              },
              "languages": {
                "af": 11936,
                "br": 3296,
                "de": 41224,
                "en": 480664,
                "es": 164960,
                "fr": 5840,
                "it": 1056,
                "ja": 91360
              },
              "page_categories": [
                {
                  "category": null,
                  "count": 200744
                }
              ],
              "page_types": {
                "blogs": 182112,
                "ecommerce": 448096,
                "message-boards": 16704,
                "news": 120064,
                "organization": 197584
              },
              "rank": 477,
              "sentiment_connotations": {
                "anger": 64,
                "fun": 1192,
                "happiness": 70400,
                "love": 6928,
                "sadness": 224,
                "share": 736744
              },
              "text_categories": [
                {
                  "category": null,
                  "count": 115448
                }
              ]
            }
          },
          "type": "content_analysis_sentiment_analysis"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "14.6624 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "14.6740 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].positive_connotation_distribution.positive / neutral / negative` | One block per polarity group. Each block describes the mentions that fall into that group. |
| `tasks[].result[].positive_connotation_distribution.positive.connotation_types` | Counts of mentions in the polarity group, split into `negative`, `neutral` and `positive` tone. |
| `tasks[].result[].sentiment_connotation_distribution.anger / fun / happiness / love` | One block per emotion. Each block describes the mentions that match that emotion. |
| `tasks[].result[].sentiment_connotation_distribution.happiness.sentiment_connotations` | Counts of mentions in the group, split by emotion: `anger`, `fun`, `happiness`, `love`, `sadness` and `share`. |
| `tasks[].result[].positive_connotation_distribution.positive.countries` | Mention counts per country code, such as `GB` or `DE`, for that group. |
| `tasks[].result[].positive_connotation_distribution.positive.languages` | Mention counts per language code, such as `en` or `ja`, for that group. |
| `tasks[].result[].positive_connotation_distribution.positive.page_types` | Mention counts per page type: `blogs`, `ecommerce`, `message-boards`, `news` and `organization`. |
| `tasks[].result[].positive_connotation_distribution.positive.page_categories[].category / count` | A category as a list of numeric IDs, or `null` when none applies, and the number of mentions in it. |
| `tasks[].result[].positive_connotation_distribution.positive.text_categories[].category / count` | Same structure as `page_categories`, but based on the category of the text itself. |
| `tasks[].result[].positive_connotation_distribution.positive.rank` | Rank value for the group. The response does not state its scale. |

### Notes

- Send the brand, product or topic to analyze as `keyword`. The request in this example used `nike`.
- Category values are lists of numeric IDs, not names. The response does not include a lookup table for them.
- Each emotion and polarity block repeats the same set of breakdowns, so you can compare groups with the same code.
- The `tasks[].id` value identifies the task. The `tasks[].data` object echoes the `keyword` you sent.

### Pricing

Billed at the actual cost of each call, about $0.024036 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/content_analysis/sentiment_analysis/live.json`](../../../../../../catalog/models/dataforseo/v3/content_analysis/sentiment_analysis/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/content_analysis/sentiment_analysis/live
