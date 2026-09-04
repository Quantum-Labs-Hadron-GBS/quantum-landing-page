import os
import re

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

    # We want to replace the current DOMContentLoaded + load refresh block with just a window.load init
    old_block_regex = r'document\.addEventListener\("DOMContentLoaded", function \(\) \{[\s\S]*?AOS\.refresh\(\);\s*\}\);'
    
    new_block = """window.addEventListener('load', function() {
            AOS.init({
                duration: 800,
                once: true,
                offset: 50,
                easing: 'ease-out-cubic'
            });
        });"""

    if re.search(old_block_regex, content):
        content = re.sub(old_block_regex, new_block, content)
        with open(file, 'w') as f:
            f.write(content)
        print(f"Fixed {file}")
    else:
        print(f"Regex didn't match in {file}")

