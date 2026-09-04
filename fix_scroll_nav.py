import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

broken_pattern = r"const hero = document\.querySelector\('\.bg-black'\);\s*const threshold = hero \? hero\.offsetHeight - 50 : window\.innerHeight \* 0\.5;\s*if \(window\.scrollY > threshold\) \{\s*mainHeader\.classList\.add\('header-light-mode'\);\s*mainHeader\.classList\.remove\('header-dark-mode'\);\s*\} else \{\s*mainHeader\.classList\.add\('header-dark-mode'\);\s*mainHeader\.classList\.remove\('header-light-mode'\);\s*\}"

replacement = """
                    const headerRect = mainHeader.getBoundingClientRect();
                    const headerCenter = headerRect.top + headerRect.height / 2;
                    const sections = document.querySelectorAll('.bg-black, main, .w-full.relative, section.w-full');
                    
                    let isDark = true;
                    for (let sec of sections) {
                        const rect = sec.getBoundingClientRect();
                        if (rect.top <= headerCenter && rect.bottom >= headerCenter) {
                            if (sec.classList.contains('bg-black')) {
                                isDark = true;
                            } else {
                                isDark = false;
                            }
                            break;
                        }
                    }
                    
                    if (isDark) {
                        mainHeader.classList.add('header-dark-mode');
                        mainHeader.classList.remove('header-light-mode');
                    } else {
                        mainHeader.classList.add('header-light-mode');
                        mainHeader.classList.remove('header-dark-mode');
                    }
"""

for f in html_files:
    if f.startswith('old_') or f.startswith('previous_') or f.startswith('google'):
        continue
    
    with open(f, 'r') as file:
        content = file.read()
        
    new_content, count = re.subn(broken_pattern, replacement.strip(), content, flags=re.DOTALL)
    
    if count > 0:
        with open(f, 'w') as file:
            file.write(new_content)
        print(f"Fixed {f}")
