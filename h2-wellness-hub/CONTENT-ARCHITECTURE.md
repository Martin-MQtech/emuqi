# H2 Wellness Hub — Content Architecture & Publishing Guide

**Scope:** H2 Wellness Hub only  
**Parent:** `../DESIGN.md` defines Emuqi-wide brand, navigation, deployment, and shared technical rules.  
**Role:** This is the single governing document for the H2 Wellness Hub sub-section: its visual identity, content architecture, bilingual publishing, SEO/GEO, source policy, update workflow, and future migration rules.

## 0. Visual identity and layout

H2 Wellness Hub is an Emuqi-hosted but industry-neutral sub-branch with a restrained editorial identity: deep navy structure, a narrow orange source accent, DM Sans for display/UI text, and Inter for body text. MUQI is one disclosed player and case source among many, never the visual or editorial default.

The H₂ sigil has two molecular nodes, a connecting bond, and a central orange mark. It should read as a research-index symbol, not a generic wellness-app icon.

```text
Ink / structure:     #0A1628
Navy:                #1A3A6E
Source accent:       #F47B20
Link blue:           #1D4ED8
Background paper:    #F5F6F8
Rules:               #DBE3ED
Display / UI:        DM Sans
Body:                Inter
```

Below the Header, each Hub edition uses a concise two-column editorial bulletin composition. The current-language content owns the full reading column; the opposite side is an edition-link card, never a duplicate long-form translation. A thin vertical rule makes the relationship visible on desktop. On mobile, the current-language content appears first and the edition card follows.

The Header is always English-first across both editions. Its category labels remain `Industry Pulse`, `Resource Desk`, and `Casebook`; Chinese belongs to the independent Chinese body content and language switch, not to the primary navigation hierarchy.

Use dates, source labels, concise headings, and direct source links for hierarchy. Avoid dashboards, large category grids, product-card walls, decorative medical imagery, and complex filters.

## 1. Purpose

H2 Wellness Hub is a lightweight bilingual industry bulletin for molecular hydrogen and hydrogen health.

It helps visitors:

1. Notice useful industry developments.
2. Reach useful external tools and organizations.
3. Learn from interesting products, applications, and cases.

It is not a research institution, broad industry database, medical-information authority, or “best products” website. It is a commercial and industry lens on the category.

## 2. Phase 1 structure

The homepage has exactly three sections, in this order:

| Order | English | Chinese | Purpose |
|---|---|---|---|
| 01 | Industry Pulse | 行业动态 | Commercial developments: brand moves, retail/channel expansion, events, standards in practice, partnerships, launches, and market changes |
| 02 | Resource Desk | 工具资源 | Academic knowledge sources: experts, research institutions, long-running public archives, patents, databases, testing, standards, regulation, and methods |
| 03 | Casebook | 行业案例 | Industry cases: research-to-market institutions, enterprises, products, channels, applications, commercialization paths, and quality/compliance lessons |

Do not add Phase 1 navigation sections for evidence, markets, standards, organizations, companies, events, or country maps. These are content types/tags inside the three sections.

Japan, the United States, China, and other regions are tags on individual items, not homepage silos.

## 3. Independent bilingual URLs

| Edition | Route | HTML language | Canonical |
|---|---|---|---|
| English | `/h2-wellness-hub/` | `en` | `https://emuqi.com/h2-wellness-hub/` |
| Simplified Chinese | `/h2-wellness-hub/zh/` | `zh-Hans` | `https://emuqi.com/h2-wellness-hub/zh/` |

Each edition has its own complete native-language reading content. The opposite visual column is only an edition card linking to the independent counterpart.

Both pages use reciprocal `hreflang="en"` and `hreflang="zh-Hans"`; English remains `x-default`. Do not use a JavaScript-only language switcher, hidden language content, or automatic machine translation as published content.

For a future substantial item, create a matching URL pair, for example:

```text
/h2-wellness-hub/pulse/example-slug.html
/h2-wellness-hub/zh/pulse/example-slug.html
```

Add reciprocal `hreflang` only when the entries genuinely match in scope and editorial review.

## 4. SEO/GEO rules

- Each edition needs native-language title, description, headings, body copy, and canonical URL.
- Use visible original-source links, dates, region tags, and a concise factual explanation of why an item matters.
- A short other-language edition card is permitted as navigation; never duplicate a complete article in both languages on one page.
- Keep content server-rendered static HTML. Do not hide it in client-side components.

## 5. Publishing rules

### Industry Pulse / 行业动态

Publish only when an item has a credible source and a practical reason for industry readers to care.

Suitable: brand moves, retail/channel expansion, events, policy, standards in practice, partnerships, launches, investment, and credible market movement. Research belongs in Resource Desk unless there is a clear business, commercialization, or industry-structure implication.

Avoid: routine press-release reposts, unsupported health claims, treating a trial registration as a positive result, and publishing merely for volume.

Minimum fields: title, date, region tag, why it matters, original source URL, source type.

### Resource Desk / 工具资源

Link to organizations that already maintain authoritative material. Do not recreate their databases.

Categories: expert profiles, long-running public knowledge archives, research institutions, publication/trial databases, patent databases, testing laboratories, accreditation directories, standards issuers, regulatory lookup tools, conferences, and industry organizations.

Minimum fields: name, one-sentence use case, official URL, region tag, last checked date, and scope note if needed.

### Casebook / 行业案例

Select an item because it demonstrates an idea or lesson, not because it supports a universal product claim.

Possible types: research-to-market institutions, research programmes, enterprise profiles, product/application design, channel models, testing/quality/compliance practice, collaborations, and event formats.

MUQI/Emuqi content is a disclosed Casebook source, not a default editorial conclusion. Treat solid-state hydrogen materials, functional ceramics, hydrogen water applications, hydrogen agriculture materials, hydrogen skincare materials, and OEM/ODM productization as internal cases. Every MUQI case must be explicitly labelled as Emuqi/MUQI content and should separate material mechanism, product design, channel/use case, and evidence boundary. It should sit alongside, not above, external cases.

Minimum fields: what it is, why it matters, source URL(s), source type, region tag, and key limitation/disclosure.

Never label an item “best”, “recommended”, medically proven, or universally effective unless a precise primary source supports the exact claim.

## 6. Source and disclosure

Source priority:

1. Regulators, standards issuers, trial registries, original publications, official event organizers, and institution pages.
2. Accredited laboratory scope pages and reputable public databases.
3. Company pages only for the company’s own declared information.

Do not turn food-use notices, registration/listing, laboratory accreditation, association membership, training certificates, marketing badges, or company reports into medical-efficacy certification.

Any Emuqi, partner, sponsored, affiliate, or company-provided content must be visibly labelled in the page body.

## 7. Maintenance and expansion

- A monthly batch update is sufficient in Phase 1.
- A quiet month can have zero Industry Pulse posts.
- Update Resource Desk links when a source changes or a better source appears.
- Add Casebook entries only when the source trail and practical lesson are clear.
- Keep candidates and research notes in `data/seed-resources.json`; surface only useful, current items.
- Split a section into a separate page only when it has enough active useful material and a realistic update owner.

If the Hub later moves to its own domain, move this folder, preserve URL patterns where practical, and redirect the Emuqi routes. The three-section model remains valid.

## 8. Chinese-world content reservoir

Chinese content is not a translation layer. It should be sourced independently from Chinese-language public material and rebuilt into original posts for the Chinese edition.

Priority Chinese source classes:

- Regulators and official databases: NMPA, SAMR, NHC, CNIPA, national standards platforms, China clinical-trial registries.
- Academic and professional bodies: Chinese medical/gerontology associations, hydrogen biomedicine branches, universities and research centers.
- Agricultural and local-government sources: agriculture bureaus, local government project pages, demonstration-base reports, standard-release notices.
- Trade shows and industry events: hydrogen health, gas equipment, health industry and functional product exhibitions.
- Company and channel sources: treated as company claims unless independently corroborated.
- Expert and knowledge sources: official university profiles, academic archives, long-running public expert columns, and verified public-account entry points. Use them as navigation and topic-discovery sources; do not automatically elevate an individual interpretation to clinical guidance.

Initial expert/knowledge-source entries include Sun Xuejun's Shanghai Jiao Tong University Hydrogen Science Center profile and public ScienceNet archive. The public WeChat knowledge sources 《氢思语》 (`hydrogen_thinker`) and 氢思云 (`hydrogen_word`) may be listed only after their currently active public entry points are verified; account posts should be quoted with author/date/source attribution and linked to primary studies where available.

Priority Chinese topic domains:

1. 氢农业 — demonstration bases, standards, irrigation/fertigation equipment, high-value crops, channel economics, agricultural service models.
2. 氢医学 — clinical projects, devices, regulatory status, hospital adoption, evidence boundaries, conference signals.
3. 氢生物学 — research platforms, patents, translational research, biological mechanisms as R&D signals rather than efficacy articles.
4. 氢健康产业 — products, supply chain, retail/channel, testing, standards, compliance, events, and real company cases.

Long-term Chinese editorial series should include: 氢农业示范账本, 富氢农业标准观察, 农业装备与气水肥系统, 氢生物学研究雷达, 科研转化与技术许可, 氢医学器械监管地图, 临床研究与证据治理, 氢健康产品合规观察, 富氢食品与饮品商业化, 产业链与制造能力, 渠道门店与服务模式, 产业投资与公司观察, 会展招采与市场信号, 风险反证与行业治理.

These series can support hundreds of future posts. The rule is to write from industry structure, commercialization, compliance, technology transfer, supply chain, and case analysis, not from generic “hydrogen benefits” education.

### Initial 140-post Chinese idea bank

Use the following as a working reservoir, not a pre-approved claim list. Every post still needs a dated source, a source-type label, and an evidence/compliance review before publication.

#### A. 氢农业示范账本

1. 富氢水稻从试验田到商品米：示范项目的商业闭环
2. 示范田之后：富氢水稻的设备、电力、人工与溢价账
3. 高温、台风与倒伏：氢农业项目如何做抗逆验证
4. 富氢草莓项目的对照组、季节数据与销售数据
5. 番茄、草莓、水稻：哪类作物适合先做商业验证
6. 从卖农产品到卖品牌：富氢标签的溢价可否持续
7. 氢农业基地如何用亩均利润而非单次增产评价项目
8. 地方政府报道中的氢农业数据，哪些需要二次核验
9. 示范面积扩大后，氢农业项目会遇到哪些运营问题
10. 农业合作社为何可能成为氢农业最早的付费客户

#### B. 富氢农业标准观察

1. 富氢水稻种植团体标准意味着什么，又不意味着什么
2. 团体标准、地方标准、行业标准、国家标准如何区分
3. 富氢水灌溉技术规程应公开哪些关键指标
4. 从水中氢浓度到田间稳定性：检测难题
5. 富氢农产品能否建立可追溯标签体系
6. 农产品品质指标如何进入技术标准
7. 设备厂商参与团体标准时如何避免自我背书
8. 氢农业标准化下一站：检测、装备接口还是示范评价
9. 一份团体标准的发布流程、适用边界与企业采用成本
10. 标准发布日期之后，企业还应追踪哪些执行信息

#### C. 农业装备与气水肥系统

1. 纳米气雾水、滴灌与水肥一体机：设备究竟卖什么
2. 气体发生装置进入农业大棚后的安全与运维清单
3. 电解、供气与灌溉联动的能源成本模型
4. 智能控制系统能否成为设备的主要利润来源
5. 易损件、检测件与售后网络的真实价值
6. 大棚改造与新建基地：两种设备适配路径
7. 农业场景低浓度气体溶解技术的竞争方向
8. 设备采购中应要求供应商披露哪些性能数据
9. 从设备交付到种植服务：商业模式的转向
10. 农服公司如何把氢农业设备纳入既有服务包

#### D. 氢农业供应链与渠道

1. 电解、材料、传感器、灌溉设备如何形成供应链
2. 经销商、农服公司与农业园区谁掌握落地入口
3. 氢农业项目的设备融资与租赁是否可行
4. 从试点到复制：最缺的是技术还是农艺服务
5. 富氢农产品进入商超、餐饮和会员店的渠道门槛
6. 区域公用品牌如何承接富氢农产品溢价
7. 如何避免设备卖出后无人维护
8. 大宗采购方如何审核相关农产品宣称
9. 农业展会参展商名单如何反映供应链变化
10. 招商新闻与真实客户订单之间差多远

#### E. 农业实证与商业尽调

1. 可信种植试验应包含哪些对照与统计指标
2. 增产之外，种植者真正关心的现金回收期
3. 为什么单季丰收不能证明可规模化
4. 地块、品种、季节与管理水平如何影响结果
5. 如何区分氢技术贡献与水肥、温控贡献
6. 第三方检测应测什么
7. 从小试到百亩的验证节点
8. 新闻稿中的“无农药”“无残留”等风险词
9. 投资人应索取的十项项目数据
10. 如何把试验数据写成负责任的商业观察

#### F. 氢生物学研究雷达

1. 氢生物学论文如何变成研究趋势，而非功效广告
2. 从氧化应激到信号通路：基础研究如何服务研发
3. 细胞、动物与人体研究的证据阶梯
4. 剂量、浓度与递送方式的可比性问题
5. 交叉研究平台如何推动材料与生命科学合作
6. 专利中常见的制备、递送、检测与设备路线
7. 联合实验室如何区分科研合作与营销背书
8. 可重复性为何是产业化门槛
9. 从论文到专利再到产品，转化在哪里断裂
10. 研究中心的公开项目如何成为产业情报线索

#### G. 科研转化与技术许可

1. 高校氢科学成果如何进入企业产品管线
2. 技术转让、许可与作价入股的选择
3. 一项氢相关专利离可销售产品还有多远
4. 专利授权率不能说明什么
5. 联合研发公告如何核验真实进度
6. 概念验证资金能否补足早期转化缺口
7. 临床资源、工程能力与注册路径谁决定效率
8. 制氢材料专利与终端设备专利的价值差异
9. 专利许可公告能揭示哪些产业链关系
10. 企业为何应把技术转移视为渠道问题

#### H. 氢医学器械监管地图

1. 氢氧气雾化机注册信息怎么读
2. 创新医疗器械通道对氢相关设备意味着什么
3. 医疗器械与健康消费设备的边界
4. 家用、机构用与康复用设备的监管差异
5. 气体设备的浓度、报警、维护与安全设计
6. 一张注册证不能覆盖哪些宣传场景
7. 器械变更公告如何成为竞争情报
8. 从样机到注册的时间、临床与质量体系成本
9. 注册之后的医院准入、招采与培训问题
10. 合规团队如何管理设备的公开材料

#### I. 临床研究与证据治理

1. 氢相关临床试验注册信息应如何阅读
2. 试验登记、论文与产品注册并不是同一件事
3. 开放标签、随机对照与真实世界研究的商业含义
4. 终点指标改善能否转成市场宣称
5. 小样本、短周期研究的解读误区
6. 结果未披露时企业如何沟通而不越界
7. 历史临床应用线索应如何写出时代背景
8. 医学事务团队如何管理证据库
9. 研究者发起研究与注册临床的角色差异
10. 透明项目如何成为行业 Casebook 内容

#### J. 氢健康产品合规观察

1. 器械、食品、日用品与服务的四类身份判断
2. 富氢水产品最常见的宣传风险词
3. “抗氧化”“改善免疫”等表述的边界
4. 体验店、会员制与老年客群的渠道风险
5. 直播销售设备时的内容审核问题
6. 广告法与器械广告审查如何衔接
7. 经销商培训材料如何避免疗效承诺
8. 消费者投诉如何暴露售后与宣称问题
9. 行政处罚案例的渠道治理启示
10. 品牌如何建立内容发布前审查表

#### K. 富氢食品与饮品商业化

1. 食品添加剂氢气标准与富氢饮品的真实关系
2. 氢浓度、包装、储存与货架期问题
3. 罐装、瓶装、现场制备三种供应模式
4. 如何做质量控制而不作保健承诺
5. 食品场景中的原料、加工与成品宣称边界
6. 常温与冷链物流成本比较
7. 高端水、功能饮品与氢水的渠道差异
8. 检测报告与消费者信任的关系
9. 科技感与合规表达的冲突
10. 即饮氢水如何走进区域零售体系

#### L. 产业链与制造能力

1. 终端设备的核心零部件清单
2. 电解槽、膜材料、催化剂与成本传导
3. 气体纯度、流量与质量体系
4. 医疗与消费级设备的质量管理差异
5. 国产化替代的机会与盲点
6. 制造成本与售后成本的双重结构
7. 从代工到自有品牌的路径选择
8. 安全检测、认证与保险如何影响商业化
9. 供应链波动下应该优先保障哪些关键件
10. MUQI 固态材料在供应链中的可能位置

#### M. 渠道、门店与服务模式

1. 氢健康体验店为何容易成为合规高风险渠道
2. 医院、康复、养老与家庭的准入逻辑
3. 设备租赁模式的商业账与责任边界
4. 售后服务是否才是硬件护城河
5. 会员制体验服务如何避免医疗宣传红线
6. 经销网络扩张前需要哪些培训与稽核
7. 产品进入药房和连锁健康店的可行路径
8. 私域健康内容审核与投诉处理
9. 组合销售的风险点
10. Echo × iCRYO 案例对中国渠道的启发

#### N. 产业投资与公司观察

1. 融资新闻应看估值还是注册与渠道进展
2. 氢医学设备公司的商业化成熟度框架
3. 氢农业创业公司的客户验证与专利数量
4. 战略合作公告如何区分订单、研发和营销联盟
5. 并购标的应重点核验哪些资产
6. 上市公司涉氢公告的业务实质与收入占比
7. 产业基金最应警惕的监管风险
8. 研发投入与销售费用如何读
9. “独家”“首创”“唯一”的核验方法
10. 木齐科技案例如何从材料端讲产业化故事

#### O. 会展、招采与市场信号

1. 一场氢健康展会如何读出供应链与渠道变化
2. 参展名单能否预测下一个产品品类
3. 论坛嘉宾与签约：商业线索还是活动传播
4. 招采公告如何发现真实采购需求
5. 政府、科研和医院采购信号的差异
6. 氢农业项目出现在招商目录意味着什么
7. 新品发布后如何追踪注册、上市和渠道验证
8. 团体标准发布时如何审阅起草单位与范围
9. 从展商到客户：如何追踪商业化兑现
10. 中日美展会的观察维度如何统一

#### P. 风险、反证与行业治理

1. 行业最需要的是可核验数据而非更多概念
2. “天然”“无毒”为什么不等于可随意宣传
3. 安全事故的制造、销售、使用与维护责任链
4. 老年人营销的合规责任不能外包给经销商
5. 标准、注册、专利、论文各自不能证明什么
6. 企业案例何时只能写成公司主张
7. 如何为商业观察建立来源等级标签
8. 氢农业“无农药”表述的监管风险
9. 一篇负责任的氢健康商业观察稿的免责声明
10. Casebook 如何同时呈现机会与边界

## 9. Hero banner asset rule

The Hub keeps MUQI's visual system: orange, white, deep blue gradients, and black, but its Hero visuals must be industry-neutral. Never use MUQI products, packaging, factory/laboratory photographs, product material shots, or other proprietary business imagery as Hub Hero material.

Future generated banners should stay in the same palette and depict a credible blend of molecular hydrogen medicine, biology, high-tech materials, and industry application. Avoid cartoon molecules, stock doctors, exaggerated medical imagery, and palettes outside MUQI's navy/black/orange/white system. The current CSS molecular-network Hero is an intentional neutral fallback until licensed or generated industry imagery is available.

## 10. Terminology and content-build log

### Editorial terminology decision — 2026-07-29

Use **Hydrogen Wellness Industry** as the preferred English term for the commercial category commonly called “氢健康产业”: products, consumer and professional wellness services, channels, quality practices, standards in use, and market cases.

**Hydrogen Health** remains a broad umbrella term and is retained where necessary for the established H2 Wellness Hub name, existing URLs, or broad discovery language. It is not the preferred industry-category label.

Use **Healthcare** only where the source is genuinely about hospital care, clinical research, medical-gas protocols, medical-device regulation, or other healthcare-system contexts. Do not use a Healthcare source to substantiate a Hydrogen Wellness Industry product claim, and do not present a wellness case as healthcare.

### Casebook article format decision — 2026-07-29

Casebook homepage entries must progressively become **local editorial articles**, rather than direct outbound links. Each substantial case has an independent English/Chinese URL pair under:

```text
/h2-wellness-hub/cases/<slug>.html
/h2-wellness-hub/zh/cases/<slug>.html
```

Each article is an original H2 Wellness Hub industry analysis: it states the case, explains the industry lesson, separates what the source establishes from what it does not establish, and provides a clearly labelled **Original source / 原始来源** card at the end. The source card links to the primary material for verification. This creates original, indexable bilingual content without obscuring provenance.

Article rules:

- The homepage must point to the local article; the local article links out to the original source.
- English and Chinese pages are independently written, paired with reciprocal `hreflang`, and never presented as a single mechanically duplicated page.
- A single Google AdSense placement belongs after the source card and before the footer. Use a visible placeholder until an approved ad-unit slot is available.
- Titles and metadata must name the organization and the industry lesson, not claim a health outcome.
- The first implementation is the AHHA industry-governance case: `cases/ahha-industry-standards.html` and `zh/cases/ahha-industry-standards.html`.

The second implementation is the Keio University UMIN000058083 exercise-study case: `cases/keio-exercise-hydrogen-study.html` and `zh/cases/keio-exercise-hydrogen-study.html`. It demonstrates the difference between a visible research protocol and a published result, and is a reference pattern for future trial-registry articles.

### Internal hashtag, SEO, and GEO navigation decision — 2026-07-29

Casebook uses a static, indexable internal hashtag system rather than a database-dependent blog taxonomy. Every materially useful topic has paired English/Chinese collection URLs under `/h2-wellness-hub/tags/` and `/h2-wellness-hub/zh/tags/`.

The first topic set is: `Hydrogen Wellness Industry`, `Industry Governance`, `Clinical Trial Registry`, `Research Transparency`, `Testing and Labeling`, and `Exercise Recovery`.

Every topic page must contain:

- a unique native-language title and meta description;
- canonical and reciprocal `hreflang` URLs;
- a concise editorial definition and evidence boundary, not just a list of links;
- `CollectionPage` and `ItemList` JSON-LD for search engines and generative search systems;
- direct internal links to the articles in that collection and cross-links to adjacent relevant topics.

Each article must display 3–5 relevant clickable hashtags above the original-source card. Link a substantive keyword inline at its first explanatory use only when it improves reader navigation; do not turn every repeated phrase into a link. A topic tag is a reader-navigation and content-classification tool, not evidence of an outcome or a keyword-stuffing surface.

### Casebook international research milestone — 2026-07-29

The first expanded international Casebook batch was added to both homepage editions. It deliberately separates industry governance and product/channel cases from healthcare research pathways.

| Region | Case / source | Why included | Boundary retained |
|---|---|---|---|
| United States | American Hydrogen Health Association launch, 8 Jul 2025, Business Wire | Industry self-organization around testing, labeling, transparency, and responsible marketing | Voluntary association; not a regulator, certification body, or clinical evidence |
| United States | Boston Children's Hospital, Hydrogen-FAST, NCT05574296 | A current hospital protocol showing how dose, timeline, and endpoint are specified in a high-risk clinical pathway | Recruiting study; registration does not establish efficacy or consumer-wellness use |
| Japan | Keio HYBRID II programme, UMIN000019820 and publication | Completed multicenter clinical-programme case with visible protocol and outcome limits | Ended early; primary endpoint was not statistically significant; never a universal efficacy claim |
| Japan | Juntendo Hospital ulcerative-colitis trial, UMIN000042017 | Illustrates a defined exploratory chronic-disease research path | Small hospital study; not a treatment claim or wellness-product support |
| France | CHU Grenoble Alpes H2COVID, NCT04633980 | Early hospital safety-engineering and medical-gas protocol case | Completed early-phase study; not general-wellness evidence |

### Regional coverage rule

Australia, Latin America, and South Africa were searched in this milestone but did not produce a sufficiently strong, molecular-hydrogen-specific institution or industry case supported by an official organization page plus an authoritative clinical or regulatory record. Keep them as research leads, not published Casebook entries. Do not fill a geographic gap with general energy-hydrogen organizations, reseller pages, or a company claim without a clear, relevant source trail.

### International Casebook and China Resource Desk expansion — 2026-07-29

This second content-build batch adds source-qualified international cases to Casebook and expands the Chinese Resource Desk into a practical verification toolkit.

#### Published international Casebook additions

| Region | Entry | Source class | Editorial use | Required boundary |
|---|---|---|---|---|
| Japan | Keio exercise inhalation study, UMIN000058083 | UMIN trial registry | Controlled-study design and status | Registry is not a result, approval, or consumer claim |
| Japan | H2FACTORY / Lourdes Hydrofix | Official company product page | Product architecture and category positioning | Company specifications do not establish clinical performance or clearance |
| Czech Republic | Palacký University, NCT05982665 | ClinicalTrials.gov | Gas purity, flow, placebo, and study-design transparency | Completed study; no posted result at review |
| Czech Republic | Palacký University, NCT05862987 | ClinicalTrials.gov | Hydrogen-water concentration, comparator, timing, and outcome fields | Completed study; not a consumer claim |
| Brazil | OH2Plus Hydrogen Full | Official company product page | Localized hardware supply, warranty, service, and test-access questions | Product information is company-reported |
| South Africa | Designer Water hydrogen-water page | Official company product page | Packaged-water process, retention testing, and traceability questions | Manufacturing and quality statements are supplier-reported |

#### China Resource Desk additions

The Chinese page now links to the NMPA drug clinical-trial registry, ChiCTR, SAMR public-data search, the national standards-information and standards-text platforms, CNAS accredited-organization search, and CNIPA patent search. Each item is written as a verification tool with its own legal and evidence boundary.

The operating rule is: no single registration, record, licence, standard, laboratory accreditation, certification, patent, or company profile establishes product safety, efficacy, or healthcare status. For a claim that requires serious review, trace the chain from study record and primary result to the exact product identity, jurisdiction, standard/test scope, and stated intended use.

#### Deferred candidates and review status

- Australia: HUVE and Opal Water were identified from official product pages but returned automated-access rate limits during this review. Keep as manual-verification candidates before publication.
- South Africa: `hydrogenhealth.co.za` was unreachable during link verification and was excluded.
- Latin America and South Africa: no suitable molecular-hydrogen-specific hospital, university, regulator, or authoritative trial-registry case was located in this batch. Published entries are therefore visibly labelled company-reported market/product cases.
