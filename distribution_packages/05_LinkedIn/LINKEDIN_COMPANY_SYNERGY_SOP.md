# 🌐 木齐科技 领英企业主页 (Company Page) 与合伙人兼 CEO 双轮协同分发 SOP

> **文档性质**: 木齐科技出海社交矩阵 • 领英（LinkedIn）主干运营指导规程  
> **企业主页**: [Shandong MUQI Health Technology (ID: 72043164)](https://www.linkedin.com/company/72043164)  
> **管理后台**: `https://www.linkedin.com/company/72043164/admin/dashboard/`  
> **发言人账号**: **Martin Chen (合伙人兼 CEO • Partner & CEO)**  
> **官方站点技术底座**: `https://www.emuqi.com/blog/`  
> **核心原则**: 权威背书 + 人设穿透、正文零外链防降权、Document 轮播画册抢占停留时长、First Comment 精准导流回官网。

---

## 1. 领英双轮协同架构 (The "Dual-Engine" B2B Formula)

领英海外 B2B 营销的核心并非单点发帖，而是通过 **“企业主页 (Corporate Authority)”** 与 **“高管人设 (Executive Thought-Leadership)”** 的相互呼应与背书，构建采购决策人视角的立体信任：

```
                             ┌──────────────────────────────────┐
                             │    emuqi.com/blog 官方技术长文    │
                             │ (Single Source of Technical Truth│
                             └─────────────────┬────────────────┘
                                               │
                                       【二创技术转化】
                                               │
                     ┌─────────────────────────┴─────────────────────────┐
                     ▼                                                   ▼
       【🏢 领英企业主页 (Company Page)】                【👤 合伙人兼 CEO (Martin Chen)】
       ─────────────────────────────────                 ─────────────────────────────────
       • 属性：国家级专精特新“小巨人”企业背书            • 属性：行业资深专家、实战派研发决策人
       • 形式：官方白皮书发布、产品矩阵发布、            • 形式：第一人称技术 Teardown、行业痛点抨击、
               SAC/TC621 国家标准动态、企业认证                  商业模式解构 (如“剃须刀与刀片”耗材模型)
       • 内容重点：严谨、客观、企业实力、合作背书        • 内容重点：敏锐、犀利、工程细节、启发式洞察
       • 动作：发布官方 PDF Document 轮播画册            • 动作：转发企业主页内容 + 补充深度个人见解
                     │                                                   │
                     └─────────────────────────┬─────────────────────────┘
                                               ▼
                                  【💬 First Comment 锁位】
                                挂载带 UTM 参数的官网 Blog 链接
                                               ▼
                               【🎯 官网询盘与样件申领转化闭环】
```

### 1.1 角色分工与执行规范
1. **企业官方主页 (`Company Page - 72043164`)**:
   - 定位：**权威性与制造实力输出**。展示 SAC/TC621 委员单位资质、SGS 检测报告、全球 35% 固态氢材料供应份额、1800+ 客户基础。
   - 统一身份：Shandong MUQI Health Technology Co., Ltd. (MUQI Tech)。
2. **合伙人兼 CEO 个人号 (`Martin Chen`)**:
   - 定位：**思想领导力与商业痛点穿透 (Thought-Leadership)**。
   - **身份铁律**：统一使用 **合伙人兼 CEO (Partner & CEO)**。**严禁使用「创始人」或「Founder」**；对外统一使用英文名 Martin Chen。

---

## 2. 领英算法机制与防降权铁律 (Algorithm Optimization Rules)

### 2.1 算法三大偏好
1. **Dwell Time（停留时长）压倒一切**：
   - 算法优先奖励让用户在 Feed 流中停留超过 20~45 秒的动态。
   - **最高权重形式：PDF Document（轮播画册）**。相比纯文本或单图，多页 PDF 可引导用户横向翻页（Swipe），产生多次点击与长达数十秒的互动，曝光量通常是普通帖的 **3~5 倍**。
2. **严惩正文出站外链（Zero External Links in Body）**：
   - 领英平台极度排斥将流量直接导向站外。若在 Post 正文直接粘贴 `emuqi.com` 链接，算法会自动将帖子曝光量削减 **50% 至 70%**。
   - **破解铁律**：正文结尾只写：  
     *“📖 Full engineering whitepaper & CAD schematics linked in the first comment below.”*
3. **First Comment（第一条评论）锁位导流 SOP**：
   - 主帖成功发出后 **10 秒内**，立即由发布账号在评论区发出带有 UTM 追踪参数的官方 Blog 链接。
   - 作者账号对该条评论**自点 1 个赞**，并保持其置顶在 Top #1 位置。

### 2.2 互动黄金 60 分钟 (The Golden Hour)
- 帖子发出后的前 60 分钟内，若能获得 3~5 条深度评论（至少 5 个英文单词以上）与多次点赞，帖子将被系统推入更大的二阶、三阶推荐池（2nd & 3rd-degree connections）。
- 协同动作：主页发帖后，合伙人 Martin Chen 与团队成员需在 30 分钟内进行点赞并撰写深度评论互动。

---

## 3. 全链路 UTM 参数追踪规范 (UTM Tracking Convention)

为了在 Google Analytics 4 (GA4) 和官网统计后台精准统计从领英引流的 B2B 访客与样品申领询盘，所有放置在 First Comment 中的外链必须严格携带以下 UTM 标签：

| 参数项 | 参数值 | 说明 |
|---|---|---|
| `utm_source` | `linkedin` | 来源平台标识 |
| `utm_medium` | `company_page` 或 `partner_profile` | 区分来自企业主页还是 Martin 个人号 |
| `utm_campaign` | `{blog-slug}` (如 `solid-state-vs-pem`) | 营销战役/博客主题 |
| `utm_content` | `first_comment` 或 `document_cta` | 链接放置位置 |

**示例链接**：
```text
https://www.emuqi.com/blog/hydrogen-water-technology-comparison-en.html?utm_source=linkedin&utm_medium=company_page&utm_campaign=solid-state-vs-pem&utm_content=first_comment
```

---

## 4. PDF Document 轮播画册制作与发布规范 (Slide Specs)

每个二创帖子均配套推荐的 **PDF Document 轮播画册**（可由 PowerPoint / Canva / Figma 导出为 PDF）：
- **比例与分辨率**：推荐 **16:9**（1920×1080）或 **4:5**（1080×1350，移动端屏占比最大）。
- **页数控制**：**5 至 8 页**最佳。
- **页面节奏**：
  - **Slide 1 (封面)**：超大反差标题（Bold Hook）+ 高清产品/实验主图 + "Swipe to teardown ➡️" 指引。
  - **Slide 2 (行业痛点/痛点撕裂)**：现有技术为何令 OEM 研发头疼（如电极结垢、臭氧、高压安规）。
  - **Slide 3~5 (核心机理解构与对比表)**：硬核参数、数据表、材料结构剖面。
  - **Slide 6 (商业模型革新)**：硬件到耗材复购、OEM 收益对比。
  - **Slide 7/8 (行动号召 CTA)**：企业实力背书（国家级小巨人、SAC/TC621）、样品申领方式。

---

## 5. 海外最佳发布时间表 (Optimal Posting Windows)

针对欧美全球采购决策人、硬件研发工程师、品牌创始人：

| 目标区域 | 推荐发布时段 (当地时间) | 对应北京时间 (GMT+8) | 推荐星期 |
|---|---|---|---|
| **北美市场 (美东 EST)** | **08:00 - 10:00 AM** | **20:00 - 22:00** (夏令时) | **周二、周三、周四** |
| **欧洲市场 (中欧 CET)** | **14:00 - 16:00 PM** | **20:00 - 22:00** (夏令时) | **周二、周三、周四** |
| **亚太/澳新 (AEST)** | **10:00 - 12:00 AM** | **08:00 - 10:00** | **周二、周五** |

> **提示**：避开周一上午（忙于周会与邮件清理）与周五下午（进入周末休假状态）。

---

## 6. 二创内容矩阵清单与索引 (Content Matrix Index)

在 `emuqi/distribution_packages/05_LinkedIn/` 目录下提供 6 套开箱即用的二创全案：

1. `post_01_solid_state_vs_pem_9d_comparison.md`: 固态氢与电解 9 维对比（8 页技术对比画册）
2. `post_02_foot_spa_4_2b_consumable_revolution.md`: 42 亿美元足浴设备耗材化（6 页剃须刀与刀片模型画册）
3. `post_03_gary_brecka_biohacking_solid_state.md`: Gary Brecka 欧美 Biohacking 热潮与固态泡腾片解构
4. `post_04_facial_steamer_nespresso_moment.md`: 高功率美容熏蒸仪外置反应仓改造（无模具损耗升级）
5. `post_05_femtech_microecology_oem.md`: 女性生殖微生态与富氢疗法（MgH2 × 活性乳酸菌）
6. `post_06_appliance_antimicrobial_icr_tech.md`: SAC/TC621 标委会与家电除菌防臭新材料解决方案
