import os, re

BASE_DIR = "/Users/martin/Documents/2026 BUSINESS MTRIX /20260721 MUQI 网站建设/emuqi"
BLOG_DIR = os.path.join(BASE_DIR, "blog")

chinese_articles = [
  {
    "slug": "antimicrobial-ceramic-balls-home-appliances-icr-technology.html",
    "date": "2026年8月25日",
    "tag": "旗舰长文",
    "title": "一颗不起眼的陶瓷球，凭什么成了家电与净水大厂的“秘密武器”？",
    "desc": "从加湿器发臭、扫地机发酸到净水二次污染：深度解析无机抗菌陶瓷球在智能家电全场景应用与木齐科技 ICR 智控释溶技术（全国抗菌表面标委会 SAC/TC621 委员单位背书）。",
    "img": "assets/images/blog/antimicrobial-ceramic-balls/maca-kdf-1.png"
  },
  {
    "slug": "gary-brecka-hydrogen-water-solid-state-breakthrough.html",
    "date": "2026年8月31日",
    "tag": "行业前沿",
    "title": "超越 Gary Brecka 氢水热潮：临床实证与免插电固态氢新材料革命",
    "desc": "Gary Brecka 引爆全球生物黑客与长寿圈！面对电解杯电极结垢、寿命短与重金属析出隐患，木齐科技固态氢新材料实现常温常压自发产生 1500ppb 富氢水与 -800mV 负电位，开启零电耗健康饮水新纪元。",
    "img": "assets/images/ceramic-ball-hero.png"
  },
  {
    "slug": "hydrogen-patch-opportunity-zh.html",
    "date": "2026年7月13日",
    "tag": "产业洞察",
    "title": "传统膏药敷贴大厂的下一个百亿风口：为什么是固态氢敷贴？",
    "desc": "2810亿大健康膏贴市场面临同质化内卷，固态氢敷贴凭借92.3%透皮渗透率与高浓度氢分子抗氧化靶向消炎，开辟大健康贴剂新品类赛道。",
    "img": "assets/images/hydrogen-patch/hydrogen-patch-1.jpg"
  },
  {
    "slug": "community-hydrogen-water-station-zh.html",
    "date": "2025年6月3日",
    "tag": "解决方案",
    "title": "木齐科技社区智能富氢水站：打造万物互联的社区健康饮水生态",
    "desc": "采用 PEM 纯水电解制氢技术与微纳米气泡高密度溶氢工艺，结合物联网智能运维，为现代社区提供高活性、抗氧化的健康直饮水解决方案。",
    "img": "assets/images/community-water-station_2.png"
  },
  {
    "slug": "muqi-hydrogen-eye-patch-zh.html",
    "date": "2025年5月20日",
    "tag": "个护抗衰",
    "title": "木齐固态氢眼贴：微纳米透皮释放技术赋能眼部深层抗氧抗衰",
    "desc": "92.3% 透皮释放效率，靶向清除眼周恶性自由基。4周临床测试显著改善眼周细纹与微循环，引领现代护肤品与眼部健康新趋势。",
    "img": "assets/images/eye-patch-product.jpg"
  },
  {
    "slug": "hydrogen-anti-tumor-zh.html",
    "date": "2025年3月29日",
    "tag": "医学科研",
    "title": "氢分子医学抗肿瘤与辅助治疗研究进展全景综述",
    "desc": "系统梳理氢分子在减轻放化疗毒副作用、靶向清除羟自由基及调节机体免疫微环境中的最新科研文献与临床实验进展。",
    "img": "assets/images/hydrogen-anti-tumor_2.jpg"
  },
  {
    "slug": "solid-hydrogen-donor-zh.html",
    "date": "2025年3月29日",
    "tag": "材料科学",
    "title": "固态氢供体在医药与功能性健康食品中的开发与应用",
    "desc": "深度解析金属镁基、微纳米单质硅基及珊瑚钙基等固态氢释放体系的化学动力学机理、生物利用度与食品安全标准。",
    "img": "assets/images/solid-hydrogen-donor_2.jpg"
  },
  {
    "slug": "cjbe-beauty-expo-zh.html",
    "date": "2025年3月11日",
    "tag": "展会动态",
    "title": "木齐科技携固态氢健康美妆新材料重磅亮相济南海峡美博会",
    "desc": "现场展示富氢随行杯、富氢水膜片、氢浴足浴片及功能性陶瓷滤芯等全系列 B2B OEM 解决方案，吸引众多美业品牌洽谈合作。",
    "img": "assets/images/cjbe-beauty-expo_2.jpg"
  },
  {
    "slug": "solid-hydrogen-dressings-zh.html",
    "date": "2025年3月5日",
    "tag": "医疗个护",
    "title": "固态氢功能敷料在卫生用品与个人护理领域的创新应用",
    "desc": "结合抗菌除臭与持续抗氧化释氢，为女性卫生巾、婴儿纸尿裤及医用创面敷料提供高附加值的功能性新材料升级方案。",
    "img": "assets/images/solid-hydrogen-dressings_2.png"
  },
  {
    "slug": "h2fizz-cup-zh.html",
    "date": "2025年3月8日",
    "tag": "消费硬件",
    "title": "H2fizz 富氢随行杯：免插电 3 秒自发产生 1500ppb 活性富氢水",
    "desc": "采用微矿物陶瓷活化技术，无需充电或更换电池，倒入饮用水即可源源不断产生弱碱性富氢负电位健康好水。",
    "img": "assets/images/h2fizz-cup_2.jpg"
  },
  {
    "slug": "deepseek-ceramics-zh.html",
    "date": "2025年2月13日",
    "tag": "AI新材料",
    "title": "DeepSeek 驱动木齐科技 AI 矿物陶瓷晶格算法与新材料研发",
    "desc": "利用前沿 AI 算法模型优化多孔陶瓷配方与 1000℃ 烧结工艺参数，实现 1500ppb 氢浓度与 -800mV 负电位的精准恒温释溶调控。",
    "img": "assets/images/deepseek-ceramics_2.png"
  },
  {
    "slug": "mq-hydrogen-ecosystem-zh.html",
    "date": "2025年2月15日",
    "tag": "生态战略",
    "title": "木齐科技全场景富氢健康新材料生态矩阵全景发布",
    "desc": "横跨家庭饮水、智能家电、农业富氢灌溉、水产健康养殖到个人护理，打造全产业链协同的固态氢功能材料赋能平台。",
    "img": "assets/images/mq-hydrogen-ecosystem_2.jpg"
  },
  {
    "slug": "ceramic-water-media-evolution-zh.html",
    "date": "2025年2月10日",
    "tag": "行业进化",
    "title": "功能陶瓷水处理滤料 20 年技术演进史与下一代材料展望",
    "desc": "从第一代单一矿化球、第二代极速除氯球，到第三代 MACA 抗菌合金与第四代固态富氢陶瓷，系统回顾水质健康材料的发展历程。",
    "img": "assets/images/ceramic-water-media-evolution_2.png"
  }
]

print(f"Total Chinese articles defined: {len(chinese_articles)}")
