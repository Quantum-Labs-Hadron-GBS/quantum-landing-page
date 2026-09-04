def fix():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    target = 'class="max-w-[87.5rem] mx-auto h-full grid grid-cols-1 lg:grid-cols-[1fr_1.2fr_1fr] gap-8 lg:gap-16 items-center pt-[5rem] px-6 md:px-8"'
    replacement = 'class="max-w-[87.5rem] mx-auto h-full grid grid-cols-1 lg:grid-cols-[1fr_1.2fr_1fr] gap-8 lg:gap-16 max-lg:items-start max-lg:pt-0 lg:items-center lg:pt-[5rem] px-6 md:px-8"'
    html = html.replace(target, replacement)

    # To be absolutely sure, let's also adjust the JS math to NOT translate so much.
    # Moving from 100vh to -100vh means it flies across the screen super fast.
    # We can just map from 15vh to -15vh.
    # This creates a gentle slide up, removing any feeling of "huge gap" during the transition!
    
    # Left Y
    target_left_y = """                        if (progress >= 0.1 && progress < 0.25) {
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
    
    replace_left_y = """                        if (progress >= 0.1 && progress < 0.25) {
                            const p = (progress - 0.1) / 0.15;
                            leftY = mapRange(p, 0, 1, window.innerHeight * 0.15, 0);
                            leftOp = mapRange(p, 0, 1, 0, 1);
                        } else if (progress >= 0.25 && progress < 0.4) {
                            const p = (progress - 0.25) / 0.15;
                            leftY = mapRange(p, 0, 1, 0, -window.innerHeight * 0.15);
                            leftOp = mapRange(p, 0, 1, 1, 0);
                        } else if (progress < 0.1) {
                            leftY = window.innerHeight * 0.15;
                        } else {
                            leftY = -window.innerHeight * 0.15;
                        }"""
    html = html.replace(target_left_y, replace_left_y)

    # Mid Y
    target_mid_y = """                        if (progress >= 0.3 && progress < 0.45) {
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
    
    replace_mid_y = """                        if (progress >= 0.3 && progress < 0.45) {
                            const p = (progress - 0.3) / 0.15;
                            midY = mapRange(p, 0, 1, window.innerHeight * 0.15, 0);
                            midOp = mapRange(p, 0, 1, 0, 1);
                        } else if (progress >= 0.45 && progress < 0.55) {
                            const p = (progress - 0.45) / 0.1;
                            midY = mapRange(p, 0, 1, 0, -window.innerHeight * 0.15);
                            midOp = mapRange(p, 0, 1, 1, 0);
                        } else if (progress < 0.3) {
                            midY = window.innerHeight * 0.15;
                        } else {
                            midY = -window.innerHeight * 0.15;
                        }"""
    html = html.replace(target_mid_y, replace_mid_y)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

fix()
print("Grid and animation math fixed")
