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

    # Remove overflow-x-clip completely
    content = content.replace('body class="antialiased font-sans overflow-x-clip"', 'body class="antialiased font-sans"')

    # Replace unpkg with cdnjs for AOS
    content = content.replace('https://unpkg.com/aos@2.3.1/dist/aos.css', 'https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css')
    content = content.replace('https://unpkg.com/aos@2.3.1/dist/aos.js', 'https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js')

    with open(file, 'w') as f:
        f.write(content)
        
    print(f"Fixed {file}")
