import os
import re
import glob

for filename in glob.glob("*.html"):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove HOME
    html = re.sub(r'<a href="index\.html"[^>]*class="nav-link[^>]*>HOME</a>\s*', '', html)
    html = re.sub(r'<a href="index\.html"[^>]*class="mobile-link[^>]*>Home</a>\s*', '', html)

    # 2. Remove FAQ
    html = re.sub(r'<a href="(index\.html)?#faq-accordion"[^>]*class="nav-link[^>]*>FAQ</a>\s*', '', html)
    html = re.sub(r'<a href="(index\.html)?#faq-accordion"[^>]*class="mobile-link[^>]*>FAQ</a>\s*', '', html)

    # 3. Rename SOLUTIONS to OFFERINGS
    html = re.sub(r'>SOLUTIONS</a>', '>OFFERINGS</a>', html)
    html = re.sub(r'>Solutions</a>', '>Offerings</a>', html)

    # 4. Extend the arrow button as CONTACT ->
    # Find the contact.html nav-link block
    pattern = r'<a href="contact\.html"[^>]*class="nav-link[^>]*>.*?</a>'
    
    def replacer(match):
        # Build the new contact button
        # We need to extract the class to keep the styling, but add 'gap-2' and change 'px-5' to 'px-6' if we want.
        # Actually just setting standard class is fine, it usually has nav-link flex items-center px-5 border-r border-white/20 hover:bg-white/20 transition-colors
        old_tag = match.group(0)
        # Extract class string
        class_match = re.search(r'class="([^"]+)"', old_tag)
        cls = class_match.group(1) if class_match else "nav-link flex items-center px-6 border-r border-white/20 hover:bg-white/20 transition-colors"
        
        # Add gap-2 if not present
        if "gap-2" not in cls:
            cls = cls.replace("flex items-center", "flex items-center gap-2")
        
        # Replace px-5 with px-6 for a bit more padding since it has text now
        cls = cls.replace("px-5", "px-6")
        
        return f'<a href="contact.html" class="{cls}">CONTACT <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 12h14M12 5l7 7-7 7"></path></svg></a>'
    
    html = re.sub(pattern, replacer, html, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {filename}")
