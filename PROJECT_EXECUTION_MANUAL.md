# 🌐 山东木齐健康科技 (MUQI Technology) 官方网站建设与全栈运维执行手册

> **文档性质**: 项目唯一根控制指导手册 (Single Source of Truth)  
> **管理方**: Martin Bin Chen (陈滨) & ZCode / Antigravity AI Agent 协同运维小组  
> **更新时间**: 2026-08-31 (V3.1 仓库地址勘误 + 全站审计修复)  
> **内容来源**: 已吸收合并三份企业档案（国际市场执行手册 v3.0 / 项目背景与产品服务汇总 v2.1 / 固态氢产品合规策略报告 PDF）  
> **精简原则**: 项目根目录下严禁创建多余、临时或重复的 `.md` 文件。所有背景、环境配置、部署 SOP、企业情报与重要里程碑统一收拢归档于本手册。

---

## 1. 项目概览与商业定位 (Project Overview & Vision)

### 1.1 企业背景与资质
- **企业全称**: 淄博木齐健康科技有限公司 (MQ Health Tech / MUQI Technology)，创立于 **2011 年**。
- **总部**: 山东省淄博市先进陶瓷产业创新园 B 座。
- **资质荣誉**: 2019 国家高新技术企业 | 2020 山东省"专精特新"+淄博"百强品牌" | 2022 **国家级专精特新"小巨人"**。
- **核心数据**: 13 项发明专利（核心专利 ZL 2023 1 0033992.7 固态负载氢气材料）、29 项企业标准、50+ 检测报告（SGS/广微测/复旦大学）、**1800+ 全球客户**、固态氢消费品核心材料**全球份额 35%**、8 国马德里商标。
- **团队**: 12 人研发团队（硕博/留学 60%），与中科院理化所（黄勇团队）、上海交大产学研合作，拥有"固态氢功能陶瓷重点实验室"。

### 1.2 核心技术：ICR 智控释溶固态氢
ICR（Intelligent Controlled Release）为第三代固态氢材料技术，核心能力为**氢矿协同释溶**——常温常压下固态氢复合材料遇水后，氢气与矿物质离子同步、可控、按需释放。

| 对比维度 | MUQI ICR 固态氢 | 传统 SPE/PEM 电解 |
|------|:---:|:---:|
| 供能 | **零电力** | 必须电池/电源 |
| 氢浓度半衰期 | **18-24h**（完全逸散>3天） | 2-4h |
| 商业模式 | **耗材复购+OEM** | 硬件一次性销售 |
| 附加价值 | 氢+矿物质同步释放 | 仅产氢 |
| 成本 | 比日本电解方案低 **35-50%** | 基准 |
| 安全性 | 本质安全，无臭氧无氯 | 需排气阀 |

**技术指标**: 氢浓度 1000-1500ppb 稳定释放 | 打样周期 5-22 天 | 材料体系：镁基/硅基/钙基氢化物+天然矿物纳米复配 | 矿物质：镁、钙、硅、锶、偏硅酸。

### 1.3 品牌战略与定位
- **核心定位**: **"MUQI Inside"**（如 Intel Inside）——不做终端品牌，做固态氢材料与应用方案供应商，将氢健康从设备型产品转化为**可嵌入、可定制、可复购、可场景化**的材料与耗材方案。
- **品牌主张**: *"Hydrogen. Simplified."* —— 无需电池、无需充电、无需等待。
- **品牌架构**: MQ HEALTH TECH（背书品牌）→ H2fizz™（C端杯袋）/ H2Tab™（耗材）/ MQ Ceramics™（B2B 原料）。
- **关键词库（SEO/GEO）**: 产品词（water filter, hydrogen water bottle, solid-state hydrogen…）/ 产业词（hydrogen health, hydrogen therapy, molecular hydrogen, hydrogen wellness…）/ 合作词（OEM, ODM, private label, distributor…）/ 场景词（hotel, spa, recovery, resort, foot bath…）。

---

## 2. 网站架构与目录规范 (Architecture & Directory Standards)

### 2.1 技术栈
- **前端架构**: 原生 HTML5 + CSS3 + Vanilla JavaScript（无繁重框架，极速加载，适配海外 B2B 与 Google / GEO 收录）。
- **视觉系统**: DM Sans + Inter 字体，全站统一木齐橙 VI (`#f47b20`)。

### 2.2 目录结构与单点真理
```text
/20260721 MUQI 网站建设/
├── PROJECT_EXECUTION_MANUAL.md      # [本文件] 唯一根控制指导手册
└── emuqi/                           # 官方代码库根目录 (Git 工作树)
    ├── DESIGN.md                    # 设计系统规范与修改日志 (V3.0)
    ├── README.md                    # 官方开源项目展示面 (Codex OSS 标准)
    ├── LICENSE                      # 标准 MIT 开源许可证 (Copyright Martin Bin Chen)
    ├── index.html                   # 官方 B2B 门户首页
    ├── 404.html                     # 品牌化 404 页面
    ├── style.css / script.js        # 全站统一样式与交互脚本
    ├── .github/workflows/deploy.yml # GitHub Actions Pages 自动部署流水线
    ├── h2-wellness-hub/             # 资源中心与 B2B 规格模块（中英双语）
    ├── blog/                        # 16+ 篇行业与技术深度文章
    └── assets/                      # 110+ 结构化产品与品牌媒体资源
```

---

## 3. 环境配置与自动化部署体系 (Infrastructure & CI/CD Pipeline)

### 3.1 GitHub 握手与认证
- **主业务仓库**: `git@github.com:Martin-MQtech/emuqi.git`（2026-08-31 实测勘误：仓库已迁移至 Martin-MQtech 账户；旧地址 `Martin-MQtech/emuqi` 由 GitHub 自动重定向，新环境配置统一使用新地址）
- **个人 Profile 仓库**: `git@github.com:Martin-MQtech/Martin-MQtech.git`
- **默认分支**: `main` | **SSH 状态**: ✅ 握手成功（`Hi Martin-MQtech!`）

### 3.2 双平台实时发布架构
| 角色 | 域名 / URL | 部署机制 | 触发条件 |
|------|-----------|---------|------------------|
| **主站域名** | `emuqi.com` | Hostinger 自动 Git 部署 (`147.79.79.250`) | 推送 `main` 分支后 1-2 分钟 |
| **镜像/备份** | `martin-mqtech.github.io/emuqi/`（2026-08-31 实测勘误：旧地址 `martin-mqtech.github.io/emuqi/` 已 404，Pages 不会随仓库迁移自动重定向） | GitHub Actions (`deploy.yml`) | 推送 `main` 分支自动构建 |

### 3.3 Mac Mini 环境配置归档（合并备忘）
```bash
# SSH 配置
mkdir -p ~/.ssh && chmod 700 ~/.ssh
cat > ~/.ssh/config << 'EOF'
Host github.com
    Hostname ssh.github.com
    Port 443
    User git
EOF
chmod 600 ~/.ssh/config
ssh-keyscan -t ed25519,rsa -p 443 ssh.github.com >> ~/.ssh/known_hosts 2>/dev/null

# Git 全局配置
git config --global user.name "Martin-MQtech"
git config --global user.email "Martin-MQtech@users.noreply.github.com"
git config --global init.defaultBranch main
git config --global core.autocrlf input
git config --global credential.helper store

# 代理快捷键 (配置于 ~/.zshrc)
alias proxy-on='export HTTP_PROXY="http://127.0.0.1:7897" HTTPS_PROXY="http://127.0.0.1:7897" ALL_PROXY="socks5://127.0.0.1:7897" NO_PROXY="localhost,127.0.0.1,*.local,192.168.*,10.*,172.16.*" && echo "✅ 代理已开启"'
alias proxy-off='unset HTTP_PROXY HTTPS_PROXY ALL_PROXY && echo "🔄 代理已关闭"'
```

---

## 4. 产品矩阵与商业模式 (Products & Business Model)

### 4.1 产品矩阵：吃·喝·洗·护·泡
| 场景 | 产品形态 | 目标客户 |
|:---:|---------|---------|
| 吃 | 氢压片糖果、泡腾氢气片 | 健康食品品牌、补充剂企业 |
| 喝 | 小氢瓷、氢水瓷、富氢滤芯（元气红芯） | 净水器厂商、饮料品牌 |
| 洗 | 小氢皂、氢沐浴产品 | 个人护理品牌、SPA 机构 |
| 护 | 氢面膜、氢气眼贴、富氢卫生巾芯片 | 美容品牌、女性护理 |
| 泡 | 足浴氢气片、氢浴包、矿物浴片 | SPA 连锁、健康度假村 |

### 4.2 B2B 核心原料线（英文官网已上线）
- **Hydrogen Generate Ceramic Ball**（富氢陶瓷球/颗粒）: ORP 陶瓷球，偏硅酸丰富、高硬度、快速制氢。
- **MACA KDF Antibacterial Ceramic Ball**（抗菌陶瓷球）: 抗菌率 ≥99%、微孔自极化。
- **MPH+ Condensate Neutralizer**（长效碱性球）: 通过 SGS 19 项饮用水卫生标准。
- **HI 矿物氢素原料**（氢压片料/面膜料/泡腾料）+ **元气红芯滤芯**（镁基微电解制氢，规格 大T/10寸/20寸）。

### 4.3 四种合作模式
| 模式 | 内容 | 适用客户 | 利润结构 |
|:---:|------|---------|---------|
| A. 原料供应 | 富氢陶瓷球/颗粒 → 水处理/净水企业 | BRITA、BWT、Coway | 低毛利大体量 |
| B. OEM/ODM | 客户品牌+木齐技术 | Lush、Kneipp、Dr Teal's | 中等毛利可规模化 |
| C. 联合品牌 | 共同推向市场 | 区域分销商 | 分摊投入共享品牌 |
| D. 技术授权 | 区域独家授权 | 日韩大型制造 | 高毛利轻资产 |

---

## 5. 市场格局与国际化路线图 (Market & Global Roadmap)

### 5.1 市场空间
| 市场 | 规模 | 远期 | CAGR |
|------|:---:|:---:|:---:|
| 全球氢水市场 | $12亿(2024) | $38亿(2034) | 12.1% |
| 氢水杯市场 | $12-24亿(2025) | $89.7亿(2035) | 14.1% |
| 分子氢吸入器 | $4.22亿(2025) | $9亿(2032) | 11.6% |
| 抗衰老消费品 | $851亿(2025) | — | 7.0% |
| 生物黑客/长寿 | $273亿(2025) | — | 13.1% |

**木齐 SAM (2029)**: $1800-5300 万/年（B2C+B2B组件+B2B渠道+OEM 四路径）。区域侧重：北美 34.2% / 欧洲 28.7% / 日本最成熟 / 东南亚增量市场。

### 5.2 四大标准化市场专项
| 专项 | 定位 | 典型画像 |
|---|---|---|
| 🧪 长寿与医疗康养 (Longevity & Medical) | 顶格高势能赛道 | 抗衰诊所、功能医学中心、干细胞疗养院、奢华长寿度假村 |
| 🎁 健康礼品 (Health Gifts) | B2B 礼品与福利 | 礼品服务商、企业 HR 采购、高管礼包 |
| 💧 氢健康垂直 (Vertical Hydrogen) | 设备与垂直机构 | 氢 SPA 中心、体验馆、氢设备分销商 |
| 💊 大健康泛渠道 (General Wellness) | 规模化泛渠道 | 连锁药房、净水品牌、日化洗护、高端超市 |

### 5.3 目标客户十大细分市场
核心行业（7）：氢健康专业机构★P0 / 高端SPA康养连锁★P0 / 健康美容品牌商★P1 / 大型零售药房★P1 / **水处理净水品牌★P0** / 酒店度假村★P2 / **银发经济老年康养★P1**（2026-07 新增战略维度）。
穿透维度（3）：医疗美容轻医美★P1 / 生物黑科技功能医学★P2 / 中医中药草本养生★P1。
**三维评分模型**: 总分 = CF（匹配度1-5）+ CV（商业价值1-5）+ CT（可触达性1-3），S≥12 / A=11 / B=9-10 / C=7-8 / D≤6。

### 5.4 市场进入优先级
| 优先级 | 市场 | 时机 | 模式 |
|:---:|------|:---:|------|
| P0 | 泰国/新加坡 | 即刻 | B2B 开发+样品 |
| P0 | 日本 | Q3 2026 | 代理商/经销商 |
| P1 | 美国 | Q4 2026 | Amazon FBA + DTC |
| P1 | 马来西亚/印尼 | 即刻 | 电商+本地代理 |
| P2 | 韩国 | Q1 2027 | 电商+KOL |
| P2 | 德国 | Q2 2027 | 经销商+Amazon DE |

### 5.5 国际展会日历
Aquatech China 2026.10（上海★5）/ Aquatech Asia 2026.11（曼谷）/ ISPO 2026.11（阿姆斯特丹）/ Aquatech Amsterdam 2027.3（★5）/ Cosmoprof Bologna 2027.3 / FIBO 2027.4（科隆）/ WQA Convention 2027.4（美国★5）。

---

## 6. 合规策略与宣传红线 (Compliance & Marketing Guardrails)

### 6.1 商标类目布局（六款核心产品）
采用**核心+功能+防御**三层策略：小氢皂(03+05) / 氢陶瓷环(11+01) / 足浴氢气片(03+05) / 氢春杯(21+11) / 氢气眼贴(03+05) / 氢浴球(03+05+35)。全程必做：第35类（渠道保护）+ 马德里国际商标（已获8国）。

### 6.2 宣传合规铁律（全球通用）
- 用**状态词**代替**结果词**（"焕发活力"优于"治疗疲劳"）；用**过程描述**代替**功效承诺**（"氢分子深度渗透"优于"清除自由基"）。
- **严禁词**：祛痘/消炎/降血压/治糖尿病/防癌/排毒/治愈失眠/改善视力等一切医疗功效承诺。
- 包装必标免责声明：*"本产品为健康消费品，不能代替药物或医疗器械，不具有疾病预防及治疗功能。"*
- 英文强制声明（海外）：*"These statements have not been evaluated by the FDA. This product is not intended to diagnose, treat, cure, or prevent any disease."*

### 6.3 两阶段市场准入策略
- **第一阶段（当前）**: 全部产品按**一般民用产品**身份进入市场，仅需企业标准（Q标）备案 + 宣传合规，零门槛快速启动。
- **第二阶段（进阶备选）**: 高潜力品类（氢浴球★★★★/氢气眼贴★★★/足浴片★★★）经**香港健康产品备案 / 澳门大健康备案** + 跨境电商回流出海，主攻东南亚、日韩、欧美。
- **风险控制**: 材料安全评估（皮肤刺激/重金属/急性毒性）+ OEM 合同责任隔离（生产方担技术合规、委托方担宣传责任）。

---

## 7. 国际市场客户开发方法论与铁律 (Trade Development Playbook)

### 7.1 全层级统一红线（Agent 必读）
1. **授权口令协议**: 唯有用户精确打出「确认发送」四字，系统方可获得发信授权，不接受任何变体。
2. **纯文本规则**: 私信/邮件禁用 Markdown 符号，输出无符号纯文本。
3. **统一商务署名**（硬编码）:
   ```text
   Best regards,
   Martin Chen
   CEO | MUQI Tech
   Email: muqizb@gmail.com
   WhatsApp: +86 13964416725
   Web: www.emuqi.com
   ```
   严禁出现 CMO 等其他身份（重大教训：2026-08-05 曾误发 12 封事故）。
4. **生存状态排雷**: 所有标的先做全网生死排查，破产/停业直接剔除；邮箱必须零退信探针验证。
5. **草稿纯净性**: 草稿只含元数据+To/CC+主题+正文+签名，禁止内部备注；主题行 100% 含客户公司名。
6. **协同策略优先**: 严禁未对齐战略就抢跑起草开发信。
7. **发送后归档**: 发送成功同轮内改状态字段+文件名（草稿→已发送）。

### 7.2 链条穿透方法论 (Network Penetration)
1. **上下游供应链穿透**: 富氢材料→滤芯厂商→Coway/Cuckoo/BRITA/BWT 水处理巨头。
2. **中间商背后买家穿透**: 礼品服务商/贸易代理→其背后百货、银行、奢华酒店。
3. **母公司/跨国分支穿透**: Boots Thailand→WBA Group；子品牌→King Power 集团。
4. **标杆客户镜像复制**: 锁定 Chiva-Som → 镜像复制 Six Senses/RAKxa/Kamalaya/Banyan Tree 等。
5. **竞品海关穿透 (Tendata CDP)**: 锁定头部竞品（卡沃罗/Olansi/龙巍等）按 HS 编码反查提单，28 个买家池、200+ 国际真实买家。

### 7.3 GEO 生成式引擎优化战略
- **AI Citation Sovereignty（AI 权威引用主权）**: 官网部署 Schema.org JSON-LD（专利/技术参数/企业标准结构化数据），抢占 Google AI Overviews 第一推荐位。
- **GEO 问答矩阵**: 建立针对各区域客户的合规/原理/半衰期/成本对比结构化 Q&A 库。
- **全流程 AI Agent 矩阵**: 全球情报扫描 → 探针验证 → GEO 内容生成 → 拟人化安全调度 端到端闭环。

---

## 7.4 氢农业内容枢纽与研究来源规范 (Hydrogen Agriculture Content Hub)

### 内容信息架构：一级 + 二级，禁止无边界下钻
- **一级入口**: `solutions-hydrogen-agriculture.html`，定位为 Hydrogen Agriculture Hub，解释 MUQI 的固态氢/硅基/矿物材料底座，并路由至四个平行方向。
- **二级研究页**: 种植与土壤生物学 / 畜牧与瘤胃研究 / 水产与水系统 / 宠物医疗护理与功能营养。每页独立承接对应 GEO/SEO 关键词、研究证据、合作试点场景和材料路径。
- **深度上限**: 不再扩展至第三级。新增文章优先挂接至现有四个二级主题，并在文章内回链一级页、材料页和 Hub 来源页。

### 研究来源与事实边界
- **优先来源**: 原始论文、PubMed、Frontiers、MDPI、FAO、Meat & Livestock Australia / CSIRO、国家级试验或标准数据库。
- **Hub 归档位置**: `h2-wellness-hub/resources.html` 的 "Plant, livestock, aquaculture, and companion-animal research" 分组。该组仅保存可核验的研究入口和机构来源，不把来源当作 MUQI 背书。
- **表达规则**: 对研究使用 "a study reported / researchers observed / a review discusses"；禁止将单一论文结果写成所有物种、所有农场或 MUQI 产品的保证。产品页只描述材料能力、设计用途与待验证试点路径。

### 初始关键词矩阵
| 平行方向 | 英文关键词 | 面向买家 |
|---|---|---|
| 种植 | hydrogen agriculture, hydrogen fertilizer, crop resilience, rhizosphere microbiome, hydroponic water treatment | 温室、灌溉、水肥、农业投入品企业 |
| 畜牧 | livestock hydrogen research, rumen hydrogen balance, cattle methane microbiome, piglet gut microbiota | 饲料、牧场、反刍动物研究、动物营养企业 |
| 水产 | hydrogen aquaculture, hydrogen-rich water fish, RAS water treatment, aquaculture water quality | 鱼虾养殖、循环水系统、水处理设备商 |
| 宠物医疗护理 | companion animal health, veterinary hydrogen research, pet wound care materials, functional pet water | 宠物医疗、护理、功能水、宠物营养品牌 |

---

## 8. AI Agent (ZCode) 协同运维 SOP

### 8.1 代码与设计更新流程
```bash
cd "/Users/martin/Documents/2026 BUSINESS MTRIX /20260721 MUQI 网站建设/emuqi"
git add .
git commit -m "feat: [具体的更新说明]"
git push origin main   # 触发 GitHub Pages + Hostinger 双部署
```

### 8.2 单点真理维护约定
- UI/CSS 样式变更 → 同步更新 `emuqi/DESIGN.md`。
- 全盘架构/部署/关键事件/企业情报 → 统一更新本手册。

---

## 9. 项目里程碑与重要事件记录 (Milestones & Episodes)

### 9.1 企业资料全量归档 (2026-08-10)
四份企业档案已全量提炼吸收至本手册，源文件已删除，保持根目录纯净：
- **国际市场执行手册 v3.0**（红线规范/客户开发方法论/GEO 战略）→ 已并入 §7。
- **项目背景与产品服务汇总 v2.1**（公司概况/技术/产品/市场/品牌）→ 已并入 §1、§4、§5。
- **固态氢产品合规策略报告 PDF**（商标/话术/两阶段准入）→ 已并入 §6。
- **固态氢敷贴视频开发与电影级剪辑执行手册 v3.0**（Remotion 视频 SOP）→ 已并入 §9.4。

### 9.4 固态氢敷贴视频开发 SOP（Remotion 电影级剪辑）
- **产品定位**: "不改产线、不加设备，给现有外用贴膏产线加一道'加氢'工序"，突破 281 亿外用贴膏同质化比价泥潭。
- **交付成片**: 中文宣传片 (~55s) + 英文宣传片 (~54s)，位于 `~/Desktop/Codex视频处理/20260807 富氢敷贴/`。
- **视觉规范**: 星夜黑底 `#080C14` + 科技氢蓝 `#00D4FF` + 数据绿 `#00FFC8` + 暖金 `#F5A623`；图文强对位红线（场景与 TopBadge/字幕 100% 语义吻合）；双语毛玻璃字幕（中 38px 白 + 英 24px 琥珀金，底边 160px 安全区）。
- **渲染命令**: `node_modules/.bin/remotion render Chinese-v2 <输出.mp4> --concurrency=2`（English-v2 同理）。

### 9.2 OpenAI Codex for OSS 开源资助申请成功递交 (2026-08-10)
- **组织 ID**: `org-MP5H013EYkOG4Yqqpgv5gvV5` | **账号/邮箱**: `13964416725@126.com`
- **叙事**: 清华 MBA / 20 年外贸专家借助 AI Agent 从零手搓 B2B 自动化（开发信生成、CBM 计算器、包材助手）。
- **状态**: ✅ 已递交，等待官方审核。

### 9.3 网站全面 SEO/合规化重构 (2026-08-10)
品牌术语全站统一（→MUQI）、sitemap 全覆盖 113 URL、品牌化 404 页、57 页 Title/Desc 精修、40 页 Hreflang、28 页 JSON-LD 结构化数据。

### 9.4 旗舰技术博客发布与全站 AI / GEO / Schema.org 体系大升级 (2026-08-25)
- **旗舰博文上线**: 发布《抗菌陶瓷球全场景应用与ICR技术深度解析》（`blog/antimicrobial-ceramic-balls-home-appliances-icr-technology.html`），搭载 5 张高精矢量架构图、3 联实拍图、TOC、参数数据卡、GEO 实体索引云及权威背书。
- **全站图谱重构**: 全站 39 个核心 HTML 页面全面完成 Schema.org `@graph` 知识图谱改造，打通 Organization、Person (Martin Chen)、SAC/TC621 国家标委会委员资质、Product 与 TechArticle 闭环。
- **SOP 规范沉淀**: 确立《全站内容生长与 AI / GEO / SEO 协同执行标准》，并固化至本执行手册第 11 章节。

---
### 9.5 全站 SEO/GEO 技术底座升级 (2026-09-02)
- **AI 爬虫战略（robots.txt 重写）**：显式欢迎 GPTBot / OAI-SearchBot / PerplexityBot / ClaudeBot / Google-Extended / Applebot 等 GEO 爬虫；屏蔽 CCBot/ImagesiftBot 纯训练爬虫；Ahrefs/Semrush/MJ12 限速保护主机；Sitemap 统一指向 `https://www.emuqi.com/sitemap.xml`。
- **llms.txt 上线**：按 llmstxt.org 规范部署 `https://www.emuqi.com/llms.txt`，向 LLM 输送企业事实锚点（ICR 参数 / 13 专利 / SAC/TC621 / 35% 份额）与核心页面路由。
- **Favicon 全站覆盖**：新建品牌 SVG 图标（深蓝底 + 木齐橙水滴 + H₂ 气泡）及 32/180/512 PNG 三件套（`assets/icons/`），124 页全部注入（按目录深度自动计算相对路径，双镜像兼容）。
- **OG 标签补全**：`og:site_name` + `og:locale`（en_US/zh_CN 按 lang 自动判定）全站覆盖。
- **Canonical 治理**：消除 `/index.html` 尾缀重复（首页、`blog/`、`blog-list` 三处），目录页 canonical 统一为斜杠根。
- **首页元数据重写**：Title/Description 注入买家关键词（solid-state hydrogen materials manufacturer / OEM/ODM / hydrogen filter cartridges），OG 同步。
- **首页 Schema 去重与增强**：消除 3 个完全重复的 @graph 块（重复 @id 会混淆解析器）；Organization 实体新增 foundingDate 2011 / slogan "Hydrogen. Simplified." / 小巨人 award / knowsAbout 七大知识领域。
- **Sitemap 清理**：移除 3 个跳转占位页（hub.html、h2-health-hub 两处），121 URL 全部为真实内容页。
- **GA4 配置化加载器**：新建 `assets/js/analytics.js`，124 页统一接入；在文件内 `ga4MeasurementId` 粘贴 `G-XXXXXXXXXX` 即全站生效（当前为空＝未激活，待建号后配置）。GSC 建议采用 HTML 文件验证法。
- **验证结果**：372 个 favicon/analytics 资源引用 0 断链；全站 JSON-LD 有效性抽查通过；robots.txt 22 条规则解析正常。

*本手册由 ZCode AI Coding Agent 统一精炼维护，为全项目唯一指导手册。*


## 10. 品牌叙事与价值观内核 (Brand Narrative & Philosophy)

> **核心精神**：让前沿健康科技无国界普惠、零门槛落地 (Democratizing Wellness through Seamless Integration)。

### 10.1 表达调性 (Tone of Voice)
- **温和而自信 (Quiet Confidence)**：我们不是现有水电解设备的“颠覆者”或“攻击者”，而是产业升级的“共赢者”与“生态拼图”。
- **人文与科技交融 (Tech meets Humanity)**：把冰冷的“材料与参数”翻译为人性化的“生活福祉”。
- **零摩擦赋能 (Zero-Friction Empowerment)**：突出“不改变用户习惯”、“零学习成本”和“极低决策门槛”。

### 10.2 顶级商业话术池 (Curated Business Expressions)
在对外沟通、GEO 结构化数据、开发信及网页文案中，强制使用以下叙事逻辑：
1. **关于与传统的共存 (On Complementing the Industry)**
   - *传统刚性表达*：Solid-state hydrogen defeats expensive electrolysis machines.
   - *🌟 升华表达*："Our solid-state solutions are designed to complement, not displace. We seamlessly integrate advanced hydrogen wellness into everyday products, offering a zero-electricity, accessible alternative that broadens the market without rendering existing infrastructure obsolete."
2. **关于 MUQI Inside 模式 (On the Collaborative Model)**
   - *传统刚性表达*：We supply raw materials and OEM services globally.
   - *🌟 升华表达*："Through the 'MUQI Inside' cooperative philosophy, we empower global brands to effortlessly upgrade their portfolios. It is a win-win ecosystem where our biological-backed materials meet your established market presence."
3. **关于普惠与用户体验 (On User Experience & Accessibility)**
   - *传统刚性表达*：Easy to use, cheap cost, and lasts 24 hours.
   - *🌟 升华表达*："By harmonizing new material science with eco-friendly principles, we democratize wellness. Our technology demands zero learning curve and imposes no new habits—just pure, lasting hydration that naturally fits into modern life with minimal decision-making costs."


### 10.3 科学引用与产品宣称的修辞艺术 (The Art of Scientific Borrowing)
> **高级合规平衡论**：不要为了所谓的“机械性合规”而自我阉割产品的科技威力与底层生物医学证据！在国际化独立站营销中，我们必须利用高强度的客观研究结论（包含治疗、治愈等锋利字眼），同时在修辞上巧妙切割产品声称，确保锋锐的商业进攻性与合规的防守底线并存。

**实施法则 ("Third-Party Science, First-Party Experience")**:
1. **科学无禁区 (Unrestricted Academic Citations)**
   - 在引用 PubMed 论文、临床双盲实验背景、或者“氢医学进展”等篇章中，**绝对不要软化或避讳使用 `treatment`, `therapy`, `anti-tumor`, `cure` 等强有力的医疗词汇**。只要前缀是“据临床研究表明(Clinical studies have demonstrated)”或“相关研究正在探索(Emerging research explores)”，这些事实就是锋利的销售武器。
2. **连接有修辞 (Bridging via Mechanism)**
   - 绝不直接宣称 *"Our Ceramic Ball cures diseases"*（这是劣质营销且越红线）。
   - **高阶句式转换**：*"With hundreds of studies outlining HTML’s therapeutic potential in addressing oxidative stress, MUQI's solid-state materials are engineered to reliably deliver the high-concentration hydrogen those studies rely on."*（用几百篇论文论证疗效，而我们只是提供科研同级别的浓度输出——借科研的刀，展示自己的工艺）。
3. **免责严兜底 (The Safety Net)**
   - 锋利的学术宣导辅以标准的 `<FDA Disclaimer>` 强制兜底。只要页面底部声明 *"This product is not intended to diagnose or treat..."*，我们在前文借用的医学界学术论文就属于完全合法的科普引流策略。


---

## 11. 全站内容生长与 AI / GEO / SEO 协同执行标准 (AI-Native GEO & SEO Engineering Manual)

> **最高指导原则**：木齐科技站点所有新增页面与内容资产（技术博文、产品页、行业方案、客户案例、白皮书等）在策划、生成与发布全流程中，**必须 100% 保持与生成式 AI 引擎 (GEO / LLMO)、Schema.org 结构化数据协议及中英双语 SEO 的原生兼容与协同**。

### 11.1 认知底座：Schema.org 的本质与在 GEO 中的战略角色
1. **本质定性**：由 Google、Microsoft (Bing)、Yahoo、Yandex 于 2011 年联合创立的**国际语义网数据词汇表协议 (Semantic Vocabulary Protocol)**。它是给搜索引擎与大语言模型（LLM）读取的**“结构化机器身份证与实体图谱”**。
2. **战略价值**：大模型（ChatGPT、Perplexity、Claude、Kimi 等）抓取网页时，非结构化文本需消耗高算力进行概率推测；而 **Schema.org JSON-LD 代码能让 AI 在 0 毫秒内精准建立实体事实链接**（如：木齐科技 $\rightarrow$ 全国抗菌表面标委会 SAC/TC621 委员单位 $\rightarrow$ MACA-KDF 抗菌合金球 $\rightarrow$ ICR 智控释溶技术）。

### 11.2 新增内容 5 大底层标准与执行流程 (The 5 Mandatory Content Pillars)

```
                    ┌────────────────────────────────────────────────────────┐
                    │            木齐科技 AI · GEO · SEO 协同增长体系        │
                    └────────────────────────────────────────────────────────┘
                                                ▲
                                               / \
      【1. Schema 实体图谱先导】              /   \             【2. 权威事实抗幻觉锚定】
      Organization / SAC/TC621 /              / 知识 \            精确参数 (1000℃/1500ppb/-800mV) /
      Person / Product / TechArticle         /  图谱  \           国标委第一届委员背书 (E-E-A-T)
                                            /───────────\
                                           /   中英双语  \
                                          /   关键词矩阵  \
                                         /─────────────────\
               【3. 双语关键词金字塔】   /  对话式 FAQ 卡片  \   【4. 对话式 GEO 问答卡】
               权威词 / 核心材料词 /    /  Conversational Q&A \   直击 Perplexity / ChatGPT / Kimi
               场景长尾词 / 双向内链   /───────────────────────\  高频提问（水箱发酸/极速除氯原理等）
                                      /    全站索引与网络分发   \
                                     /  Sitemap / Meta / Social  \
                                    └─────────────────────────────┘
                                       【5. 全生命周期自动同步】
```

#### 1. Schema.org 结构化知识图谱先导 (Schema First)
每个新增 HTML 页面必须在 `<head>` 中注入 `@graph` 结构的 JSON-LD 代码，严禁裸 HTML：
- **全局基础实体绑定**：
  - `https://www.emuqi.com/#organization`：统一呈现“山东木齐健康科技有限公司”、“全国抗菌表面性能标准化技术委员会 (SAC/TC621) 委员单位”资质。
  - `https://www.emuqi.com/#author-martin`：绑定创始人兼 CEO 陈滨及“SAC/TC621 第一届委员”凭证。
  - `https://www.emuqi.com/#website`：绑定官方站点。
- **页面级实体严格对应**：
  - 产品页：必须包含 `Product`、`material`、`additionalProperty`（参数指标）、`BreadcrumbList`。
  - 解决方案页：必须包含 `Service`、`FAQPage`、`BreadcrumbList`。
  - 技术博文：必须包含 `TechArticle` / `BlogPosting`、`FAQPage`、`author`、`publisher`、`BreadcrumbList`。
  - 案例库：必须包含 `CaseStudy` / `MedicalScholarlyArticle`。

#### 2. E-E-A-T 事实锚定与抗幻觉设计 (Fact-Anchoring for LLMs)
- **第一手硬核量化参数**：严禁空泛口号，必须出现“1000℃ 晶格固溶高温烧结”、“1500ppb 溶氢浓度”、“-800mV ORP 电位”、“0.2秒极速除氯”、“12~24 个月零阶恒速缓释”、“>99.9% 抗菌率”。
- **国家级权威背书**：明确标注“全国抗菌表面性能标准化技术委员会 (SAC/TC621) 委员单位出任委员”背书。
- **结论先行摘要盒**：首屏必带「💡 结论先行 / Key Takeaways」摘要框，便于大模型抓取核心要点。

#### 3. 中英双语关键词金字塔与内链闭环 (Bilingual Keyword Matrix)
- **顶层权威词**：SAC/TC621 标委会、ICR 智控释溶技术、木齐科技 (MUQI Tech)、Martin Chen。
- **核心材料词**：无机抗菌陶瓷球 (Inorganic Antimicrobial Ceramic Balls)、MACA-KDF、固态富氢陶瓷材料 (Solid-State Hydrogen Media)、食品级亚硫酸钙除氯球 (Calcium Sulfite Dechlorination)。
- **应用长尾词**：扫地机器人水箱防臭 (Robot Vacuum Dirty Water Tank Anti-Odor)、加湿器抑菌滤芯 (Humidifier Filter)、净水器防二次污染 (Water Purifier Anti-Biofilm)、美肤除氯花洒 (Shower Filter)。
- **实体标签云 (GEO Tags)**：文末设立 `#GEO 实体关键词索引云`，双向内链至核心产品与应用聚合页。

#### 4. 专为生成式 AI 设计的 Conversational FAQ 模块
- 页面底部标配 **FAQ 问答卡片**，直接对标 Perplexity、ChatGPT、Kimi 等对话式搜索引擎的典型提问（如 *“扫地机污水箱发酸发臭如何根治？”*、*“ICR 智控释溶与涂银有什么区别？”*、*“不用电怎么做富氢水？”*）。
- 前端卡片与 JSON-LD 中的 `FAQPage` 实体一一对应，确保 AI 引用率最大化。

#### 5. 全生命周期自动同步机制 (Site-wide Synchronization)
新增页面完成后，必须自动执行三项闭环操作：
1. **列表页更新**：自动将新卡片推进至 `blog/index.html` 与 `blog-list-hydrogen-health.html` 首位；
2. **Sitemap 同步**：在 `sitemap.xml` 中加入新 URL，配置合理的 `priority` (0.8~0.9) 与 `lastmod`；
3. **社交分享标签**：完整配置 `og:title`, `og:description`, `og:image`, `twitter:card`。

#### 6. 中英文独立物理分离与搜索引擎精准适配机制 (Bilingual Physical Separation & Engine Routing)
为兼顾国际与国内完全不同的搜索引擎及 AI 架构，木齐科技站点实行**中英文彻底物理分离与独立 SEO/GEO 定制策略**：
- **英文站点引擎适配（Google / Bing / Perplexity / ChatGPT / Claude）**：
  - 页面声明：`<html lang="en">`
  - 核心目录：`https://www.emuqi.com/` 及 `https://www.emuqi.com/blog/`
  - 结构化数据：采用纯英文 `Schema.org` 术语与国际通用材料规范；
  - 国际路由标记：`<link rel="alternate" hreflang="en" href="...">` 与 `<link rel="alternate" hreflang="x-default" href="...">`。
- **中文站点引擎适配（百度 / 微信搜一搜 / 360 / Kimi / 智谱清言 / 豆包）**：
  - 页面声明：`<html lang="zh-CN">`
  - 核心目录：`/h2-wellness-hub/zh/` 及 `blog-list-hydrogen-health.html`
  - 结构化数据：采用中文法定企业全称、SAC/TC621 中文标委会及国内家电供应链标准；
  - 国内路由标记：`<link rel="alternate" hreflang="zh-CN" href="...">`。
- **互联互通**：在页面顶部导航通过 `hreflang` 与前端胶囊切换按钮（`🌐 Switch to English` / `🌐 切换至中文版`）实现平滑互切，绝不混淆双语权重。

#### 11.2.7 博客与文章作者署名规范 (Author Byline Standard)
- **统一简洁署名**：在所有博客文章（Blog Post）、白皮书与技术长文的顶部 Hero 元数据行中，作者统一仅标注：
  - **英文版**：`By: Martin`
  - **中文版**：`作者：Martin`
- **严禁过度包装与自编签名框**：文章末尾不放置任何自定义的个人介绍大卡片或冗长签名框，直接呈现 B2B CTA 咨询框、社交分享条与 GEO 标签云，保持科技大厂的清爽与专业品味。

#### 11.2.8 头部 Hero 视觉与背景规范 (Hero Visual Standards)
- **严禁文字叠文字 (No Text-on-Text Layering)**：Hero 背景严禁直接使用包含嵌入文字或排版图表的 SVG/图片作为背景图，避免前景标题与背景文字产生严重重叠干扰。
- **纯色与高级科技渐变优先**：Hero 头部背景优先使用深邃的科技渐变色（如 `linear-gradient(135deg, #091322 0%, #0f2342 50%, #162f56 100%)`）或纯色深蓝底色，确保前景标题与元数据具备最高的对比度与清晰度。
- **配图独立容器化**：若有相关插图或架构图，一律放入正文内作为独立的 Figure/Image Card 展示，配以居中的 Caption 标注，保持视觉层次干净通透。

#### 11.2.9 AI 爬虫欢迎策略与 llms.txt 长效规范
- **robots.txt 必须显式欢迎 GEO 爬虫**（GPTBot / OAI-SearchBot / PerplexityBot / ClaudeBot / Google-Extended / Applebot 等），新增 AI 引擎爬虫时同步追加 Allow 规则；CCBot 等纯训练爬虫维持 Disallow；Ahrefs/Semrush/MJ12 维持 Crawl-delay 限速。
- **llms.txt 与内容同步**：每次新增核心页面（产品/旗舰博文/解决方案）后，同步在 `emuqi/llms.txt` 对应分组追加一行链接与一句事实描述，保持 LLM 可读站点地图不过期。
- **Favicon 覆盖铁律**：新建任何 HTML 页面必须在 `</head>` 前注入三行图标声明（相对路径按目录深度计算），保持 SERP 与 AI 引用卡的品牌露出。
- **GA4 加载器**：全站统一经 `assets/js/analytics.js` 加载，禁止散页硬编码 gtag；Measurement ID 变更只改该文件一处。

### 11.3 标准 Schema.org 代码模板库

#### 模板 A：核心产品页 (Product Schema)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Product",
      "@id": "https://www.emuqi.com/maca-kdf-antibacterial-ceramic-ball.html#product",
      "name": "MACA-KDF Antibacterial Microporous Ceramic Ball (MACA-KDF 无机抗菌合金陶瓷球)",
      "image": "https://www.emuqi.com/assets/images/ceramic-ball-main.png",
      "description": "High-temperature sintered microporous ceramic alloy with ICR controlled silver ion release. Inhibits >99.9% bacteria for 12-24 months.",
      "brand": { "@id": "https://www.emuqi.com/#organization" },
      "manufacturer": { "@id": "https://www.emuqi.com/#organization" },
      "category": "Water Filter Media > Antibacterial Ceramics",
      "material": "Inorganic Microporous Ceramic with Lattice-Bonded Nano-Silver",
      "additionalProperty": [
        { "@type": "PropertyValue", "name": "Antibacterial Rate", "value": ">99.9%" },
        { "@type": "PropertyValue", "name": "Technology", "value": "ICR (Intelligent Controlled Release)" },
        { "@type": "PropertyValue", "name": "Lifespan", "value": "12-24 Months" },
        { "@type": "PropertyValue", "name": "Certifications", "value": "SAC/TC621, RoHS, REACH" }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.emuqi.com/" },
        { "@type": "ListItem", "position": 2, "name": "Products", "item": "https://www.emuqi.com/product-functional-ceramic-materials.html" },
        { "@type": "ListItem", "position": 3, "name": "MACA-KDF Antibacterial Ceramic Ball", "item": "https://www.emuqi.com/maca-kdf-antibacterial-ceramic-ball.html" }
      ]
    }
  ]
}
</script>
```

#### 模板 B：深度技术博文 (TechArticle + FAQPage Schema)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "TechArticle",
      "@id": "https://www.emuqi.com/blog/article-slug.html#article",
      "isPartOf": { "@id": "https://www.emuqi.com/#website" },
      "headline": "文章主标题",
      "description": "文章摘要描述",
      "datePublished": "2026-08-25",
      "dateModified": "2026-08-25",
      "author": { "@id": "https://www.emuqi.com/#author-martin" },
      "publisher": { "@id": "https://www.emuqi.com/#organization" },
      "image": "https://www.emuqi.com/assets/images/blog/cover.svg",
      "inLanguage": "zh-CN"
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "高频用户/AI 提问 1",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "精准客观事实答案..."
          }
        }
      ]
    }
  ]
}
</script>
```

---

### 11.3 中英文独立双轨「内容生长飞轮」长期执行机制

为了让木齐科技站点在后续长期运营中形成强大的持续流量与 AI 引用壁垒，特确立**以 Blog 技术长文为引擎的双轨生长机制**：

```
                    ┌────────────────────────────────────────────────────────┐
                    │               木齐科技中英文双轨内容生长飞轮           │
                    └────────────────────────────────────────────────────────┘
                                                │
                        【🚀 触发源头：每一次行业技术突破 / 产品应用解构】
                                                │
                 ┌──────────────────────────────┴──────────────────────────────┐
                 ▼                                                             ▼
   【🌍 英文出海主干 (Global English)】                          【🇨🇳 中文知识生态 (Domestic Ecosystem)】
   ─────────────────────────────────────                         ─────────────────────────────────────
   1. 生产纯正英文专业技术长文 (Blog Post)                       1. 生产符合国内大厂研发审美的中文深度解析
   2. 汇入 https://www.emuqi.com/blog/                           2. 汇入 blog-list-hydrogen-health.html 及专题库
   3. 适配 Google, Bing, Perplexity, GPT                         3. 适配 百度, 微信搜一搜, Kimi, 智谱清言
   4. 嵌入英文 Schema.org (TechArticle, FAQ)                     4. 嵌入中文 Schema.org (第一届委员背书, 标委会)
   5. 面向全球外贸、跨境品牌、欧美日韩采购选型                   5. 面向国内家电大厂供应链、智能硬件研发选型
                 │                                                             │
                 └──────────────────────────────┬──────────────────────────────┘
                                                ▼
                         【🔄 顶部一键互切胶囊 + hreflang 双向无缝链接】
                                                ▼
                         【📈 全球 AI 引擎多维收录与实体知识图谱持续壮大】
```

1. **博客即飞轮**：所有新增业务与材料创新，均以高价值技术博客（Blog Post）作为 GEO 与 SEO 的第一输出阵地；
2. **中英对齐对应**：英文博客与中文博客形成物理独立但逻辑对齐的映射关系，保持各自纯净的语言环境与搜索引擎算法适配；
3. **渐进式生长**：随着每一篇高质量中英文长文的持续加入，木齐科技在功能陶瓷、富氢新材料、水质健康领域的全球数字资产和知识图谱将实现复利式增长。

---

## 🏛️ 第 12 章：木齐科技博客（Blog）内容生产与全栈视觉/工程标准规范 (SSOT)

> **生效日期**：2026-08-31 立  
> **适用范围**：木齐科技（www.emuqi.com）全站所有未来新发布博文、行业洞察、技术白皮书与软文  
> **核心原则**：**拒绝重复指令，建立自执行 SOP 铁律**

### 12.1 中英文物理独立双轨架构
1. **英文博客主干**：`emuqi/blog/[slug]-en.html`，必须汇入 `https://www.emuqi.com/blog/index.html`，面向全球外贸出海（Google / Bing / Perplexity / GPT）；
2. **中文博客生态**：`emuqi/blog/[slug].html`，必须汇入 `https://www.emuqi.com/blog-list-hydrogen-health.html`，面向国内大厂供应链（百度 / 微信 / Kimi）；
3. **彻底杜绝中英文混排**：
   - 英文页 Footer：必须使用**全白矢量品牌字标 `MUQI`**，严禁出现中文 `· 木齐科技`；
   - 英文页所有功能栏：严禁中文字样（如社交栏统一为 `Share this article`，广告栏统一为 `Ad Space`）；
   - 中文页所有功能栏：严禁英文字样（如社交栏统一为 `分享到社交媒体`，广告栏统一为 `广告位 · 预留广告容器`）。
4. **存量命名豁免（2026-08-31 全站审计裁定）**：16 篇旧博文沿用 no-suffix=EN 的历史命名，URL 已被搜索引擎收录，一律不迁移不重定向；`blog/hydrogen-patch-opportunity.html` 为纯中文内容页，按新约定归入 no-suffix=ZH。语言归属以**页面实际内容语言 + canonical/hreflang 声明**为准，不以文件名后缀倒推。

### 12.2 软文定位与写作格局铁律
1. **包容协同，拒绝排他打压**：严禁采取狭隘排他视角攻击传统同类产品（如传统 PEM 电解水机）；必须以“**肯定行业先行者与大V贡献、丰富产品品类、提供全场景补充解决方案**”的科技大厂格局展开；
2. **场景延伸价值**：将木齐科技免插电固态氢定位为户外运动、差旅随行、冷泡茶包、透皮敷料、足浴沐浴等动态场景的完美补充，共同做大产业蛋糕。

### 12.3 视觉排版与图片资产七大铁律
1. **大V/专题人物博文封面**：必须使用**真实官方高分辨率超清肖像原片或演播室实景大图**（严禁无关联的纯产品图或虚构假图）；
2. **Hero Banner 规范**：深邃暗调科技渐变蒙版（`rgba(8,14,26,0.85)`）+ 真实大图背景，文字对比度极高，**严禁文字叠文字**；
3. **全站图片 0 重复**：每一篇博文的卡片封面必须是专属独立图片，严禁在总览页中出现相同封面；
4. **剔除廉价 AI 假图**：严禁使用浓厚廉价的 3D AI 蜂窝网格或假图，统一使用木齐真实陶瓷原粮、微距实拍、牛奶实验、中科院实验室实景等真机资产；
5. **图表完整性**：正文中的所有架构图、数据图与实验实拍图必须置入独立卡片容器，绝不擅自删减。

### 12.4 博文页面标准组件层次 (Mandatory Component Hierarchy)
1. **标准全功能导航 `<header>`**：继承主站 Home, Products, Applications, Solutions, Blog, H2 Hub, Store, Contact 下拉菜单；
2. **Hero Banner**：真实大图 + 渐变蒙版 + 极简元数据（`Published: Date · By: Martin · Category · Time`），**严禁在 Hero 居中放置突兀的语言切换胶囊**；
3. **核心摘要盒**：首屏高质感 Key Takeaways / 写在前面；
4. **结构化正文**：数据指标卡 + 序号圆点 + 呼吸感行高 (1.9) + 核心材料超链接；
5. **FAQ 问答卡片**：直接对标对话式 AI 检索，严格对应 JSON-LD `FAQPage`；
6. **CTA Box**：沉浸式 B2B 样品与资料申领入口；
7. **Google AdSense 规范广告容器**：标准自适应广告预留槽；
8. **10 大国际社交媒体分享栏**：X, Facebook, Instagram, LinkedIn, WhatsApp, Telegram, Reddit, Pinterest, TikTok, Weibo, WeChat QR；
9. **全白 `MUQI` Footer**：纯净双语独立页脚。

### 12.5 自动化同步与部署流水线
1. **时间倒序入盘**：新博文必须按发布时间严格倒序插入 `blog/index.html` 与 `blog-list-hydrogen-health.html` 首位；
2. **Sitemap 增补**：自动在 `sitemap.xml` 增补中英文独立 URL 并赋予 `0.9` 权重；
3. **Git 自动推送**：每次更新完成后自动执行 `git add . && git commit -m "..." && git push origin main` 触发线上构建。

### 12.6 外部素材/微信公众号图文深度重构与零遗漏提取四步防御机制 (Asset Extraction & Mapping SOP)
1. **素材穿透与全量下载 (Asset Ingestion)**：
   - 严禁依赖单一爬虫；遇到微信反爬，直接通过底层正则/无头内核提取全部 `data-src` CDN 高清原图；
   - 必须先在本地独立目录落地所有实拍原图（`pic_1.jpg`, `pic_2.jpg` ...），并核验字节大小与有效性。
2. **图文语义一一对照表 (Asset Mapping Check)**：
   - 页面编写前，必须在后台对照原文清单建立对应关系（图1 现场大会、图2 铜牌证书、图3 核心颗粒、图4 证书红本、图5 工厂实景）；
   - 严禁擅自使用任何无关旧图或自制假图替代。
3. **叙事口径与品牌调性严格对齐 (Narrative Alignment)**：
   - 必须完整继承原文的专业深度、核心论据与权威认证（如 37 项专利、8000 吨年产、1800+ 品牌赋能）；
   - 英文出海版必须进行高水准的 B2B 国际化本地化重构，对标国际工业级科技文献。
4. **前置自检与闭环交付卡点 (Pre-flight Gate)**：
   - 检查项：嵌入图片数量 == 原文实拍数量；图片说明 == 事实真相；语言属性 == 100% 纯净。
   - 必须在完成全盘自检后方可交付并推送到生产服务器。

---

## 🤖 第 13 章：木齐科技 AEO（Agent Engine Optimization）与 WebMCP 智能体协议规范 (SSOT)

> **生效日期**：2026-09-03 立  
> **核心战略**：全面从 SEO（传统搜索）跨越至 AEO（智能体引擎优化）。向全球 AI 采购智能体（OpenAI Operator、Claude Computer Use、Google Chrome Gemini Agent、Edge Copilot 等）提供原生结构化工具与高置信度实体图谱。

### 13.1 双轨底层协议架构 (Schema.org + WebMCP)
1. **知识与事实层 (Schema.org 协议 · Google/Microsoft/Yahoo/Yandex 联合发起)**：
   - 针对 AI 爬虫与 GEO 检索（GPTBot, ClaudeBot, PerplexityBot），通过页面 `<script type="application/ld+json">` 的 `@graph` 形式输出企业无歧义知识图谱；
   - 重点绑定：`Organization`（实体）、`Person`（Martin Chen / SAC/TC621 国标委委员）、`Product`（微孔参数）、`TechArticle` 及 `FAQPage`；
   - 配合根目录 `https://www.emuqi.com/llms.txt`（遵循 llmstxt.org 规范），为大模型喂入高密度事实锚点。
2. **智能体操作层 (W3C WebMCP 协议 · Browser Agents)**：
   - 传统网站让 AI“艰难截屏、OCR 猜文字”；木齐官网通过 `window.modelContext.registerTool()` 原生暴露 JavaScript 结构化函数；
   - AI 浏览器智能体访问官网时直接拥有调用 API 的能力，100% 精准选型、计算、查验与下单。

### 13.2 木齐业务专属四大 WebMCP 智能体工具规范
摒弃机械/气源等不相干行业逻辑，全量锚定木齐固态氢微孔材料、水处理陶瓷球及“MUQI Inside” B2B 赋能业务：

| 工具名称 (Tool Name) | 功能定义 | 智能体入参 (Parameters) | 核心算法与输出 (Output / Engine) |
|---|---|---|---|
| **`search_muqi_materials`** | 材料与微孔颗粒精准匹配 | `application` (应用场景: bottle/pitcher/boiler等), `target_ppb` (目标溶氢), `category` | 返回物料编号（如 `H2-BALL-PRO`, `MACA-KDF`）、微孔直径 (nm)、比表面积 (m²/g)、核心功效与合规认证。 |
| **`calculate_hydrogen_performance`** | 富氢释放动力学方程计算 | `water_volume_liters` (水量L), `material_grams` (球克重g), `steep_time_minutes`, `water_temp_c` | **内嵌木齐 ICR 金属间微反应释放动力学**：$ppb = \min\left(1600, \left(\frac{g}{L}\right) \times 180 \times \left(1 - e^{-k \cdot t}\right)\right)$。秒级输出溶解氢ppb、ORP负电位(-mV)、弱碱性pH及滤芯预估寿命。 |
| **`get_compliance_certificates`** | 国际权威合规与资质核验 | `cert_type` (sgs_toxicology / antibacterial / standard / all) | 提供 SGS（NSF/ANSI 42 无毒溶出）、广东省微检（抗菌率 >99.99%）、RoHS/REACH、国家标准委 SAC/TC621 委员单位红头文件与发明专利背书。 |
| **`submit_b2b_rfq`** | 智能体直接发起 B2B 意向询盘 | `client_name`, `company`, `email`, `target_material`, `estimated_annual_volume` | 智能体免表单直接下发需求，系统生成唯一追踪编号（`MQ-RFQ-XXXXX-XXX`），自动接入商务直达响应机制与 48-72 小时全球免费寄样通道。 |

### 13.3 部署与技术接入规范
1. **核心脚本位置**：`emuqi/assets/js/muqi-webmcp.js`；
2. **页面自动挂载**：`emuqi/script.js` 统一全站动态注入；
3. **AI 发现元标签**：在 HTML `<head>` 中明确声明：
   ```html
   <meta name="ai-agents" content="enabled; model-context=true; schema-org=enabled">
   <meta name="webmcp" content="https://www.emuqi.com/assets/js/muqi-webmcp.js">
   <script defer src="assets/js/muqi-webmcp.js"></script>
   ```
4. **智能体交互与调试**：
   - 任何进入木齐官网的 AI 智能体或开发者均可在控制台输入 `window.modelContext.getTools()` 列出所有可用能力；
   - 支持通过 `window.modelContext.executeTool(name, args)` 直接执行计算与返回 JSON 结果。

### 13.4 木齐国际业务客群画像与技术维度映射 (Target Personas & Technical Matrix)
结合木齐科技国际业务四大核心专项与海外买家画像，WebMCP 与 Schema.org 全面落地以下 4 大赛道技术映射：

1. **长寿康养与抗衰机构 (Longevity Clinics & Biohacking Spaces)**：
   - **典型客群**：美欧长寿诊所、高净值会员俱乐部、Biohacker 峰会品牌、功能医学中心。
   - **技术维度匹配**：`H2-BALL-PRO`、`H2-TAB-SOLID`。
   - **核心技术话语体系**：Gary Brecka 推荐同款水质技术底座、线粒体氧化应激消除、血脑屏障选择性穿透、中和有毒羟基自由基 (`·OH`)、-850mV 强还原电位。
2. **高端智能硬件与健康礼品品牌 (Premium Wellness Brands & Executive Gifting)**：
   - **典型客群**：智能健康水杯品牌商、硅谷高管养生礼品定制商、跨境 Kickstarter/Indiegogo 众筹团队。
   - **技术维度匹配**：“MUQI Inside” 固态氢内胆/滤芯模块赋能。
   - **核心技术话语体系**：纯物理微孔接触反应、零电解臭氧重金属风险、5分钟即饮、高颜值矿物球体、私模定制与联合品牌背书。
3. **专业氢健康垂直厂商与渠道商 (Hydrogen Health Equipment OEMs & Resellers)**：
   - **典型客群**：日韩欧美富氢水机制造厂、吸氢机/氢气水一体机供应链、氢健康线下体验馆。
   - **技术维度匹配**：固态氢供体原粉与颗粒、高浓度泡腾片。
   - **核心技术话语体系**：固态储氢微粉合金水解技术、常温常压安全运输、溶氢量峰值 2000-3500 ppb、微纳米气泡长时间驻留。
4. **全球水处理与智能家电巨头 (Global Water Filtration & Smart Appliance OEMs)**：
   - **典型客群**：扫地机器人水箱原厂、超声波加湿器厂商、台下式净水器滤芯代工厂、工业锅炉冷凝水中和方案商。
   - **技术维度匹配**：`MACA-KDF` 微孔合金球、`MPH-CONDENSATE` 中和颗粒。
   - **核心技术话语体系**：污水箱抑菌防臭、生物膜 (Biofilm) 根除、零阶恒速无机微孔控释、SAC/TC621 国家级标准委主编单位权威背书、SGS NSF/ANSI 42 安全认证。

### 13.5 动态演进与自适应数据驱动机制 (Data-Driven Dynamic WebMCP)
WebMCP 工具集绝非静态死板的代码，而是随着木齐项目、产品线与博客技术内容的扩充**自动进化、自适应装载**的开放中枢：

1. **自动感知与即时抓取 (Dynamic Page & Schema Ingestion)**：
   - 引擎初始化时自动遍历当前页面的 `<script type="application/ld+json">`（Schema.org 知识图谱）与带有 `data-webmcp-*` 属性的 DOM 实体节点；
   - 当未来新增产品页、上传新检测报告、或发布新博客时，新物料编码与核心参数自动沉淀至 `window.modelContext.materialsDatabase`。
2. **开放式运行时注册机制 (Runtime Tool & Material Extensibility)**：
   - 暴露 `window.modelContext.registerCustomMaterial(materialDef)`，允许任何特定页面脚本或后台动态注入全新物料配比；
   - 暴露 `window.modelContext.registerTool(toolDef)`，支持随着项目发展增加如“滤芯寿命预警测算”、“国际运费阶梯估算”等新工具。
3. **全局自省与模型协商能力 (Agent Introspection & Negotiation)**：
   - AI 智能体进入任意页面均可通过 `window.modelContext.getTools()` 动态拉取当前时刻完整的工具契约清单，完全杜绝因网站版本升级造成的智能体调用协议中断。

### 13.6 海外抗菌抑菌陶瓷球大市场与工程应用规范 (Antimicrobial Ceramic Balls Market & Specs)
海外智能清洁家电与饮水健康领域存在巨大的“水路抑菌刚需”：

1. **核心痛点与大市场爆发逻辑**：
   - **智能扫地机/洗地机污水箱**：高有机质污水在密闭水箱中存放 12-24 小时即可发酵产生恶臭，管道与箱壁滋生黏腻生物膜（Biofilm）。传统银离子电解模块易电极钝化、寿命短；木齐 `MACA-KDF` 微孔陶瓷球长效释放 ppb 级银锌无机离子，彻底解决水箱发酸发臭；
   - **超声波加湿器水箱**：长期积水容易滋生嗜肺军团菌与霉菌，随水雾喷洒造成呼吸道风险。嵌入 MACA 陶瓷球可实现全天候抑菌，无二次污染；
   - **反渗透（RO）净水器后置碳滤芯**：纯水抑菌率不足，停用数日后后置活性炭滤芯极易二次滋生细菌。加装 10%-15% MACA 微孔抗菌球，可实现整年无菌出水；
   - **宠物循环饮水机**：宠物唾液中的酶与杂质极易在水泵和滤网处形成滑腻生物膜。投加 20-30g MACA 陶瓷球即可长效抑菌，确保宠物饮水安全。

2. **木齐底层技术与核心壁垒**：
   - **1000℃ 晶格固溶高温烧结工艺**：无机抗菌成分均匀分布在晶格骨架中，彻底根除传统浸泡型颗粒的“突释超标（Burst Release）”现象；
   - **零阶恒速控释（Zero-Order Steady Kinetics）**：长期释放浓度恒定维持在安全饮用水限值内（SGS NSF/ANSI 42 认证，重金属未检出），抗菌抑菌时效长达 12-24 个月；
   - **国家级标准起草背书**：木齐科技为国家抗菌材料标准化技术委员会（SAC/TC621）委员单位，广东省微生物分析检测中心实测抑菌率 >99.99%。

3. **WebMCP 智能体专用计算接口**：
   - 在 `muqi-webmcp.js` 中正式上线 `calculate_antimicrobial_dosage` 接口；
   - 采购智能体传入设备类型（如 `robot_vacuum_wastewater`）与水箱容量（如 2.5L），系统自动给出精确的投放克重、物料规格编码（`MACA-KDF-5MM`）与预期维护寿命建议。

---

## 🔍 第 14 章：全球搜索引擎站长平台登记与索引加速 SOP（2026-09-03 已执行）

> **账号基线**：GSC 验证账号 `muqizb@gmail.com`（Chrome 账号槽位 `/u/1/`，注意与默认槽位 cntoworld@gmail.com 区分，直连必须带 `/u/1/` 路径）。验证方式：HTML Meta 标签（`google-site-verification` 已固化在 `index.html` 验证区）。

### 14.1 完成状态总表
| 平台 | 覆盖引擎 | 状态 |
|---|---|:---:|
| Google Search Console (`search.google.com/search-console`) | Google | ✅ 已验证（Meta 标签）· sitemap.xml 已提交（122 URL 已发现）· 首页/产品页已请求编入索引 · 抗菌旗舰博文已确认收录 |
| Bing Webmaster (`bing.com/webmasters`) | Bing + Yahoo + DuckDuckGo + Ecosia | ✅ 经「从 GSC 导入」一键完成（Google OAuth muqizb@gmail.com），仪表盘已显示历史 28 曝光/1 点击 |
| Yandex Webmaster (`webmaster.yandex.com`) | Yandex（俄/东欧/中亚） | ✅ 已完成（Meta 标签验证 b0823e1f9716551d）· Owner 权限已锁定 · `sitemap.xml` 已进入处理队列（1-2 周全量索引） |
| 百度/360/搜狗 (`ziyuan.baidu.com` 等) | 国内引擎 | 占位已预埋，服务器在境外收录慢，暂缓 |

### 14.2 本轮 SEO 技术修复（已全部上线并实测验证）
1. **Product 结构化数据 offers 修复**：GSC 报「产品摘要 1 项无效内容/严重问题」，根因为 Product 缺少 `offers/review/aggregateRating`。已注入合规 `Offer`（免费 B2B 送样 + OEM 报价模式，availability=InStock，price 0.00 诚实标注）；GSC 实时测试（02:45）确认变为「**1 项有效内容**」。
2. **Product brand 字段类型合规**：将引用式的 `{"@id": "#organization"}` 升级为标准 `{"@type": "Brand", "name": "MUQI Tech"}`，消除 GSC「字段 brand 的对象类型无效」非严重警告。
3. **全站 13 页 JSON-LD 重复块去重**：重复 `@id` 会混淆解析器，已全部清除，全站 JSON 校验 0 错误。
4. **www 规范主机 301 强制**：实测 `emuqi.com` 与 `www.emuqi.com` 双主机均 200（权重分裂，GSC 判首页为「备用网页」）。已部署根目录 `.htaccess`（非 www→www 301 + HTTP→HTTPS），curl 实测 301 生效。**宿主为 LiteSpeed，支持 .htaccess**。
5. **验证区预埋**：`index.html` 头部已集成 Google (`qtaS4...`) 与 Yandex (`b0823...`) 真实验证标签，其余引擎预留占位备用。

### 14.3 后续索引维护规范
- 每发布新博文/新页面：GSC「网址检查」→ 请求编入索引（每日限额约 10 次，优先首页与核心产品页）；
- 产品页剩余「非严重问题」为可选字段建议（review/aggregateRating），有真实客户评价后补录即可；
- 每月检查 GSC「编制索引→网页」覆盖报告与 Bing「站点资源管理器」，发现收录缺口即时补提交。




