<div align="center">

# 🌐 EMUQI — AI-Native B2B Global Trade Infrastructure

**An AI-Native B2B global trade website & business automation project**  
*Built from scratch with AI Agents & Codex*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Build Status](https://img.shields.io/github/actions/workflow/status/Martin-MQtech/emuqi/deploy.yml?branch=main&label=GitHub%20Pages%20Deploy)](https://github.com/Martin-MQtech/emuqi/actions)
[![Built with Codex](https://img.shields.io/badge/Built_with-OpenAI_Codex_%26_AI_Agents-00A67E.svg)](https://openai.com)
[![Live Site](https://img.shields.io/badge/Live_Site-emuqi.com-f47b20.svg)](https://emuqi.com)

</div>

---

## 📌 Introduction & Project Identity

**EMUQI** (`emuqi.com`) is a real-world, production-grade **AI-Native B2B global trade website & automation project**. It represents a new paradigm of enterprise web architecture and operational automation designed specifically for international B2B commerce.

Entirely **built with AI Agents & OpenAI Codex**, this repository serves dual roles:
1. **Production Storefront & Portal**: The official multilingual digital presence for **Shandong MUQI Health Technology Co., Ltd.** (a national "Little Giant" enterprise in solid-state hydrogen materials & functional ceramic media).
2. **Global Trade Automation Suite**: An open-source suite of embedded B2B micro-tools and operational workflows created to bridge critical friction points in international trade.

---

## 💡 Why We Built This / The Builder Story

For decades, international trade has faced a persistent divide: **"Those who understand technology rarely understand complex commercial workflows, and those who master global trade cannot write code."**

### The Founder's Perspective
This project was conceived and created by a builder with a **Tsinghua MBA background and 20+ years of deep experience in global B2B trade**. 

In traditional enterprise environments:
- Off-the-shelf SaaS solutions are often rigid, bloated, and fail to address domain-specific B2B trade nuances.
- Developing custom software required heavy engineering teams and complex requirement handoffs that blurred domain intent.

### The Breakthrough with AI Agents
The advent of **OpenAI Codex and frontier AI Agents** opened a whole new universe. By pairing deep domain expertise with AI-assisted code generation:
- Domain experts can now **directly transform intricate B2B commercial logic into production-grade software** without traditional engineering bottlenecks.
- Micro-workflows that big software vendors ignore—such as container loading optimization, technical specification sheets, and context-aware multi-language outreach—can be rapidly prototyped, built, and deployed.

`emuqi` stands as a living testament to how non-developer domain experts, powered by AI Agents, can "hand-craft" robust, commercial-grade digital infrastructure from zero.

---

## 🛠️ Core Operational Scenarios & Micro-Tools

Big software suites often overlook the "small, messy, daily friction points" of physical B2B export workflows. `emuqi` integrates targeted micro-tools and automation scripts to solve these exact scenarios:

### 1. 📧 Context-Aware B2B Outreach Email Generation
- **Problem**: Cold outreach in international B2B trade fails when emails sound generic or AI-hallucinated.
- **Solution**: Embedded prompts and context-aware generation workflows that take verified product parameters (e.g., ICR hydrogen release half-life, water treatment specs) and target buyer profiles to generate precise, professional English outreach drafts.

### 2. 📦 Logistics & CBM (Cubic Meter) Calculator
- **Problem**: Freight calculation, pallet loading, and container space utilization (20GP / 40HQ) are critical during quote negotiation but tedious to recalculate manually for custom packaging.
- **Solution**: Lightweight client-side calculators for instant CBM volume, gross weight estimation, and container loading capacity planning.

### 3. 📄 Packaging Design & Product Spec Assistants
- **Problem**: B2B buyers require detailed technical data sheets (TDS), MSDS summaries, OEM packaging dimensions, and custom labeling specs.
- **Solution**: Automated metadata parser and spec sheet generator (`parse_emuqi.py` and dynamic hub components) that transform raw material specs into clean, customer-ready HTML/PDF handouts.

### 4. ⚡ High-Performance Static B2B Infrastructure
- **Problem**: Modern frontend frameworks add heavy JavaScript bundles that hurt loading speeds in overseas markets and slow down search engine indexing (SEO / GEO).
- **Solution**: Ultra-fast, zero-dependency HTML5 / CSS3 / Vanilla JS architecture featuring DM Sans & Inter typography, unified orange VI (`#f47b20`), and automated GitHub Actions + Hostinger dual-hosting CI/CD pipeline.

---

## 📂 Repository Structure

```text
emuqi/
├── index.html                             # Main B2B Portal Homepage
├── DESIGN.md                              # Single Source of Truth for Design System (V3.0)
├── README.md                              # Open-source project documentation
├── LICENSE                                # Standard MIT License
├── parse_emuqi.py                         # Automation script for page & spec parsing
├── style.css                              # Unified brand design stylesheet (#f47b20 VI)
├── script.js                              # Client-side interactive scripts
├── .github/workflows/deploy.yml           # Automated GitHub Pages CI/CD workflow
├── h2-wellness-hub/                       # B2B Resource Hub & Spec Library
├── blog/                                  # 16+ Deep technical & industry articles
├── assets/images/                         # 110+ Structured product & brand assets
└── *.html                                 # 18+ B2B application & product pages
```

---

## 🚀 Getting Started & Deployment

### Local Development
Because the core site is designed for maximum speed and portability with zero build step overhead, you can run it locally with any simple HTTP server:

```bash
# Clone the repository
git clone https://github.com/Martin-MQtech/emuqi.git
cd emuqi

# Start a local web server (Python 3)
python3 -m http.server 8000
```
Open `http://localhost:8000` in your browser.

### CI/CD & Deployment Pipeline
- **Primary Domain (`emuqi.com`)**: Automatically deployed via Hostinger Git integration upon push to `main`.
- **Mirror / Staging (`martin-mqtech.github.io/emuqi/`)**: Deployed via GitHub Actions workflow (`.github/workflows/deploy.yml`).

---

## 📜 License

This project is open-source software licensed under the [MIT License](LICENSE).

---

## 🌍 Our Vision

> **"Operating from a region with digital and payment barriers, we deeply value OpenAI’s mission to make frontier AI accessible to all of humanity. AI is the greatest equalizer for global builders. Despite local constraints, we are dedicated to supporting this vision through real-world open-source innovation, contributing to a more inclusive AI ecosystem whenever and however we can."**
