import re
import os

files = [
    'ai-infrastructure.html',
    'how-we-work.html',
    'index.html',
    'blogs.html',
    'pqc-security.html',
    'quantum-technology.html',
    'contact.html',
    'article.html',
    'why-quantum.html'
]

desktop_insert_regex = r'(<div class="relative group h-full flex">[\s\S]*?</div>\s*</div>\s*)(<a href="how-we-work\.html")'
desktop_new_link = r'\1<a href="why-quantum.html" class="nav-link flex items-center px-6 border-r border-white/20 hover:bg-white/20 transition-colors">WHY QUANTUM?</a>\n                \2'

mobile_insert_regex = r'(<div class="py-2 border-y border-white/10 my-4">[\s\S]*?</div>\s*)(<a href="how-we-work\.html")'
mobile_new_link = r'\1<a href="why-quantum.html" class="block text-2xl font-bold py-2 text-white/80 hover:text-white transition-colors">WHY QUANTUM?</a>\n                    \2'

for file in files:
    if not os.path.exists(file):
        continue
    
    with open(file, 'r') as f:
        content = f.read()

    # If it's already there, skip
    if 'href="why-quantum.html"' in content and file != 'why-quantum.html':
        print(f"Skipping {file} (already updated)")
        continue
    
    # Desktop
    content, d_count = re.subn(desktop_insert_regex, desktop_new_link, content)
    # Mobile
    content, m_count = re.subn(mobile_insert_regex, mobile_new_link, content)
    
    if d_count > 0 or m_count > 0:
        with open(file, 'w') as f:
            f.write(content)
        print(f"Updated {file} (Desktop: {d_count}, Mobile: {m_count})")
    else:
        print(f"Regex failed on {file}")

