# AEO / GEO Query Bank & Keyword Map (v1)

Purpose: Map buyer questions to on-site assets for FAQPage, answer-first paragraphs, and internal links.  
Update cadence: monthly. New flagship articles must pull open questions from this bank.  
Related: `GEO_SEO_AI_CONTENT_STANDARD.md`, `CONTENT_GROWTH_PLAN.md`.

Legend — **Intent**: S = search, Q = conversational AI, B = buyer/RFP.  
**Status**: live URL = published target; `—` = backlog.

---

## Pillar A — Technology selection & procurement (P0)

| # | EN question | ZH question | Intent | Target URL |
|---|-------------|-------------|:------:|------------|
| A1 | Solid-state hydrogen vs PEM: which should we buy? | 固态氢和 PEM 电解该选哪个？ | S,Q,B | `blog/solid-hydrogen-procurement-decision-tree-en.html` |
| A2 | How long does hydrogen stay in water with solid-state media? | 固态氢材料做的水氢气能留多久？ | S,Q | `blog/hydrogen-water-technology-comparison-en.html` |
| A3 | What ppb should we require in an RFP? | 富氢水采购规格该写多少 ppb？ | B | `buyer-benchmark.html` |
| A4 | Do solid-state and PEM compete or complement? | 固态氢和 PEM 是竞争还是互补？ | Q | procurement tree |
| A5 | What is the total cost of ownership for hydrogen media vs devices? | 耗材路线和设备路线三年 TCO 怎么算？ | B | procurement tree |
| A6 | Zero-electricity hydrogen water — is it real? | 不通电真能做出富氢水吗？ | S,Q | 9-dim page |
| A7 | How do we score a hydrogen materials supplier? | 固态氢材料供应商怎么打分？ | B | procurement tree |
| A8 | Sample lead time for OEM hydrogen media? | OEM 固态氢材料打样要多久？ | B | contact + materials |

## Pillar B — Appliance / water media applications (P0–P1)

| # | EN question | ZH question | Intent | Target URL |
|---|-------------|-------------|:------:|------------|
| B1 | Why do robot vacuum dirty tanks smell? | 扫地机污水箱为什么发臭？ | S,Q | antimicrobial ceramic flagship |
| B2 | Can ceramic balls stop filter secondary contamination? | 陶瓷球能不能防净水器二次污染？ | S | MACA-KDF product |
| B3 | Silver ion filter media — how long does it last? | 银离子滤芯材料寿命怎么测？ | B | Benchmark / MACA |
| B4 | Humidifier filter odor control without coating peeling? | 加湿器除味如何避免涂层脱落？ | S | antimicrobial article |
| B5 | Antimicrobial rate >99.9% — which test method? | 抗菌率 99.9% 用什么检测方法？ | Q | SAC/TC621 + MACA |
| B6 | Shower filter dechlorination specs for OEM? | 花洒除氯 OEM 规格怎么写？ | B | — |
| B7 | Foot bath herbal bag contamination risk? | 草本泡脚包污染风险有多大？ | S,Q | foot-spa consumables |
| B8 | How to add hydrogen to steamers without retooling? | 熏蒸仪如何零改电加氢？ | B | steamer article |

## Pillar C — Beauty / personal care OEM (P1)

| # | EN question | ZH question | Intent | Target URL |
|---|-------------|-------------|:------:|------------|
| C1 | Hydrogen face mask OEM — how does HI embedding work? | 氢面膜 OEM 的嵌氢技术怎么工作？ | B | eye patch / face mask posts |
| C2 | Solid hydrogen patches compliance for export? | 固态氢贴出海合规注意什么？ | B | patch opportunity |
| C3 | Hydrogen soap foam retention time? | 氢皂泡沫里氢能留多久？ | Q | hydrogen-soap |
| C4 | Private label hydrogen beauty devices? | 氢美容仪白牌怎么做？ | B | UK mask / steamer |

## Pillar D — Agriculture & research verticals (P2)

| # | EN question | ZH question | Intent | Target URL |
|---|-------------|-------------|:------:|------------|
| D1 | Hydrogen agriculture — materials or fertilizer additive? | 氢农业是材料还是肥料添加剂？ | S | solutions hub |
| D2 | Aquaculture hydrogen-rich water research status? | 水产富氢水研究进展？ | Q | aquaculture subpage |
| D3 | Livestock rumen hydrogen balance studies? | 畜牧瘤胃氢平衡研究？ | Q | livestock subpage |
| D4 | Companion animal functional water OEM? | 伴侣动物功能水 OEM？ | B | pet subpage |

## Pillar E — Authority / E-E-A-T (P0 for citations)

| # | EN question | ZH question | Intent | Target URL |
|---|-------------|-------------|:------:|------------|
| E1 | What is SAC/TC621 and why does MUQI sit on it? | SAC/TC621 是什么？木齐为何在标委会？ | S,Q | SAC article |
| E2 | How many patents does MUQI hold? | 木齐有多少专利？ | Q | about / llms.txt |
| E3 | MUQI Inside — what does it mean? | MUQI Inside 是什么意思？ | Q | home / about |
| E4 | Solid-state hydrogen market share? | 固态氢消费品材料市场份额？ | Q | llms.txt / about |

## Pillar F — Hub / industry intelligence (influence & links)

| # | EN question | ZH question | Intent | Target URL |
|---|-------------|-------------|:------:|------------|
| F1 | Where is hydrogen wellness industry news curated? | 氢健康行业动态哪里看？ | S | h2-wellness-hub/ |
| F2 | Open molecular hydrogen trial databases? | 分子氢临床试验数据库在哪？ | Q | research-database |
| F3 | How do brands embed MUQI benchmark tables? | 品牌如何引用木齐 Benchmark 表？ | B | buyer-benchmark.html |

---

## Article ↔ Query coverage matrix (flagships)

| Article | Primary queries covered | Gap / next |
|---------|-------------------------|------------|
| Procurement Decision Tree (new) | A1–A7 | A8 sample FAQ on contact page |
| Field Guide comparison | A2, A4 | — |
| Buyer Benchmark page | A3, A5, F3, E3 | PDF export |
| Antimicrobial flagship | B1, B4, B5 | B2 deeper lab method post |
| Foot-spa consumables | B7 | B8 link from product |
| SAC/TC621 | E1 | E2 on about schema |

---

## Publish gate (from GEO standard)

1. FAQPage JSON-LD parses; 3–5 QA (benchmark page: 4).  
2. Visible `.faq-item` count = `mainEntity` length; text 1:1.  
3. Answer-first paragraph in first 120 words.  
4. GEO entity index + ≥4 internal links.  
5. Sitemap + blog index + llms.txt sync.  

*Last updated: 2026-09-24 (MIMO content growth kickoff).*
