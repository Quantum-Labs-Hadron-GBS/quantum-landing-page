with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the inline style that broke FAQ
html = html.replace('max-height: 0rem;', 'max-height: 0px;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
