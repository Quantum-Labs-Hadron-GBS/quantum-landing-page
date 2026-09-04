import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix body tag
html = html.replace('overflow-x-hidden', 'overflow-x-clip')

# 2. Fix 'Where Quantum Matters' typography
html = html.replace(
    'class="text-5xl md:text-7xl font-medium tracking-tight text-brand-dark mb-6 leading-tight"',
    'class="text-[clamp(2.5rem,7vw,5rem)] font-medium tracking-tight text-brand-dark mb-6 leading-[1.1]"'
)

# Fix background image of transition section
html = html.replace(
    'style="height: 95%; top: -25%; left: 50%; transform: translateX(-50%); mix-blend-mode: multiply; -webkit-mask-image: linear-gradient(to bottom, black 50%, transparent 90%); mask-image: linear-gradient(to bottom, black 50%, transparent 90%); will-change: transform;"',
    'style="height: auto; min-height: 95%; max-width: 180%; top: -15%; left: 50%; transform: translateX(-50%); mix-blend-mode: multiply; -webkit-mask-image: linear-gradient(to bottom, black 50%, transparent 90%); mask-image: linear-gradient(to bottom, black 50%, transparent 90%); will-change: transform;"'
)

# 3. Horizontal Carousel Cards Mobile Width (75vw -> 85vw)
html = html.replace('w-[75vw]', 'w-[85vw]')

# 4. JS Engine Pointer Events
# For left-col:
js_left_col_old = """                                // Show left col
                                leftCol.style.opacity = Math.min(1, layerProgress * 5);
                                leftCol.style.transform = `translateY(${10 - (layerProgress * 30)}px)`;"""
js_left_col_new = """                                // Show left col
                                leftCol.style.opacity = Math.min(1, layerProgress * 5);
                                leftCol.style.pointerEvents = layerProgress > 0.3 ? 'none' : 'auto';
                                leftCol.style.transform = `translateY(${10 - (layerProgress * 30)}px)`;"""
html = html.replace(js_left_col_old, js_left_col_new)

js_graph_old = """                            if (layerProgress > 0.25 && layerProgress <= 0.66) {
                                // Middle phase (0.33 to 0.66): Graph is active
                                const graphProgress = (layerProgress - 0.25) / 0.41;
                                graphContent.style.opacity = Math.min(1, graphProgress * 5);
                                graphContent.style.transform = `translateY(${20 - (graphProgress * 20)}px)`;"""
js_graph_new = """                            if (layerProgress > 0.25 && layerProgress <= 0.66) {
                                // Middle phase (0.33 to 0.66): Graph is active
                                const graphProgress = (layerProgress - 0.25) / 0.41;
                                graphContent.style.opacity = Math.min(1, graphProgress * 5);
                                graphContent.style.pointerEvents = (graphProgress > 0.1 && layerProgress <= 0.55) ? 'auto' : 'none';
                                graphContent.style.transform = `translateY(${20 - (graphProgress * 20)}px)`;"""
html = html.replace(js_graph_old, js_graph_new)

js_graph_hide_old = """                                // Fade out graph
                                const fadeOutProgress = (layerProgress - 0.66) / 0.34;
                                graphContent.style.opacity = Math.max(0, 1 - (fadeOutProgress * 5));
                                graphContent.style.transform = `translateY(${-fadeOutProgress * 20}px)`;"""
js_graph_hide_new = """                                // Fade out graph
                                const fadeOutProgress = (layerProgress - 0.66) / 0.34;
                                graphContent.style.opacity = Math.max(0, 1 - (fadeOutProgress * 5));
                                graphContent.style.pointerEvents = 'none';
                                graphContent.style.transform = `translateY(${-fadeOutProgress * 20}px)`;"""
html = html.replace(js_graph_hide_old, js_graph_hide_new)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html polished successfully")
