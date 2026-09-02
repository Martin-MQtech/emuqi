import os, re

root_dir = os.path.abspath('emuqi')

for list_page in ['emuqi/blog-list-hydrogen-health.html', 'emuqi/blog/index.html']:
    with open(list_page, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    page_dir = os.path.dirname(os.path.abspath(list_page))
    links = re.findall(r'<a\s+[^>]*href=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</a>', content, re.DOTALL)
    
    print(f"\nChecking links in {list_page}:")
    for href, text in links:
        if href.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#')):
            continue
        clean_l = href.split('#')[0].split('?')[0]
        if not clean_l:
            continue
        if clean_l.startswith('/'):
            target = os.path.normpath(os.path.join(root_dir, clean_l.lstrip('/')))
        else:
            target = os.path.normpath(os.path.join(page_dir, clean_l))
        
        target_html = target + '.html' if not os.path.splitext(target)[1] else target
        target_idx = os.path.join(target, 'index.html')
        
        exists = os.path.exists(target) or os.path.exists(target_html) or os.path.exists(target_idx)
        clean_text = re.sub(r'<[^>]+>', '', text).strip()[:50]
        if not exists:
            print(f"  [MISSING] href: '{href}' -> text: '{clean_text}'")
        else:
            rel_target = os.path.relpath(target if os.path.exists(target) else target_html if os.path.exists(target_html) else target_idx, root_dir)
            # print(f"  [OK] {href} -> {rel_target}")
