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

for file in files:
    if not os.path.exists(file): continue
    
    with open(file, 'r') as f:
        content = f.read()
        
    # 1. Remove the misplaced mobile link that is hanging in the desktop nav
    # The misplaced link looks like: <a href="why-quantum.html" class="mobile-link ...">Why Quantum?</a>
    # We only want to remove it if it occurs BEFORE the mobile-menu div.
    mobile_menu_idx = content.find('id="mobile-menu"')
    if mobile_menu_idx != -1:
        desktop_part = content[:mobile_menu_idx]
        mobile_part = content[mobile_menu_idx:]
        
        # Remove any misplaced mobile links from desktop part
        desktop_part = re.sub(r'\s*<a href="why-quantum\.html" class="mobile-link.*?">Why Quantum\?</a>', '', desktop_part)
        
        # Now, make sure the mobile link is correctly inserted into the mobile part
        if 'href="why-quantum.html"' not in mobile_part:
            pqc_idx = mobile_part.find('pqc-security.html"')
            if pqc_idx != -1:
                first_div = mobile_part.find('</div>', pqc_idx)
                second_div = mobile_part.find('</div>', first_div + 6)
                
                insert_pos = second_div + 6
                
                if 'text-brand-dark' in mobile_part[pqc_idx:insert_pos]:
                    color_class = 'text-brand-dark/70 hover:text-brand-dark'
                else:
                    color_class = 'text-[#0a0a0a]/70 hover:text-[#0a0a0a]'
                    
                link = f'\n            <a href="why-quantum.html" class="mobile-link {color_class} transition-colors">Why Quantum?</a>'
                
                mobile_part = mobile_part[:insert_pos] + link + mobile_part[insert_pos:]
        
        content = desktop_part + mobile_part
        
        with open(file, 'w') as f:
            f.write(content)
        print(f"Fixed {file}")

