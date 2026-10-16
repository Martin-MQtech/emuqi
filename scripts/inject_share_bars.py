import glob
import os
import re

def run():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, '..'))
    zh_dir = os.path.join(base_dir, 'zh', 'blog')

    with open(os.path.join(base_dir, 'templates', 'canonical_social_share_zh.html'), 'r', encoding='utf-8') as f:
        tpl_share = f.read()

    zh_files = glob.glob(os.path.join(zh_dir, '*.html'))
    for f in sorted(zh_files):
        if f.endswith('index.html'):
            continue
        fname = os.path.basename(f)
        slug = fname[:-5]
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()

        m_h1 = re.search(r'<h1[^>]*>(.*?)</h1>', c, re.DOTALL)
        if m_h1:
            title = re.sub(r'<[^>]+>', '', m_h1.group(1)).strip()
        else:
            m_t = re.search(r'<title>(.*?)</title>', c)
            title = m_t.group(1).split('·')[0].split('|')[0].strip() if m_t else slug

        url = f'https://www.emuqi.com/zh/blog/{fname}'
        clean_title = title.replace('"', '&quot;').replace("'", "\\'")
        share_block = tpl_share.replace('{PAGE_URL}', url).replace('{PAGE_TITLE}', clean_title)

        if 'mqOpenWechatShareModal' in c:
            print(f'{fname}: already has new share bar')
            continue

        # Try to replace existing social share block
        old_share_regex = re.compile(r'(?:<!--.*?-->\s*)?<div[^>]*class=[\"\'][^\"\']*social-share[^\"\']*[\"\'].*?</div>(?:\s*</div>)?', re.DOTALL)
        if old_share_regex.search(c):
            c = old_share_regex.sub(share_block, c, count=1)
            print(f'{fname}: replaced old share bar')
        else:
            m_old_generic = re.search(r'(<!--\s*分享到社交媒体\s*-->.*?</div>\s*</div>)', c, re.DOTALL)
            if m_old_generic:
                c = c.replace(m_old_generic.group(1), share_block)
                print(f'{fname}: replaced generic share block')
            else:
                m_tags = re.search(r'(<div[^>]*class=[\"\'][^\"\']*tag[^\"\']*[\"\'])', c, re.IGNORECASE)
                if m_tags:
                    pos = m_tags.start()
                    c = c[:pos] + share_block + '\n\n    ' + c[pos:]
                    print(f'{fname}: inserted before tags')
                else:
                    m_main = re.search(r'(</main>)', c, re.IGNORECASE)
                    if m_main:
                        pos = m_main.start()
                        c = c[:pos] + share_block + '\n\n  ' + c[pos:]
                        print(f'{fname}: inserted before </main>')
                    else:
                        m_foot = re.search(r'(<footer)', c, re.IGNORECASE)
                        pos = m_foot.start()
                        c = c[:pos] + share_block + '\n\n' + c[pos:]
                        print(f'{fname}: inserted before <footer')

        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)

    print('All Chinese blog articles now equipped with WeChat, Xiaohongshu, Bilibili, Weibo, Copy Link & Global channels!')

if __name__ == '__main__':
    run()
