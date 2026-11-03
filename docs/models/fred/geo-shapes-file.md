# FRED GeoFRED Shape Files API: pricing, parameters and code examples

`fred/geo-shapes-file` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

GeoFRED Shape Files from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/geo-shapes-file", "shape": "bea"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/geo-shapes-file', {'shape': 'bea'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/geo-shapes-file", {
  "shape": "bea"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/geo-shapes-file", sandbase.Params{
	"shape": "bea",
})
```

Same call via the path form: `POST /v1/api/fred/geo-shapes-file` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `shape` | string | yes | The type of shape you want to pull GeoJSON data for. Available Shape Types: bea (Bureau of Economic Anaylis Region) msa (Metropolitan Statistical Area) frb (Federal Reserve Bank Districts) necta (New England City and… one of: `bea`, `msa`, `frb`, `necta`, `state`, `country`, `county`, `censusregion`, `censusdivision` |

## Details

Returns GeoJSON boundary shapes for a chosen type of US region, such as BEA regions, states, counties or Federal Reserve districts. It needs one input, `shape`, which sets the region type.

### Use cases

- Draw a map of BEA economic regions in a web or desktop mapping tool.
- Join the shapes to regional values from GeoFRED to build a choropleth map.
- Match region names to shapes to label charts that group data by region.
- Load county or state boundaries into a GIS tool without downloading shape files by hand.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/geo-shapes-file" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"shape": "bea"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shape` | string | Yes | The type of shape you want to pull GeoJSON data for. Available Shape Types: bea (Bureau of Economic Anaylis Region) msa (Metropolitan Statistical Area) frb (Federal Reserve Bank Districts) necta (New England City and Tow |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "crs": {
    "properties": {
      "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
    },
    "type": "name"
  },
  "features": [
    {
      "geometry": {
        "coordinates": [
          [
            [
              [
                1485
              ]
            ]
          ]
        ],
        "type": "MultiPolygon"
      },
      "properties": {
        "bea_regi_1": "Far West",
        "bea_region": 8
      },
      "type": "Feature"
    }
  ],
  "name": "state_bea_region",
  "type": "FeatureCollection"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `name` | Name of the shape set returned. For `shape` set to `bea` it is `state_bea_region`. |
| `type` | GeoJSON type of the whole response. The value is `FeatureCollection`. |
| `crs.properties.name` | Coordinate reference system identifier for the shapes. The value is `urn:ogc:def:crs:OGC:1.3:CRS84`. |
| `features[]` | One entry per region. Each entry is a GeoJSON `Feature` with a `geometry` and a `properties` object. |
| `features[].geometry.type` | Geometry type of the region. The sample shows `MultiPolygon`, so one region can have several separate parts. |
| `features[].geometry.coordinates` | Nested lists of `[x, y]` points that outline each polygon of the region. The sample values are large whole numbers, not longitude and latitude degrees, so check them before you plot on a world map. |
| `features[].properties.bea_regi_1` | Name of the BEA region, for example `Far West`, `Great Lakes` or `Southwest`. |
| `features[].properties.bea_region` | Numeric code for the BEA region, for example `8` for `Far West`. |

### Notes

- Property names inside `features[].properties` depend on the `shape` value. The names `bea_regi_1` and `bea_region` appear for `bea`.
- Allowed `shape` values are `bea`, `msa`, `frb`, `necta`, `state`, `country`, `county`, `censusregion` and `censusdivision`.
- To get data values for these regions, call [FRED GeoFRED Regional Data](/apis/fred/geo-regional-data) and match them to the shapes by region name or code.
- To find series that exist by region, see [FRED GeoFRED Series Group](/apis/fred/geo-series-group).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/geo-shapes-file.json`](../../../catalog/models/fred/geo-shapes-file.json) · Store page: https://www.sandbase.ai/model/fred/geo-shapes-file
