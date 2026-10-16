import glob
import os
import re

def clean_title(title):
    t = re.sub(r'<[^>]+>', '', title).strip()
    t = t.split('|')[0].split('·')[0].split(' - ')[0].strip()
    return t.replace('"', '&quot;').replace("'", "\\'")

def get_share_block_en(tpl_share, fname, content):
    m_h1 = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if m_h1:
        title = clean_title(m_h1.group(1))
    else:
        m_t = re.search(r'<title>(.*?)</title>', content)
        title = clean_title(m_t.group(1)) if m_t else fname[:-5]
    
    url = f"https://www.emuqi.com/blog/{fname}"
    return tpl_share.replace('{PAGE_URL}', url).replace('{PAGE_TITLE}', title)

def replace_or_insert_en(content, share_block):
    # If already has canonical English share modal, replace it
    if 'mqOpenEnWechatModal' in content:
        # Replace existing canonical block
        m = re.search(r'<!-- Canonical English Social Share Bar -->.*?<!-- English Toast -->\s*<div id="mq-en-share-toast".*?</script>', content, re.DOTALL)
        if m:
            return content[:m.start()] + share_block + content[m.end():], 'replaced canonical English share bar'

    # Case 1: <!-- Social Share Bar --> ... social-share-wrap
    if 'class="social-share-wrap"' in content:
        m = re.search(r'(?:<!--\s*Social Share Bar\s*-->\s*)?<div class="social-share-wrap">.*?</div>', content, re.DOTALL)
        if m:
            return content[:m.start()] + share_block + content[m.end():], 'replaced social-share-wrap'

    # Case 2: <!-- 10-Channel Social Share Bar --> or class="social-share"
    if '<!-- 10-Channel Social Share Bar -->' in content:
        m = re.search(r'<!-- 10-Channel Social Share Bar -->\s*<div class="social-share">.*?</div>', content, re.DOTALL)
        if m:
            return content[:m.start()] + share_block + content[m.end():], 'replaced 10-Channel share bar'

    # Case 3: class="share-bar" (e.g. gary-brecka)
    if 'class="share-bar"' in content:
        m = re.search(r'(?:<!--\s*Social Share Bar\s*-->\s*)?<div class="share-bar">.*?</div>\s*</div>', content, re.DOTALL)
        if m:
            return content[:m.start()] + share_block + content[m.end():], 'replaced share-bar'

    # Case 4: <!-- SHARE --> (18 legacy files)
    if '<!-- SHARE -->' in content:
        pos_start = content.find('<!-- SHARE -->')
        # find end of container: it ends right before <!-- GOOGLE ADS or similar
        pos_ads = content.find('<!-- GOOGLE ADS PLACEHOLDER -->', pos_start)
        if pos_ads != -1:
            return content[:pos_start] + share_block + '\n\n    ' + content[pos_ads:], 'replaced legacy <!-- SHARE --> container'
        else:
            # alternative: find </div>\s*</div>
            m = re.search(r'<!-- SHARE -->\s*<div style="[^"]*margin-top:40px[^"]*">.*?</div>\s*</div>', content, re.DOTALL)
            if m:
                return content[:m.start()] + share_block + content[m.end():], 'replaced legacy <!-- SHARE --> via regex'

    # Case 5: solid-hydrogen-procurement-decision-tree-en.html (custom share container)
    pos_tree = content.find('Share this article')
    if pos_tree != -1:
        start_div = content.rfind('<div', 0, pos_tree)
        # count div nesting to find end of this container
        cur = start_div
        depth = 0
        end_pos = -1
        while cur < len(content):
            if content[cur:cur+4] == '<div':
                depth += 1
                cur += 4
            elif content[cur:cur+6] == '</div>':
                depth -= 1
                cur += 6
                if depth == 0:
                    end_pos = cur
                    break
            else:
                cur += 1
        if end_pos != -1:
            return content[:start_div] + share_block + content[end_pos:], 'replaced tree share container'

    # Case 6: No existing share block -> insert before tags or article end or main end
    # Check tags
    m_tags = re.search(r'(<div[^>]*class=[\"\'][^\"\']*tag[^\"\']*[\"\'])', content, re.IGNORECASE)
    if m_tags:
        pos = m_tags.start()
        return content[:pos] + share_block + '\n\n    ' + content[pos:], 'inserted before tags'

    m_back = re.search(r'(<div style="margin-top:28px;text-align:center">\s*<p><a href="index\.html")', content)
    if m_back:
        pos = m_back.start()
        return content[:pos] + share_block + '\n\n    ' + content[pos:], 'inserted before Back to Blog'

    m_main = re.search(r'(</main>)', content, re.IGNORECASE)
    if m_main:
        pos = m_main.start()
        return content[:pos] + share_block + '\n\n  ' + content[pos:], 'inserted before </main>'

    m_art = re.search(r'(</article>)', content, re.IGNORECASE)
    if m_art:
        pos = m_art.start()
        return content[:pos] + share_block + '\n\n  ' + content[pos:], 'inserted before </article>'

    m_foot = re.search(r'(<footer)', content, re.IGNORECASE)
    if m_foot:
        pos = m_foot.start()
        return content[:pos] + share_block + '\n\n' + content[pos:], 'inserted before <footer'

    return content, 'no change'

def run():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, '..'))
    blog_dir = os.path.join(base_dir, 'blog')

    with open(os.path.join(base_dir, 'templates', 'canonical_social_share_en.html'), 'r', encoding='utf-8') as f:
        tpl_share_en = f.read()

    with open(os.path.join(base_dir, 'templates', 'canonical_social_share_zh.html'), 'r', encoding='utf-8') as f:
        tpl_share_zh = f.read()

    files = glob.glob(os.path.join(blog_dir, '*.html'))
    en_count = 0
    zh_count = 0

    for f in sorted(files):
        if f.endswith('index.html'):
            continue
        fname = os.path.basename(f)
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()

        if 'http-equiv="refresh"' in c or 'window.location.replace' in c:
            continue

        m_lang = re.search(r'<html[^>]*lang=[\"\']([^\"\']+)[\"\']', c)
        lang = m_lang.group(1) if m_lang else 'en'

        if lang == 'zh-CN' or fname == 'hydrogen-patch-opportunity.html':
            # Chinese article in blog/
            m_h1 = re.search(r'<h1[^>]*>(.*?)</h1>', c, re.DOTALL)
            title = clean_title(m_h1.group(1)) if m_h1 else fname[:-5]
            url = f"https://www.emuqi.com/blog/{fname}"
            share_block = tpl_share_zh.replace('{PAGE_URL}', url).replace('{PAGE_TITLE}', title)
            
            # replace legacy share block
            pos_share = c.find('<!-- SHARE -->')
            if pos_share != -1:
                pos_ads = c.find('<!-- GOOGLE ADS PLACEHOLDER -->', pos_share)
                if pos_ads != -1:
                    new_c = c[:pos_share] + share_block + '\n\n    ' + c[pos_ads:]
                    with open(f, 'w', encoding='utf-8') as fp:
                        fp.write(new_c)
                    print(f'{fname} (ZH): successfully updated with Chinese canonical share bar')
                    zh_count += 1
            continue

        # English blog article
        share_block = get_share_block_en(tpl_share_en, fname, c)
        new_c, action = replace_or_insert_en(c, share_block)
        if new_c != c:
            with open(f, 'w', encoding='utf-8') as fp:
                fp.write(new_c)
            print(f'{fname} (EN): {action}')
            en_count += 1
        else:
            print(f'{fname} (EN): no change ({action})')

    print(f'\nDone! Updated {en_count} English blog articles and {zh_count} Chinese blog article.')

if __name__ == '__main__':
    run()
