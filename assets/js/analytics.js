/* ============================================================
   MUQI Tech — Site-wide Analytics Loader (config-driven)
   ------------------------------------------------------------
   HOW TO ACTIVATE GA4 (one-time, 30 seconds):
   1. Google Analytics → Admin → Data Streams → Web → emuqi.com
   2. Copy the Measurement ID (format: G-XXXXXXXXXX)
   3. Paste it below into ga4MeasurementId
   4. Commit & push → GA4 goes live on ALL pages at once.

   GOOGLE SEARCH CONSOLE (GSC):
   Use the HTML-file verification method: download the
   googleXXXXXXXXxxxx.html file from GSC, drop it in the repo
   root, commit & push, then click "Verify" in GSC.
   ============================================================ */
var MUQI_ANALYTICS = {
  ga4MeasurementId: "" // ← paste e.g. "G-XXXXXXXXXX"
};

(function () {
  var id = MUQI_ANALYTICS.ga4MeasurementId;
  if (!id || !/^G-[A-Z0-9]+$/i.test(id)) return; // not configured yet → no-op
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  window.gtag('js', new Date());
  window.gtag('config', id, { anonymize_ip: true });
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(id);
  document.head.appendChild(s);
})();
