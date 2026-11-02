# Qwen Image 3 Edit API: pricing, parameters and code examples

`alibaba/qwen-image-3/edit` · image generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.043 per run, depending on parameters · **Modes:** async

Alibaba Qwen Image 3 image editing model with support for up to three reference images.

## Pricing

- Depends on parameters (`params.images`).

| parameters | USD |
|---|---|
| defaults | 0.043 |

Formula: `0.04 + len(params.images ?? []) * 0.003`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen-image-3/edit", "aspect_ratio": "1:1", "images": ["https://static.sandbase.ai/examples/f17ae866-160b-49bb-aae6-735643de913f/input/343ea4a5-3866-4623-9a00-49b64ad429a8.png"], "prompt": "Make the sky orange at sunset"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/qwen-image-3/edit', {'aspect_ratio': '1:1', 'images': ['https://static.sandbase.ai/examples/f17ae866-160b-49bb-aae6-735643de913f/input/343ea4a5-3866-4623-9a00-49b64ad429a8.png'], 'prompt': 'Make the sky orange at sunset'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/qwen-image-3/edit", {
  "aspect_ratio": "1:1",
  "images": [
    "https://static.sandbase.ai/examples/f17ae866-160b-49bb-aae6-735643de913f/input/343ea4a5-3866-4623-9a00-49b64ad429a8.png"
  ],
  "prompt": "Make the sky orange at sunset"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/qwen-image-3/edit", sandbase.Params{
	"aspect_ratio": "1:1",
	"images": []any{"https://static.sandbase.ai/examples/f17ae866-160b-49bb-aae6-735643de913f/input/343ea4a5-3866-4623-9a00-49b64ad429a8.png"},
	"prompt": "Make the sky orange at sunset",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility (0-2147483647).  |
| `images` | array | yes | List of input image URLs for editing. Supports 1 to 3 images.  |
| `prompt` | string | yes | The editing instruction describing what changes to make. default `"用途：precise-object-edit。图像1是唯一编辑目标。这是中国高中数学试卷批改真实性测试。\n严格保留原图的木桌、相机视角、纸张轮廓与阴影，以及全部黑色印刷文字、题号、公式、图形和版式；禁止重绘、改写、移动或删除原试卷内容。只新增以下红色教师签字笔笔迹：\n1. 在试卷右上角写“112/150”并用红笔圈住。\n2. 在四个部分标题旁依次写“45/60”“15/20”“10/20”“42/70”。\n3. 仅在第3、14、25题题号旁画红色叉号；仅在第1、13、21题题号旁画红色勾号。\n4. 在第25题旁写“计算错误”，在第22题旁写“过程不完整”。\n红笔必须像中国高中教师真实批卷：自然手写、轻微倾斜、压感和墨迹浓淡变化，位置准确且不遮挡题干。不要添加学生答案、手、人物、文具、印章、水印或其他内容。除指定红笔内容外，画面保持不变。"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`; default `"3:4"` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

Edit up to three images with an instruction using Qwen Image 3 (Pro). It handles precise local edits, text replacement, and multi-image composition while keeping untouched areas unchanged.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 800 characters. |
| `images` | image URL[] (≤3), required | — | Images to edit, Image 1 to Image 3. The first is the main edit target. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | `3:4` | Output shape. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.04 per output image plus $0.003 per input image, Alibaba's list price for Qwen Image 3.0 Pro.

| Input images | Price |
|---|---|
| 1 | $0.043 |
| 2 | $0.046 |
| 3 | $0.049 |

Failed runs are not charged.

### Prompting

- Say which image is the edit target and what each other image contributes.
- List what must stay unchanged: layout, faces, printed text.
- Quote replacement text exactly.

### Limits

- Up to 3 input images; the prompt is limited to 800 characters.

### Also on SandBase

Related: `alibaba/qwen-image-3/text-to-image`, `alibaba/qwen-image-edit/2511`.

---
Machine-readable: [`catalog/models/alibaba/qwen-image-3/edit.json`](../../../../catalog/models/alibaba/qwen-image-3/edit.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen-image-3/edit
