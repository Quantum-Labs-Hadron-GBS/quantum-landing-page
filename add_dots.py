import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '<div class="absolute inset-0 w-full h-full pointer-events-none" style="background-image: linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px); background-size: 100px 100px;"></div>'

replacement = """        <!-- Background Grid & Floating Dots -->
        <div class="absolute inset-0 w-full h-full pointer-events-none overflow-hidden" style="background-image: linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px); background-size: 100px 100px;">
            <!-- Orange Grid Anchors -->
            <div class="absolute w-1.5 h-1.5 bg-brand-orange shadow-[0_0_12px_rgba(255,159,43,0.8)]" style="top: 300px; left: 200px; transform: translate(-50%, -50%);"></div>
            <div class="absolute w-2 h-2 bg-brand-orange shadow-[0_0_15px_rgba(255,159,43,0.6)]" style="top: 800px; left: 800px; transform: translate(-50%, -50%); opacity: 0.6;"></div>
            <div class="absolute w-1.5 h-1.5 bg-brand-orange shadow-[0_0_10px_rgba(255,159,43,0.8)]" style="top: 1500px; left: 300px; transform: translate(-50%, -50%); opacity: 0.9;"></div>
            <div class="absolute w-2 h-2 bg-brand-orange shadow-[0_0_10px_rgba(255,159,43,0.5)]" style="top: 2200px; left: 1100px; transform: translate(-50%, -50%); opacity: 0.4;"></div>
            <div class="absolute w-1.5 h-1.5 bg-brand-orange shadow-[0_0_12px_rgba(255,159,43,0.7)]" style="top: 3100px; left: 500px; transform: translate(-50%, -50%); opacity: 0.8;"></div>
            
            <!-- Secondary White Dots -->
            <div class="absolute w-1 h-1 bg-white shadow-[0_0_8px_rgba(255,255,255,0.4)]" style="top: 1100px; left: 100px; transform: translate(-50%, -50%); opacity: 0.5;"></div>
            <div class="absolute w-1 h-1 bg-white shadow-[0_0_8px_rgba(255,255,255,0.4)]" style="top: 2700px; left: 700px; transform: translate(-50%, -50%); opacity: 0.3;"></div>
            <div class="absolute w-1 h-1 bg-white shadow-[0_0_8px_rgba(255,255,255,0.4)]" style="top: 500px; left: 1300px; transform: translate(-50%, -50%); opacity: 0.4;"></div>
            <div class="absolute w-1 h-1 bg-brand-orange shadow-[0_0_8px_rgba(255,159,43,0.4)]" style="top: 3600px; left: 200px; transform: translate(-50%, -50%); opacity: 0.5;"></div>
        </div>"""

html = html.replace(target, replacement)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
