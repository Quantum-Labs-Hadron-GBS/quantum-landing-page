import re

def fix():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Left Col Parent
    html = html.replace('<div class="w-full h-full relative lg:col-start-auto col-start-1 row-start-1">',
                        '<div class="max-lg:absolute max-lg:inset-0 max-lg:h-[100vh] w-full h-full relative lg:col-start-auto col-start-1 row-start-1">')

    # 2. Left Col
    html = html.replace('id="left-col" class="absolute top-0 left-0 w-full flex flex-col pointer-events-auto mt-2"',
                        'id="left-col" class="max-lg:absolute max-lg:inset-0 max-lg:justify-center absolute top-0 left-0 w-full flex flex-col pointer-events-auto max-lg:mt-0 mt-2"')

    # 3. Middle Col
    # Need to regex it because it might have my old max-md garbage
    middle_pattern = r'<div id="middle-col-placeholder"[^>]*>'
    middle_replacement = '<div id="middle-col-placeholder" class="max-lg:absolute max-lg:inset-0 max-lg:h-[100vh] max-lg:flex max-lg:flex-col max-lg:justify-center relative w-full lg:h-[43.75rem] pointer-events-none mt-4 lg:mt-0 lg:col-start-auto col-start-1 row-start-1">'
    html = re.sub(middle_pattern, middle_replacement, html)

    # 3b. graph-content
    html = html.replace('id="graph-content"\n                            class="absolute inset-0 opacity-0 flex flex-col p-8 lg:p-10 pointer-events-auto bg-[#1a1a1a] rounded-[2rem] lg:bg-transparent lg:rounded-none shadow-2xl lg:shadow-none"',
                        'id="graph-content"\n                            class="max-lg:relative max-lg:h-auto max-lg:w-[90%] max-lg:mx-auto absolute inset-0 opacity-0 flex flex-col p-8 lg:p-10 pointer-events-auto bg-[#1a1a1a] rounded-[2rem] lg:bg-transparent lg:rounded-none shadow-2xl lg:shadow-none"')

    # 4. Right Col
    right_pattern = r'<div id="right-col" class="[^"]*">'
    right_replacement = '<div id="right-col" class="max-lg:absolute max-lg:inset-0 max-lg:h-[100vh] max-lg:justify-center relative w-full h-auto lg:h-[43.75rem] flex flex-col gap-3 pointer-events-auto lg:col-start-auto col-start-1 row-start-1 pt-12 lg:pt-0">'
    html = re.sub(right_pattern, right_replacement, html)

    # 5. Fix JS Math offsets
    # We want translateY(0) to be perfectly centered since the containers are 100vh and justify-center.
    # We already did this mapping in the previous script!
    # Let's verify: `leftY = mapRange(p, 0, 1, window.innerHeight, 0);`
    # Let's ensure rightColY starts from window.innerHeight and goes to targetEndRightY.
    # Wait, if rightCol is 100vh and justify-center, it centers the 4 cards.
    # If we want the cards to scroll through the screen:
    # rightColY = mapRange(progress, 0.55, 1.0, window.innerHeight, -window.innerHeight);
    # This will slide the cards up from bottom to top!
    
    # Let's replace the JS for rightCol
    target_right_js = """                        const rightColContainer = document.getElementById('right-col');
                        const targetEndRightY = (window.innerHeight * 0.5) - rightColContainer.offsetHeight;
                        const rightColY = mapRange(progress, 0.55, 1.0, window.innerHeight, targetEndRightY);
                        rightColContainer.style.transform = `translateY(${rightColY}px)`;"""

    replace_right_js = """                        const rightColContainer = document.getElementById('right-col');
                        const rightColY = mapRange(progress, 0.55, 1.0, window.innerHeight, -window.innerHeight * 0.5);
                        rightColContainer.style.transform = `translateY(${rightColY}px)`;"""
    
    html = html.replace(target_right_js, replace_right_js)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

fix()
print("Success")
