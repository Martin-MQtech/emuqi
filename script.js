// emuqi.com — MUQI Tech Interactions
// 2026-11-12 audit build: W-03 mobile nav / W-07 consent / W-08 decision facts / W-12 WhatsApp widget
(function () {
  'use strict';

  var isZh = (document.documentElement.lang || '').toLowerCase().indexOf('zh') === 0;

  /* ---------------- W-03: Mobile navigation enhancement ----------------
     The desktop nav is a single flex row (~999px wide). Below 820px it is
     converted to a toggle button + dropdown sheet, only when the row
     actually overflows (idempotent, measured with overrides removed). */
  function initMobileNav() {
    var header = document.querySelector('header');
    if (!header) return;
    var nav = header.querySelector('nav');
    if (!nav) return;

    var wasOn = document.body.classList.contains('mq-mobilenav');
    if (wasOn) document.body.classList.remove('mq-mobilenav');
    var overflows = nav.scrollWidth > nav.clientWidth + 24;
    if (wasOn) document.body.classList.add('mq-mobilenav');

    if (window.innerWidth <= 820 && overflows) {
      document.body.classList.add('mq-mobilenav');
      if (!nav.id) nav.id = 'mqPrimaryNav';
      var btn = document.getElementById('mqNavToggle');
      if (!btn) {
        btn = document.createElement('button');
        btn.id = 'mqNavToggle';
        btn.type = 'button';
        btn.className = 'mq-nav-toggle';
        btn.setAttribute('aria-expanded', 'false');
        btn.setAttribute('aria-controls', nav.id);
        btn.setAttribute('aria-label', isZh ? '打开导航菜单' : 'Open navigation menu');
        btn.innerHTML = '<span class="mq-nav-burger" aria-hidden="true"><i></i><i></i><i></i></span>' +
          '<span class="mq-nav-toggle-label">' + (isZh ? '菜单' : 'Menu') + '</span>';
        if (nav.parentNode === header) { header.insertBefore(btn, nav); } else { header.appendChild(btn); }
        btn.addEventListener('click', function () {
          var open = document.body.classList.toggle('mq-nav-open');
          btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
        nav.addEventListener('click', function (e) {
          if (e.defaultPrevented) return;
          if (e.target && e.target.closest && e.target.closest('a')) {
            document.body.classList.remove('mq-nav-open');
            btn.setAttribute('aria-expanded', 'false');
          }
        });
        document.addEventListener('keydown', function (e) {
          if (e.key === 'Escape' && document.body.classList.contains('mq-nav-open')) {
            document.body.classList.remove('mq-nav-open');
            btn.setAttribute('aria-expanded', 'false');
          }
        });
        document.addEventListener('click', function (e) {
          if (!document.body.classList.contains('mq-nav-open')) return;
          if (!header.contains(e.target)) {
            document.body.classList.remove('mq-nav-open');
            btn.setAttribute('aria-expanded', 'false');
          }
        });
      }
    } else {
      document.body.classList.remove('mq-nav-open');
      var b = document.getElementById('mqNavToggle');
      if (b) b.setAttribute('aria-expanded', 'false');
      if (window.innerWidth > 820) document.body.classList.remove('mq-mobilenav');
    }
  }

  /* ---------------- W-07: Cookie consent (accept OR decline) ----------------
     Optional analytics and advertising stay blocked until explicit consent.
     Loaders are centralized here so no page can bypass the consent gate. */
  var analyticsVersion = '20261128';
  var adsPublisherId = 'ca-pub-8740168077394877';
  var currentScriptUrl = document.currentScript && document.currentScript.src ? document.currentScript.src : null;

  function siteAsset(path) {
    if (!currentScriptUrl) return path;
    try { return new URL(path, currentScriptUrl).href; } catch (e) { return path; }
  }

  function getConsent() {
    try { return localStorage.getItem('mq_cookie_consent'); } catch (e) { return null; }
  }

  function setConsentMode(granted) {
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    window.gtag('consent', 'default', {
      analytics_storage: 'denied',
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied'
    });
    if (granted) {
      window.gtag('consent', 'update', {
        analytics_storage: 'granted',
        ad_storage: 'granted',
        ad_user_data: 'granted',
        ad_personalization: 'granted'
      });
    }
  }

  function loadAnalytics() {
    if (getConsent() !== 'accepted' || window.__muqiAnalyticsLoaderAdded) return;
    if (document.querySelector('script[src*="/assets/js/analytics.js"]')) return;
    window.__muqiAnalyticsLoaderAdded = true;
    var ga = document.createElement('script');
    ga.src = siteAsset('assets/js/analytics.js') + '?v=' + analyticsVersion;
    ga.defer = true;
    document.head.appendChild(ga);
  }

  function loadAds() {
    if (getConsent() !== 'accepted' || window.__muqiAdsLoaderAdded) return;
    if (document.querySelector('script[src*="adsbygoogle.js"]')) return;
    window.__muqiAdsLoaderAdded = true;
    var ads = document.createElement('script');
    ads.async = true;
    ads.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' + encodeURIComponent(adsPublisherId);
    ads.crossOrigin = 'anonymous';
    document.head.appendChild(ads);
  }

  function loadOptionalServices() {
    var accepted = getConsent() === 'accepted';
    setConsentMode(accepted);
    if (accepted) {
      loadAnalytics();
      loadAds();
    }
  }

  function initCookieBanner() {
    loadOptionalServices();
    var banner = document.getElementById('cookie-banner');
    if (!banner) return;
    var consent = getConsent();
    function hide() { banner.classList.add('hidden'); }
    if (consent === 'accepted' || consent === 'rejected') {
      hide();
      return;
    }

    var textEl = banner.querySelector('.cookie-banner-text');
    if (textEl) {
      if (/By continuing/i.test(textEl.textContent)) {
        textEl.innerHTML = 'We use essential cookies for the site to work, and optional analytics only with your consent. Choose <strong>Accept</strong> or <strong>Decline</strong>. Read our <a href="/privacy-policy.html">Privacy Policy</a>.';
      } else if (/继续浏览/.test(textEl.textContent)) {
        textEl.innerHTML = '我们使用网站运行所必需的 Cookie；分析类 Cookie 仅在您同意后启用。您可选择<strong>接受</strong>或<strong>拒绝</strong>。详见<a href="/privacy-policy.html">隐私政策</a>。';
      }
    }

    var actions = banner.querySelector('.cookie-banner-actions');
    var acceptBtn = document.getElementById('cookieAcceptBtn');
    var rejectBtn = document.getElementById('cookieRejectBtn');
    if (actions && acceptBtn && !rejectBtn) {
      rejectBtn = document.createElement('button');
      rejectBtn.type = 'button';
      rejectBtn.id = 'cookieRejectBtn';
      rejectBtn.className = 'cookie-btn-reject';
      rejectBtn.textContent = isZh ? '拒绝' : 'Decline';
      rejectBtn.setAttribute('aria-label', isZh ? '拒绝非必要 Cookie（分析统计将保持关闭）' : 'Decline non-essential cookies (analytics stays off)');
      actions.insertBefore(rejectBtn, acceptBtn);
    }

    if (rejectBtn && !rejectBtn.dataset.mqBound) {
      rejectBtn.dataset.mqBound = '1';
      rejectBtn.addEventListener('click', function () {
        try { localStorage.setItem('mq_cookie_consent', 'rejected'); } catch (e) {}
        setConsentMode(false);
        hide();
      });
    }

    if (acceptBtn && !acceptBtn.dataset.mqBound) {
      acceptBtn.dataset.mqBound = '1';
      acceptBtn.addEventListener('click', function () {
        try { localStorage.setItem('mq_cookie_consent', 'accepted'); } catch (e) {}
        loadOptionalServices();
        banner.style.opacity = '0';
        banner.style.transform = 'translateY(16px)';
        setTimeout(hide, 300);
      });
    }
  }

  /* ---------------- W-12: Floating WhatsApp quick-connect ----------------
     Ships statically on index.html only; injected site-wide here when the
     page does not already provide #waWidget. */
  function initWhatsAppWidget() {
    if (document.getElementById('waWidget') || !document.body) return;
    var aside = document.createElement('aside');
    aside.id = 'waWidget';
    aside.setAttribute('aria-label', isZh ? 'WhatsApp 快捷询盘' : 'WhatsApp Quick Inquiry');
    aside.style.cssText = 'position:fixed;bottom:24px;right:24px;z-index:9999;display:flex;align-items:center';
    var hover = "this.style.transform='translateY(-2px)';this.style.boxShadow='0 12px 28px rgba(37,211,102,0.55)'";
    var out = "this.style.transform='translateY(0)';this.style.boxShadow='0 8px 24px rgba(37,211,102,0.45)'";
    aside.innerHTML =
      '<a href="https://wa.me/8613964416725?text=Hello%20MUQI%20Tech%2C%20I%20would%20like%20to%20inquire%20about%20your%20solid-state%20hydrogen%20ceramics%20and%20sample%20testing." target="_blank" rel="noopener noreferrer" style="display:inline-flex;align-items:center;gap:10px;background:#25D366;color:#ffffff;padding:11px 18px;border-radius:9999px;text-decoration:none;font-size:13.5px;font-weight:700;box-shadow:0 8px 24px rgba(37,211,102,0.45);transition:all 0.2s" onmouseover="' + hover + '" onmouseout="' + out + '">' +
      '<span style="display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.664-.699c.97.529 1.771.815 2.796.815 3.182 0 5.768-2.586 5.769-5.766.001-3.181-2.584-5.768-5.769-5.768zm7.55 5.767c-.002 4.161-3.387 7.545-7.55 7.545-1.314 0-2.573-.342-3.676-.991l-4.081 1.07 1.09-3.98c-.719-1.144-1.1-2.474-1.1-3.844.002-4.161 3.387-7.546 7.55-7.546 4.162 0 7.549 3.385 7.55 7.546z"/></svg></span>' +
      '<span>' + (isZh ? 'WhatsApp 咨询' : 'WhatsApp Us') + '</span>' +
      '<span style="width:8px;height:8px;border-radius:50%;background:#ffffff;display:inline-block;animation:pulseWa 2s infinite"></span>' +
      '</a>';
    document.body.appendChild(aside);
    if (!document.getElementById('pulseWaStyle')) {
      var st = document.createElement('style');
      st.id = 'pulseWaStyle';
      st.textContent = '@keyframes pulseWa { 0% { opacity: 1; transform: scale(1); } 50% { opacity: 0.35; transform: scale(0.8); } 100% { opacity: 1; transform: scale(1); } }';
      document.head.appendChild(st);
    }
  }

  /* ---------------- W-08: B2B decision-relief facts strip ----------------
     Injected above the RFQ forms. Facts only — all four lines already exist
     on emuqi.com or in llms-full.txt (no invented MOQ/warranty numbers). */
  function initDecisionFacts() {
    var anchor = document.getElementById('b2bInquiryForm') || document.getElementById('homeRfqForm');
    if (!anchor || document.getElementById('mqDecisionFacts')) return;
    var facts = isZh
      ? ['⚡ 12 个工作小时内响应', '🧪 样品窗口 5–22 天', '🏭 OEM 批量 20–25 个工作日发货', '🧾 SGS 等第三方检测报告可提供', '💰 最小起订金额 10,000 美元', '📅 产品有效期 12–60 个月（因产品而异）']
      : ['⚡ Response within 12 business hours', '🧪 Sample window 5–22 days', '🏭 OEM batches dispatched in 20–25 business days', '🧾 SGS third-party test reports available', '💰 Minimum order value USD 10,000', '📅 Product validity 12–60 months (varies by product)'];
    var strip = document.createElement('div');
    strip.id = 'mqDecisionFacts';
    strip.setAttribute('role', 'list');
    strip.setAttribute('aria-label', isZh ? '服务与交付事实' : 'Service and delivery facts');
    strip.style.cssText = 'display:flex;flex-wrap:wrap;gap:8px 20px;align-items:center;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:10px;padding:12px 16px;font-size:13px;color:#334155;margin:0 0 18px';
    strip.innerHTML = facts.map(function (f) { return '<span role="listitem">' + f + '</span>'; }).join('');
    anchor.parentNode.insertBefore(strip, anchor);
  }

  /* ---------------- RFQ privacy-safe email intent ---------------- */
  function initRfqForms() {
    var contactForm = document.getElementById('b2bInquiryForm');
    if (contactForm) {
      try {
        var params = new URLSearchParams(window.location.search);
        var category = document.getElementById('interestCategory');
        if (params.get('intent') === 'sample' && category && !category.value) {
          category.value = 'Sample / Evaluation Request';
        }
      } catch (e) {}
    }

    document.querySelectorAll('#homeRfqForm, #b2bInquiryForm').forEach(function (form) {
      if (!form || form.dataset.mqRfqBound) return;
      form.dataset.mqRfqBound = '1';
      form.addEventListener('submit', function (event) {
        event.preventDefault();
        var honeypot = form.querySelector('.mq-hp-field');
        if (honeypot && honeypot.value) { form.reset(); return; }

        var value = function (id) {
          var field = document.getElementById(id);
          return field ? field.value.trim() : '';
        };
        var isHome = form.id === 'homeRfqForm';
        var name = isHome ? value('rfqName') : (value('firstName') + ' ' + value('lastName')).trim();
        var email = value(isHome ? 'rfqEmail' : 'workEmail');
        var company = value(isHome ? 'rfqCompany' : 'companyName');
        var phone = isHome ? '' : value('phoneWhatsApp');
        var interest = value(isHome ? 'rfqMaterial' : 'interestCategory');
        var message = value(isHome ? 'rfqMessage' : 'inquiryMessage');
        var lines = ['Name: ' + name, 'Email: ' + email, 'Company: ' + company];
        if (phone) lines.push('WhatsApp/Phone: ' + phone);
        lines.push('Interest: ' + interest, '', 'Requirements:', message);
        var subject = 'B2B Inquiry: ' + (company || name || 'MUQI Ceramics');
        var mailto = 'mailto:muqizb@gmail.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));

        if (getConsent() === 'accepted') {
          window.dataLayer = window.dataLayer || [];
          window.dataLayer.push({ event: 'rfq_email_intent', form: form.id, interest: interest });
        }
        var success = document.getElementById(isHome ? 'homeRfqSuccess' : 'formSuccessMsg');
        if (success) success.style.display = 'block';
        window.location.href = mailto;
        form.reset();
      });
    });
  }

  function initAll() {
    initMobileNav();
    initCookieBanner();
    initRfqForms();
    initWhatsAppWidget();
    initDecisionFacts();

    // Unified dropdown support for canonical .dd menus and legacy .dropdown-menu menus.
    document.querySelectorAll('header nav > div').forEach(function (group, index) {
      var trigger = null;
      Array.prototype.forEach.call(group.children, function (child) {
        if (!trigger && child.tagName === 'A') trigger = child;
      });
      var menu = group.querySelector('.dd, .dropdown-menu');
      if (!trigger || !menu || group.dataset.mqDdBound) return;
      group.dataset.mqDdBound = '1';
      var isCanonical = menu.classList.contains('dd');
      if (!menu.id) menu.id = 'mq-dd-menu-' + index;

      function setOpen(open, force) {
        group.classList.toggle('is-open', open);
        if (isCanonical && (window.innerWidth <= 820 || force)) {
          menu.style.display = open ? 'block' : 'none';
        }
        trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
      }

      trigger.setAttribute('aria-haspopup', 'true');
      trigger.setAttribute('aria-expanded', 'false');
      trigger.setAttribute('aria-controls', menu.id);
      trigger.addEventListener('click', function (e) {
        if (window.innerWidth <= 820) {
          e.preventDefault();
          setOpen(!group.classList.contains('is-open'));
        }
      });
      trigger.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowDown') {
          e.preventDefault();
          setOpen(true, true);
          var first = menu.querySelector('a');
          if (first) first.focus();
        }
      });
      group.addEventListener('focusin', function () {
        if (window.innerWidth > 820) trigger.setAttribute('aria-expanded', 'true');
      });
      group.addEventListener('focusout', function (e) {
        if (!group.contains(e.relatedTarget)) {
          trigger.setAttribute('aria-expanded', 'false');
          group.classList.remove('is-open');
          if (isCanonical && window.innerWidth <= 820) menu.style.display = 'none';
        }
      });
      group.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') {
          setOpen(false, true);
          trigger.focus();
        }
      });
    });

    // Product-detail galleries use native buttons and keep alt text in sync.
    document.querySelectorAll('#gallery-thumbs').forEach(function (strip) {
      var heroImg = document.getElementById('gallery-hero');
      if (!heroImg) return;
      strip.querySelectorAll('.gallery-thumb').forEach(function (thumb) {
        thumb.addEventListener('click', function () {
          var image = thumb.querySelector('img');
          if (!image) return;
          heroImg.src = image.src;
          heroImg.alt = image.alt;
          strip.querySelectorAll('.gallery-thumb').forEach(function (item) {
            item.setAttribute('aria-pressed', item === thumb ? 'true' : 'false');
          });
        });
      });
    });

    // Application page thumbnail swap
    document.querySelectorAll('.application-thumbs').forEach(function (strip) {
      var heroImg = strip.closest('.application-product-bg') ? strip.closest('.application-product-bg').querySelector('img') : null;
      if (!heroImg) return;
      strip.querySelectorAll('.gallery-thumb').forEach(function (thumb) {
        thumb.addEventListener('click', function () {
          var image = thumb.querySelector('img');
          if (!image) return;
          heroImg.src = image.src;
          heroImg.alt = image.alt;
          strip.querySelectorAll('.gallery-thumb').forEach(function (item) {
            item.classList.toggle('active', item === thumb);
            item.setAttribute('aria-pressed', item === thumb ? 'true' : 'false');
          });
        });
      });
    });

    // Application page scroll-reveal for product panels
    if ('IntersectionObserver' in window) {
      var panels = document.querySelectorAll('.application-product-panel');
      panels.forEach(function (p) { p.style.opacity = '0'; p.style.transform = 'translateY(24px)'; p.style.transition = 'opacity .6s ease, transform .6s ease'; });
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { if (e.isIntersecting) { e.target.style.opacity = '1'; e.target.style.transform = 'translateY(0)'; } });
      }, { threshold: 0.15 });
      panels.forEach(function (p) { io.observe(p); });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }

  var mqResizeTimer;
  window.addEventListener('resize', function () {
    clearTimeout(mqResizeTimer);
    mqResizeTimer = setTimeout(initMobileNav, 200);
  });
})();

// Load MUQI WebMCP Agentic Web Engine once (root-relative for nested pages).
(function () {
  if (document.querySelector('script[src*="/assets/js/muqi-webmcp.js"], script[src*="muqi-webmcp.js"]')) return;
  var mcpScript = document.createElement('script');
  var mcpBase = document.currentScript && document.currentScript.src ? document.currentScript.src : null;
  try {
    mcpScript.src = mcpBase ? new URL('assets/js/muqi-webmcp.js', mcpBase).href : 'assets/js/muqi-webmcp.js';
  } catch (e) {
    mcpScript.src = 'assets/js/muqi-webmcp.js';
  }
  mcpScript.src += '?v=20261128';
  mcpScript.defer = true;
  document.head.appendChild(mcpScript);
})();
