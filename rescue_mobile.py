import glob

def fix_z_index():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()

        # Fix z-index for main-header
        html = html.replace('id="main-header" class="fixed top-0 left-0 w-full z-[100]',
                            'id="main-header" class="fixed top-0 left-0 w-full z-[9999]')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

def fix_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Decouple the columns on mobile using absolute positioning so they don't stretch the grid
    # Left Col
    html = html.replace('id="left-col" class="relative z-10 w-full lg:max-w-sm flex flex-col justify-center pointer-events-none opacity-0 h-[50vh] lg:h-[43.75rem] lg:col-start-auto col-start-1 row-start-1"',
                        'id="left-col" class="max-md:absolute max-md:inset-0 max-md:px-6 max-md:items-center relative z-10 w-full lg:max-w-sm flex flex-col justify-center pointer-events-none opacity-0 h-full max-md:h-[100vh] lg:h-[43.75rem] lg:col-start-auto col-start-1 row-start-1"')
    
    # Middle Col
    html = html.replace('id="middle-col-placeholder"\n                        class="relative w-full h-[21.875rem] lg:h-[43.75rem] pointer-events-none mt-4 lg:mt-0 lg:col-start-auto col-start-1 row-start-1"',
                        'id="middle-col-placeholder"\n                        class="max-md:absolute max-md:inset-0 max-md:px-6 max-md:flex max-md:flex-col max-md:justify-center relative w-full h-[21.875rem] lg:h-[43.75rem] pointer-events-none mt-4 lg:mt-0 lg:col-start-auto col-start-1 row-start-1"')

    # Right Col
    html = html.replace('id="right-col" class="relative w-full h-auto lg:h-[43.75rem] flex flex-col gap-3 pointer-events-auto mt-2 lg:col-start-auto col-start-1 row-start-1 pt-12 lg:pt-0"',
                        'id="right-col" class="max-md:absolute max-md:left-6 max-md:right-6 max-md:top-[10vh] relative w-full h-auto lg:h-[43.75rem] flex flex-col gap-3 pointer-events-auto mt-2 lg:col-start-auto col-start-1 row-start-1 pt-12 lg:pt-0"')


    # 2. Fix the JS Math (replace 0.8 / 0.1 with 1 / 0 and -1)
    # Left Y
    target_left_y = """                        let leftY = window.innerHeight;
                        let leftOp = 0;
                        if (progress >= 0.1 && progress < 0.25) {
                            const p = (progress - 0.1) / 0.15;
                            leftY = mapRange(p, 0, 1, window.innerHeight * 0.8, window.innerHeight * 0.1);
                            leftOp = mapRange(p, 0, 1, 0, 1);
                        } else if (progress >= 0.25 && progress < 0.4) {
                            const p = (progress - 0.25) / 0.15;
                            leftY = mapRange(p, 0, 1, window.innerHeight * 0.1, -window.innerHeight * 0.5);
                            leftOp = mapRange(p, 0, 1, 1, 0);
                        } else if (progress < 0.1) {
                            leftY = window.innerHeight * 0.8;
                        } else {
                            leftY = -window.innerHeight * 0.5;
                        }"""
    
    replace_left_y = """                        let leftY = window.innerHeight;
                        let leftOp = 0;
                        if (progress >= 0.1 && progress < 0.25) {
                            const p = (progress - 0.1) / 0.15;
                            leftY = mapRange(p, 0, 1, window.innerHeight, 0);
                            leftOp = mapRange(p, 0, 1, 0, 1);
                        } else if (progress >= 0.25 && progress < 0.4) {
                            const p = (progress - 0.25) / 0.15;
                            leftY = mapRange(p, 0, 1, 0, -window.innerHeight);
                            leftOp = mapRange(p, 0, 1, 1, 0);
                        } else if (progress < 0.1) {
                            leftY = window.innerHeight;
                        } else {
                            leftY = -window.innerHeight;
                        }"""
    html = html.replace(target_left_y, replace_left_y)

    # Mid Y
    target_mid_y = """                        let midY = window.innerHeight;
                        let midOp = 0;
                        if (progress >= 0.3 && progress < 0.45) {
                            const p = (progress - 0.3) / 0.15;
                            midY = mapRange(p, 0, 1, window.innerHeight * 0.8, window.innerHeight * 0.2);
                            midOp = mapRange(p, 0, 1, 0, 1);
                        } else if (progress >= 0.45 && progress < 0.55) {
                            const p = (progress - 0.45) / 0.1;
                            midY = mapRange(p, 0, 1, window.innerHeight * 0.2, -window.innerHeight * 0.5);
                            midOp = mapRange(p, 0, 1, 1, 0);
                        } else if (progress < 0.3) {
                            midY = window.innerHeight * 0.8;
                        } else {
                            midY = -window.innerHeight * 0.5;
                        }"""

    replace_mid_y = """                        let midY = window.innerHeight;
                        let midOp = 0;
                        if (progress >= 0.3 && progress < 0.45) {
                            const p = (progress - 0.3) / 0.15;
                            midY = mapRange(p, 0, 1, window.innerHeight, 0);
                            midOp = mapRange(p, 0, 1, 0, 1);
                        } else if (progress >= 0.45 && progress < 0.55) {
                            const p = (progress - 0.45) / 0.1;
                            midY = mapRange(p, 0, 1, 0, -window.innerHeight);
                            midOp = mapRange(p, 0, 1, 1, 0);
                        } else if (progress < 0.3) {
                            midY = window.innerHeight;
                        } else {
                            midY = -window.innerHeight;
                        }"""
    html = html.replace(target_mid_y, replace_mid_y)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

fix_z_index()
fix_index()
print("Mobile Structural Rescue applied!")
