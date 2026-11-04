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

**仍需人工处理的一项（不在仓库内）：** Cloudflare 边缘已经缓存过 30 天的 `robots.txt`/`sitemap.xml`，源站头改了也救不了已命中的副本。需要在 Cloudflare 控制台对 `www.emuqi.com/robots.txt`、`/sitemap.xml` 执行 Purge（或 Custom Cache Rule 把这两个路径设为 Cache-Control: no-cache / 短 TTL），否则新 URL 的发现延迟照旧。

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
