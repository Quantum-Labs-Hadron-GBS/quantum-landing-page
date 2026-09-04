import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change observers-text from z-20 to z-0
html = html.replace('id="observers-text" class="relative z-20', 'id="observers-text" class="relative z-0')

# Change observers-quantum from z-0 to z-10
html = html.replace('alt="Quantum Computer Core" class="absolute z-0', 'alt="Quantum Computer Core" class="absolute z-10')

# Change observers-people from z-10 to z-20
html = html.replace('id="observers-people" class="absolute z-10', 'id="observers-people" class="absolute z-20')

# Ensure the composition container has a z-index higher than text so its absolute children stay above relative text
html = html.replace('<!-- Composition -->\n        <div class="relative w-full flex justify-center items-end" style="height: 65vh; min-height: 500px;">', '<!-- Composition -->\n        <div class="relative z-10 w-full flex justify-center items-end" style="height: 65vh; min-height: 500px;">')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
