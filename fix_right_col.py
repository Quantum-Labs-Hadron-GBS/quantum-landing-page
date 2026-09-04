def fix():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Right Col
    html = html.replace('id="right-col" class="max-lg:absolute max-lg:inset-0 max-lg:h-[100vh] max-lg:justify-center relative w-full h-auto lg:h-[43.75rem] flex flex-col gap-3 pointer-events-auto lg:col-start-auto col-start-1 row-start-1 pt-12 lg:pt-0"',
                        'id="right-col" class="max-lg:absolute max-lg:inset-0 max-lg:h-[100vh] relative w-full h-auto lg:h-[43.75rem] flex flex-col gap-3 pointer-events-auto lg:col-start-auto col-start-1 row-start-1 pt-12 lg:pt-0"')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

fix()
