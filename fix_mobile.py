import re
import glob

def fix_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Bug 1: Hero News Card Anchoring
    # Original: <div class="absolute" style="bottom: 10.6%; right: calc(8.1% - 10px); width: 22%; min-width: 18.75rem;">
    target_hero = '<div class="absolute" style="bottom: 10.6%; right: calc(8.1% - 10px); width: 22%; min-width: 18.75rem;">'
    replacement_hero = '<div class="absolute bottom-[20%] left-1/2 -translate-x-1/2 w-[90%] md:bottom-[10.6%] md:left-auto md:right-[calc(8.1%-10px)] md:-translate-x-0 md:w-[22%] md:min-w-[18.75rem]">'
    html = html.replace(target_hero, replacement_hero)

    # Bug 3: Where Quantum Matters Image Blocking
    # Original style="height: 95%; top: -25%; left: 50%; transform: translateX(-50%); mix-blend-mode: multiply; ..."
    # We will strip height and top from the inline style and add tailwind classes.
    html = html.replace('alt="Quantum Computer Core" class="absolute z-10 w-auto object-contain"\n                style="height: 95%; top: -25%;',
                        'alt="Quantum Computer Core" class="absolute z-10 w-auto object-contain h-[75%] top-[10%] md:h-[95%] md:top-[-25%]"\n                style="')

    # Bug 4: Horizontal Scroll Card Overflow
    # Track
    html = html.replace('id="quantum-track" class="flex items-center w-[max-content] h-[25rem] md:h-[30rem]',
                        'id="quantum-track" class="flex items-center w-[max-content] h-auto py-12 md:py-0 md:h-[30rem]')
    # Cards
    html = html.replace('class="w-[85vw] md:w-[56vw] h-full max-h-[30rem]',
                        'class="w-[85vw] md:w-[56vw] h-auto min-h-[25rem] md:h-full md:max-h-[30rem]')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

def fix_all_files():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()

        # Bug 2: Mobile Menu Overlay Scroll
        html = html.replace('class="fixed inset-0 bg-white/95 backdrop-blur-xl z-[9998] opacity-0 pointer-events-none transition-all duration-300 flex flex-col justify-center px-10"',
                            'class="fixed inset-0 bg-white/95 backdrop-blur-xl z-[9998] opacity-0 pointer-events-none transition-all duration-300 flex flex-col justify-start md:justify-center pt-24 pb-12 overflow-y-auto px-10"')

        # Bug 5: Typography Clamps (reducing 2.5rem floor to 2rem to prevent breaking on 390px)
        html = html.replace('text-[clamp(2.5rem,', 'text-[clamp(2rem,')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

fix_index()
fix_all_files()
print("Mobile bug fixes applied!")
