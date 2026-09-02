import os

files_to_fix = [
    'index.html',
    'blogs.html',
    'article.html',
    'contact.html'
]

replacements = {
    'href="/"': 'href="index.html"',
    'href="/blogs.html"': 'href="blogs.html"',
    'href="/contact.html"': 'href="contact.html"',
    'href="/#solutions"': 'href="index.html#solutions"',
    'href="/#workflow"': 'href="index.html#workflow"',
    'href="/#pricing"': 'href="index.html#pricing"',
    'href="/#faq-accordion"': 'href="index.html#faq-accordion"',
    'href="/#about"': 'href="index.html#about"',
    'href="/#pqc"': 'href="index.html#pqc"',
    'href="#solutions"': 'href="index.html#solutions"',
    'href="#workflow"': 'href="index.html#workflow"',
    'href="#pricing"': 'href="index.html#pricing"',
    'href="#faq-accordion"': 'href="index.html#faq-accordion"'
}

for filename in files_to_fix:
    path = os.path.join('/Users/inno/Desktop/Quantum-website/quantum-landing-page', filename)
    if not os.path.exists(path):
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Be careful, index.html might want its hash links to just be hash links to avoid reloading
    if filename == 'index.html':
        # For index.html, we want #solutions to stay #solutions so it smooth scrolls instead of reloading!
        # But we DO want to fix href="/" -> href="index.html", etc.
        index_repl = {
            'href="/"': 'href="index.html"',
            'href="/blogs.html"': 'href="blogs.html"',
            'href="/contact.html"': 'href="contact.html"',
            'href="/#solutions"': 'href="#solutions"',
            'href="/#workflow"': 'href="#workflow"',
            'href="/#pricing"': 'href="#pricing"',
            'href="/#faq-accordion"': 'href="#faq-accordion"',
            'href="/#about"': 'href="#about"',
            'href="/#pqc"': 'href="#pqc"'
        }
        for k, v in index_repl.items():
            content = content.replace(k, v)
    else:
        for k, v in replacements.items():
            content = content.replace(k, v)
            
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Links updated successfully.")
