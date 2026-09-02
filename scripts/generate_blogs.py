import os

# Define CSS matching hydrogen-patch-opportunity.html
common_css = """
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: "DM Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #f5f6f8; color: #1a1a2e; }
.hero { 
  background: linear-gradient(135deg, rgba(10,22,40,0.82) 0%, rgba(26,58,110,0.70) 60%, rgba(10,22,40,0.78) 100%), 
              url('../assets/images/blog/antimicrobial-ceramic-balls/maca-kdf-1.png') center/cover no-repeat; 
  padding: 160px 40px 110px; 
  text-align: center; 
}
.hero h1 { font-size: 36px; font-weight: 700; color: #fff; letter-spacing: -0.5px; line-height: 1.25; margin-bottom: 16px; text-shadow: 0 2px 12px rgba(0,0,0,0.5); max-width: 900px; margin-left: auto; margin-right: auto; }
.hero .meta { color: rgba(255,255,255,0.75); font-size: 14px; margin-bottom: 20px; }
.hero .meta span { color: #f47b20; font-weight: 600; }
.hero .sub { font-size: 17px; color: rgba(255,255,255,0.9); max-width: 720px; margin: 0 auto; line-height: 1.7; font-weight: 300; text-shadow: 0 1px 8px rgba(0,0,0,0.3); }
.hero .lang-pill { display: inline-flex; align-items: center; gap: 6px; padding: 6px 16px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); color: #fff; border-radius: 999px; text-decoration: none; font-size: 13px; font-weight: 600; margin-top: 24px; transition: all 0.2s; }
.hero .lang-pill:hover { background: #f47b20; border-color: #f47b20; }
.wrap { max-width: 820px; margin: -48px auto 80px; padding: 0 24px; }
.card { background: #fff; border-radius: 16px; padding: 56px; box-shadow: 0 2px 20px rgba(0,0,0,0.04); }
.card h2 { font-size: 22px; color: #1a3a6e; font-weight: 700; margin: 44px 0 18px; line-height: 1.35; }
.card h3 { font-size: 17px; color: #1d4ed8; font-weight: 600; margin: 26px 0 12px; }
.card p { font-size: 16px; line-height: 1.85; color: #2d3748; margin-bottom: 20px; }
.card img { width: 100%; border-radius: 12px; margin: 28px 0; box-shadow: 0 4px 16px rgba(0,0,0,0.08); }
.card .img-caption { font-size: 13px; color: #64748b; text-align: center; margin: -16px 0 24px; }
.card .box { background: #f0f4ff; border-radius: 12px; padding: 24px 28px; margin-bottom: 32px; border-left: 4px solid #1d4ed8; }
.card .box p { margin: 0; font-size: 15px; color: #2d3a5e; line-height: 1.8; }
.card .highlight { background: #EFF4FF; border-left: 4px solid #1d4ed8; border-radius: 0 10px 10px 0; padding: 18px 22px; margin: 24px 0; }
.card .highlight p { margin: 0; font-size: 15px; line-height: 1.85; }
.card table { width: 100%; border-collapse: collapse; font-size: 14px; margin: 24px 0; }
.card table th { padding: 11px 14px; border: 1px solid #E5E7EB; background: #1d4ed8; color: #fff; font-weight: 600; text-align: left; font-size: 13.5px; }
.card table td { padding: 10px 14px; border: 1px solid #E5E7EB; color: #374151; font-size: 13.5px; }
.card table tr:nth-child(even) td { background: #F8FAFC; }
.card .cta-box { background: #0a1628; border-radius: 12px; padding: 40px; text-align: center; margin: 40px 0; }
.card .cta-box h3 { color: #f47b20; font-size: 20px; margin: 0 0 10px; }
.card .cta-box p { color: rgba(240,236,228,0.7); font-size: 14.5px; margin-bottom: 20px; }
.card .cta-box a { display: inline-block; padding: 12px 32px; background: #f47b20; color: #fff; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 14.5px; transition: all 0.2s; }
.card .cta-box a:hover { background: #d4a84b; }
.faq-item { padding: 20px 0; border-bottom: 1px solid #f0f0f2; }
.faq-item:last-child { border: none; }
.faq-item h4 { font-size: 16px; color: #1a3a6e; font-weight: 600; margin-bottom: 8px; }
.faq-item p { font-size: 15px; color: #475569; margin: 0; line-height: 1.8; }
.stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 28px 0; }
.stat-card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; text-align: center; }
.stat-card .num { font-size: 28px; font-weight: 800; color: #1d4ed8; margin-bottom: 4px; }
.stat-card .label { font-size: 13px; color: #64748b; font-weight: 500; }
"""

# Social share snippet matching hydrogen-patch-opportunity.html
def get_share_html(url, title):
    return f"""
    <!-- SHARE -->
    <div style="margin-top:40px;padding:28px 0;border-top:1px solid #E5E7EB;text-align:center">
      <p style="font-size:13px;color:#94a3b8;margin:0 0 16px;letter-spacing:0.5px">Share this article · 分享到社交媒体</p>
      <div style="display:flex;justify-content:center;gap:8px;flex-wrap:wrap">
        <a href="https://twitter.com/intent/tweet?url={url}&text={title}" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;justify-content:center;width:42px;height:36px;background:#000;color:#fff;border-radius:8px;text-decoration:none;transition:opacity 0.2s" title="X / Twitter"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
        <a href="https://www.facebook.com/sharer/sharer.php?u={url}" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;justify-content:center;width:42px;height:36px;background:#1877F2;color:#fff;border-radius:8px;text-decoration:none;transition:opacity 0.2s" title="Facebook"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></a>
        <a href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;justify-content:center;width:42px;height:36px;background:#0A66C2;color:#fff;border-radius:8px;text-decoration:none;transition:opacity 0.2s" title="LinkedIn"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>
        <a href="https://wa.me/?text={title}%20{url}" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;justify-content:center;width:42px;height:36px;background:#25D366;color:#fff;border-radius:8px;text-decoration:none;transition:opacity 0.2s" title="WhatsApp"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg></a>
        <a href="https://t.me/share/url?url={url}&text={title}" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;justify-content:center;width:42px;height:36px;background:#0088CC;color:#fff;border-radius:8px;text-decoration:none;transition:opacity 0.2s" title="Telegram"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.479.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg></a>
        <a href="https://reddit.com/submit?url={url}&title={title}" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;justify-content:center;width:42px;height:36px;background:#FF4500;color:#fff;border-radius:8px;text-decoration:none;transition:opacity 0.2s" title="Reddit"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0zm5.01 4.744c.688 0 1.25.561 1.25 1.249a1.25 1.25 0 0 1-2.498.056l-2.597-.547-.8 3.747c1.824.07 3.48.632 4.674 1.488.308-.309.73-.491 1.207-.491.968 0 1.754.786 1.754 1.754 0 .716-.435 1.333-1.01 1.614a3.111 3.111 0 0 1 .042.52c0 2.694-3.13 4.87-7.004 4.87-3.874 0-7.004-2.176-7.004-4.87 0-.183.015-.366.043-.534A1.748 1.748 0 0 1 4.028 12c0-.968.786-1.754 1.754-1.754.463 0 .898.196 1.207.49 1.207-.883 2.878-1.43 4.744-1.487l.885-4.182a.342.342 0 0 1 .14-.197.35.35 0 0 1 .238-.042l2.906.617a1.214 1.214 0 0 1 1.108-.701zM9.25 12C8.561 12 8 12.562 8 13.25c0 .687.561 1.248 1.25 1.248.687 0 1.248-.561 1.248-1.249 0-.688-.561-1.249-1.249-1.249zm5.5 0c-.687 0-1.248.561-1.248 1.25 0 .687.561 1.248 1.249 1.248.688 0 1.249-.561 1.249-1.249 0-.687-.562-1.249-1.25-1.249zm-5.466 3.99a.327.327 0 0 0-.231.094.33.33 0 0 0 0 .463c.842.842 2.484.913 2.961.913.477 0 2.105-.056 2.961-.913a.361.361 0 0 0 .029-.463.33.33 0 0 0-.464 0c-.547.533-1.684.73-2.512.73-.828 0-1.979-.196-2.512-.73a.326.326 0 0 0-.232-.095z"/></svg></a>
        <a href="https://service.weibo.com/share/share.php?url={url}&title={title}" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;justify-content:center;width:42px;height:36px;background:#E6162D;color:#fff;border-radius:8px;text-decoration:none;transition:opacity 0.2s" title="Weibo"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M10.098 20.323c-3.977.391-7.414-1.406-7.672-4.02-.259-2.609 2.759-5.047 6.74-5.441 3.979-.394 7.413 1.404 7.671 4.018.259 2.6-2.759 5.049-6.739 5.443zM9.05 17.219c-.384.616-1.208.884-1.829.602-.612-.279-.793-.991-.406-1.593.379-.595 1.176-.86 1.797-.584.626.279.819.972.438 1.575zm1.27-1.627c-.141.237-.449.353-.689.253-.236-.09-.313-.361-.177-.586.138-.227.436-.346.672-.24.239.09.315.345.194.573zm.408-4.579c-3.086-.799-6.586.591-7.882 3.103-1.321 2.557-.066 5.38 3.05 6.21 3.223.851 6.938-.549 8.187-3.229 1.227-2.633-.165-5.302-3.355-6.084zm7.009 1.348c-.261-.073-.437-.122-.302-.441.301-.699.333-1.3.008-1.725-.611-.794-2.283-.75-4.211-.02 0 0-.601.249-.447-.214.294-.903.251-1.658-.207-2.105-1.036-1.006-3.783.038-6.147 2.329C5.466 12.539 4.2 14.842 4.2 16.861c0 3.849 4.921 6.191 9.713 6.191 6.274 0 10.454-3.649 10.454-6.52 0-1.751-1.474-2.744-2.878-3.373z"/></svg></a>
      </div>
    </div>
    <!-- GOOGLE ADS PLACEHOLDER -->
    <div style="margin-top:32px;text-align:center">
      <div style="background:#f9fafb;border:2px dashed #d1d5db;border-radius:12px;padding:40px 20px;color:#9ca3b8;font-size:13px">
        <p style="margin:0 0 4px;font-weight:600;color:#6b7280">Ad Space · 广告位</p>
        <p style="margin:0;font-size:11px">Google AdSense — Replace with your ad code</p>
      </div>
    </div>
    """

print("Generator ready")
