# Emuqi SEO / GEO 诊断与分阶段方案

**审计日期：** 2026-07-31  
**审计对象：** `https://emuqi.com/` 及仓库中的静态 HTML 页面  
**范围：** Google 抓取与收录、SEO 元数据、内容措辞、结构化数据、内部链接、GEO 可引用性、社交分发与 Google Ads 顺序  
**本报告性质：** 诊断与行动方案，不是本轮代码修改清单

## 结论先行

当前最可能阻碍收录的主因不是“缺少关键词”，而是内容信任和页面质量信号不稳定：博客中存在大量“临床验证”“治疗 100+ 疾病”“proved/proven”“therapeutic threshold”等健康或疗效表达，很多页面没有在正文中提供可核验的一手来源、测试条件、作者/审阅者和证据边界。

技术基础并非全线失效：仓库扫描到 81 个 HTML 页面，title 和 meta description 基本全覆盖，`robots.txt` 允许抓取并声明了 sitemap，sitemap XML 有效，canonical 缺失只发现 1 个页面。但仍存在收录治理问题：sitemap 与实际 HTML 路径不完全一致，旧兼容路径仍在 sitemap/页面资产中，部分页面没有结构化数据或 Open Graph 元数据，博客与 Hub 的内容级内链不足。

Google 官方资料明确：sitemap 主要帮助发现和理解 URL，不保证收录；AI Overviews/AI Mode 没有独立的“GEO 技巧”，页面必须先被 Google 索引并符合普通 Search 的技术与内容要求。也就是说，投流和社媒可以帮助带来访问、品牌搜索和外部发现机会，但不能替代 Search Console、原创内容、可信来源和持续抓取。

## 证据与限制

- 本地静态扫描：81 个 HTML 文件、77 个 sitemap URL、18 个 `blog/` 页面、43 个 Hub HTML 页面。
- 本地元数据扫描：title 缺失 0；description 缺失 0；canonical 缺失 1；H1 缺失 0；多 H1 0；OG title 缺失 5；OG description 缺失 5；未放 JSON-LD 的页面 25；重复 title 1 组，主要是兼容入口 `H2 Wellness Hub | Emuqi`。
- 线上抓取：`blog-list-hydrogen-health.html` 返回 HTTP 200，但抓取缓存曾显示旧页面；之后本地修复已提交为 `2729ae6`。线上抓取服务存在超时/缓存差异，不能把一次抓取结果当成稳定部署证明。
- 公开搜索结果：对 `site:emuqi.com`、`site:emuqi.com/blog`、`site:emuqi.com/h2-wellness-hub` 的结果非常弱或为空，但搜索引擎池不完整，不能代替 Google Search Console。
- 未取得 Search Console 属性权限，因此无法确认每个 URL 属于 `Indexed`、`Crawled - currently not indexed`、`Discovered - currently not indexed`、重复 canonical、软 404 或其他排除原因。

## P0：先处理内容可信度与健康宣称

这是最紧急的一层。当前博客和博客列表页把公司产品材料、研究假设、实验指标和临床/治疗结论混在同一叙述层级，容易造成：

1. Google 的 people-first / reliable content 评估无法判断哪些是事实、公司自述、研究结果还是编辑观点。
2. 健康相关主题缺少清楚的来源、作者、审阅和限制，E-E-A-T 信号不足。
3. 生成式搜索系统无法安全引用，因为一句话可能同时包含未证实的功效、精确数字和医疗结论。
4. 后续 Google Ads 审核和落地页合规风险上升，尤其是疾病治疗、临床验证和医疗器械暗示。

### 代表性问题页面

| 严重度 | 页面 | 当前问题类型 |
|---|---|---|
| P0 | `blog/hydrogen-anti-tumor.html` | “anti-tumor therapy”“100+ diseases”“improves treatment outcomes”“ideal adjunct therapy”等治疗/疾病表述，缺少逐条原始研究和结果边界 |
| P0 | `blog/hydrogen-medicine-report.html` | “Diseases Treated”“100+ conditions”“approved hydrogen inhalation therapy”等高风险医疗和监管表述 |
| P0 | `blog/muqi-hydrogen-eye-patch.html` | `92.3%`、`18.7%`、`23.4%`、`clinically proven`，未在页面中给出试验对象、样本、对照、方法、来源和适用产品批次 |
| P0 | `blog/hydrogen-face-mask.html` / `blog/hydrogen-soap.html` | 皮肤修复、抗衰、抗炎、术后恢复等功效性表达，缺少产品特定测试与合规边界 |
| P0 | `blog/solid-hydrogen-dressings.html` | 抗炎、抗菌、减轻痛经、慢性疾病等外用/健康功效表述，证据层级没有分开 |
| P1 | `blog-list-hydrogen-health.html` / `blog/index.html` | 列表摘要重复放大“clinical data”“proven”“therapeutic threshold”等高风险词，搜索摘要可能直接展示这些句子 |

### 建议的内容改写规则

- 公司自述：使用 `Company-reported specification` / `企业公开资料`，给出原始产品页，不写成独立事实。
- 研究登记：写成“研究问题/方案/状态”，不写成结果或疗效。
- 研究结果：必须给论文/注册记录/出版物、样本、对照、终点、统计和限制。
- 产品数字：同时写测试对象、方法、条件、时间点、批次/型号和检测方；缺一项就降级为“公司声明，待独立核验”。
- 医疗语境：将“treat/cure/proven/clinically validated/approved”列入发布前审查词表，除非页面有精确、当前、可核验的监管或临床来源支持完全相同的命题。
- 每篇文章加入可见的 `Published`、`Updated`、作者/编辑责任人、来源卡、证据边界和免责声明；免责声明不能替代正文事实核验。

## P1：技术与索引治理问题

### 1. sitemap 不是收录保证

Google 官方说明 sitemap 帮助搜索引擎更高效抓取，并可提供更新时间和语言替代版本；如果页面已经被良好内链，Google 通常仍可发现大部分页面。Google 也说明 canonical 信号强度大致为：重定向较强、HTML `rel=canonical` 较强、sitemap 收录较弱。当前网站已经有 sitemap，但它只能解决“告诉 Google 有哪些页面”，不能解决页面质量、重复内容或 canonical 选择。

来源：

- [Google: What Is a Sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)
- [Google: Specify a Canonical URL](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)

### 2. sitemap 与 HTML 文件清单存在不一致

本地对比发现：

- 14 个实际 HTML 路径没有出现在 sitemap，包括 `blog/` 目录首页、旧 Hub 兼容页、中文关键词页和模板文件。
- sitemap 使用 URL 编码后的中文路径，而文件系统扫描使用原始 Unicode 路径；这本身不一定是错误，但必须用线上 HTTP 200 和 canonical 逐个确认。
- 旧 `/h2-health-hub/` 兼容路径仍可作为桥接页存在，但不应作为主内容候选进入 sitemap；主 sitemap 应只保留当前 canonical 内容页。
- `blog/index.html` 和 `templates/blog-article-template.html` 是否应该进入搜索需要明确分类。模板页通常应从 sitemap 排除，博客目录页则应决定使用 `/blog/` 还是 `blog-list-hydrogen-health.html` 作为唯一主入口。

### 3. 元数据覆盖率不错，但质量和一致性不足

- `blog/index.html` 缺 canonical，是明确的技术修复项。
- 5 个页面缺 OG title/description；这不直接决定 Google 收录，但会削弱社交分享和页面实体表达。
- 25 个页面没有 JSON-LD；不是所有页面都必须有 schema，但 Blog/Article、Organization、Breadcrumb、CollectionPage 应按页面类型统一，而不是部分页面使用、部分页面缺失。
- 兼容入口出现重复 title；如果保留桥接页，应明确 canonical 到 Wellness Hub，并避免把桥接页作为主 sitemap 内容。
- Hub 页面整体的 canonical/hreflang/CollectionPage 结构优于旧博客，但博客系统尚未采用同等标准。

### 4. 结构化数据必须与可见内容一致

Google 官方强调结构化数据是帮助理解页面的显式线索，必须描述页面上可见的内容，不应为了富结果添加空数据、隐藏数据或不准确字段；“少量完整准确字段”优于大量不完整字段。

来源：[Google: Intro to Structured Data Markup](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)

当前重点不是给所有博客机械添加 FAQ schema，而是：

- Blog Article：`headline`、`description`、`image`、`datePublished`、`dateModified`、`author`、`publisher`、`mainEntityOfPage`。
- Hub Casebook：保留 Article，但显式写 source type、editorial owner、about topic，且不把公司声明标成医学事实。
- 分类/主题页：使用 CollectionPage/ItemList，ItemList 只列真实存在、可访问、确实属于该主题的文章。
- 暂不为没有正文证据的疗效 FAQ 添加 FAQ schema。

## P1：GEO 可引用性与内容架构

Google 对 AI Overviews/AI Mode 的官方要求并不是一套独立 GEO 标记。页面必须先被索引并具备可显示 snippet 的资格；官方建议仍是允许抓取、用内部链接让重要页面可发现、把关键内容放在文本中、保持 structured data 与可见内容一致、提供良好页面体验。

来源：[Google: AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features)

对 Emuqi 来说，GEO 的核心动作是让页面成为“可安全引用的证据单元”：

1. 开头先给一句准确结论，随后列出“来源支持什么/不支持什么”。
2. 每个数字有来源、日期、测试条件和对象。
3. 明确页面是公司资料、行业观察、注册记录解读还是独立研究摘要。
4. 有作者/编辑责任人、更新时间和稳定的关于页。
5. 文章之间按主题互链：一篇文章链接 1 个父主题、2-3 个相邻主题和原始来源。
6. Hub Casebook 作为“来源导航与边界解释层”，博客作为“具体文章层”，不要两套页面只做模板级互链。

当前主要 GEO 缺口：博客文章缺少统一来源卡和证据边界，很多 FAQ 把营销结论写成确定答案，博客列表摘要会放大高风险断言，且 Blog 与 Hub 的内容级关系不足。

## P2：关键词与页面架构

### 目前不宜做的动作

- 不要继续批量创建只换关键词、正文很薄的页面。
- 不要把同一篇内容同时包装成 Hydrogen Health、Hydrogen Medicine、Hydrogen Wellness、Hydrogen Biology 而不说明语境差异。
- 不要把关键词密度、meta keywords 或重复 H1 当作收录主策略。
- 不要用大量 AI 改写文章制造数量；Google 官方 people-first 指导要求原创信息、完整描述、实质分析、清晰来源和可信作者背景。

来源：[Google: Creating Helpful, Reliable, People-First Content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

### 建议的主题分层

- **商业/产业层：** Hydrogen Wellness Industry、channels、products、testing、labeling、OEM/ODM、supply chain。
- **研究导航层：** Hydrogen Medicine、Molecular Hydrogen Biology、Clinical Trial Registry；只讨论研究方向、方案、状态和证据边界。
- **产品形态层：** Hydrogen Water Cup、Hydrogen Dressing、Hydrogen Eye Patch、Hydrogen Facial Mask、Hydrogen Soap；每种产品需要独立的规格与合规语境。
- **案例层：** 只选择有来源、可解释产业教训、可明确披露来源状态的页面。

H2 Wellness Hub 已经具备这套分层的雏形，应把博客逐步迁移到同一语义系统，而不是再增加一套平行标签。

## Google 收录诊断与操作顺序

### 第一步：建立 Search Console 事实表

在没有 Search Console 数据前，所有“没有收录”的判断都只能叫“公开搜索未发现”或“待验证”。应建立 URL 表，至少包含：

`URL | page type | canonical | sitemap | HTTP | robots | lastmod | indexed status | exclusion reason | clicks | impressions | query cluster | next action`

优先检查：

1. 首页、`blog-list-hydrogen-health.html`、`blog/index.html`。
2. 3 篇高商业价值但当前高风险的 Blog：眼贴、氢敷料、氢水杯。
3. 3 篇研究类文章：氢医学报告、抗肿瘤文章、临床/研究主题。
4. H2 Wellness Hub 英文/中文首页、Topics、Casebook 文章和 5 个已挂案例的主题页。

Search Console 中要区分：`Indexed`、`Crawled - currently not indexed`、`Discovered - currently not indexed`、重复页/Google 选择其他 canonical、软 404、服务器错误、手动措施/安全问题。

### 第二步：做技术清理

1. 为 `blog/index.html` 补 self-canonical。
2. 决定博客主入口，只保留一个 sitemap 和导航主 URL。
3. 从 sitemap 移除模板页和旧兼容桥接页，除非有明确的搜索入口目的。
4. 校验所有 sitemap URL 线上返回 200、canonical 自洽、语言页 reciprocal hreflang 自洽。
5. 给 Blog Article 补一致的 OG 和 Article JSON-LD；用 Rich Results Test 验证，不盲目添加 FAQ schema。
6. 修复 Blog 与 Hub 的内容级内链，而不只是统一页头入口。

### 第三步：内容可信度修复

先修 10-15 篇最容易伤害整体信任的文章，再扩展数量。每篇通过一个发布门槛：

- 事实断言有来源。
- 性能数字有方法和条件。
- 医疗/疗效断言有适配的临床/监管来源，或者改写为研究假设/企业声明。
- 有作者、日期、来源卡、限制说明。
- 标题和 meta 不夸大，不把结果未明的研究写成产品效果。
- 页面有至少 2-3 条 Hub/相邻文章内部链接。

### 第四步：请求重新抓取

完成内容和技术修复后，再提交 sitemap，并对优先 URL 使用一次 Request indexing。不要高频重复提交同一个 URL；请求抓取不是质量修复，也不保证收录。

## 社交媒体与 Google Ads

### Social media

社媒应该用于三件事：带来真实读者、建立品牌与主题实体、为原创文章带来可追踪的访问和讨论。建议每篇高质量文章形成一个内容包：

- 1 篇站内主文；
- 1 条 LinkedIn B2B 摘要，带来源和限制；
- 1 个短图/流程图，解释一个事实而不是宣传全部功效；
- 1 个 X/社媒短帖，引用一个可核验数字并链接原文；
- 1 个后续问题帖，收集行业反馈。

社媒链接本身不是 Google 收录保证，且不要用自动化刷量、重复贴文或大量低质量外链替代真实分发。先分发“证据透明”的 Hub 案例和行业观察，再分发产品页。

### Google Ads

不建议现在直接对高风险医疗宣称页面投流。原因：

- 付费点击不会自动让自然结果收录。
- 高风险疗效/治疗词会增加广告审核、落地页信任和合规风险。
- 如果自然页面的证据和转化路径尚未稳定，投流只会放大跳出和负反馈。

推荐先做小规模、低风险 B2B 意图测试：

- functional ceramic water media manufacturer
- solid-state hydrogen materials OEM/ODM
- hydrogen water product development
- hydrogen dressing material supplier

落地页应使用经过 P0 修复的产品/材料页面，目标是询盘或资料下载，不使用“cure”“clinically proven”“treats disease”等词。先验证搜索词、询盘质量、页面停留和合规，再决定扩大预算。

## 30/60/90 天落地路线

### 0-7 天：止损与事实确认

- 建立 Search Console 属性并导出真实索引状态。
- 暂停高风险文章的投流和强功效社媒转发。
- 修正 blog canonical、sitemap 资产清单、OG/schema 基线。
- 建立 P0 断言台账，逐条标记 source / company claim / research status / unsupported。

### 8-30 天：重写核心内容

- 优先重写 10-15 篇博客，而不是全站机械替换关键词。
- 每篇加入来源卡、作者/更新日期、证据边界和 Hub 互链。
- 把研究文章重构为“研究导航/证据解读”，把产品文章重构为“产品架构/采购尽调/规格披露”。
- 对事实、性能和监管表述做人工审核，并用 Rich Results Test 检查 schema。

### 31-60 天：建立内容与分发闭环

- 每月发布 2-4 篇真正有来源的文章和 1-2 个 Hub Casebook 条目。
- 每篇做 LinkedIn、X、邮件/行业社群分发，记录 URL、发布时间、来源、点击和询盘。
- 用 Search Console 查询数据反推标题、段落和内链，不根据猜测堆关键词。

### 61-90 天：低风险投流与复盘

- 只对 P0 已清理、来源明确、商业意图清晰的 B2B 页面做小预算测试。
- 分离品牌词、材料/OEM 词、产品形态词和医疗研究词，避免混在同一广告组。
- 每周检查 Search Console 与 Ads：索引、展现、点击、搜索词、跳出、询盘和合规拒登。

## 最终优先级

1. **P0：** 清理未证实医疗/疗效/性能/监管表述，建立来源和证据边界。
2. **P1：** Search Console 事实表、canonical/sitemap/OG/schema/内链基线。
3. **P1：** 统一 Blog 与 H2 Wellness Hub 的内容层级和引用结构。
4. **P2：** 只保留有真实意图和独立价值的关键词页面。
5. **P2：** 先做透明、可引用的社媒分发，再做低风险 B2B Google Ads。

## 开放问题

- Google Search Console 的真实属性是否已验证，当前具体排除原因是什么？
- Hostinger/GitHub Pages 的最终生产源是否完全一致，是否存在缓存或双源部署？
- 现有精确性能数字对应哪些样品、批次、测试机构、测试条件和原始报告？
- 哪些产品确实拥有可公开引用的临床、监管或第三方实验室证据？
- Emuqi 希望优先获得哪类询盘：材料 OEM、产品开发、品牌合作、经销商还是研究合作？

## 关键来源

1. Google Search Central — [What Is a Sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)
2. Google Search Central — [Specify a Canonical URL](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
3. Google Search Central — [Creating Helpful, Reliable, People-First Content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
4. Google Search Central — [Intro to Structured Data Markup](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
5. Google Search Central — [AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features)
