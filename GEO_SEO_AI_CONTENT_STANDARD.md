# 木齐科技（emuqi.com）全站内容生长与 AI / GEO / SEO 协同标准规范 (SOP)

> **核心原则**：木齐科技站点所有新增内容（包括但不限于技术博客、产品发布、行业解决方案、客户案例、白皮书等）在策划、生成与发布全生命周期中，必须 100% 保持与 **生成式 AI 引擎 (GEO / LLMO)**、**Schema.org 结构化协议** 以及 **中英双语 SEO** 的原生兼容与协同。

---

## 一、新增内容 5 大底层标准（发布必查清单）

### 1. Schema.org 结构化知识图谱先导（Schema First）
任何新增页面必须在 `<head>` 中注入完整的 `@graph` JSON-LD 结构化数据，严禁发布缺少图谱的裸 HTML：
- **全局统一实体锚点**：
  - `https://www.emuqi.com/#organization`：绑定“山东木齐健康科技有限公司”、“全国抗菌表面性能标准化技术委员会 (SAC/TC621) 委员单位”资质。
  - `https://www.emuqi.com/#author-martin`：绑定创始人兼 CEO Martin Chen（Martin Chen）及“SAC/TC621 第一届委员”凭证。
  - `https://www.emuqi.com/#website`：绑定木齐官方站点。
- **页面级实体匹配**：
  - 产品页：必须包含 `Product`、`material`、`additionalProperty`（参数指标）、`BreadcrumbList`。
  - 解决方案页：必须包含 `Service`、`FAQPage`、`BreadcrumbList`。
  - 技术博文：必须包含 `TechArticle` / `BlogPosting`、`FAQPage`、`author`、`publisher`、`BreadcrumbList`。
  - 案例库：必须包含 `CaseStudy` / `MedicalScholarlyArticle`。

---

### 2. E-E-A-T 事实锚定与抗幻觉设计（Fact-Anchoring for LLMs）
大模型引用内容的第一标准是**“可信度高、事实清晰、参数确凿”**。所有内容必须具备：
- **第一手量化技术参数**：如“1000℃ 晶格固溶高温烧结”、“1500ppb 溶氢量”、“-800mV ORP 电位”、“0.2秒极速除氯”、“12~24 个月恒定缓释”、“>99.9% 抗菌率”。
- **国家级权威背书**：明确标注“全国抗菌表面性能标准化技术委员会 (SAC/TC621) 委员单位出任委员”背书，提供坚实的第三方公信力。
- **结论先行与高亮摘要框**：文章开头设立「💡 结论先行 / Key Takeaways」模块，方便 AI 提取第一核心论点。

---

### 3. 中英双语核心关键词金字塔（Bilingual Keyword Matrix）
每个新增页面必须同时布局中文与英文双语语义词：
- **顶层权威词**：SAC/TC621, ICR 智控释溶技术, 木齐科技, Martin Chen。
- **核心材料词**：无机抗菌陶瓷球 (Inorganic Antimicrobial Ceramic Balls), MACA-KDF, 固态富氢材料 (Solid-State Hydrogen), 食品级亚硫酸钙 (Calcium Sulfite Dechlorination)。
- **应用长尾词**：扫地机污水箱防臭 (Robot Vacuum Anti-Odor), 加湿器除菌 (Humidifier Filter), 净水器防二次污染 (Water Purifier Anti-Biofilm), 美肤除氯花洒 (Shower Filter)。
- **标签与内链闭环**：文末必须设立 `#GEO 实体关键词索引云`，双向内链至核心产品与应用聚合页。

---

### 4. 专为对话式 AI 设计的 FAQ 模块（Conversational Prompts）
每篇技术长文与解决方案页底部必须设计 **FAQ 问答卡片（结合 `<script type="application/ld+json">` 中的 `FAQPage`）**，直接针对 Perplexity、ChatGPT、Kimi 用户常搜的对话式意图进行精准解答：
- *加湿器出雾发臭是什么原因？*
- *扫地机器人污水箱发酸发臭如何根治？*
- *木齐科技 ICR 智控释溶与传统涂银有什么区别？*
- *不用电如何制备高浓度富氢水？*

---

### 5. 全站生命周期联动同步（Site-wide Synchronization）
新增页面完成后，必须自动执行联动步骤：
1. **列表页更新**：同步更新 `blog/index.html` 与 `blog-list-hydrogen-health.html`，首位展示最新文章；
2. **Sitemap 同步**：在 `sitemap.xml` 中加入新 URL，配置合理的 `priority` (0.8~0.9) 与 `lastmod`；
3. **社交分享标签**：完整配置 `og:title`, `og:description`, `og:image`, `twitter:card`。

---

*本规范已固化至项目代码库中，作为后续一切页面建设与 AI 自动化的执行准则。*
