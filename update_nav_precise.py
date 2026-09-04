import re
import glob

def update_nav():
    for filename in glob.glob("*.html"):
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()

        # 1. RENAME OFFERINGS TO ENTERPRISE SOLUTIONS (Desktop)
        html = re.sub(
            r'<a href="javascript:void\(0\)"([^>]*>)\s*OFFERINGS\s*</a>',
            r'<a href="javascript:void(0)"\1ENTERPRISE SOLUTIONS</a>',
            html
        )
        
        # 2. RENAME OFFERINGS TO Enterprise Solutions (Mobile)
        html = re.sub(
            r'<a href="javascript:void\(0\)"([^>]*>)\s*Offerings\s*</a>',
            r'<a href="javascript:void(0)"\1Enterprise Solutions</a>',
            html
        )
        
        # 3. REMOVE OLD #workflow AND #pricing LINKS (Desktop)
        html = re.sub(r'<a href="(index\.html)?#workflow"[^>]*>.*?</a>\s*', '', html, flags=re.DOTALL)
        html = re.sub(r'<a href="(index\.html)?#pricing"[^>]*>.*?</a>\s*', '', html, flags=re.DOTALL)

        # 4. INSERT HOW WE WORK INTO DESKTOP NAV
        # Find the end of the dropdown block (which is a </div>) right before the contact link
        # The dropdown block is <div class="relative group h-full flex">...</div>
        # We can find the contact link, and insert HOW WE WORK right before it.
        contact_pattern = r'<a href="contact\.html"[^>]*class="(nav-link[^"]*)"[^>]*>CONTACT.*?</a>'
        match = re.search(contact_pattern, html, flags=re.DOTALL)
        if match:
            classes = match.group(1)
            # Remove gap-2 if present, since it's just text
            classes = classes.replace('gap-2 ', '').replace(' gap-2', '')
            how_we_work = f'<a href="how-we-work.html" class="{classes}">HOW WE WORK</a>\n                '
            # Only insert if it's not already there
            if 'href="how-we-work.html"' not in html:
                html = html[:match.start()] + how_we_work + html[match.start():]
                
        # 5. INSERT How We Work INTO MOBILE NAV
        mobile_contact_pattern = r'<a href="contact\.html"[^>]*class="(mobile-link[^"]*)"[^>]*>Contact Us</a>'
        mmatch = re.search(mobile_contact_pattern, html, flags=re.DOTALL)
        if mmatch:
            mclasses = mmatch.group(1)
            # Remove specific colors that might be on contact.html
            if "text-brand-orange" in mclasses:
                mclasses = mclasses.replace("text-brand-orange", "text-brand-dark/70").replace("hover:text-brand-orange/80", "hover:text-brand-dark")
            # For pages with white nav
            if "color:#ff9f2b" in mclasses:
                mclasses = mclasses.replace('style="color:#ff9f2b;"', '')
            how_we_work_mobile = f'<a href="how-we-work.html" class="{mclasses.strip()}">How We Work</a>\n            '
            
            # Since we are inserting, we need to check if we already inserted it
            # But the first insert (desktop) might have added it. So we check if "How We Work" is there in mobile block
            if 'class="mobile-link' not in html or html.count('how-we-work.html') < 2:
                # Find the position of mobile contact link again since html string changed
                mmatch2 = re.search(mobile_contact_pattern, html, flags=re.DOTALL)
                if mmatch2:
                    html = html[:mmatch2.start()] + how_we_work_mobile + html[mmatch2.start():]

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated Navigation in {filename}")

if __name__ == '__main__':
    update_nav()
