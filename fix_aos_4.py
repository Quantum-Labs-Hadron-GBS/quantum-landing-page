import os
import re

files = [
    'how-we-work.html',
    'ai-infrastructure.html',
    'pqc-security.html',
    'quantum-technology.html'
]

old_block_regex = r"window\.addEventListener\('load', function\(\) \{\s*AOS\.init\(\{\s*duration: 800,\s*once: true,\s*offset: 50,\s*easing: 'ease-out-cubic'\s*\}\);\s*\}\);"

new_block = """function initAOS() {
            AOS.init({
                duration: 800,
                once: true,
                offset: 50,
                easing: 'ease-out-cubic'
            });
        }
        if (document.readyState === 'complete') {
            initAOS();
        } else {
            window.addEventListener('load', initAOS);
        }"""

for file in files:
    if not os.path.exists(file):
        continue
    
    with open(file, 'r') as f:
        content = f.read()

    if re.search(old_block_regex, content):
        content = re.sub(old_block_regex, new_block, content)
        with open(file, 'w') as f:
            f.write(content)
        print(f"Fixed {file}")
    else:
        print(f"Regex didn't match in {file}")

