import markdown
import re

cdn_map = {
    'fig5-cover-en.png': 'https://substackcdn.com/image/fetch/$s_!tRRO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7fd3373-d69b-4d90-8203-04b3b5b11e7a_2160x920.png',
    'case_a_htoeau_product_cans.png': 'https://substackcdn.com/image/fetch/$s_!FAse!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6292244-08cb-44cd-8aa7-902598c7b7da_400x400.png',
    'case_a_prof_sergej_ostojic.jpg': 'https://substackcdn.com/image/fetch/$s_!Pqb8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74d1c51a-bd40-46ae-a0cd-19b945f0be91_800x800.jpeg',
    'fig2-four-endpoints-grid-en.png': 'https://substackcdn.com/image/fetch/$s_!yMvr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40504da8-bdaa-4b26-b3c5-bc751a585684_2160x2240.png',
    'case_b_aquastamina_product.png': 'https://substackcdn.com/image/fetch/$s_!_yW3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0757c5b8-04f4-4af4-83fb-3f346a9dc7fb_1024x768.png',
    'fig1-case-comparison-table-en.png': 'https://substackcdn.com/image/fetch/$s_!Oqfh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06067bbe-a967-4c16-8945-869941031b17_2160x1918.png',
    'fig4-two-cases-timeline-en.png': 'https://substackcdn.com/image/fetch/$s_!Zk7G!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8b41cbed-7c66-45c3-abd4-bac6ae9d59b1_1600x1422.png',
    'fig3-0-6-percent-axis-en.png': 'https://substackcdn.com/image/fetch/$s_!vB1t!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F547630f1-e351-4887-8fe4-9585c38cc5ea_1600x1126.png',
}

with open('emuqi/distribution_packages/european_hydrogen_water_cases/03_Substack/newsletter_draft.md') as f:
    lines = f.readlines()

content_lines = []
# Prepend the cover banner image right at top
content_lines.append(f'![Two European Cases Cover]({cdn_map["fig5-cover-en.png"]})\n\n')

body_started = False
in_table = False
for line in lines:
    if line.startswith('# Does Hydrogen Water Work?'):
        continue
    if line.startswith('*A side-by-side comparative cross-investigation'):
        body_started = True
        continue
    if body_started:
        if line.strip().startswith('| Dimension |'):
            in_table = True
            continue
        if in_table:
            if line.strip().startswith('|') and '|' in line.strip()[1:]:
                continue
            else:
                in_table = False
        mod_line = line
        for k, v in cdn_map.items():
            if k in mod_line:
                mod_line = re.sub(r'https?://[^\s\)]+/' + re.escape(k), v, mod_line)
        content_lines.append(mod_line)

md_content = ''.join(content_lines)
html = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

with open('/tmp/substack_article.html', 'w') as f:
    f.write(html)

print('Generated /tmp/substack_article.html successfully! Size:', len(html))
