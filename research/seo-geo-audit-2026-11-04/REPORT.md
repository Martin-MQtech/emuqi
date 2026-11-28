# Emuqi SEO / GEO 全站体检与修复报告（/zh/ 双轨架构上线后）

**审计日期：** 2026-11-04
**审计对象：** 仓库 `main`（基线 `18c7902`）与线上 `https://www.emuqi.com/`
**范围：** 中英文物理分轨一致性、canonical / hreflang / sitemap 三方对齐、元数据长度、结构化数据语言码、断链与存根页跳转
**本报告性质：** 本轮代码修改清单 + 剩余项定性，不是设计方案（方案见 `PROJECT_EXECUTION_MANUAL.md`）

## 结论先行

站点在 2026-10 完成中文内容向 `/zh/` 分支迁移后，双语架构基本成型，但迁移收尾留下三类技术债：一是中文正文仍有一个文件躺在英文树里（`blog/hydrogen-patch-opportunity.html`，582 处中文 + `lang="zh-CN"` + 自封 `hreflang="en"`）；二是 34 个 Hub 标签/主题页仍写旧语言码 `zh-Hans`（`hreflang` 属性与 `<html lang>` / `<a lang>` 两种载体各约一半）；三是新迁移页面的 canonical / hreflang / og 元数据存在缺失与自指错配。本轮共修复 **56 个文件**，审计问题从 **69 项降到 4 项**，且 4 项全部经核实属有意设计或规范内写法，不再改动。

线上本身健康：关键路径全部 200，`.htaccess` 301 生效，`emuqi.com → www.emuqi.com` 收敛正确，TLS 有效，404 页正常。此前多次"站点打不开"的判定不成立，故障在本地 TUN 虚假 IP + 代理内核（VLESS+REALITY 在协议层超时，同机 Hysteria2 192–432ms 正常），与站点无关。

## 证据与方法

- 静态扫描：192 个 HTML（剔除 `templates/`、`scripts/`、`node_modules/`、`distribution_packages/` 等非发布目录）、162 条 sitemap URL、13 条 `.htaccess` 301 规则 + 1 条前缀规则。
- 判定前先消误报：原始命中 239 项，其中 164 项属 robots 禁抓目录、存根页与资源文件，真实问题 75 项，修复后剩 4 项。
- 基线以 `git fetch` 后远端 `main` 为准（本地工作副本曾落后 2 个月，期间并行 Agent 推入 12 个提交，含日文 v1.1 全本与四语 PDF 压缩）。补丁在 `18c7902` 工作树逐文件复核后落地，未回退任何他人改动。
- 结构校验：56 个变更文件无 `/zh/zh/` 双前缀、无 `emuqi.com/https://` 双协议、无空 title、html/body/script 标签配平一致。
- **本目录附带 `audit.py`**，在仓库根目录执行 `python3 research/seo-geo-audit-2026-11-04/audit.py` 即可复跑全部规则（A 断链 / B sitemap 双向 / C-D canonical 与 hreflang / E-G 元数据 / H JSON-LD / I-J 语言 / K-L 列表与迁移 / M-N 资源与标题 / O 可见语言切换器）。2026-11-04 当时输出为 4 项且均为有意项；2026-11-27 的 V3 复检结果见文末追加记录。

## 本轮改了什么

| 类别 | 数量 | 具体内容 |
|---|---|---|
| 双语分轨收尾 | 3 | 中文长文迁入 `zh/blog/hydrogen-patch-opportunity.html`；原路径改为跳转存根（`meta refresh` + `noindex,follow` + canonical + `location.replace`）；`.htaccess` 增补对应 301 |
| 语言码统一 | 34 | `zh-Hans` → `zh-CN` 共 36 处：Hub 标签/主题页的 `hreflang` 声明（18 处）与 `<html lang>` / 语言切换链接 `<a lang>`（18 处） |
| 内链与引用 | 4 | `blog/index.html` 英文卡片改指 `/zh/blog/…` 并标注 `Industry Insight · Chinese edition`；`zh/blog/index.html` 卡片由 `/blog/` 改指 `/zh/blog/`；WordPress 分发稿 4 处双协议图片 URL 修正 |
| hreflang 自指纠错 | 16 | 删除迁移过程中遗留的 `hreflang="en"` / `x-default` 自指，补齐 `hreflang="zh-CN"` 双向配对 |
| 元数据合规 | 12 | 8 个页面 title 收敛至 50–65 字符、description 收敛至 130–160 字符（含新增的 `papers-to-fields` 英文稿）；中文旗舰稿 title 去掉重复副标题 |
| OG / Twitter 补齐 | 2 | `h2report/reader/index.html` 补 canonical（指向 `/h2report/`）+ og 五件套 + `twitter:card`，并把 charset/viewport/title 归位到 head 顶部；`zh/index.html` 补 `twitter:card` |
| sitemap | 1 | 新中文正文 URL 入图，存根 URL 不入图 |
| 英文页语言提示 | 1 | 版权页中文切换项 tooltip 改为英文表述 |

## 线上复验追加发现（第二轮，同批提交）

第一轮修完立即做线上取证（`curl` 逐条核状态与正文），发现三处静态扫描规则本身覆盖不到的问题，均已修复；审计脚本同时新增 M/N 两条规则，用修复前的树做过反向验证，两条规则都能命中：

1. **`zh/blog/hydrogen-patch-opportunity.html` 头图 404** —— 文件从 `blog/` 迁到 `zh/blog/` 后相对深度 +1，`href`/`src` 已批量改成 `../../`，但内联 `<style>` 里的 `url('../assets/...')` 不在替换模式里，hero 背景图实际指向 `/zh/assets/...`。改为 `../../assets/...`。**教训：迁移自检必须包含 CSS `url()`，不能只看 `href`/`src`。**
2. **中文树页面却是英文标题与英文 H1** —— 该文实为“中文导语 + 英文正文”的双语稿，`<title>`、description、og 与 hero H1 全英文，与 `/zh/` 位置和 `zh/blog/index.html` 的中文卡片（「膏药贴牌大厂新风口：为什么必须布局固态氢敷贴？」）自相矛盾，百度/搜狗拿到的是英文快照。已把 title/description/og/H1/日期栏统一为中文（正文双语结构不动）。
3. **`sitemap.xml` 与 `robots.txt` 被缓存 30 天** —— `.htaccess` 的 `ExpiresDefault "access plus 1 month"` 兜到了这两类文件，实测响应头 `cache-control: public, max-age=2592000`、`cf-cache-status: HIT`、`age: 32418`。新页面发布后爬虫最长可能 30 天看不到更新 sitemap。已加 `FilesMatch "^(sitemap.*\.xml|robots\.txt)$"` → `max-age=300, must-revalidate` 并 `unset Expires`，同时给 `application/xml` 单独设 5 分钟 Expires。

**仍需人工处理的一项（不在仓库内）：** 站点前面叠了两层缓存——Cloudflare（`cf-cache-status`）与 Hostinger 自己的 HCDN（`x-hcdn-cache-status`）。源站头已经改对，但 **Cloudflare 边缘里那个按 30 天 TTL 存进去的旧副本还在服务**：修复后实测 `GET /robots.txt` 仍返回 `cache-control: public, max-age=2592000`、`cf-cache-status: HIT`、`age: 32886`，而同一条 URL 加查询串绕过缓存（`/robots.txt?v=…`）就立刻返回 `max-age=300, must-revalidate`、`cf-cache-status: MISS`；`/sitemap.xml` 同理（`cf-cache-status: DYNAMIC` 但 `last-modified` 仍是 2026-10-18）。

处置：进 Cloudflare 控制台 → Caching → Configuration → **Custom Purge**，明确列出 `https://www.emuqi.com/robots.txt`、`https://www.emuqi.com/sitemap.xml` 两个 URL 清除（比 Purge Everything 稳妥）；若 Hostinger hPanel 里启用了 HCDN/CDN 缓存，同样在其缓存设置里清一次。清完后用 `curl -I https://www.emuqi.com/robots.txt` 复验：`cache-control` 应为 `max-age=300`。若希望一劳永逸，可在 Cloudflare 建 Cache Rule：对 `/robots.txt`、`/sitemap*.xml` 设 Standard Cache 或直接设 `Cache-Control: no-cache` 的边缘覆盖。

## 剩余 4 项：均为有意，不改

1. `h2report/reader/index.html` 不在 sitemap —— 该页 canonical 已指向 `/h2report/`，交互式阅读器不单独参与收录，属预期。
2. 版权页 `blog/muqi-solid-hydrogen-lab-icr-copyright-certificates-en.html` 含中文 —— 命中的是 `国作登字`/`鲁作登字` 著作权登记号和 JSON-LD `alternateName` 里的 `木齐科技`，前者是证书原文照录、后者是实体别名信号，均非页面功能栏文案。
3. `h2-wellness-hub/enterprise-archive.html` 含中文 —— 企业目录逐条列明厂商注册名称原文（潓美医疗、纳诺巴伯、科力恩、日立、株式会社等），属数据而非导航文案。
4. `h2-wellness-hub/methodology.html` 含中文 —— 中英双语免责声明与 `🌐 中文` / `中文版 (Chinese)` 语言切换项。语言切换项按国际惯例以目标语言本身书写，功能栏（分享栏、广告位等）已按手册 §12.1 全英文。

## 部署与验证

```bash
cd "…/20260721 MUQI 网站建设/emuqi"
git fetch origin main && git rev-list --count HEAD..origin/main   # 必须为 0 才提交
git add <本次 56 个文件> && git commit && git push origin main
```

推送后 Hostinger 自动同步（1–2 分钟），GitHub Pages 由 `deploy.yml` 构建（数分钟，`gh api repos/Martin-MQtech/emuqi/pages --jq .status` 读到 `built` 为准）。落地验收：`/blog/hydrogen-patch-opportunity.html` 应 301 到 `/zh/blog/…`（`curl -I` 看 `location`）；全站 `grep -rl 'zh-Hans' --include='*.html' .` 应为 0；`sitemap.xml` 应包含新中文正文 URL 且不含存根 URL；`blog/index.html` 的对应卡片应指向 `/zh/blog/…` 并标注 Chinese edition。

**存根页在 GitHub Pages 上的注意点：** Pages 不解析 `.htaccess`，旧中文 URL 在镜像上靠存根页的 `meta refresh` + JS 跳转兜底，不是 301。因此新加中文文章迁移时，存根 HTML 与 `.htaccess` 规则必须同批提交，缺一个镜像就会露 404 或重复内容。

---

## 2026-11-27 V3 复检与修复追加记录

**基线**：`git fetch` 后 `HEAD = origin/main = f278c5d`。本轮只检查生产页面，排除 `scratch/`、`research/`、`scripts/`、`distribution_packages/`、模板与验证文件；并行 Agent 的未跟踪 `scratch/w14/` 未改动、未提交。

**审计范围**：196 个生产 HTML、191 个 sitemap URL、17 条显式 301 规则 + 1 条 Hub 前缀规则。V3 新增 canonical 当前页校验、hreflang 互指/重复/x-default 一致性、JSON-LD `inLanguage`、可见语言切换器对照、301 源内链检测和 `llms.txt` / `llms-full.txt` 文章覆盖检测，并把 5 个有意保留中文的英文页列入显式豁免：双语视频、版权证书原文、SAC 公告原文、企业注册名目录、方法论双语提示。

| 修复类别 | 数量 | 处置 |
|---|---:|---|
| 英文博客重复 hreflang | 18 页 | 保留首组 EN/ZH/x-default，删除后续重复 EN/x-default |
| 中文博客 JSON-LD 语言码 | 17 页 | 文章 `inLanguage` 由 `en` 改为 `zh-CN` |
| 可见语言切换器错链 | 21 处 | 18 个中文页 EN 胶囊改指对应英文文章；3 个英文页中文胶囊改指对应中文文章 |
| 旧 Hub / 旧文章内链 | 20 处 | 18 个 `/zh/h2-wellness-hub/` 改指 `/h2-wellness-hub/zh/`；视频页 2 个旧英文 URL 改指 `-en.html` |
| x-default | 3 处 | 视频与植物蛋白两组统一指向英文 canonical；农业英文页补 x-default |
| 隐私页虚假中文 hreflang | 1 处 | 删除指向中文首页的 `zh-CN` alternate；站点无中文隐私政策译文，不制造假配对 |
| 元数据超长 | 6 项 | 3 个 title、3 个 description 收敛，并同步 OG / JSON-LD headline / H1 |
| AI 知识库覆盖 | 15 + 64 URL | `llms.txt` 补 15 个缺失文章 URL；`llms-full.txt` 增加 65 篇完整双语文章索引 |
| 当前架构文档 | 3 处 | 手册目录树与 §12.1 更新为 33 篇中文正文、32 篇英文正文、11 个存根桩 |
| 中文博客列表 | 16 张重复英文卡 | 删除已有中文译文的英文目标重复卡，33 张中文卡按发布日期降序重排；V3 增加卡片语言树、重复与日期顺序检查 |

**复检结果**：生产静态审计 `问题总数: 0`；博客 chronological hard gate 中英文各 33 张卡片全部通过。首次推送后 GitHub Pages 构建被既有中文列表乱序阻断，已修复并重新提交。本轮未改 `.htaccess`、未改产品参数、未触碰站外账号或缓存配置；线上部署状态在提交推送后另行复核。

## 2026-11-27 V3.1 可见语言切换补齐与边缘缓存收尾

**触发原因**：V3 的 O 段原先只能发现“已有语言胶囊指错”，不能发现“整页没有语言切换”。本轮把 O 段升级为同时检查错链与缺失，并过滤 YouTube 等外部链接，避免把播放列表名称里的“中文 / English”误判为站内切换器。

| 修复类别 | 数量 | 处置 |
|---|---:|---|
| 旧英文博客缺中文入口 | 15 页 | 在导航 Contact 后补统一 EN / 中文语言胶囊，中文目标逐页对应 `/zh/blog/<slug>.html` |
| 主题地图语言链接回错首页 | 2 页 | 英文与中文 topics 页互指对应孪生页，不再只回 Hub 首页 |
| 中文 SAC 文章缺英文入口 | 1 页 | 无导航头页面补固定右上角 English 入口，指向对应 `-en.html` 正文 |
| Hub 页脚语言链接回错首页 | 6 页 | methodology、enterprise-archive、research-database 三组中英文页互指对应孪生页 |
| sitemap 时戳 | 9 条 | 上述 Hub / topics / SAC 页面 `lastmod` 更新为 `2026-11-27`；15 个英文博客此前已是该日期 |

**边缘缓存处置**：正常 URL 的旧 Cloudflare HIT 已通过 Purge Everything 清除，抽检 `/blog/hydrogen-soap.html`、`/zh/blog/hydrogen-soap.html`、`/zh/blog/` 均返回 200 / MISS 与新版内容。AI 索引规则 `Edge Cache AI Spec Files (llms.txt)` 已从“忽略源站头、固定 2 小时”改为“源站有 Cache-Control 则遵循，否则 bypass”，保存后重新打开规则确认目标选项仍为选中状态，使 `.htaccess` 的 `max-age=300, must-revalidate` 可以实际生效。

**门禁结果**：修复后生产静态审计恢复 `问题总数: 0`，中英文博客各 33 张卡片 chronological hard gate 全部通过，`git diff --check` 通过。本次 24 个生产页面与审计脚本随本轮提交推送，部署后再做正常 URL 线上复验与 Purge Everything。

## 2026-11-27 V3.2 相对路径规范化与旧 Hub 内链清零

**触发原因**：V3.1 推送后的浏览器实测发现，中文氢皂文章“探索相关主题”中的 `../h2-wellness-hub/` 会被浏览器解析为旧路径 `/zh/h2-wellness-hub/`，继而触发 301。V3.1 的静态规则只拼接相对路径、没有折叠 `..`，因此漏报；这是审计规则盲区，不是页面偶发错误。

**审计升级**：A 段先按页面所在目录解析相对路径，再用 `posixpath.normpath` 执行与浏览器一致的 POSIX 规范化，保留结尾斜杠语义后检查 301 源。升级后反向命中 9 个中文博客页面，确认规则能够发现该类问题。

| 修复类别 | 数量 | 处置 |
|---|---:|---|
| 中文文章旧 Hub 相对链接 | 9 处 | `../h2-wellness-hub/` 统一改为 `/h2-wellness-hub/zh/`，直接进入中文 Hub，不再经过旧路径 301 |
| sitemap 时戳复核 | 9 条 | 对应中文正文 `lastmod` 已全部为 `2026-11-27`，无需重复修改 |

**门禁结果**：生产静态审计 `问题总数: 0`；中英文博客各 33 张卡片 chronological hard gate 全部通过；`git diff --check` 通过。本轮生产修改为 9 个中文博客页面，另同步升级审计脚本至 V3.2。

## 2026-11-28 V4 全站深度审计与优化路线图

### 1. 审计范围与总体判断

本轮在 V3.2 链接与 SEO/GEO 门禁通过的基础上，扩大到性能、移动端、可访问性、隐私与安全、表单转化、双语商务路径、内容可信度和部署韧性。审计时仓库与远端 `main` 均为 `48527f7`；未回退并行 Agent 成果，`scratch/w14/` 保持未跟踪且未提交。

扫描覆盖生产 HTML 200 个（V3 审计脚本纳入 196 个）、图片 753 张、脚本与样式引用、`.htaccess`、GitHub Actions、公开仓库凭据风险、Cloudflare 响应头和 6 类代表页面的真实浏览器运行数据。

**总体判断**：SEO、canonical、hreflang、sitemap、历史 URL 兼容等基础层已经稳定；当前主要矛盾不再是“搜索引擎能否找到页面”，而是“页面是否足够快、移动端是否可用、第三方脚本是否尊重同意、询盘是否安全且可追踪，以及内容数字是否可信”。建议保持现有静态站架构，不引入大型前端框架，按 P0 → P3 分批治理。

**边界说明**：PageSpeed Insights API 本轮返回 HTTP 429，未取得官方 PSI / Core Web Vitals 分数。以下浏览器数据来自 274 px 视口的单次运行，仅用于定位方向性问题，不等同于官方实验室分数。本轮未修改生产代码、未轮换凭据、未改写 Git 历史、未调整 Cloudflare 规则。

### 2. 关键页面运行时基线

| 页面 | DCL | load | 主要观察 |
|---|---:|---:|---|
| 英文首页 | 1,988 ms | 2,570 ms | TTFB 616 ms；21 图，4 eager / 17 lazy；资源传输约 444 KB；无失败请求或控制台错误 |
| 中文氢皂文章 | 773 ms | 4,625 ms | GA4 `ERR_CONNECTION_CLOSED`；AdSense QUIC timeout |
| 中文 H2 Wellness Hub | 878 ms | 937 ms | 18 图全部 lazy；无失败请求 |
| 英文产品页 | 219 ms | 4,211 ms | AdSense timeout 拉长 load |
| 英文联系页 | 186 ms | 354 ms | 无失败请求，是当前性能较好的承接页 |
| 氢健康应用页 | — | 4,353 ms | 22 图，17 eager；大 PNG 与广告脚本共同拖慢 |
| 中文采购决策树 | 623 ms | 4,277 ms | HTML 传输 1,016,648 B；base64 图片与广告脚本是主要负担 |

这些数据说明：联系页证明静态轻量页面可以很快；文章、产品、应用和决策树页的 4.2–4.6 秒 load 主要来自第三方脚本和图片策略，而不是静态架构本身。

### 3. P0：立即处理的安全、隐私与发布可靠性问题

| 编号 | 问题与证据 | 影响 | 修复方案 | 验收标准 |
|---|---|---|---|---|
| P0-1 | 公开仓库 `Martin-MQtech/emuqi` 仍跟踪 `scripts/publish_devto_steamer.py` 与 `scripts/submit_chinese_engines.py`，其中分别含明文 `api_key` 与 `DEFAULT_BAIDU_TOKEN`；未读取或输出实际值 | 凭据泄露、第三方账号滥用、推送接口被阻断 | 立即吊销/轮换两个凭据；改为环境变量或 GitHub Secrets；启用 secret scanning / push protection；必要时清理 Git 历史。轮换必须先于历史清理，因为旧提交中的值不会因删文件自动失效 | 旧凭据失效；新代码无明文值；无 Secrets 时脚本明确失败；推送含疑似 Secret 被拦截 |
| P0-2 | Cloudflare 正常根 URL 仍返回 `HIT`、`age: 32299`，同 URL 加查询参数才为 `MISS`；源站 HTML 已设置 `max-age=0, must-revalidate` | 发布后可能继续向用户与搜索引擎提供旧 HTML，双语修复和内容更新延迟可见 | 调整 Cache Rule 顺序与表达式，让 HTML 始终 bypass；保留图片/指纹资源的长期缓存；发布后自动 Purge Everything；用正常 URL 而不是查询参数验证 | 首页、中文首页、博客、产品页的正常 URL 在部署后均为 `MISS`/`DYNAMIC`，`age` 不大于可接受范围；强刷不复用旧 HTML |
| P0-3 | 64 个生产 HTML、共 67 处直接加载 `adsbygoogle.js`；Cookie 逻辑只门禁 GA4，不门禁广告 | 用户同意前已向 Google 发起广告请求；隐私政策与实际行为不一致；广告网络失败会拉长 load | 删除硬编码广告脚本，统一由 Consent Manager 在 opt-in 后加载；启用 Google Consent Mode v2；Decline 后广告和 GA4 均不初始化、不发非必要请求 | 新会话未同意时网络记录中广告与 GA4 请求为 0；接受后正常加载；拒绝后刷新仍保持关闭 |
| P0-4 | 首页与联系页表单无 `action/method`，只由内联 `onsubmit` 打开 `mailto`；JS 失效时会默认 GET 到当前 URL，姓名、邮箱、电话等可能进入地址栏、历史和日志；打开邮件客户端即记 `generate_lead` | PII 泄露、线索统计虚高、邮件客户端未配置时用户流失 | 主站新增受保护的 POST 接口；前端仅做即时校验；服务端再次校验并加蜜罐/限流/Turnstile；接口接受后才记线索；无 JS 时提供明确 mailto/WhatsApp 降级，不提交到当前 URL | 禁用 JS 后 URL 不含 PII；正常提交产生服务端接收回执；只有接收成功才触发线索事件；重复提交与机器人请求被拦截 |

> P0-1、P0-2 涉及账号凭据、Git 历史和 Cloudflare 配置，属于高风险动作，必须获得明确授权后执行。P0-3、P0-4 可先准备代码变更和测试方案，再按发布窗口上线。

### 4. P1：高影响性能、移动体验、可访问性与转化问题

| 编号 | 问题与证据 | 影响 | 修复方案 | 验收标准 |
|---|---|---|---|---|
| P1-1 | 中英文采购决策树页各约 1.47–1.48 MB；各内嵌 5 张 base64 图片，base64 字符 1,407,588，解码后约 1,055,691 B；中文页线上 HTML 传输 1,016,648 B | HTML 无法被图片缓存复用；移动端解析、传输和内存成本高；每次内容更新都重复传输图片 | 图片解码后外置为 WebP/AVIF；使用 `<picture>`、`srcset/sizes`；仅首屏图 preload/fetchpriority，其余 lazy；CSS 提取共享版本化文件 | 决策树 HTML 传输降至约 200 KB 以内；图片可独立缓存；页面功能与视觉回归通过 |
| P1-2 | 应用页仍引用 `app-overview.png`（2,093,587 B）、`water-bottle-1.png`（1,265,743 B）、`water-bottle-2.png`（1,177,546 B）、`water-bottle-3.png`（2,113,954 B）；对应 WebP 已存在，合计仅 336,630 B | 单组图片从约 6.65 MB 降至约 337 KB 的空间很大；当前 22 图中 17 张 eager | 引用已有 WebP；非首屏全部 lazy；首屏只保留 1 张高优先级图；为产品/应用主图增加响应式尺寸 | 首屏图片传输显著下降；除首屏必要图外无 eager 图片；缩略图点击和主图功能不回归 |
| P1-3 | 753 张图片中 471 张非 lazy，`srcset=0`、`sizes=0`；虽然全部有 alt 和宽高属性，但缺少分辨率适配 | 手机下载桌面尺寸图片，流量和 LCP 成本偏高 | 建立图片模板规范：`width/height` 保留；首屏 `loading=eager fetchpriority=high`；其余 `loading=lazy decoding=async`；大图增加 `srcset/sizes` | 所有非首屏图片 lazy；核心 hero/product 图具备至少 2 档响应式资源；无 CLS 回归 |
| P1-4 | 文章/产品/应用/决策树页 load 4.2–4.6 秒并出现 AdSense QUIC timeout；124 个页面同时直接包含 `analytics.js` 与 `script.js`，存在重复 loader 请求 | 第三方网络故障拖慢 `load`，控制台报错，影响质量感知和转化 | 统一为一个 consent-aware loader；删除重复入口；广告/分析非关键化并隔离失败；评估是否减少广告位或改为用户触发 | 关键页面无脚本错误；第三方失败不再决定页面 load；每个第三方脚本只有一个加载入口 |
| P1-5 | `style.css` 用 `html/body overflow-x:hidden` 掩盖溢出；多处网格含 `minmax(320px, ...)`，375 px 视口加 gap/padding 后超宽；氢水袋页有 `minmax(320px,440px)` + `56px` gap | 内容被裁切、横向滚动被隐藏、移动端布局不可用 | 窄屏改单列；网格统一 `minmax(0,1fr)`；审查固定宽度、白空间和长英文串；修复后移除全局 overflow 遮蔽 | 360 / 390 / 768 px 视口横向溢出为 0；首页、氢水袋页、产品页、决策树页无裁切 |
| P1-6 | 缩略图使用带 `onclick` 的 `img`，无 `tabindex/role`/键盘处理；报告封面使用 `div onclick`；至少 31 个交互目标键盘不可达；语言按钮有 `outline:none`，全局 `:focus-visible` 不完整；灯箱缺少完整 dialog 与焦点管理 | 键盘和辅助技术用户无法完成关键操作，存在 WCAG 2.2 AA 风险 | 交互元素改为原生 `button`；灯箱使用 `<dialog>` 或 `role=dialog aria-modal=true`，支持 Esc、焦点陷阱和关闭后焦点返回；统一 `:focus-visible`；下拉按钮补 `aria-expanded` | 所有交互可用 Tab/Enter/Space 完成；焦点始终可见；灯箱打开、关闭和焦点返回测试通过 |
| P1-7 | 中文首页首屏主 CTA 是白皮书和博客；合作区只有电话/邮箱/地址与说明，没有询价或样品按钮；页头页脚虽有入口，但高意向用户主路径不连续；部分核心商务页仍落到英文页 | 中文高意向流量需要多次寻找入口，报价/样品转化率受损 | 首屏增加“获取报价 / 申请样品”主 CTA；合作区加入同页 RFQ 或明确按钮；补齐中文 Contact / Sample Request / Products 承接；电话、邮箱、WhatsApp 均可点击并预填产品上下文 | 从中文首页到询盘不超过 2 次点击；主要商务页面有中文版本；移动端 CTA 固定可达且不遮挡 Cookie 横幅 |
| P1-8 | 203 处 CSS/JS 引用无版本参数，却与图片一样享受一年 `immutable`；GitHub Actions 曾出现 artifact 元数据竞争和重跑后同名 artifact 重复 | 用户长期使用旧 CSS/JS；部署成功不代表浏览器已更新；回滚也缺少清晰版本 | 为 CSS/JS 增加内容哈希或发布版本；同步更新全站引用；HTML 保持短缓存/bypass；artifact 名称包含 run id，发布步骤清理旧 artifact | CSS/JS URL 随内容变化；旧资源仍可回滚；同一 run 只有一个部署 artifact；部署后静态与线上 smoke test 通过 |
| P1-9 | 中文首页仍写“全 24 篇”（实际中文博客 33 篇）和“17 个真实商业案例”（Hub 已为 18 个唯一案例）；“35% 全球份额”在中文首页作为事实展示，而英文 benchmark 标为 company-reported / verify | 内容数字漂移损害信任与 GEO 一致性；无来源的市场份额声明存在合规风险 | 从结构化内容清单生成文章/案例数量；建立“声明—对象—指标类型—方法—来源—日期—负责人”证据台账；未核实声明降级为“公司自述”或删除；中文首页与英文 benchmark 口径一致 | 文章/案例数量由清单自动生成；35% 份额有可审计来源或改为公司自述；关键数字在中英文页一致 |

### 5. P2/P3：工程化、可发现性与长期治理

| 编号 | 问题与证据 | 影响 | 修复方案 | 验收标准 |
|---|---|---|---|---|
| P2-1 | 线上 CSP 只有 `upgrade-insecure-requests`；`.htaccess` 未配置完整 CSP | XSS、数据外发和第三方注入缺少浏览器层防线 | 先上线 `Content-Security-Policy-Report-Only`，收集破坏项；广告/分析域名白名单；内联脚本逐步 nonce/hash 化；稳定后强制 | Report-Only 无意外阻断；强制模式关键页面无功能回归；违规报告可监控 |
| P2-2 | 272 个 `target=_blank` 链接缺 `noopener`；174 页加载 Google Fonts CSS，存在多种 URL 变体 | reverse-tabnabbing 风险与首屏阻塞；字体请求变多 | 外链统一 `target=_blank rel="noopener noreferrer"`；自托管并子集化实际使用字体；统一字体 URL 与 `font-display` | 外链属性扫描为 0 缺失；字体自托管；关键页面无字体阻塞 |
| P2-3 | 20/200 页无 `<main>`；19/200 页非单一 H1；67 个无角色的 `div aria-label` | 语义结构和屏幕阅读器导航不一致 | 模板化补齐 main/H1；无效 ARIA 删除或改为合适语义；加入自动语义门禁 | 所有生产页有唯一 main 和 H1；ARIA 扫描无无效用法 |
| P2-4 | Store 明示 `COMING SOON`，8 张产品卡不可点击，只有底部统一 Contact；博客/Hub 缺搜索、筛选与相关推荐 | 用户无法按型号或主题继续探索，内容流量承接弱 | Store 改名为“样品申请/产品询价”或让产品卡深链到预填询盘；博客增加轻量静态搜索/主题筛选；文章末增加相关产品/文章与 CTA；Hub 增加案例筛选和商务出口 | 每个产品卡可进入询盘或详情；博客/Hub 可按主题筛选；内容页有下一步商务动作 |
| P2-5 | 导航项较多，部分下拉在移动端依赖 hover/click 混合行为；中文与英文信息架构不完全对称 | 移动端找产品/应用/联系路径不稳定 | 顶层收敛为 Products / Applications / Research / About / Contact；移动端子菜单点击展开；桌面保留 hover + focus；双语导航映射成一张清单 | 中英文主导航一一对应；触屏与键盘均可展开；无悬停-only 操作 |
| P2-6 | 部署 workflow 有 chronological gate，但无 smoke test、告警、自动 purge、回滚；曾因 artifact 竞争失败并重跑产生重复 artifact | 发布失败发现晚、双层缓存不同步、回滚成本高 | 明确唯一发布 workflow；artifact 名称包含 run id；发布后对 Hostinger 和 GitHub Pages 做 URL/标题/hreflang/表单 smoke test；失败告警；记录上一个已知良好 commit；自动或半自动 purge | 失败 run 有告警；发布后 smoke test 全绿；可快速回滚到上一个 commit；缓存复验通过 |

### 6. 建议实施顺序

**阶段 0：24 小时内止血（P0）**

先轮换并吊销泄露凭据，再处理历史；修正 Cloudflare HTML bypass 并 Purge；停止同意前广告/分析请求；为表单提供不泄露 PII 的降级路径。此阶段以减少安全暴露和发布不确定性为目标，不做视觉改版。

**阶段 1：1 周内低风险性能与内容快赢（P1）**

决策树 base64 外置；应用页 PNG 换已有 WebP；非首屏 lazy；核心图加 `srcset/sizes`；合并 analytics loader；资源版本化；外链补 `noopener`；修正 24/33、17/18 和 35% 口径。每批上线后用相同页面、相同视口复测，避免把第三方网络波动误判为优化收益。

**阶段 2：2–4 周移动端、可访问性与询盘重构（P1/P2）**

重构窄屏网格和全局溢出遮蔽；把图像/Div 点击改成按钮；完成灯箱焦点管理；建立中文首屏报价/样品 CTA；上线受保护 POST 表单与 Consent Manager。表单建议主站使用 Cloudflare Worker + Turnstile，GitHub Pages 镜像保留 mailto/WhatsApp 降级；若团队更倾向传统运维，也可采用 Hostinger PHP，但需同时设计跨源站的一致性。

**阶段 3：1–2 个月工程化与内容治理（P2/P3）**

引入结构化内容清单、声明证据台账、搜索/筛选、相关推荐、CSP Report-Only、字体自托管和完整 CI smoke test。此阶段重点是防止问题再次产生，而不是继续堆页面功能。

### 7. 推荐技术边界

- **不重写为 SPA 或 React**：现有静态页、SEO/GEO 和 GitHub Pages 镜像已经稳定，重构收益低于风险。
- **表单后端与静态镜像解耦**：主站 `/api/inquiry` 只接受 POST，返回 JSON；前端根据 HTTP 状态显示成功/失败；镜像无后端时明确降级。
- **同意状态只有一个事实源**：`mq_cookie_consent` 只负责 accepted/rejected；GA4 和广告都由同一 loader 按状态初始化。
- **资源更新必须可观测**：CSS/JS 用内容哈希；HTML 用短缓存；部署后检查实际响应头，而不是只看源站配置。
- **内容数字必须可生成**：文章数、案例数、企业数、文献数来自清单；营销页面只引用清单，不再手写。
- **声明必须带证据类型**：设备氢气纯度、材料抑菌率、检测方法、市场份额是不同指标，不能因为都接近 99% 或 35% 而混用。

### 8. 验收目标

| 维度 | 当前证据 | 建议目标 |
|---|---|---|
| 决策树 HTML | 中文页传输 1,016,648 B | ≤200 KB，图片独立缓存 |
| 应用页四张大图 | PNG 合计 6,650,830 B；已有 WebP 合计 336,630 B | 首屏图片总传输 ≤500 KB，非首屏 lazy |
| 图片策略 | 471 张非 lazy；0 srcset | 非首屏全部 lazy；核心主图有响应式资源 |
| 隐私同意 | 广告在同意前加载 | 未同意时广告/GA4 请求为 0 |
| 表单隐私 | JS 失效可能 GET 到当前 URL | 任何情况下 PII 不进入 URL；服务端成功后才记线索 |
| 移动布局 | 固定最小宽度 + overflow 隐藏 | 360/390/768 px 横向溢出为 0 |
| 键盘可用性 | 至少 31 个交互目标不可达 | 所有交互可键盘完成，灯箱焦点闭环 |
| 中文转化 | 首屏无报价/样品主 CTA | 首页到询盘 ≤2 次点击 |
| 内容一致性 | 24/33、17/18、35% 口径漂移 | 数量由清单生成；声明有证据或标公司自述 |
| 发布可靠性 | HTML 正常 URL 仍 HIT；workflow 无 smoke test | 正常 URL 部署后 MISS/DYNAMIC；smoke test、告警、回滚齐备 |
| 可访问性 | 20 页无 main，19 页多 H1 | 所有生产页唯一 main/H1，自动门禁通过 |

### 9. 仍未执行的外部高风险动作

未轮换或吊销凭据，未改写 Git 历史，未修改 Cloudflare Cache Rule。当前树中的明文凭据已移除，但旧提交中的历史值仍然有效，直至账号侧完成轮换/吊销；Cloudflare 正常 URL 的 HTML bypass 与部署后 Purge 仍需在控制台复核。以上动作不属于本轮代码授权范围。

### 10. 2026-11-28 授权实施结果（V4.1）

用户明确授权“实施、修改、优化、推送”后，已完成以下代码与本地验证：

- **凭据与隐私**：两个运维脚本改为读取环境变量，当前树不再包含明文密钥；178 个 Cookie 横幅均提供 Accept / Decline；静态 HTML 中 GA4 与 AdSense loader 均为 0，统一由 `script.js` 在 accepted 后加载，Consent Mode v2 默认 denied。
- **表单与中文转化**：首页和联系页移除内联 `onsubmit`，增加 `mailto` POST / `text/plain` 无 JS 降级与 `<noscript>` 联系方式；不再提前触发 `generate_lead`，仅在同意后发送不含 PII 的 `rfq_email_intent`；`?intent=sample#b2bInquiryForm` 自动选择样品申请；中文首页补齐报价/样品 CTA、可点击联系方式、18/33 数字与公司自述式份额表述；Store 八个产品均可进入对应询盘。
- **性能与缓存**：中英文决策树各 5 张 base64 图片外置，HTML 从约 1.47 MB 降至 68,890 B / 74,301 B；应用页改用已有 WebP，19 张非首屏图 lazy；共享 CSS/JS 加 `?v=20261128`；`.htaccess` 对 200 静态资源长期缓存、错误响应不缓存、HTML `no-store`。
- **移动端与可访问性**：修复首页、产品详情、证书页等固定网格；移除相关页面的全局 `overflow-x:hidden`；产品/应用缩略图改为原生 button，并修复应用页缩略图命中区域、产品页图集事件和移动端子菜单状态；补齐焦点可见、下拉键盘操作、18 个报告灯箱触发的 dialog/焦点闭环、Reader 原生 TOC button / `inert` / `aria-expanded`；1,196 个 `target=_blank` 链接均含 `noopener`。
- **发布门禁**：审计脚本发现问题即非零退出；workflow 增加 chronological gate、严格 SEO/GEO 审计、凭据扫描、`git diff --check`、生产入口检查和发布后 smoke test；安全头增加 CSP、COOP、跨域策略、HSTS、权限策略与引用策略。

**本地验收**：严格审计扫描 196 个 HTML、181 个 sitemap URL、22 条以上重定向规则，`问题总数: 0`；中英文博客各 33 张卡片通过日期严格递减门禁；JavaScript / Python 语法与 `git diff --check` 通过；应用页 5 个图集共 14 个原生按钮、0 个直接图片子节点、0 个嵌套按钮；5 个产品页 13 个原生缩略图全部修复。使用本机 Chrome + Playwright 对首页、氢水瓶产品页、应用页、报告页、Reader 页执行 360 / 390 / 768 / 1280 px 回归，横向溢出均为 0；应用缩略图均为 122 × 92 px，产品图集点击后主图切换且仅一个 pressed；移动端菜单/子菜单开关与 Escape、报告灯箱焦点闭环、Reader `inert`、同意拒绝/接受脚本加载行为全部通过；关键页无控制台错误或 HTTP 失败。

**推送与线上复验（2026-11-28）**：代码提交 `5fc8082` 已推送 `main`；GitHub Actions Run `46098256003` 的审计、凭据扫描、部署与 smoke test 全部通过。Hostinger 主站首页、联系页、应用页已确认加载新 Consent/Decline 与 `v=20261128`，静态 GA4/AdSense loader 为 0；HTML 返回 `no-store`，CSP、COOP、nosniff、referrer/permissions/cross-domain 策略生效，CSS/JS 为一年 immutable，Cloudflare 对 HTML 返回 MISS/DYNAMIC。GitHub Pages 首页、中文首页、联系页、应用页、产品页和英文决策树页均通过内容与资源检查。随后对主站报告页和 sitemap/404 的连续实测触发 Cloudflare HTTP 429，未完成主站全量浏览器复验；该限流不是页面断言失败，本地五页回归与 Pages 检查均已通过。

**验证边界与后续项**：PageSpeed Insights API 仍受 429 限制，未取得官方 CWV 分数；GitHub Pages 由平台返回 `max-age=600`，不读取 Hostinger `.htaccess`。尚未建设服务端 POST / Turnstile，尚未全站增加 `srcset/sizes`、自托管字体或补齐全部页面 main/H1；这些属于后续阶段，不冒充本轮已完成。凭据吊销、Git 历史清理和 Cloudflare bypass/Purge 仍需另行授权执行。
