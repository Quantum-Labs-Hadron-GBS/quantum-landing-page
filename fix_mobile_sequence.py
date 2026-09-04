import glob

def fix_all_html():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()

        # Fix z-[60] to z-[9999] for mobile menu button
        html = html.replace('z-[60]', 'z-[9999]')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

def fix_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Hide hero news card on mobile
    target_card = '<div class="absolute bottom-[20%] left-1/2 -translate-x-1/2 w-[90%] md:bottom-[10.6%] md:left-auto md:right-[calc(8.1%-10px)] md:-translate-x-0 md:w-[22%] md:min-w-[18.75rem]">'
    replacement_card = '<div class="absolute hidden md:block bottom-[20%] left-1/2 -translate-x-1/2 w-[90%] md:bottom-[10.6%] md:left-auto md:right-[calc(8.1%-10px)] md:-translate-x-0 md:w-[22%] md:min-w-[18.75rem]">'
    html = html.replace(target_card, replacement_card)

    # Compress Text timeline
    target_text = """                        let leftY = window.innerHeight;
                        let leftOp = 0;
                        if (progress >= 0.2 && progress < 0.35) {
                            const p = (progress - 0.2) / 0.15;
                            leftY = mapRange(p, 0, 1, window.innerHeight * 0.8, window.innerHeight * 0.1);
                            leftOp = mapRange(p, 0, 1, 0, 1);
                        } else if (progress >= 0.35 && progress < 0.5) {
                            const p = (progress - 0.35) / 0.15;
                            leftY = mapRange(p, 0, 1, window.innerHeight * 0.1, -window.innerHeight * 0.5);
                            leftOp = mapRange(p, 0, 1, 1, 0);
                        } else if (progress < 0.2) {
                            leftY = window.innerHeight * 0.8;
                        } else {
                            leftY = -window.innerHeight * 0.5;
                        }"""
    replacement_text = """                        let leftY = window.innerHeight;
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
    html = html.replace(target_text, replacement_text)

    # Compress Graph timeline
    target_graph = """                        let midY = window.innerHeight;
                        let midOp = 0;
                        if (progress >= 0.45 && progress < 0.6) {
                            const p = (progress - 0.45) / 0.15;
                            midY = mapRange(p, 0, 1, window.innerHeight * 0.8, window.innerHeight * 0.2);
                            midOp = mapRange(p, 0, 1, 0, 1);
                        } else if (progress >= 0.6 && progress < 0.75) {
                            const p = (progress - 0.6) / 0.15;
                            midY = mapRange(p, 0, 1, window.innerHeight * 0.2, -window.innerHeight * 0.5);
                            midOp = mapRange(p, 0, 1, 1, 0);
                        } else if (progress < 0.45) {
                            midY = window.innerHeight * 0.8;
                        } else {
                            midY = -window.innerHeight * 0.5;
                        }"""
    replacement_graph = """                        let midY = window.innerHeight;
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
    html = html.replace(target_graph, replacement_graph)

    # Compress Cards timeline
    target_cards = """                        const rightColContainer = document.getElementById('right-col');
                        const targetEndRightY = (window.innerHeight * 0.5) - rightColContainer.offsetHeight;
                        const rightColY = mapRange(progress, 0.6, 1.0, window.innerHeight, targetEndRightY);
                        rightColContainer.style.transform = `translateY(${rightColY}px)`;

                        const rightScroll = mapRange(progress, 0.6, 1.0, 0, 1);"""
    replacement_cards = """                        const rightColContainer = document.getElementById('right-col');
                        const targetEndRightY = (window.innerHeight * 0.5) - rightColContainer.offsetHeight;
                        const rightColY = mapRange(progress, 0.55, 1.0, window.innerHeight, targetEndRightY);
                        rightColContainer.style.transform = `translateY(${rightColY}px)`;

                        const rightScroll = mapRange(progress, 0.55, 1.0, 0, 1);"""
    html = html.replace(target_cards, replacement_cards)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

fix_all_html()
fix_index()
print("Mobile JS sequence fixes applied!")
