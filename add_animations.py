import os
import re

files_to_animate = ['quantum-technology.html', 'ai-infrastructure.html', 'pqc-security.html']

for filename in files_to_animate:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add AOS CSS to head if not present
    if "aos.css" not in html:
        html = html.replace('</head>', '    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\n</head>')

    # 2. Add AOS JS to body if not present
    if "aos.js" not in html:
        aos_script = """
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            AOS.init({
                duration: 800,
                once: true,
                offset: 100,
                easing: 'ease-out-cubic'
            });
        });
    </script>
</body>"""
        html = html.replace('</body>', aos_script)

    # 3. Animate Headers (sharplink-h2)
    # Be careful not to add it multiple times
    if 'data-aos="fade-up"' not in html:
        # Add to headers
        html = re.sub(r'(class="sharplink-h2[^"]*")', r'\1 data-aos="fade-up"', html)
        
        # Add to glass cards
        html = re.sub(r'(class="bg-white/40 backdrop-blur-md[^"]*")', r'\1 data-aos="fade-up" data-aos-delay="100"', html)
        
        # Add to the "How we approach it" step cards (ai-infrastructure)
        html = re.sub(r'(class="flex flex-col items-center text-center p-6 bg-white rounded-3xl[^"]*")', r'\1 data-aos="zoom-in" data-aos-delay="50"', html)
        
        # Add to big black deliverables cards
        html = re.sub(r'(class="bg-black text-white p-12 rounded-3xl[^"]*")', r'\1 data-aos="fade-left" data-aos-delay="200"', html)
        
        # Add to the "Business Problem Discovery" step rows (quantum-technology, pqc-security)
        html = re.sub(r'(<div class="flex items-start gap-4">|<div class="flex gap-4">)', r'\1 data-aos="fade-up"', html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Animated {filename}")
