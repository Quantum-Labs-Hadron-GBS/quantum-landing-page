import re
import os

files = [
    'how-we-work.html',
    'ai-infrastructure.html',
    'pqc-security.html',
    'quantum-technology.html'
]

for file in files:
    if not os.path.exists(file):
        continue
    
    with open(file, 'r') as f:
        content = f.read()

    # 1. Replace overflow-x-hidden on body with overflow-x-clip
    content = content.replace('body class="antialiased font-sans overflow-x-hidden"', 'body class="antialiased font-sans overflow-x-clip"')

    # 2. Update AOS init and add load event for refresh
    old_aos = """        document.addEventListener("DOMContentLoaded", function () {
            AOS.init({
                duration: 800,
                once: true,
                offset: 100,
                easing: 'ease-out-cubic'
            });
        });"""

    new_aos = """        document.addEventListener("DOMContentLoaded", function () {
            AOS.init({
                duration: 800,
                once: true,
                offset: 50,
                easing: 'ease-out-cubic'
            });
        });
        window.addEventListener('load', function() {
            AOS.refresh();
        });"""
        
    if old_aos in content:
        content = content.replace(old_aos, new_aos)
    else:
        print(f"Warning: Could not find exact AOS block in {file}, trying regex...")
        # Fallback regex
        content = re.sub(
            r'document\.addEventListener\("DOMContentLoaded", function \(\) \{\s*AOS\.init\(\{\s*duration: 800,\s*once: true,\s*offset: 100,\s*easing: \'ease-out-cubic\'\s*\}\);\s*\}\);',
            new_aos,
            content
        )

    with open(file, 'w') as f:
        f.write(content)
        
    print(f"Fixed {file}")
