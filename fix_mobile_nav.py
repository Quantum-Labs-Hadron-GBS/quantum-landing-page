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

# The closing of the enterprise solutions dropdown block usually looks like:
#                 </div>
#             </div>
# We want to inject right after this.
# Let's find "pqc-security.html", then the next two "</div>".

def insert_mobile_nav(content):
    if 'href="why-quantum.html"' in content.split('id="mobile-menu"')[1] if 'id="mobile-menu"' in content else False:
        return content, 0

    pqc_idx = content.find('pqc-security.html"')
    if pqc_idx == -1: return content, 0
    
    first_div = content.find('</div>', pqc_idx)
    second_div = content.find('</div>', first_div + 6)
    
    insert_pos = second_div + 6
    
    # Check if this file uses brand-dark or #0a0a0a
    if 'text-brand-dark' in content[pqc_idx:insert_pos]:
        color_class = 'text-brand-dark/70 hover:text-brand-dark'
    else:
        color_class = 'text-[#0a0a0a]/70 hover:text-[#0a0a0a]'
        
    link = f'\n            <a href="why-quantum.html" class="mobile-link {color_class} transition-colors">Why Quantum?</a>'
    
    new_content = content[:insert_pos] + link + content[insert_pos:]
    return new_content, 1

for file in files:
    if not os.path.exists(file): continue
    
    with open(file, 'r') as f:
        content = f.read()
        
    new_content, count = insert_mobile_nav(content)
    if count > 0:
        with open(file, 'w') as f:
            f.write(new_content)
        print(f"Updated mobile nav in {file}")

