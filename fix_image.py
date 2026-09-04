with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

bad_style = 'style="height: auto; min-height: 95%; max-width: 180%; top: -15%; left: 50%; transform: translateX(-50%); mix-blend-mode: multiply; -webkit-mask-image: linear-gradient(to bottom, black 50%, transparent 90%); mask-image: linear-gradient(to bottom, black 50%, transparent 90%); will-change: transform;"'
good_style = 'style="height: 95%; top: -25%; left: 50%; transform: translateX(-50%); mix-blend-mode: multiply; -webkit-mask-image: linear-gradient(to bottom, black 50%, transparent 90%); mask-image: linear-gradient(to bottom, black 50%, transparent 90%); will-change: transform;"'

html = html.replace(bad_style, good_style)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
