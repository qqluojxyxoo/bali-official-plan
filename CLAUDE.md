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

## ⚙️ 修改工作流（Claude 必须遵守）

**每次对行程进行任何修改，必须同步完成以下三件事：**

1. **更新 `public/index.html`** — 修改对应的时间线节点、信息卡片等
2. **更新 Mac 日历**（iCloud「日程」日历）— 用 `mac-calendar` skill 通过 AppleScript 同步增删改日历事件
3. **推送到 Vercel** — `git add public/index.html && git commit -m "..." && git push origin main`，自动触发 Vercel 部署

> **三步缺一不可。** 不能只改 HTML 不改日历，也不能改了不推送。改完后告知用户 Vercel 链接。

---

## 用户真实需求

用户要求行程单满足：

- **时间线清晰、合理、无重叠**：每个时间节点都要符合实际逻辑（如：入境要排队，换钱在先，走路时间要算进去）
- **时间线顺序 = 真实行动顺序**：信息卡片（警告框、酒店信息、攻略）必须放在对应时间节点之后，而非之前
- **内容贴心实用**：每个节点要有详细说明、避坑提醒、具体找路指南，标注价格（IDR + 人民币参考）
- **两端同步**：HTML 是给两人查看的线上行程单，Mac 日历是出行时的提醒工具，两者必须保持一致

---

## 行程概览

| 天数 | 日期 | 内容 |
|------|------|------|
| D0 | 2/19 周四 | 凌晨广州出发 → 雅加达 T3 入境 → **Jakarta Airport Hotel T2 补眠** → 飞巴厘岛 → 仓古入住 |
| D1 | 2/20 周五 | 仓古：租摩托 → 稻田瑜伽 → Sensorium Brunch → Dang! Cookies → **AT 06 数字游民体验** → Love Anchor 集市 → 海神庙日落 → 夜生活 |
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

**⚠️ 雅加达 T2 / T3 之间有免费 Skytrain 接驳（T3 二楼，步行约 3 分钟，每 13 分钟一班，全程免费，06:00-24:00）。**

---

## 酒店信息

- **Amandaya Canggu**
  - 地址：9 Gang Jalak Indah, Canggu, Bali 80361
  - 入住：2/19（周四）22:00，退房：2/23（周一）12:00，共 4 晚
  - 房型：Deluxe Room（大床/无烟），含免费早餐 + WiFi
  - Agoda 预订号：955713410

---

## D0 详细时间线（雅加达段）

> 雅加达时间 = 北京时间 - 1 小时

| 时间（当地） | 内容 |
|---|---|
| 06:35 | 落地 T3 |
| 06:35 — 07:30 | 排队入境（约 40-60 分钟） |
| 07:30 — 08:00 | 换钱（ATM：BCA/Mandiri，取 300-400 万 IDR）+ 买 SIM（Telkomsel） |
| 08:00 — 08:30 | 步行前往 Digital Airport Hotel（出国际到达口→上 2F→找 5 号门→坐电梯下 1F） |
| 08:30 — 14:00 | 胶囊酒店补眠（约 5.5 小时） |
| 14:00 — 15:00 | 退房 → 洗漱 → 吃饭 |
| 15:00 — 15:30 | Skytrain T3→T2（从酒店→2F Skytrain 站→T2，约 5 分钟） |
| 15:30 — 18:00 | T2 办理 QZ818 值机手续，候机 |
| 18:00 | 起飞，飞巴厘岛 |

**Digital Airport Hotel 信息：**
- 位置：T3 国内区域 1 层
- 房型：胶囊舱，2 舱
- 费用：约 360,000–380,000 IDR/舱（≈165–175 元）
- 押金：50,000 IDR/人（退房退还）
- 联系：+62 811 9000 619
- 官网：digitalairporthotel.com

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
- `.highlight-box`：蓝色高亮信息卡片（用于找路攻略、酒店信息等）
- `.warning-box`：黄色警告信息卡片（用于重要提醒）
- `.tl-tag`：标签（tag-food / tag-sight / tag-transport / tag-tip / tag-beach / tag-culture / tag-nightlife）
- `.day-section`：每天的 section 容器
- `.timeline`：时间线容器（`::before` 是竖线，`.tl-item::before` 是圆点）

**时间线分段技巧（用于在时间线中插入信息卡片）：**
```html
<!-- 先关闭 timeline div -->
</div>

<!-- 插入 warning-box 或 highlight-box -->
<div class="warning-box">...</div>
<div class="highlight-box">...</div>

<!-- 再开新的 timeline div 继续 -->
<div class="timeline">
```

---

## 用户偏好 & 对话约定

- **语言：** 中文（用户是中文母语）
- **风格：** 贴心、实用，内容详实，有备选方案（省钱/高档），有避坑提醒
- **价格：** 优先标注 IDR，括号内附人民币参考（1 CNY ≈ 2,200 IDR）
- **时区：** 日历事件存为北京时间（UTC+8）；雅加达是 UTC+7（比北京慢 1 小时）
- **修改后必须执行：** 改 HTML → 改日历 → git push（三步缺一不可）

---

---

## Xulin Wei 地点收藏（对象 Wishlist）

> 文件存档：`xulin-wishlist.md`，2026-02-20 录入

### 🌴 巴厘岛 - 仓古（已纳入或备选）

| 地点 | 类型 | 备注 | 纳入行程 |
|------|------|------|---------|
| **AT 06 Train at Six** | 数字游民餐厅+办公 | ⭐4.9，D1下午主打 | ✅ D1 |
| **Sensorium Bali** | Brunch 咖啡厅 | ⭐4.6，D1 brunch | ✅ D1 |
| **Dang! Cookies** | 饼干甜品 | ⭐4.8，D1下午 | ✅ D1 |
| **Love Anchor Canggu** | 集市 | ⭐4.0，D1傍晚逛 | ✅ D1 |
| **Atlas Beach Club** | 海滩俱乐部 | ⭐4.7，Berawa Beach | 备选 D1/D4 |
| **FINNS Beach Club** | 海滩俱乐部 | ⭐4.7，免费入场 | 备选 D1/D4 |
| **Luigi's Hot Pizza Canggu** | 披萨 | ⭐4.3 | 备选 |
| **AKASA** | 咖啡店 | ⭐4.5 | 备选 |
| **Maiku Cafe** | 咖啡提拉米苏 | ⭐4.4 | 备选 |
| **Tropical Nomad Coworking** | 联合办公 | ⭐4.4，Day Pass 150k IDR | 备选 |
| **PUCO Rooftop Coworking** | 屋顶联合办公 | ⭐4.9，Day Pass 150k IDR | 备选 |
| **B Work Bali** | 联合办公 | ⭐4.3，Day Pass 280k IDR | 备选 |
| **Tribal Bali Coworking Hostel** | 数字游民青旅 | ⭐4.6，Pererenan | 备选 |

### 🌿 巴厘岛 - 乌布
| 地点 | 类型 | 备注 | 纳入行程 |
|------|------|------|---------|
| **Sacred Monkey Forest Sanctuary** | 猴林 | ⭐4.5 | ✅ D2 |
| **Seniman Coffee** | 数字游民咖啡厅 | ⭐4.6 | 备选 D2 |

### 🏖️ 巴厘岛 - 乌鲁瓦图
| 地点 | 类型 | 备注 | 纳入行程 |
|------|------|------|---------|
| **Blue Point Beach** | 海滩 | ⭐4.6 | ✅ D3 |
| **Rock Bar** | 悬崖酒吧 | ⭐4.5 | 备选 D3 |
| **Luna Beach Club** | 洞穴 bar | ⭐4.4 | 备选 D3 |

### 🏙️ 雅加达（D5）
| 地点 | 类型 | 备注 | 纳入行程 |
|------|------|------|---------|
| **National Monument (Monas)** | 纪念碑 | ⭐4.6 | ✅ D5 |
| **Taman Fatahillah + Café Batavia** | 历史地标 + 餐厅 | ⭐4.6/4.5 | ✅ D5 |
| **Jakarta History Museum** | 历史博物馆 | ⭐4.6 | ✅ D5 |
| **Scarlett's House BLOK M** | 虾油炒意面 | ⭐4.5 | 备选 D5 |
| **Blok M Square** | 购物中心 | ⭐4.4 | 备选 D5 |
| **Toko Kopi TUKU** | 本地人气咖啡 | ⭐4.7 | 备选 D5 |
| **Hotel GranDhika Iskandarsyah** | 雅加达酒店 | ⭐4.5 | 备选 D5 住宿 |

---

## D0 详细信息（已更新）

> 实际执行：T3入境换钱 → Skytrain T3→T2 → **Jakarta Airport Hotel T2** 补眠至15:00 → T2退房吃饭 → 值机QZ818

**Jakarta Airport Hotel（T2）信息：**
- 位置：T2 出发层上方，步行 3–5 分钟可达
- 联系：WhatsApp +62 811 184 8008 / @jakartaairport_hotel
- 退房时间：15:00 雅加达时间（北京时间 16:00）

---

*最后更新：2026-02-20*
