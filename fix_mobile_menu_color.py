import glob
import re

def fix():
    html_files = glob.glob('*.html')
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()

        # Fix 1: When opening menu
        target_open = "mobileMenu.classList.remove('opacity-0', 'pointer-events-none');"
        replace_open = "mobileMenu.classList.remove('opacity-0', 'pointer-events-none');\n                        mobileMenuBtn.style.color = '#0a0a0a';"
        
        # Fix 2: When closing menu (toggle)
        target_close = "mobileMenu.classList.add('opacity-0', 'pointer-events-none');"
        replace_close = "mobileMenu.classList.add('opacity-0', 'pointer-events-none');\n                        mobileMenuBtn.style.color = '';"
        
        # Fix 3: When closing menu (link click)
        # It's actually the same line as target_close, so a generic replace might hit both.
        
        new_html = html.replace(target_open, replace_open).replace(target_close, replace_close)
        
        if new_html != html:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print(f"Fixed {file}")

fix()
print("Done")
