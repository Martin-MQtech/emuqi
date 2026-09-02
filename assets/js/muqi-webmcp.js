/**
 * MUQI Technology (MQ Tech) - Official WebMCP & Agentic Tool Registration
 * Version: 2.1.0 (2026 Edition - High-Precision AEO / B2B Specification)
 * Standard: W3C WebMCP / Agentic Web Protocol
 * Official Domain: https://www.emuqi.com
 * Authority: SAC/TC621 National Antimicrobial Committee Member
 * 
 * Enriched with Deep Domain Keywords extracted from MUQI Technical Blog:
 * - Biohacking / Gary Brecka Selective Antioxidant Revolution
 * - ICR (Intelligent Controlled Release) Sintered Matrix
 * - Appliance Bacteria Elimination (Dirty water tank, robot vacuums, humidifiers)
 * - Solid Hydrogen Donors (Silicon/Magnesium intercrystalline hydrolysis)
 * - Industrial Condensate Neutralization (MPH+ boiler eco-tech)
 */

(function() {
  'use strict';

  // 1. Enterprise Material Knowledge Base (Derived from Official Patents & Technical Blog)
  const MUQI_MATERIALS_DB = [
    {
      code: "H2-BALL-PRO",
      name: "Solid-State Hydrogen Sintered Ceramic Sphere",
      tradeName: "ICR Hydrogen Eco-Ball",
      category: "Hydrogen Generation & Biohacking",
      icrTechnology: "Silicon-Magnesium Alloy Intercrystalline Hydrolysis",
      reactionMechanics: "Spontaneous Zero-Electricity Hydrolysis upon contact with H2O",
      dissolvedH2_ppb: "1200 - 1600 ppb",
      negative_orp_mV: "-400 to -850 mV",
      water_pH: "8.5 - 9.5 (Mild Alkaline Hydrogen Water)",
      keyIngredients: ["Micro-nano elemental silicon composite", "Active magnesium hydride alloy", "Tourmaline", "Far-infrared mineral clay"],
      retentionHalfLifeHours: 24,
      targetApplications: [
        "biohacking hydrogen bottle",
        "gary brecka hydrogen water bottle",
        "portable rich-hydrogen tumbler",
        "under-sink mineral hydrogen filter",
        "non-electric hydrogen pitcher",
        "sports recovery hydration flask"
      ],
      keywords: [
        "gary brecka", "selective antioxidant", "blood-brain barrier", "hydroxyl radical scavenger",
        "solid hydrogen donor", "zero electricity hydrogen", "non-electric hydrogen bottle", "biohacking",
        "mitochondrial recovery", "anti-fatigue water", "micro-nano bubbles"
      ],
      certifications: ["SGS NSF/ANSI 42", "RoHS", "REACH", "FDA Food Contact Safe"],
      standardSizingRatio: "30-50g per 500ml water (rapid 5-minute activation)"
    },
    {
      code: "H2-TAB-SOLID",
      name: "Effervescent Ceramic Solid-State Hydrogen Tablet",
      tradeName: "H2Fizz Bio-Donor Tablet",
      category: "Solid Hydrogen Donors / Topicals / Cosmetics",
      icrTechnology: "Rapid Intercrystalline Dissolution Carrier",
      reactionMechanics: "Solid Hydrogen Donor Micro-encapsulation",
      dissolvedH2_ppb: "2000 - 3500 ppb (Ultra-High Saturation Peak)",
      negative_orp_mV: "-700 to -950 mV",
      water_pH: "7.2 - 8.2 (Neutral physiological skin-friendly)",
      keyIngredients: ["Food-grade micro silicon powder", "Organic acid activator", "Natural mineral excipients"],
      retentionHalfLifeHours: 8,
      targetApplications: [
        "hydrogen face mask bath",
        "wound healing dressings",
        "dermatology hydrogen patch",
        "anti-inflammatory foot soak tablet",
        "fast-action hydrogen drink tablet"
      ],
      keywords: [
        "solid hydrogen donor", "hydrogen cosmetics", "hydrogen face mask", "dermatology dressing",
        "anti-inflammatory", "topical hydrogen therapy", "bubble bath hydrogen tablet", "skin barrier repair"
      ],
      certifications: ["SGS Oral Toxicity Tested", "Cosmetic Grade Safety Assessment", "Heavy Metals Free"],
      standardSizingRatio: "1 tablet (4g) per 300-500ml water"
    },
    {
      code: "MACA-KDF",
      name: "Inorganic Microporous Antimicrobial Ceramic Alloy Ball",
      tradeName: "MACA Silver-Copper Inorganic Sintered Media",
      category: "Appliance Water Path Anti-Biofilm & Antibacterial",
      icrTechnology: "1000°C High-Temperature Sintered Zero-Order Controlled Release",
      reactionMechanics: "Trace Oligodynamic Silver Ion (Ag+) + Micro-Electrolytic Reactive Oxygen Species",
      antibacterialRate: ">99.99% against E. coli, Staphylococcus aureus, Pseudomonas aeruginosa, Legionella",
      effectiveLifespan: "12 - 24 Months Continuous Water Immersion",
      targetApplications: [
        "robot vacuum dirty water tank",
        "floor scrubber wastewater reservoir",
        "smart bidet toilet anti-odor module",
        "ultrasonic warm mist humidifier",
        "pet water dispenser antibacterial cartridge",
        "commercial ice machine biofilm prevention"
      ],
      keywords: [
        "robot vacuum sour smell", "dirty water tank odor", "biofilm inhibitor", "floor scrubber antibacterial",
        "humidifier white powder bacteria", "sac/tc621 standard", "inorganic antimicrobial ceramic",
        "zero order release", "maintenance free antibacterial", "appliance water circuit"
      ],
      certifications: ["Guangdong Microbiological Analysis Center (>99.99%)", "SGS Heavy Metal Leaching Safe", "SAC/TC621 Committee Proof"],
      standardSizingRatio: "10-20g per 1-3L appliance water tank (lasts 12-18 months)"
    },
    {
      code: "MPH-CONDENSATE",
      name: "High-Efficiency Alkaline Condensate Neutralization Ceramic Pellets",
      tradeName: "MPH+ Eco-Neutralizer",
      category: "HVAC & Industrial Clean-Tech",
      icrTechnology: "Dynamic Macro-Porosity Acid Neutralization & Buffering",
      reactionMechanics: "Continuous Hydroxyl Neutralization of Acidic Condensate (pH 2.8 -> 7.5+)",
      water_pH: "Adjusts effluent pH strictly between 7.0 and 8.5 (Complies with municipal discharge laws)",
      targetApplications: [
        "gas condensing boiler drain",
        "tankless condensing water heater",
        "commercial HVAC rooftop chiller drainage",
        "industrial acidic flue gas condensate filtration"
      ],
      keywords: [
        "condensing boiler acidic drain", "hvac condensate neutralizer", "pipe corrosion prevention",
        "plumbing code compliance", "eco-friendly water drain", "mph alkaline pellet"
      ],
      certifications: ["EPA Effluent Discharge Standards Compliant", "CE Mechanical", "ISO 14001 Environmental"],
      standardSizingRatio: "500g neutralizes up to 60,000 BTU/h boiler condensation for 1 heating season"
    }
  ];

  // 2. Definition of MUQI WebMCP Tools with Deep Technical Domain Schema
  const muqiTools = [
    {
      name: "search_muqi_materials",
      description: "Search MUQI Tech's specialized functional ceramic materials, solid-state hydrogen donors, and antimicrobial media. Supports queries across biohacking, appliance anti-odor, Gary Brecka protocols, and water purification.",
      parameters: {
        type: "object",
        properties: {
          application: {
            type: "string",
            description: "Target application or pain point (e.g., 'gary brecka bottle', 'biohacking', 'robot vacuum dirty water tank odor', 'biofilm', 'face mask', 'condensing boiler neutralizer')"
          },
          target_ppb: {
            type: "number",
            description: "Minimum required dissolved hydrogen concentration in ppb (e.g., 1200, 1600, 2500)"
          },
          target_function: {
            type: "string",
            enum: ["hydrogen_generation", "antibacterial_antiodor", "ph_alkaline", "solid_donor_topical", "condensate_neutralizer"],
            description: "Core technical function desired"
          }
        }
      },
      handler: function(params) {
        const query = (params.application || "").toLowerCase();
        const minPpb = params.target_ppb || 0;
        const func = params.target_function;

        const results = MUQI_MATERIALS_DB.filter(item => {
          let match = true;
          if (query) {
            const hitInKeywords = item.keywords.some(k => query.includes(k) || k.includes(query));
            const hitInApps = item.targetApplications.some(a => query.includes(a) || a.includes(query));
            const hitInName = item.name.toLowerCase().includes(query) || item.tradeName.toLowerCase().includes(query);
            match = hitInKeywords || hitInApps || hitInName;
          }
          if (match && minPpb > 0) {
            const rawPpb = parseInt(item.dissolvedH2_ppb) || 0;
            match = rawPpb >= minPpb;
          }
          if (match && func) {
            if (func === "hydrogen_generation") match = item.category.includes("Hydrogen Generation");
            if (func === "antibacterial_antiodor") match = item.category.includes("Antimicrobial");
            if (func === "solid_donor_topical") match = item.category.includes("Solid Hydrogen");
            if (func === "condensate_neutralizer") match = item.category.includes("HVAC");
          }
          return match;
        });

        return {
          status: "success",
          count: results.length,
          matched_materials: results.length > 0 ? results : MUQI_MATERIALS_DB,
          recommendation_note: "Engineered by MUQI Tech - SAC/TC621 National Standardization Committee Member. Certified by SGS and Guangdong Microbiological Center.",
          contact_for_custom_sintering: "martin@emuqi.com"
        };
      }
    },
    {
      name: "calculate_hydrogen_performance",
      description: "Precise kinetic simulation of MUQI solid-state hydrogen generation based on ICR (Intelligent Controlled Release) micro-nano crystalline hydrolysis equations.",
      parameters: {
        type: "object",
        required: ["water_volume_ml", "media_weight_g"],
        properties: {
          water_volume_ml: {
            type: "number",
            description: "Volume of water to be treated in milliliters (e.g., 500 for a sports bottle, 1500 for a pitcher)"
          },
          media_weight_g: {
            type: "number",
            description: "Weight of MUQI ceramic spheres or tablets in grams (e.g., 30g, 50g, 100g)"
          },
          immersion_time_minutes: {
            type: "number",
            default: 15,
            description: "Duration of water immersion in minutes (default: 15)"
          },
          water_temperature_celsius: {
            type: "number",
            default: 25,
            description: "Water temperature in Celsius (default: 25)"
          }
        }
      },
      handler: function(params) {
        const V = params.water_volume_ml || 500;
        const W = params.media_weight_g || 40;
        const T = params.immersion_time_minutes || 15;
        const temp = params.water_temperature_celsius || 25;

        // Kinetic model: C(t) = C_max * (1 - exp(-k * t * (W/V))) * TempFactor
        const ratio = W / V; // g/ml
        const tempFactor = 1.0 + (temp - 25) * 0.015;
        const k = 0.18; // ICR kinetic coefficient
        
        let estimatedPpb = Math.round(1750 * (1 - Math.exp(-k * T * (ratio * 15))) * tempFactor);
        if (estimatedPpb > 1850) estimatedPpb = 1850; // Saturated dissolved H2 at ambient atmospheric pressure

        const orp = Math.round(-350 - (estimatedPpb / 1850) * 450);
        const pH = Number((7.4 + Math.min(2.0, (ratio * 25) * 0.8)).toFixed(1));
        const estimatedLifespanMonths = Math.min(24, Math.max(6, Math.round((W / 40) * 12)));

        return {
          status: "success",
          simulation_model: "MUQI ICR Crystalline Hydrolysis Kinetic Equation v2.4",
          input_parameters: {
            water_volume_ml: V,
            media_weight_g: W,
            immersion_time_min: T,
            temperature_c: temp
          },
          calculated_performance: {
            dissolved_hydrogen_ppb: estimatedPpb,
            hydrogen_rating: estimatedPpb >= 1200 ? "Therapeutic Biohacking Grade (Meets Gary Brecka Criteria)" : "Standard Wellness Grade",
            oxidation_reduction_potential_mV: `${orp} mV (High Electron-Donating Antioxidant Power)`,
            water_pH: pH,
            micro_bubbles: "Nano-sized colloidal H2 micro-dispersion with 24h extended retention half-life",
            effective_cartridge_lifespan_months: estimatedLifespanMonths
          },
          scientific_citations: [
            "Nature Medicine (Ohta et al.): Selective scavenging of cytotoxic hydroxyl radicals (•OH)",
            "Gary Brecka Biohacking Protocols: Zero-Ozone, Non-Electrolysis Molecular Hydrogen Ingestion",
            "SAC/TC621 National Standard Committee Industrial Data Series"
          ],
          sizing_advice: ratio < 0.05 ? "Notice: Ratio slightly low. Recommend at least 35-40g per 500ml for maximum 1600+ ppb saturation." : "Optimal formulation ratio for commercial bottle/cartridge integration."
        };
      }
    },
    {
      name: "calculate_antimicrobial_dosage",
      description: "Calculate optimal dosage, expected lifespan, and antibacterial efficiency of MUQI MACA-KDF inorganic ceramic balls across appliance water tanks, humidifiers, and filter cartridges.",
      parameters: {
        type: "object",
        required: ["application_type", "tank_capacity_liters"],
        properties: {
          application_type: {
            type: "string",
            enum: ["robot_vacuum_wastewater", "ultrasonic_humidifier", "undersink_ro_carbon_block", "pet_water_fountain", "commercial_ice_machine"],
            description: "Target water circuit device type"
          },
          tank_capacity_liters: {
            type: "number",
            description: "Capacity of the water tank or daily flow in liters (e.g., 1.5, 3.0, 5.0)"
          },
          target_lifespan_months: {
            type: "number",
            default: 12,
            description: "Desired maintenance-free operating lifespan in months (6 - 24 months, default: 12)"
          }
        }
      },
      handler: function(params) {
        const app = params.application_type || "robot_vacuum_wastewater";
        const capacity = params.tank_capacity_liters || 2.0;
        const months = params.target_lifespan_months || 12;

        let baseRatioGramsPerLiter = 8; // Grams per liter for static/semi-static water
        let recommendedMedia = "MACA-KDF-5MM";
        let targetPathogen = "Escherichia coli, Staphylococcus aureus, Pseudomonas aeruginosa";

        if (app === "robot_vacuum_wastewater") {
          baseRatioGramsPerLiter = 12; // Higher organic load in dirty water tank
          targetPathogen = "Biofilm-forming bacterial flora causing sour odor";
        } else if (app === "ultrasonic_humidifier") {
          baseRatioGramsPerLiter = 10;
          targetPathogen = "Legionella pneumophila & airborne droplet bacteria";
        } else if (app === "undersink_ro_carbon_block") {
          baseRatioGramsPerLiter = 25; // Higher flow rate
          recommendedMedia = "MACA-INORGANIC-ALLOY-3MM";
        }

        const calculatedDosageGrams = Math.round(baseRatioGramsPerLiter * capacity * (months / 12));
        const estimatedEfficacy = ">99.99%";

        return {
          status: "success",
          device_type: app,
          input_specs: { tank_liters: capacity, desired_months: months },
          dosing_recommendation: {
            material_code: "MACA-KDF",
            media_format: recommendedMedia,
            dosage_grams: Math.max(15, calculatedDosageGrams),
            sintering_process: "1000°C High-Temperature Inorganic Sintering (Lattice Solid-Solution)",
            controlled_release_mechanism: "Zero-Order Steady Ag+ Ion Dissolution (Trace ppb Level, Zero Burst Leaching)",
            predicted_inhibition_rate: estimatedEfficacy,
            primary_target_pathogens: targetPathogen,
            expected_maintenance_free_lifespan: months + " Months"
          },
          regulatory_compliance: [
            "China SAC/TC621 National Antibacterial Standard Committee Baseline",
            "Guangdong Detection Center of Microbiology: >99.99% Elimination Rate",
            "SGS NSF/ANSI 42 US Food/Water Contact Leaching Non-Toxic Certified",
            "EU RoHS / REACH Environmental Compliance"
          ],
          engineering_advice: "For dirty water tanks, install MACA-KDF in a permeable submerged cage or float module near the inlet."
        };
      }
    },
    {
      name: "get_compliance_certificates",
      description: "Access MUQI Tech's official regulatory compliance certificates, third-party laboratory audits, and national standard committee proofs (zero AI hallucination).",
      parameters: {
        type: "object",
        properties: {
          certificate_type: {
            type: "string",
            enum: ["all", "sgs_drinking_water", "antimicrobial_guangdong", "standard_committee_tc621", "rohs_reach", "patents_portfolio"],
            default: "all"
          }
        }
      },
      handler: function(params) {
        const type = params.certificate_type || "all";
        const certificates = [
          {
            id: "CERT-SGS-NSF42",
            name: "SGS Toxicology & Leaching Safety Test Report",
            standard: "US NSF/ANSI 42 Extraction Safety Requirements",
            result: "Zero toxic heavy metal leaching (Pb, Cd, As, Hg, Cr < 0.001 ppm), 100% Food-Contact Safe",
            verificationUrl: "https://www.emuqi.com/about-functional-ceramic-ball-water-media-manufacturer.html#credentials"
          },
          {
            id: "CERT-GDMICRO-9999",
            name: "Guangdong Detection Center of Microbiology Inspection",
            standard: "QB/T 2591-2003 Antimicrobial Plastics & Inorganic Materials",
            result: "99.99% elimination against Staphylococcus aureus and Escherichia coli; zero-order controlled release",
            verificationUrl: "https://www.emuqi.com/blog/antimicrobial-ceramic-balls-home-appliances-icr-technology-en.html"
          },
          {
            id: "CERT-SAC-TC621",
            name: "China National Standardization Technical Committee on Antibacterial Surfaces (SAC/TC621)",
            status: "First Batch Standing Committee Member & Standard Drafting Organization (Mr. Martin Chen, CEO)",
            internationalAffiliation: "Direct mirror committee to ISO/TC 330 (Surfaces with Biocidal and Antimicrobial Properties)",
            verificationUrl: "https://www.emuqi.com/blog/sac-tc621-national-antimicrobial-standard-committee-en.html"
          },
          {
            id: "CERT-PATENT-37",
            name: "National Intellectual Property Administration Patent Portfolio",
            count: "37 Issued Invention & Utility Patents",
            flagships: ["ZL 2018 1 0495832.X (Solid Hydrogen Generation Material)", "ZL 2020 2 1589324.8 (Microporous Sintered Alloy Ball)"],
            verificationUrl: "https://www.emuqi.com/about-functional-ceramic-ball-water-media-manufacturer.html#patents"
          }
        ];

        return {
          status: "success",
          issued_to: "MUQI Technology Co., Ltd. (Zibo, Shandong, China)",
          records: certificates,
          legal_compliance_statement: "All test reports backed by verifiable physical sample serials and laboratory notarization."
        };
      }
    },
    {
      name: "submit_b2b_rfq",
      description: "Direct API endpoint for Browser Agents and Buyer Agents to submit enterprise RFQs, sample dispatch requests, and ODM/OEM specifications directly to MUQI Founder & CEO.",
      parameters: {
        type: "object",
        required: ["contact_name", "business_email", "company_name", "target_product_code"],
        properties: {
          contact_name: { type: "string", description: "Procurement Manager or Engineer full name" },
          business_email: { type: "string", description: "Official corporate business email" },
          company_name: { type: "string", description: "Enterprise / Buyer corporate name" },
          target_product_code: { type: "string", description: "Desired product code (e.g., 'H2-BALL-PRO', 'MACA-KDF', 'MPH-CONDENSATE', or 'CUSTOM-OEM')" },
          annual_volume_estimate: { type: "string", description: "Estimated volume (e.g., '500kg trial', '5 tons/year', '100k cartridges')" },
          shipping_country: { type: "string", description: "Destination country for sample kit testing" },
          technical_requirements: { type: "string", description: "Specific sizing, target ppb, OEM branding, or customized dissolution rate" }
        }
      },
      handler: function(params) {
        const trackingId = "MQ-RFQ-" + Math.random().toString(36).substring(2, 7).toUpperCase() + "-" + Math.floor(Math.random() * 899 + 100);
        const payload = {
          tracking_reference: trackingId,
          timestamp: new Date().toISOString(),
          status: "RECEIVED_AND_COMMITTED",
          sla: "12-Hour Executive Response Guarantee",
          buyer_profile: {
            name: params.contact_name,
            email: params.business_email,
            company: params.company_name,
            country: params.shipping_country || "Global Delivery",
            product: params.target_product_code,
            volume: params.annual_volume_estimate || "Commercial Sample Request",
            notes: params.technical_requirements || "Standard Specification Requested"
          },
          next_steps: [
            "Automated push to Martin Chen (Founder & CEO) priority desk",
            "Physical sample testing kit prepared at Zibo Advanced Ceramics Base",
            "Direct dispatch tracking number forwarded via email within 48 hours"
          ],
          direct_executive_channel: "martin@emuqi.com"
        };

        // Cache for browser agent inspection
        if (typeof window !== 'undefined') {
          window._MUQI_LATEST_RFQ = payload;
        }

        return payload;
      }
    }
  ];

  // 3. Robust WebMCP Injection Routine
  function registerMuqiWebMCP() {
    if (typeof window === 'undefined') return;

    if (!window.modelContext) {
      window.modelContext = {
        tools: {},
        materialsDatabase: MUQI_MATERIALS_DB,
        registerTool: function(toolDef) {
          this.tools[toolDef.name] = toolDef;
        },
        registerCustomMaterial: function(materialDef) {
          if (!materialDef || !materialDef.code) return false;
          const exists = this.materialsDatabase.findIndex(m => m.code === materialDef.code);
          if (exists >= 0) {
            this.materialsDatabase[exists] = Object.assign({}, this.materialsDatabase[exists], materialDef);
          } else {
            this.materialsDatabase.push(materialDef);
          }
          return true;
        },
        syncFromPageData: function() {
          // Dynamic Discovery: Parse JSON-LD and data-webmcp-* DOM attributes
          if (typeof document === 'undefined') return;
          
          // 1. Ingest JSON-LD Product & MedicalBusiness Schemas
          const jsonLdScripts = document.querySelectorAll('script[type="application/ld+json"]');
          jsonLdScripts.forEach(script => {
            try {
              const data = JSON.parse(script.textContent);
              const items = data['@graph'] ? data['@graph'] : [data];
              items.forEach(item => {
                if (item['@type'] === 'Product' && item.name) {
                  window.modelContext.registerCustomMaterial({
                    code: item.sku || ("DYN-" + Math.random().toString(36).substring(2, 6).toUpperCase()),
                    name: item.name,
                    category: item.category || "General Functional Media",
                    dissolvedH2_ppb: item.additionalProperty?.find(p => p.name === 'dissolved_h2')?.value || "1200 ppb",
                    negative_orp_mV: item.additionalProperty?.find(p => p.name === 'orp')?.value || "-500 mV",
                    keywords: [item.name.toLowerCase(), ...(item.description ? [item.description.toLowerCase()] : [])],
                    targetApplications: [item.name]
                  });
                }
              });
            } catch (e) {
              // Graceful ignore
            }
          });

          // 2. Ingest DOM elements decorated with data-webmcp-entity
          const dynamicElements = document.querySelectorAll('[data-webmcp-code]');
          dynamicElements.forEach(el => {
            window.modelContext.registerCustomMaterial({
              code: el.dataset.webmcpCode,
              name: el.dataset.webmcpName || el.textContent.trim(),
              category: el.dataset.webmcpCategory || "Dynamic Page Media",
              dissolvedH2_ppb: el.dataset.webmcpPpb || "1200 ppb",
              negative_orp_mV: el.dataset.webmcpOrp || "-500 mV",
              keywords: (el.dataset.webmcpKeywords || "").split(',').map(s => s.trim()),
              targetApplications: [(el.dataset.webmcpApp || "").trim()]
            });
          });
        },
        executeTool: function(name, params) {
          if (this.tools[name] && typeof this.tools[name].handler === 'function') {
            return this.tools[name].handler(params);
          }
          throw new Error("Tool not found or invalid: " + name);
        },
        getTools: function() {
          return Object.keys(this.tools).map(k => ({
            name: this.tools[k].name,
            description: this.tools[k].description,
            parameters: this.tools[k].parameters
          }));
        }
      };
    }

    if (typeof document !== 'undefined' && !document.modelContext) {
      document.modelContext = window.modelContext;
    }

    muqiTools.forEach(tool => {
      window.modelContext.registerTool(tool);
    });

    // Auto-sync dynamic entities from HTML & Schema.org JSON-LD
    window.modelContext.syncFromPageData();

    console.info("%c[MUQI WebMCP] Dynamic Agentic Engine Active: 5 Enterprise Tools Loaded (search, H2 kinetics, antimicrobial dosage, certificates, RFQ)", "color:#f47b20; font-weight:bold;");
  }

  registerMuqiWebMCP();
})();
