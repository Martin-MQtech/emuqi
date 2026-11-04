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
| 知乎 | 国内知识 | ZH | `01_Zhihu/article_zhihu.md` | 专栏/想法（拟人化） | 📦 资产就绪 |
| 今日头条 | 国内资讯 | ZH | `02_Toutiao/article_toutiao.txt`（标题 22 字 ≤30 红线） | 头条号后台 | 📦 资产就绪 |
| 搜狐号 | 百度高权重门户 | ZH | `03_Sohu/article_sohu.html` | 搜狐号后台 | 📦 资产就绪 |
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
| 2026-11-04 (用户在线指令) | 知乎专栏 | ✅ 上线（Draft.js 编辑器 HTML paste 注入，28 块结构完整） | https://zhuanlan.zhihu.com/p/2101226470999863502 |
| 2026-11-04 (用户在线指令) | 微博 | ✅ 上线（@Martin木齐科技CEO，208 字 + emuqi 链接 + 双话题，sinaurl 包装） | https://weibo.com/u/1671664707 |
| 2026-11-04 (用户在线指令) | Substack | ⏸ 草稿 223407258 内容完整（标题/副标/正文/SEO 全注入，受众=Everyone）。用户改口「不群发」→ 含邮件的发布已及时取消（回到草稿态），改 web-only 重发时 Substack 触发安全门并临时拒绝连接；恢复后最后一步=Continue → 取消勾选 "Send via email and the Substack app" → Publish（按钮自动变为 web-only） | — |

### X 串推六条链谱（存档）
1. https://x.com/MARTINPARK111/status/2117659600485003541
2. https://x.com/MARTINPARK111/status/2117661708923830532
3. https://x.com/MARTINPARK111/status/2117661772488519934
4. https://x.com/MARTINPARK111/status/2117661835344458061
5. https://x.com/MARTINPARK111/status/2117661897462091779
6. https://x.com/MARTINPARK111/status/2117661960477286779
