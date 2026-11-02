# Xiaohongshu Hot Search API: pricing, parameters and code examples

`xiaohongshu/hot-search` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.020833 per call · **Modes:** sync

Search Xiaohongshu (RedNote) hot-content entries with optional keyword, content-category path, pagination, ranking metric, and time-range controls.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/hot-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/hot-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/hot-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/hot-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/hot-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `nd` | string |  | Time range in days. one of: `DAY_3`, `DAY_7`, `DAY_14`, `DAY_30`; default `"DAY_7"` |
| `orderBy` | string |  | Sort metric for the result set. one of: `premium_imp_num`, `premium_good_read_rate`, `premium_read_num`, `premium_engage_num`, `premium_engage_rate`, `premium_like_num`, `premium_fav_num`, `premium_cmt_num`; default `"premium_imp_num"` |
| `pageNum` | integer |  | Page number for pagination. default `1` |
| `searchWord` | string |  | Search keyword.  |
| `noteContentCategory` | string |  | Content category filter. Pass one complete Pugongying category path joined with # separators. You may pass a parent path or append one listed child with another #. Only one path is accepted. Available values: Content…  |

## Details

Search Xiaohongshu (RedNote) hot-content entries with optional keyword, content-category path, pagination, ranking metric, and time-range controls.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/hot-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `searchWord` | string | No | Search keyword. |
| `pageNum` | integer | No | Page number for pagination. |
| `orderBy` | string | No | Sort metric for the result set. |
| `nd` | string | No | Time range in days. |
| `noteContentCategory` | string | No | Content category filter. Pass one complete Pugongying category path joined with # separators. You may pass a parent path or append one listed child with another #. Only one path is accepted. Available values: Content categories: - 内容类目#美妆: 整体妆容, 唇妆, 眼妆, 美甲, 底妆, 美妆合集, 香水, 美妆其他 - 内容类目#护肤: 面部保养, 面部清洁, 护肤合集, 护肤其他 - 内容类目#个人护理: 头发产品, 身体护理, 口腔护理, 护理其他 - 内容类目#母婴: 母婴日常, 早教, 婴童用品, 婴童洗护, 婴童食品, 婴童时尚, 孕期穿搭, 孕产经验, 产后恢复, 育儿经验, 宝宝才艺, 宝宝写真, 母婴其他 - 内容类目#时尚: 穿搭, 配饰, 发型, 箱包, 鞋靴, 时尚其他 - 内容类目#美食: 美食教程, 美食探店, 美食展示, 美食测评, 吃播, 美食其他 - 内容类目#家居家装: 装修, 家居用品, 花艺园艺, 家居装饰, 家具, 家电, 室内设计, 居家经验, 家居家装其他 - 内容类目#影视综资讯: 动漫, 娱乐资讯, 影视, 民生资讯, 综艺, 影视综其他 - 内容类目#运动健身: 减脂塑形, 滑雪, 滑板, 水上活动, 运动其他, 足球, 篮球, 跑步, 游泳 - 内容类目#宠物: 猫, 狗, 动物其他 - 内容类目#文化艺术: 社科, 文化, 艺术, 文化艺术其他 - 内容类目#兴趣爱好: 绘画, 手工, 阅读, 文具手账, 舞蹈, 兴趣爱好其他, 玩具周边 - 内容类目#生活记录: 接地气生活, 日常片段, 中外生活, 品质生活, 校园生活 - 内容类目#教育: 大学教育, k12教育, 家庭教育, 学习日常, 留学教育, 教育其他, 语言教育 - 内容类目#职场: 职场干货, 职场行业, 职业考试, 职场其他 - 内容类目#情感: 情感知识, 情感日常, 情感其他 - 内容类目#摄影: 人文风光摄影, 摄影技巧, 胶片摄影, 人像摄影, 摄影其他 - 内容类目#游戏: 手机游戏, 主机游戏, 游戏其他, 线下游戏 - 内容类目#科技数码: 移动数码, 玩机攻略, 数码科技其他 - 内容类目#出行旅游: 城市出行, 户外, 旅行 - 内容类目#音乐 - 内容类目#搞笑 - 内容类目#健康养生 - 内容类目#汽车: 用车攻略, 汽车评测, 汽车其他 - 内容类目#婚嫁: 婚礼造型, 婚礼记录, 婚礼经验, 婚礼用品 - 内容类目#商业财经 - 内容类目#素材 - 内容类目#其他 Industry categories: - 所属行业#母婴: 母婴出行, 哺乳喂养工具, 婴童个护清洁, 母婴家居, 母婴奶粉, 母婴辅零食, 婴童服饰鞋靴, 玩具相关, 母婴纸品, 孕产妇相关, 母婴营养品, 婴童面部护肤, 母婴小家电 - 所属行业#家用电器: 大家电, 厨卫电器, 生活电器, 家电套系 - 所属行业#3C数码: 手机, 数码设备, 电脑, 办公设备, 操作系统 - 所属行业#食品饮料: 休闲零食, 方便速食, 粮油调味, 预制菜, 饮料冲调, 乳制品, 水果/水产, 肉禽蛋品, 功能性食品, 酒类（新） - 所属行业#美妆个护: 彩妆, 美容护肤, 香水香薰, 身体洗护, 口腔护理, 头发护理, 美容仪器 - 所属行业#汽车出行: 乘用车, 摩托车, 电动自行车, 自行车, 卡车, 汽车用品, 维修保养, 汽车服务 - 所属行业#本地生活: 奶茶果汁(新), 咖啡(新), 甜品烘焙(新), 熟食卤味(新), 特色小吃/特产(新), 酒吧(新), 西式快餐(新), 中式快餐(新), 中式正餐(新), 西式正餐(新), 线下零售 - 所属行业#日化家清: 家务工具, 家用清洁, 纸品, 护理用品 - 所属行业#医疗健康: OTC, 保健食品, 保健用品, 非OTC药品, 健康机械, 视力保健, 家用医疗器械, 成人计生（械） - 所属行业#宠物（新）: 宠物服务, 宠物食品, 宠物用品, 养宠经验, 宠物药保 - 所属行业#家居家装: 灯饰光源, 家居百货, 家居建材零售, 家具, 家装辅材, 家装主材, 五金电具, 装修设计与工程服务, 智能家居, 家居卖场, 家居展会, 家纺, 餐厨杯 - 所属行业#出行旅游: 交通出行, 酒店住宿, 国内游(新), 出境游(新), 景点景区(新), 旅游攻略(新), 旅游主题(新) - 所属行业#教育培训: K12教育, 素质教育, 图书, 成人兴趣培训, 学历教育, 语言及留学, 早教, 职业教育 - 所属行业#金融行业: 保险, 贷款, 银行, 证券 - 所属行业#医疗医美: 口腔医疗, 眼科医疗, 皮肤美容, 植发养发, 体检机构(新), 月子妇产(新), 面部塑形, 医美身体塑形, 中医医疗 - 所属行业#免税平台: 美妆个护, 奢侈品 - 所属行业#服饰鞋包: 女装, 男装, 女鞋, 男鞋, 女士内衣, 男士内衣, 服饰配件, 童装/亲子装, 箱包, 旅行箱, 童鞋/亲子鞋 - 所属行业#珠宝配饰: 腕表, 首饰, 眼镜, 配饰, 珠宝摆件, 金条、金币 - 所属行业#运动户外: 运动鞋, 户外鞋, 运动服装, 户外服装, 运动户外装备, 运动服配, 健身器械, 运动现场 - 所属行业#文玩娱乐: 玩具, 游戏, 文玩收藏, 文体, 文具 - 所属行业#到店综合: 商务服务, 生活服务 - 所属行业#奢侈品: 箱包, 服饰, 鞋履, 珠宝配饰, 腕表, 运动户外, 品质生活, 婴童, 内衣, 高端酒店, 书写工具 - 所属行业#互联网: 平台电商, 网服, 游戏, 内容消费, 生活服务, 软件工具, 会员服务 - 所属行业#影像婚美: 婚纱摄影, 写真摄影, 婚礼服务, 婚恋交友 - 所属行业#房地产: 房产中介, 房产开发, 商业地产 Examples: - 内容类目#美妆 - 内容类目#美妆#整体妆容 - 所属行业#母婴#母婴出行 |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/hot-search.json`](../../../catalog/models/xiaohongshu/hot-search.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/hot-search
