# 巴厘岛行程单项目 · Claude 上下文

## 项目背景

这是一个为 **LUO/JIAXI & WEI/XULIN** 两人准备的巴厘岛旅行行程单，以 HTML 单页面形式呈现，部署在 Vercel 上，方便两个人随时查看。

- **出行时间：** 2026 年 2 月 19 日（周四）— 2 月 25 日（凌晨）
- **行程：** 广州 → 雅加达转机 → 巴厘岛（仓古 / 乌布 / 乌鲁瓦图）→ 雅加达过夜 → 广州

---

## 文件结构

```
bali plan04/
├── public/
│   └── index.html        ← ⭐ 唯一维护的主文件（Vercel 部署此文件）
├── bali-itinerary.html   ← 历史备份，不再维护，请忽略
├── vercel.json           ← Vercel 配置（outputDirectory: public）
├── CLAUDE.md             ← 本文件（项目上下文）
└── .gitignore
```

> **重要：以后所有修改只改 `public/index.html`，不要动 `bali-itinerary.html`。**

---

## 部署方式

- **GitHub 仓库：** https://github.com/qqluojxyxoo/bali-official-plan
- **线上地址：** https://bali-official-plan.vercel.app
- **Vercel 项目：** qqluojxyxoos-projects / bali-official-plan

修改完 `public/index.html` 后，执行：

```bash
cd "/Users/jiaxiluo/Haha/临时/bali plan04"
git add public/index.html
git commit -m "描述修改内容"
git push origin main
```

Vercel 会自动检测 GitHub push，1 分钟内线上同步更新。

---

## 行程概览

| 天数 | 日期 | 内容 |
|------|------|------|
| D0 | 2/19 周四 | 凌晨广州出发 → 雅加达 T3 入境 → **Digital Airport Hotel 胶囊酒店补眠** → T3→T2 Skytrain → 飞巴厘岛 → 仓古入住 |
| D1 | 2/20 周五 | 仓古：Batu Bolong 冲浪 → 稻田骑行 → 海神庙 Tanah Lot 日落 → 夜生活 |
| D2 | 2/21 周六 | 乌布一日游：梯田 → 圣泉寺 → 猴林 → 王宫 |
| D3 | 2/22 周日 | 乌鲁瓦图：Single Fin 悬崖餐厅 → 蓝点海滩 → 乌鲁瓦图寺 → Kecak 火舞 → 金巴兰海鲜 |
| D4 | 2/23 周一 | 仓古告别早晨 → 超市扫货 → 飞雅加达 |
| D5 | 2/24 周二 | 雅加达：Monas → Nasi Padang → 购物 → 飞广州 |
| 返程 | 2/25 凌晨 | 01:30 广州白云 T2 落地 |

---

## 关键航班信息

| 航班 | 日期 | 出发 | 到达 | 备注 |
|------|------|------|------|------|
| 8B861 | 2/19 | 广州 T2 02:30 | 雅加达 T3 06:35 | PNR: YJD13E |
| QZ818 | 2/19 | 雅加达 T2 18:00 | 巴厘岛 20:50 | — |
| QZ809 | 2/23 | 巴厘岛 18:50 | 雅加达 T2 19:50 | — |
| 8B860 | 2/24 | 雅加达 T3 18:50 | 广州 T2 01:30+1 | — |

**⚠️ 雅加达 T2 / T3 之间有免费 Skytrain 接驳，约 10 分钟。**

---

## 酒店信息

- **Amandaya Canggu**
  - 地址：9 Gang Jalak Indah, Canggu, Bali 80361
  - 入住：2/19（周四）22:00，退房：2/23（周一）12:00，共 4 晚
  - 房型：Deluxe Room（大床/无烟），含免费早餐 + WiFi
  - Agoda 预订号：955713410

---

## D0 重要变更（已更新）

原计划：雅加达半日游（科塔图阿、清真寺、Cafe Batavia）
**现计划：落地后直接去机场胶囊酒店休息**

**Digital Airport Hotel**
- 位置：T3 国内区域 1 层（Domestic Area 1F）
- 房型：2 舱（每人一舱）
- 费用：约 360,000-380,000 IDR/舱（≈165-175 元）
- 押金：50,000 IDR/人（退房退还）
- 联系：+62 811 9000 619
- 官网：digitalairporthotel.com
- **找路：** 出国际到达口 → 上 2 层出发层 → 找 5 号门 → 坐电梯下一层 → 到达

---

## HTML 页面结构说明

`public/index.html` 是一个自包含的单 HTML 文件，无外部依赖。

主要 CSS 变量（在 `:root` 中定义）：
- `--ocean`: #0a84ff（蓝色，D0 主色）
- `--teal`: #30d5c8（青色，D1 主色）
- `--green`: #34c759（绿色，D2 主色）
- `--sunset`: #ff6723（橙色，D3 主色）
- `--purple`: #af52de（紫色，D4 主色）
- `--gold`: #f5a623（金色）

关键 CSS 类：
- `.tl-item`：时间线节点（卡片）
- `.tl-item.tl-ocean / tl-teal / tl-sunset...`：控制时间线圆点颜色
- `.highlight-box`：蓝色高亮信息卡片
- `.warning-box`：黄色警告信息卡片
- `.tl-tag`：标签（tag-food / tag-sight / tag-transport / tag-tip / tag-beach / tag-culture / tag-nightlife）
- `.day-section`：每天的 section 容器
- `.timeline`：时间线容器（`::before` 是竖线，`.tl-item::before` 是圆点）

---

## 用户偏好 & 对话约定

- **语言：** 中文（用户是中文母语）
- **风格：** 贴心、实用，内容详实，有备选方案（省钱/高档），有避坑提醒
- **价格：** 优先标注 IDR，括号内附人民币参考（1 CNY ≈ 2,200 IDR）
- **修改后的部署流程：** 改 `public/index.html` → git commit → git push（自动触发 Vercel）
- **日历同步：** 重要行程变更后同步更新 Mac 日历（iCloud「日程」日历）

---

*最后更新：2026-02-18*
