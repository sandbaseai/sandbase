# DataForSEO OnPage Lighthouse Audit API: pricing, parameters and code examples

`dataforseo/v3/on_page/lighthouse/live/json` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Returns real-time Google Lighthouse audit data and web performance metrics for target web pages. Helps assess on-page speed, accessibility, best practices, and search optimization standards.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/on_page/lighthouse/live/json"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/on_page/lighthouse/live/json', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/on_page/lighthouse/live/json", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/on_page/lighthouse/live/json", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/on_page/lighthouse/live/json` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | Page URL.  |

## Details

Runs a Google Lighthouse audit on one web page and returns the full report. It needs a single `url` and returns category scores for performance, accessibility, best practices and SEO, plus the individual audits behind them.

### Use cases

- Track the `performance` score of a landing page and compare it with competitor pages.
- Find accessibility failures and the exact HTML elements that cause them.
- Check basic SEO audits such as crawlability, title and meta description on a page.
- Add a Lighthouse score check to a site monitoring or reporting job.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/on_page/lighthouse/live/json" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.python.org/"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | No | Page URL. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "on_page",
        "function": "lighthouse",
        "url": "https://www.python.org/"
      },
      "id": "11030829-1614-0324-0000-b309897db776",
      "path": [
        "v3"
      ],
      "result": [
        {
          "audits": {
            "accesskeys": {
              "description": "Access keys let users quickly focus a part of the page. For proper navigation, e…",
              "id": "accesskeys",
              "score": null,
              "scoreDisplayMode": "notApplicable",
              "title": "`[accesskey]` values are unique"
            },
            "agent-accessibility-tree": {
              "description": "A well-formed [accessibility tree](http://goo.gle/lighthouse-agentic-a11y) helps…",
              "details": {
                "items": [
                  {
                    "title": "Failed Audits",
                    "type": "list-section",
                    "value": {
                      "headings": [
                        {
                          "key": "description",
                          "label": "Description",
                          "valueType": "text"
                        }
                      ],
                      "items": [
                        {
                          "description": "Certain ARIA roles must contain particular children",
                          "node": {
                            "boundingRect": {
                              "bottom": 0,
                              "height": 0,
                              "left": 75,
                              "right": 1275,
                              "top": 0,
                              "width": 1200
                            },
                            "lhId": "1-0-UL",
                            "nodeLabel": "Python\nPSF\nDocs\nPyPI\nJobs\nCommunity",
                            "path": "1,HTML,1,BODY,0,DIV,2,DIV,0,NAV,2,UL",
                            "selector": "div#touchnav-wrapper > div#top > nav.meta-navigation > ul.menu",
                            "snippet": "<ul class=\"menu\" role=\"tree\">",
                            "type": "node"
                          }
                        }
                      ],
                      "type": "table"
                    }
                  }
                ],
                "type": "list"
              },
              "id": "agent-accessibility-tree",
              "score": 0,
              "scoreDisplayMode": "binary",
              "title": "Accessibility tree is not well-formed"
            },
            "aria-allowed-attr": {
              "description": "Each ARIA `role` supports a specific subset of `aria-*` attributes. Mismatching …",
              "details": {
                "headings": [
                  {
                    "key": "node",
                    "label": "Failing Elements",
                    "subItemsHeading": {
                      "key": "relatedNode",
                      "valueType": "node"
                    },
                    "valueType": "node"
                  }
                ],
                "items": [],
                "type": "table"
              },
              "id": "aria-allowed-attr",
              "score": 1,
              "scoreDisplayMode": "binary",
              "title": "`[aria-*]` attributes match their roles"
            },
            "aria-allowed-role": {
              "description": "Many HTML elements can only be assigned certain ARIA roles. Using ARIA roles whe…",
              "id": "aria-allowed-role",
              "score": null,
              "scoreDisplayMode": "notApplicable",
              "title": "Uses ARIA roles only on compatible elements"
            },
            "aria-command-name": {
              "description": "When an element doesn't have an accessible name, screen readers announce it with…",
              "id": "aria-command-name",
              "score": null,
              "scoreDisplayMode": "notApplicable",
              "title": "`button`, `link`, and `menuitem` elements have accessible names"
            },
            "aria-conditional-attr": {
              "description": "Some ARIA attributes are only allowed on an element under certain conditions. [L…",
              "details": {
                "headings": [
                  {
                    "key": "node",
                    "label": "Failing Elements",
                    "subItemsHeading": {
                      "key": "relatedNode",
                      "valueType": "node"
                    },
                    "valueType": "node"
                  }
                ],
                "items": [],
                "type": "table"
              },
              "id": "aria-conditional-attr",
              "score": 1,
              "scoreDisplayMode": "binary",
              "title": "ARIA attributes are used as specified for the element's role"
            },
            "aria-deprecated-role": {
              "description": "Deprecated ARIA roles may not be processed correctly by assistive technology. [L…",
              "details": {
                "headings": [
                  {
                    "key": "node",
                    "label": "Failing Elements",
                    "subItemsHeading": {
                      "key": "relatedNode",
                      "valueType": "node"
                    },
                    "valueType": "node"
                  }
                ],
                "items": [],
                "type": "table"
              },
              "id": "aria-deprecated-role",
              "score": 1,
              "scoreDisplayMode": "binary",
              "title": "Deprecated ARIA roles were not used"
            },
            "aria-dialog-name": {
              "description": "ARIA dialog elements without accessible names may prevent screen readers users f…",
              "id": "aria-dialog-name",
              "score": null,
              "scoreDisplayMode": "notApplicable",
              "title": "Elements with `role=\"dialog\"` or `role=\"alertdialog\"` have accessible names."
            }
          },
          "categories": {
            "accessibility": {
              "auditRefs": [
                {
                  "group": "a11y-navigation",
                  "id": "accesskeys",
                  "weight": 0
                }
              ],
              "description": "These checks highlight opportunities to [improve the accessibility of your web a…",
              "id": "accessibility",
              "manualDescription": "These items address areas which an automated testing tool cannot cover. Learn mo…",
              "score": 0.79,
              "supportedModes": [
                "navigation"
              ],
              "title": "Accessibility"
            },
            "agentic-browsing": {
              "auditRefs": [
                {
                  "group": "agent-accessibility",
                  "id": "agent-accessibility-tree",
                  "weight": 1
                }
              ],
              "categoryScoreDisplayMode": "fraction",
              "description": "These checks ensure high-quality, [browsable websites for AI agents](https://goo…",
              "id": "agentic-browsing",
              "score": 0.42,
              "supportedModes": [
                "navigation"
              ],
              "title": "Agentic Browsing"
            },
            "best-practices": {
              "auditRefs": [
                {
                  "group": "best-practices-trust-safety",
                  "id": "is-on-https",
                  "weight": 5
                }
              ],
              "id": "best-practices",
              "score": 1,
              "supportedModes": [
                "navigation"
              ],
              "title": "Best Practices"
            },
            "performance": {
              "auditRefs": [
                {
                  "acronym": "FCP",
                  "group": "metrics",
                  "id": "first-contentful-paint",
                  "weight": 10
                }
              ],
              "id": "performance",
              "score": 0.94,
              "supportedModes": [
                "navigation"
              ],
              "title": "Performance"
            },
            "seo": {
              "auditRefs": [
                {
                  "group": "seo-crawl",
                  "id": "is-crawlable",
                  "weight": 4.043478260869565
                }
              ],
              "description": "These checks ensure that your page is following basic search engine optimization…",
              "id": "seo",
              "manualDescription": "Run these additional validators on your site to check additional SEO best practi…",
              "score": 0.92,
              "supportedModes": [
                "navigation"
              ],
              "title": "SEO"
            }
          },
          "categoryGroups": {
            "a11y-aria": {
              "description": "These are opportunities to improve the usage of ARIA in your application which m…",
              "title": "ARIA"
            },
            "a11y-audio-video": {
              "description": "These are opportunities to provide alternative content for audio and video. This…",
              "title": "Audio and video"
            },
            "a11y-best-practices": {
              "description": "These items highlight common accessibility best practices.",
              "title": "Best practices"
            },
            "a11y-color-contrast": {
              "description": "These are opportunities to improve the legibility of your content.",
              "title": "Contrast"
            },
            "a11y-language": {
              "description": "These are opportunities to improve the interpretation of your content by users i…",
              "title": "Internationalization and localization"
            },
            "a11y-names-labels": {
              "description": "These are opportunities to improve the semantics of the controls in your applica…",
              "title": "Names and labels"
            },
            "a11y-navigation": {
              "description": "These are opportunities to improve keyboard navigation in your application.",
              "title": "Navigation"
            },
            "a11y-tables-lists": {
              "description": "These are opportunities to improve the experience of reading tabular or list dat…",
              "title": "Tables and lists"
            }
          },
          "configSettings": {
            "additionalTraceCategories": null,
            "auditMode": false,
            "blankPage": "about:blank",
            "blockedUrlPatterns": null,
            "channel": "cli",
            "clearStorageTypes": [
              "file_systems"
            ],
            "cpuQuietThresholdMs": 1000,
            "debugNavigation": false
          },
          "entities": [
            {
              "isFirstParty": true,
              "isUnrecognized": true,
              "name": "python.org",
              "origins": [
                "https://www.python.org"
              ]
            }
          ],
          "environment": {
            "benchmarkIndex": 2797.5,
            "credits": {
              "axe-core": "4.12.1"
            },
            "hostUserAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessC…",
            "networkUserAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like …"
          },
          "fetchTime": "2026-11-03T08:29:30.845Z",
          "finalDisplayedUrl": "https://www.python.org/"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "12.2082 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "12.2554 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].categories.performance.score / categories.accessibility.score / categories.best-practices.score / categories.seo.score` | Category scores as numbers from 0 to 1. For example, `0.94` for performance and `0.79` for accessibility. |
| `tasks[].result[].categories.agentic-browsing.score` | Score for the Agentic Browsing category, which checks how well AI agents can browse the page. It sits next to the four standard categories. |
| `tasks[].result[].categories.performance.auditRefs[]` | Lists the audits that make up a category. Each row has the audit `id`, its `weight` in the category score, and a `group`. Performance metrics also carry an `acronym` such as `LCP` or `TBT`. |
| `tasks[].result[].audits` | Object of individual audits keyed by audit id, such as `aria-allowed-attr`. Use the keys from `auditRefs` to look up each audit. |
| `tasks[].result[].audits.*.score / scoreDisplayMode` | The audit score, with `null` when `scoreDisplayMode` is `notApplicable`. A `binary` mode audit scores `1` for pass and `0` for fail. |
| `tasks[].result[].audits.*.title / description` | Readable name and explanation of what the audit checks. The title changes with the result, for example "Accessibility tree is not well-formed". |
| `tasks[].result[].audits.*.details.items[]` | Details on what the audit found. An empty list in a table means no failing elements. |
| `tasks[].result[].audits.agent-accessibility-tree.details.items[].value.items[].node.selector / snippet / nodeLabel` | CSS selector, HTML snippet and label of an element that failed the audit. Use them to find the element in the page source. |
| `tasks[].result[].audits.agent-accessibility-tree.details.items[].value.items[].node.boundingRect` | Position and size of the failing element on the page, with `top`, `left`, `width` and `height`. |
| `tasks[].id` | Task ID for this call, in a format like `11030829-1614-0324-0000-b309897db776`. |

### Notes

- Send one page in `url`. Use the full address including `https://`.
- The response is large. Read `categories` first for the scores, then open the audits you care about through `auditRefs[].id`.
- The `tasks[].data` object echoes the `url` that was audited.

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/on_page/lighthouse/live/json.json`](../../../../../../../catalog/models/dataforseo/v3/on_page/lighthouse/live/json.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/on_page/lighthouse/live/json
