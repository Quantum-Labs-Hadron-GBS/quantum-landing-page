def fix():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Right Col
    html = html.replace('id="right-col" class="max-lg:absolute max-lg:inset-0 max-lg:h-[100vh] relative w-full h-auto lg:h-[43.75rem] flex flex-col gap-3 pointer-events-auto lg:col-start-auto col-start-1 row-start-1 pt-12 lg:pt-0"',
                        'id="right-col" class="max-lg:absolute max-lg:top-0 max-lg:left-6 max-lg:right-6 relative w-full h-auto lg:h-[43.75rem] flex flex-col gap-3 pointer-events-auto lg:col-start-auto col-start-1 row-start-1 pt-12 lg:pt-0"')

    # Put back targetEndRightY logic for mobile JS
    target_right_js = """                        const rightColContainer = document.getElementById('right-col');
                        const rightColY = mapRange(progress, 0.55, 1.0, window.innerHeight, -window.innerHeight * 0.5);
                        rightColContainer.style.transform = `translateY(${rightColY}px)`;"""

    replace_right_js = """                        const rightColContainer = document.getElementById('right-col');
                        const targetEndRightY = (window.innerHeight * 0.5) - rightColContainer.offsetHeight;
                        const rightColY = mapRange(progress, 0.55, 1.0, window.innerHeight, targetEndRightY);
                        rightColContainer.style.transform = `translateY(${rightColY}px)`;"""

    html = html.replace(target_right_js, replace_right_js)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

fix()
