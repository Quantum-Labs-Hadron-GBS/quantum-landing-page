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

    # Add overflow-x-clip back to body
    content = content.replace('body class="antialiased font-sans"', 'body class="antialiased font-sans overflow-x-clip"')

    with open(file, 'w') as f:
        f.write(content)
        
    print(f"Fixed {file}")
