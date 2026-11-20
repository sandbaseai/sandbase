# Meshy models API: 40 endpoints with pricing and code examples

Call 40 Meshy models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`meshy/6.0-lite/image-to-3d`](../models/meshy/6.0-lite/image-to-3d.md) | Meshy 6 Lite turns a single image into a 3D model at a lower price, with optional textures, PBR maps, humanoid rigging and animation. | from $0.2 to $0.92 per run, depending on parameters |
| [`meshy/6.0-lite/multi-image-to-3d`](../models/meshy/6.0-lite/multi-image-to-3d.md) | Meshy 6 Lite turns 1–4 views of the same object into a 3D model at a lower price, with optional textures, PBR maps, humanoid rigging and… | from $0.2 to $0.92 per run, depending on parameters |
| [`meshy/6.0-lite/retexture`](../models/meshy/6.0-lite/retexture.md) | Meshy 6 Lite Retexture is the lower-cost Meshy retexturing model: repaint an existing 3D model from a text or image style. | $0.4 per call |
| [`meshy/6.0-lite/text-to-3d`](../models/meshy/6.0-lite/text-to-3d.md) | Meshy 6 Lite turns a text prompt into a 3D model at a lower price: a preview mesh, then textures, with optional humanoid rigging and… | from $0.2 to $0.92 per run, depending on parameters |
| [`meshy/6.0/retexture`](../models/meshy/6.0/retexture.md) | Meshy 6 Retexture repaints an existing 3D model from a text or image style, with optional PBR maps and up to 8K textures. | from $0.4 to $0.6 per run, depending on parameters |
| [`meshy/7.0/image-to-3d`](../models/meshy/7.0/image-to-3d.md) | Meshy 7 turns a single image into a 3D model, with optional textures, PBR maps, 2K geometry, humanoid auto-rigging and animation. | from $0.8 to $1.72 per run, depending on parameters |
| [`meshy/7.0/multi-image-to-3d`](../models/meshy/7.0/multi-image-to-3d.md) | Meshy 7 reconstructs a 3D model from 1–4 views of the same object, with optional textures, PBR maps, 2K geometry, auto-rigging and… | from $0.8 to $1.72 per run, depending on parameters |
| [`meshy/7.0/retexture`](../models/meshy/7.0/retexture.md) | Meshy 7 Retexture repaints an existing 3D model from a text or image style, with optional PBR maps and up to 8K textures. | from $0.4 to $0.6 per run, depending on parameters |
| [`meshy/7.0/text-to-3d`](../models/meshy/7.0/text-to-3d.md) | Meshy 7 generates a 3D model from a text prompt, either as an untextured preview mesh or fully textured, with optional 2K geometry,… | from $0.8 to $1.72 per run, depending on parameters |
| [`meshy/7.1/image-to-3d`](../models/meshy/7.1/image-to-3d.md) | Meshy 7.1 turns a single image into a textured, optionally rigged and animated 3D model. | from $0.8 to $1.72 per run, depending on parameters |
| [`meshy/7.1/multi-image-to-3d`](../models/meshy/7.1/multi-image-to-3d.md) | Meshy 7.1 reconstructs a textured, optionally rigged 3D model from 1–4 views of the same object. | from $0.8 to $1.72 per run, depending on parameters |
| [`meshy/7.1/text-to-3d`](../models/meshy/7.1/text-to-3d.md) | Meshy 7.1 generates a textured, optionally rigged and animated 3D model from a text prompt. | from $1.2 to $1.72 per run, depending on parameters |
| [`meshy/convert`](../models/meshy/convert.md) | Meshy Convert exports an existing 3D model to GLB, OBJ, FBX, STL, USDZ, BLEND or 3MF. | $0.04 per call |
| [`meshy/creative-lab/brick-figure`](../models/meshy/creative-lab/brick-figure.md) | Turns a photo into a textured brick-style minifigure. | $1.44 per call |
| [`meshy/creative-lab/fidget-collapsible`](../models/meshy/creative-lab/fidget-collapsible.md) | Turns a photo into a print-in-place collapsible fidget toy. | $0.24 per call |
| [`meshy/creative-lab/fidget-pixel`](../models/meshy/creative-lab/fidget-pixel.md) | Turns a photo into a multi-color pixel-art fidget board, returned as a 3MF. | $1.44 per call |
| [`meshy/creative-lab/figure`](../models/meshy/creative-lab/figure.md) | Turns a photo into a textured chibi-style figurine. | $1.44 per call |
| [`meshy/creative-lab/fridge-magnet`](../models/meshy/creative-lab/fridge-magnet.md) | Turns a photo into a colorized relief fridge magnet ready to 3D print. | $1.44 per call |
| [`meshy/creative-lab/keycap`](../models/meshy/creative-lab/keycap.md) | Turns a photo into a full-color custom mechanical keyboard keycap (Cherry MX 1u by default). | $2.48 per call |
| [`meshy/creative-lab/keychain`](../models/meshy/creative-lab/keychain.md) | Turns a photo into a 3D-printable keychain medallion, optionally with a name on its face. | $1.44 per call |
| [`meshy/creative-lab/lamp`](../models/meshy/creative-lab/lamp.md) | Turns a photo into a 3D-printable lithophane-style lampshade and base. | $1.44 per call |
| [`meshy/creative-lab/vinyl-figure`](../models/meshy/creative-lab/vinyl-figure.md) | Turns a photo into a textured big-head vinyl collectible figure. | $1.44 per call |
| [`meshy/meshy-v6`](../models/meshy/meshy-v6.md) | Meshy 6 turns a single image into a 3D model, with optional textures, PBR maps, humanoid auto-rigging and animation. | from $0.8 to $1.52 per run, depending on parameters |
| [`meshy/meshy-v6/multi-image-to-3d`](../models/meshy/meshy-v6/multi-image-to-3d.md) | Meshy 6 reconstructs a 3D model from 1–4 views of the same object, with optional textures, PBR maps, auto-rigging and animation. | from $0.8 to $1.52 per run, depending on parameters |
| [`meshy/meshy-v6/text-to-3d`](../models/meshy/meshy-v6/text-to-3d.md) | Meshy 6 generates a 3D model from a text prompt, either as an untextured preview mesh or fully textured, with optional rigging and… | from $0.8 to $1.52 per run, depending on parameters |
| [`meshy/n1/retexture`](../models/meshy/n1/retexture.md) | Meshy N1 Retexture repaints an existing 3D model from one reference image or up to four reference views, producing a 2K base color texture. | $0.4 per call |
| [`meshy/print/analyze`](../models/meshy/print/analyze.md) | Meshy Analyze Printability checks a 3D model for watertightness, holes, non-manifold edges, degenerate faces and thin walls before printing. | free |
| [`meshy/print/multi-color`](../models/meshy/print/multi-color.md) | Meshy Multi-Color Print turns a textured 3D model into color regions and returns a 3MF ready for a multi-color slicer. | $0.4 per call |
| [`meshy/print/repair`](../models/meshy/print/repair.md) | Meshy Print Repair fixes holes, non-manifold geometry and thin walls so a 3D model can be printed. | $0.4 per call |
| [`meshy/relief`](../models/meshy/relief.md) | Meshy Relief turns a photo into a printable 3D relief (GLB and STL) with emboss or engrave carving and an optional curved bend. | $0.8 per call |
| [`meshy/remesh`](../models/meshy/remesh.md) | Meshy Remesh rebuilds an existing 3D model at a target face count, as triangles or quads. | $0.2 per call |
| [`meshy/resize`](../models/meshy/resize.md) | Meshy Resize scales an existing 3D model to a real-world height or longest side, or estimates the size automatically. | $0.04 per call |
| [`meshy/rigging`](../models/meshy/rigging.md) | Meshy Rigging adds a humanoid skeleton to an existing character model and can also apply one animation preset. | from $0.2 to $0.32 per run, depending on parameters |
| [`meshy/rigging/multi-animation`](../models/meshy/rigging/multi-animation.md) | Meshy Rigging Multi-Animation rigs an existing humanoid character model and generates up to 10 animation clips on the same rig. | from $0.56 per run, depending on parameters |
| [`meshy/t2.5/image-to-3d`](../models/meshy/t2.5/image-to-3d.md) | Meshy T2.5 turns a single image into a clean Smart Topology triangle mesh (up to 30,000 triangles), with optional textures, rigging and… | from $0.2 to $0.92 per run, depending on parameters |
| [`meshy/t2.5/text-to-3d`](../models/meshy/t2.5/text-to-3d.md) | Meshy T2.5 generates a clean Smart Topology triangle mesh (up to 30,000 triangles) from a text prompt, untextured in preview mode or… | from $0.2 to $0.92 per run, depending on parameters |
| [`meshy/t2/image-to-3d`](../models/meshy/t2/image-to-3d.md) | Meshy T2 turns a single image into a clean Smart Topology triangle mesh (up to 15,000 triangles), with optional textures, rigging and… | from $0.2 to $0.92 per run, depending on parameters |
| [`meshy/t2/text-to-3d`](../models/meshy/t2/text-to-3d.md) | Meshy T2 generates a clean Smart Topology triangle mesh (up to 15,000 triangles) from a text prompt, untextured in preview mode or… | from $0.2 to $0.92 per run, depending on parameters |
| [`meshy/text-to-motion`](../models/meshy/text-to-motion.md) | Meshy Text to Motion generates a standalone character motion clip from a text prompt, as FBX (prime) or BVH (swift). | from $0.12 to $0.4 per run, depending on parameters |
| [`meshy/uv-unwrap`](../models/meshy/uv-unwrap.md) | Meshy UV Unwrap creates a clean UV layout for an existing 3D model before texturing. | $0.2 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/6.0-lite/image-to-3d", "image": "https://static.sandbase.ai/examples/d324d6bd-de63-48bc-aa2c-3878d72ef6c2/input/5cde95a4-2e7d-4dfb-a1ff-5ea4277fd765.png"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
