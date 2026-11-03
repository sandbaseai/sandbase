# Instagram User About Details API: pricing, parameters and code examples

`instagram/v3/user-about` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns About This Account details for an Instagram profile using a target username. Output includes metadata such as account join date, location, and former usernames.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-about", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-about', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-about", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-about", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-about` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Instagram username (required)  |

## Details

Returns the About This Account screen for an Instagram profile as a nested layout payload. It needs one input, the `username` of the target account. The screen text includes the account name and the `Date joined` value, and can include location and former usernames.

### Use cases

- Read the `Date joined` text to check how old an account is before you work with it.
- Compare the join date of a brand's official account with look-alike accounts to spot impostors.
- Pull the About This Account text for a list of creators during due diligence.
- Check the verified badge icon and the account name on the screen when you vet a profile.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-about" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username (required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "__ar": 1,
  "lid": "7703845594882346698",
  "payload": {
    "layout": {
      "bloks_payload": {
        "data": [
          {
            "data": {
              "initial": true,
              "key": "IG_ABOUT_THIS_ACCOUNT:about_this_account_country_visibility",
              "mode": "p"
            },
            "id": "sy2gtiuq3",
            "type": "gs"
          }
        ],
        "error_attribution": {
          "logging_id": "{\"callsite\":\"{\\\"product\\\":\\\"bloks_unknown\\\",\\\"feature\\\":\\\"unknown\\\",\\\"oncall\\\":\\…",
          "source_map_id": "B8uVo85a"
        },
        "ft": {
          "sy2gtius7": "\t(f43 \"nme_entrypoint_event\" \"\" (f4i (dkc \"event\" \"entrypoint\" \"log_channel\" \"ev…"
        },
        "payload_spec_ids": [
          "bk.types.ThemedColor"
        ],
        "props": [
          {
            "id": "-4100637133163749715",
            "name": "ttrc_instance_id"
          }
        ],
        "templates": {
          "sy2gtiuso": {
            "㐵": {
              "#": "#7FFFFFFF",
              "$": "#7FFFFFFF"
            }
          },
          "sy2gtiusp": {
            "㐵": {
              "#": "#FFFFFFFF",
              "$": "#FFFFFFFF"
            }
          },
          "sy2gtiusq": {
            "㐵": {
              "#": "#FF5E646D",
              "$": "#FFA2AAB4"
            }
          },
          "sy2gtiusr": {
            "㐵": {
              "#": "#FFF8F9F9",
              "$": "#FF212328"
            }
          },
          "sy2gtiuss": {
            "㐵": {
              "#": "#FF5E646D",
              "$": "#FFA2AAB4"
            }
          },
          "sy2gtiust": {
            "㐵": {
              "#": "#FFF8F9F9",
              "$": "#FF212328"
            }
          }
        },
        "tree": {
          "㚞": {
            "#": {
              "㐈": {
                " ": [
                  {
                    "㐅": {
                      " ": [
                        {
                          "㐈": {
                            " ": [
                              {
                                "㐈": {
                                  " ": [
                                    {
                                      "㐈": {
                                        " ": [
                                          {
                                            "㐋": {
                                              "!": "di6qzs:13",
                                              ")": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/550891366_18667771684001…"
                                            }
                                          }
                                        ],
                                        "&": {
                                          "㐂": {
                                            "&": {
                                              "㐵": {
                                                "#": "#26FFFFFF",
                                                "$": "#26000000"
                                              }
                                            },
                                            "(": "0.5px",
                                            "+": true,
                                            ".": "40dp"
                                          }
                                        },
                                        "": {
                                          "庉": {
                                            ")": "80dp",
                                            ":": "80dp",
                                            "A": 0
                                          }
                                        },
                                        "": []
                                      }
                                    }
                                  ],
                                  "$": "center",
                                  ")": "column",
                                  "6": "8dp",
                                  ";": "16dp"
                                }
                              }
                            ],
                            ")": "column",
                            "6": "12dp",
                            "": []
                          }
                        }
                      ],
                      "*": "column"
                    }
                  }
                ],
                ")": "column",
                "": [
                  {
                    "㕘": {
                      "#": "\t(e53, 1)"
                    }
                  }
                ]
              }
            },
            "$": {
              "㗙": {
                "$": "About this account"
              }
            },
            "&": []
          }
        }
      }
    },
    "server_data": {
      "bloks_app_id": "ig_web",
      "controller_name": "IGAboutThisAccountScreenController",
      "falco_log_policy_map": null,
      "versioning_id": "6dcb7a5a5382571703b748d37b710083a08c68c3ef222cea50d3aebd37b6d25d"
    }
  },
  "rid": "AirlI6jnvMZ8NbxVZyOSM26"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `payload.layout.bloks_payload.tree` | Nested layout of the About This Account screen. The account details sit in its text nodes. A label such as `Date joined` is followed by its value, for example `February 2012`. |
| `payload.layout.bloks_payload.data[].data.key` | Name of a screen state entry, for example `IG_ABOUT_THIS_ACCOUNT:about_this_account_country_visibility`. It shows which About This Account setting the entry belongs to. |
| `payload.layout.bloks_payload.data[].id / payload.layout.bloks_payload.data[].type` | Short identifier and type code of each screen state entry. |
| `payload.layout.bloks_payload.props[].name` | Names of the screen properties, for example `ttrc_instance_id` and `infra_screen_id`. Each has an `id` string. |
| `payload.layout.bloks_payload.templates` | Color templates the layout uses. Values are hex colors such as `#FFFFFFFF`. |
| `payload.layout.bloks_payload.error_attribution.logging_id` | Logging string for the screen request. It holds a `request_id`. |
| `lid` | String identifier returned with the response. |

### Notes

- The response is a screen layout, not flat JSON. Search the text nodes under `payload.layout.bloks_payload.tree` for labels such as `Date joined` and read the value that follows.
- Pass the profile name without the `@` sign in `username`, for example `instagram`.
- To get profile data such as bio and counts, call [Instagram User Profile (V3)](/apis/instagram/v3/user-profile). To convert a username into a numeric ID, call [Instagram User ID Lookup](/apis/instagram/v3/user-id-by-username).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-about.json`](../../../../catalog/models/instagram/v3/user-about.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-about
