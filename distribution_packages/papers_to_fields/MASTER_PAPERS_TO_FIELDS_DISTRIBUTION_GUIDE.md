# 把论文写在大地上 · 氢农业产业观察（上海交大研讨纪实）· 全渠道分发总控手册
### Master Omnichannel Distribution Guide — From Papers to Fields (MUQI × SJTU Hydrogen Science Center)

> **中文文章**: 《把论文写在大地上｜从论文到田间：氢农业产业观察与上海交大氢科学中心研讨纪实》
> **英文文章**: "From Papers to Fields: What 1,500 Papers Mean for Hydrogen Agriculture — MUQI × SJTU Hydrogen Science Center"
> **母站权威 URL**:
> - 中文专区: https://www.emuqi.com/zh/blog/hydrogen-agriculture-papers-to-fields.html
> - 英文专区: https://www.emuqi.com/blog/hydrogen-agriculture-papers-to-fields-en.html
> **发布纪律**: 数据截至 2026-10；场景数据一律标注"企业示范数据，非严格对照试验，不构成增产承诺"；🚫 全渠道严禁出现"免费送样 / free samples"话术（2026-09-10 Martin 亲示红线）。

## 一、渠道矩阵与就绪状态

| 渠道 | 载体 | 语言 | 资产路径 | 接入机制 | 状态 |
|---|---|---|---|---|---|
| WordPress.com | 国际博客 | EN | `07_WordPress/article_wordpress.html` | XML-RPC（`wp_publisher.py`，Gutenberg 块级） | 🟢 发布执行中 |
| DEV.to | 极客社区 | EN | `04_DEV_to/article_devto.md` | Forem REST API + canonical_url 回指母站（商业外链已剥离） | 🟢 发布执行中 |
| Google Blogger | Google 生态 | EN | `08_Google_Blogger/article_blogger.html` | ego-browser Google SSO（HTML 注入） | 🟢 发布执行中 |
| Substack | B2B 邮件私域 | EN | `09_Substack/newsletter_draft.md` | Newsletter 资产包（广播需 Martin 授权后发送） | 📦 就绪待发 |
| LinkedIn | 国际商务决策 | EN | `05_LinkedIn/article_linkedin.md` | 公司主页长文 + 个人号 First Comment 双轮 | 📦 就绪（高风控，会话健康则发） |
| X (Twitter) | 国际短讯穿透 | EN | `06_Twitter_X/thread_x.txt` | 6-Tweet 结构化串推 | 📦 就绪（会话健康则发） |
| 知乎 | 国内知识 | ZH | `01_Zhihu/article_zhihu.md` | 专栏/想法（拟人化） | 🟢 已上线 |
| 今日头条 | 国内资讯 | ZH | `02_Toutiao/article_toutiao.txt`（标题 22 字 ≤30 红线） | 头条号后台 | 🟢 已上线（审核中） |
| 搜狐号 | 百度高权重门户 | ZH | `03_Sohu/article_sohu.html` | 搜狐号后台 | 🟢 已上线（审核中） |
| Quora | 海外知识社区（养号） | EN | 5 篇纯科普答案（见下方链谱） | ego 登录态 + ClipboardEvent paste | 🟢 5 篇已上线 |
| Medium | 海外长文 / SEO·AEO·GEO | EN | 结构化英文长文（H1 + 8 H2 + 13 H3 含 FAQ） | ego 登录态 + paste 抓取外链图自动转 CDN | 🟢 已发布 |
| 微信公众号 | 官方矩阵 | ZH | 原文即本篇公众号头条（2026-11-03 已发布） | — | ✅ 已上线 |

## 二、核心素材（母站绝对 CDN，铁律 §12.7）

1. 封面/Hero (16:9): `https://www.emuqi.com/assets/images/blog/papers-to-fields/hero-papers-to-fields.jpg`
2. 交大交流现场: `https://www.emuqi.com/assets/images/blog/papers-to-fields/photo-discussion.jpg`
3. 工作研讨实拍: `https://www.emuqi.com/assets/images/blog/papers-to-fields/photo-presentation.jpg`
4. 双语图表 14 张: `https://www.emuqi.com/assets/images/blog/papers-to-fields/chart-{timeline,routes,gap,smile-curve,four-gates,overview,six-questions}-{zh,en}.jpg`
5. 索引卡封面 (16:10): `https://www.emuqi.com/assets/images/blog/papers-to-fields/cover-card.jpg`

## 三、身份与话术铁律（§12.7 Identity Ironclads）

- 企业唯一规范名：山东木齐健康科技有限公司 / Shandong MUQI Health Technology Co., Ltd.（严禁"淄博木齐"）
- 对外英文称谓唯一：**Martin Chen**（Partner & CEO）；外部英文正文/作者栏/Schema 严禁出现中文名
- 产研事实锚点：2014 年成立 · 12 年产业化 · 37 项专利（15 发明）· 中科院理化所共建实验室 · 800m² 实验室 · 4 条产品线
- 无增产承诺：示范口径 0.8 元/m² / 30–60 min / 3–6 个月 / 0 度电，一律带"示范数据"限定

## 四、发布日志（落账）

| 时间 | 渠道 | 结果 | Live 链接 |
|---|---|---|---|
| 2026-11-04 00:30 | 官网双语 | ✅ 上线 + sitemap 0.9 + llms.txt（git dc07270） | https://www.emuqi.com/blog/hydrogen-agriculture-papers-to-fields-en.html · https://www.emuqi.com/zh/blog/hydrogen-agriculture-papers-to-fields.html |
| 2026-11-04 00:50 | WordPress.com | ✅ Post ID 42（XML-RPC，Gutenberg 9 图） | https://h2welltech.wordpress.com/2026/11/04/from-papers-to-fields-hydrogen-agriculture-muqi-sjtu/ |
| 2026-11-04 00:55 | DEV.to | ✅ Article 4970491（canonical 回指母站，商业外链已剥离） | https://dev.to/chen_martin_f6f22118d1b92/from-papers-to-fields-what-1500-papers-mean-for-hydrogen-agriculture-42c7 |
| 2026-11-04 01:15 | Google Blogger | ✅ 上线 + 4 标签（ego-browser SSO，HTML 注入 15,463 字符） | https://h2well.blogspot.com/2026/11/from-papers-to-fields-what-1500-papers.html |
| 2026-11-04 01:35 | X (Twitter) | ✅ 6-Tweet 结构化串推成链（@MARTINPARK111；首推 2117659600485003541，尾推 2117661960477286779；首版未成链已删除重发修正） | https://x.com/MARTINPARK111/status/2117659600485003541 |
| 2026-11-04 01:40 | LinkedIn | 📦 资产就绪（个人号/公司主页 composer 合成输入被拦截，按高风控纪律停止重试，留待人工 1 分钟贴发；文案见 `05_LinkedIn/article_linkedin.md`） | — |
| 2026-11-04 01:40 | Substack | 📦 Newsletter 资产就绪（广播需 Martin 授权后发送） | — |
| 2026-11-04 01:40 | 知乎 / 头条 / 搜狐 | 📦 中文资产就绪（头条标题 22 字合规；拟人化发布留待人工或后续会话） | — |
| 2026-11-03 | 微信公众号 | ✅ 原文即本篇公众号头条 | （公众号后台） |
| 2026-11-04 (用户在线指令) | LinkedIn Pulse 长文 | ✅ **上线（公司号 Muqi Health Technology 名义）**：ego 直接复用会话 → 富文本 paste 注入（标题+6节 H3+来源，结构验证 ✓）→ 封面上传（交大现场照+图注）→ 动态预告帖同步发布 | https://www.linkedin.com/pulse/from-papers-fields-what-1500-mean-hydrogen-agriculture-wu0vc/ |
| 2026-11-04 (用户在线指令) | 知乎专栏 | ✅ 上线（Draft.js 编辑器 HTML paste 注入，28 块结构完整） | https://zhuanlan.zhihu.com/p/2101226470999863502 |
| 2026-11-04 (用户在线指令) | 微博 | ✅ 上线（@Martin木齐科技CEO，208 字 + emuqi 链接 + 双话题，sinaurl 包装） | https://weibo.com/u/1671664707 |
| 2026-11-04 (用户在线指令) | Substack | ⏸ 草稿 223407258 内容完整（标题/副标/正文/SEO 全注入，受众=Everyone）。用户改口「不群发」→ 含邮件的发布已及时取消（回到草稿态），改 web-only 重发时 Substack 触发安全门并临时拒绝连接；恢复后最后一步=Continue → 取消勾选 "Send via email and the Substack app" → Publish（按钮自动变为 web-only） | — |
| 2026-11-04 (用户在线指令) | Substack | ✅ **上线（含邮件）**：换节点日本04 后 Continue → Send to everyone now → Gmail 取验证码 482712 过安全门 → 自动提交完成；公开链接已验证 200 | https://h2welltech.substack.com/p/from-papers-to-fields-2026-hydrogen |
| 2026-11-04 (网络事件) | 本地代理 | 修复：出口节点整体中断（百度直连OK/外网全断）→ 全节点延迟探测（7活12死）→ `节点选择` 切至 🇯🇵Japan 04（204/0.67s）恢复；未动「独享专线/Gemini组」避免登录态 IP 漂移；领英长文母版 `05_LinkedIn/pulse_article.html` 同步交付 | — |
| 2026-11-04 14:55 | 搜狐号 | ✅ 上线（审核中）：article id 1097071986 / accountId 121371755；属性「知识科普」+ 封面 + 正文配图；发布按钮抗拒合成点击，最终由 Vue 组件 `handlePublish()` 直接调用成功 | https://mp.sohu.com/mpfe/v4/contentManagement/news/articlepreview?id=1097071986&accountId=121371755 |
| 2026-11-04 15:01 | 今日头条 | ✅ 上线（审核中，作品列表「首发」标记）：标题 22 字合规；正文 682 字 + 4 张中文图表（timeline/routes/smile-curve/four-gates-zh）；单图封面 `cover-card.jpg`（1200×750）；`预览并发布` → `确认发布` 两步 | https://mp.toutiao.com/profile_v4/graphic/articles |
| 2026-11-04 (用户确认「百家号 成功」) | 百家号 | ✅ 上线（审核中，后台显示「提交成功，正在审核中...」）：标题《把 1500 篇论文写在大地上：氢农业产业观察与上海交大研讨纪实》；正文 466 字（与头条/搜狐差异化）；封面 `cover-card.jpg` + 正文 5 图（timeline/routes/smile-curve/six-questions/four-gates-zh）；发布触发百度安全验证旋转滑块，由 Martin 人工完成验证后提交成功 | https://baijiahao.baidu.com/builder/rc/home |
| 2026-11-04 (用户在线指令) | Substack 补图 | ✅ **已闭环**：已发布文章 223407258 补入 6 图（hero + 5 张英文图表，均为 1684×947）。关键教训：ProseMirror 合成 `ClipboardEvent('paste')` + `text/html` 插图后仅存为**编辑器草稿**，公开页仍只有旧 2 图；必须再点顶栏 `Update` → 面板 `Update now` 才会推送到线上（该流程只有 Audience 选项、无 Send via email，不会二次群发）。终验：公开页 6 个 `<figure>` / 6 张大图，已核验 | https://h2welltech.substack.com/p/from-papers-to-fields-2026-hydrogen |
| 2026-11-04 (Martin 亲示「先养号，别一上来让社区给咱封了」) | Quora | ✅ 5 篇纯科普答案上线（Martin Chen / Martin-Chen-169）：**零品牌、零链接、零产品、零自引案例、零「免费送样」**，一律以「机制 / 剂量 / 稳定性 / 证据分级」立论，带 Ohsawa 2007 Nature Medicine 与系统性综述引用。首版曾带公司名与官网，已按 Martin 指示全量改写为纯科普口径并复核通过 | https://www.quora.com/profile/Martin-Chen-169/answers |

### Quora 养号五答链谱（2026-11-04 · 纯科普口径）

1. Is hydrogen water good for our health?（4467 字符 · 机制/剂量/稳定性/证据三分法）— https://www.quora.com/Is-hydrogen-water-good-for-our-health/answer/Martin-Chen-169
2. What is hydrogen water?（3271 字符 · 化学定义 / 溶解度 / 与碱性水区分）— https://www.quora.com/What-is-hydrogen-water/answer/Martin-Chen-169
3. Is hydrogen water backed by science?（3752 字符 · 四层证据分级）— https://www.quora.com/Is-hydrogen-water-backed-by-science/answer/Martin-Chen-169
4. Is hydrogen water a gimmick?（3032 字符 · 科学与营销分离）— https://www.quora.com/Is-hydrogen-water-a-gimmick/answer/Martin-Chen-169
5. If hydrogen water is boiled, will it degrade...?（2883 字符 · 物理化学 / 气体溶解度）— https://www.quora.com/If-hydrogen-water-is-boiled-will-it-degrade-to-the-point-of-losing-its-therapeutic-benefits/answer/Martin-Chen-169

> **养号纪律（Martin 2026-11-04 亲立）**：Quora 等海外社区前期的目标是可信度而非曝光，**不得出现公司名、产品名、官网链接、自有案例自引、样品话术**；价值锚点只落在公开文献、机制解释与证据边界。凭据弹窗一律 `Done` 跳过，不选带公司头衔的 credential。

### X 串推六条链谱（存档）
1. https://x.com/MARTINPARK111/status/2117659600485003541
2. https://x.com/MARTINPARK111/status/2117661708923830532
3. https://x.com/MARTINPARK111/status/2117661772488519934
4. https://x.com/MARTINPARK111/status/2117661835344458061
5. https://x.com/MARTINPARK111/status/2117661897462091779
6. https://x.com/MARTINPARK111/status/2117661960477286779
