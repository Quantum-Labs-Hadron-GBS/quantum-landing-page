import re

# Read a good file (like index.html) to extract the mobile menu
with open('index.html', 'r') as f:
    index_content = f.read()

mobile_menu_start = index_content.find('<div id="mobile-menu"')
mobile_menu_end = index_content.find('</div>\n\n    <!-- Sticky Scroll')
if mobile_menu_end == -1:
    mobile_menu_end = index_content.find('<!-- Sticky Scroll') # or whatever is after
    
# Let's extract properly using simple string splitting
start_tag = '<!-- Mobile Menu Overlay -->'
end_tag = '<!-- Sticky Scroll Sequence Container -->'

if start_tag in index_content and end_tag in index_content:
    mobile_menu = start_tag + index_content.split(start_tag)[1].split(end_tag)[0]
else:
    # fallback to just finding the div
    mm_start = index_content.find('<div id="mobile-menu"')
    mm_end = index_content.find('</div>', index_content.rfind('pointer-events-none -z-10"></div>')) + 6 # very hacky
    # Let's just hardcode the mobile menu block from our known good state to be absolutely safe
    pass

hardcoded_mobile_menu = """
    <!-- Mobile Menu Overlay -->
    <div id="mobile-menu" class="fixed inset-0 bg-white/95 backdrop-blur-xl z-[9998] opacity-0 pointer-events-none transition-all duration-300 flex flex-col justify-center px-10" aria-hidden="true">
        <nav class="flex flex-col gap-8 text-3xl font-medium tracking-tight">
            <a href="blogs.html" class="mobile-link text-brand-dark/70 hover:text-brand-dark transition-colors">Blogs</a>
            <div class="flex flex-col gap-4">
                <a href="javascript:void(0)" class="mobile-link text-brand-dark/70 hover:text-brand-dark transition-colors cursor-default">Enterprise Solutions</a>
                <div class="flex flex-col gap-3 pl-6 border-l-2 border-brand-dark/10">
                    <a href="quantum-technology.html" class="text-xl font-medium text-brand-dark/60 hover:text-brand-dark transition-colors">Quantum Technology</a>
                    <a href="ai-infrastructure.html" class="text-xl font-medium text-brand-dark/60 hover:text-brand-dark transition-colors">AI Infrastructure</a>
                    <a href="pqc-security.html" class="text-xl font-medium text-brand-dark/60 hover:text-brand-dark transition-colors">PQC Security</a>
                </div>
            </div>
            <a href="why-quantum.html" class="mobile-link text-brand-dark/70 hover:text-brand-dark transition-colors">Why Quantum?</a>
            <a href="how-we-work.html" class="mobile-link text-brand-dark/70 hover:text-brand-dark transition-colors">How We Work</a>
            <a href="contact.html" class="mobile-link text-brand-orange hover:text-brand-orange/80 transition-colors">Contact Us</a>
            <div class="h-[1px] w-12 bg-brand-dark/10 my-2"></div>
            <a href="https://www.hadrongbs.com" target="_blank" rel="noopener" class="text-brand-dark/40 hover:text-brand-dark transition-colors flex items-center gap-2 text-xl">
                Hadron GBS Main Site
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6"/><path d="M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/></svg>
            </a>
        </nav>
        <div class="absolute bottom-0 right-0 w-[500px] h-[500px] bg-[radial-gradient(ellipse_at_bottom_right,rgba(255,159,43,0.15),transparent_60%)] pointer-events-none -z-10"></div>
    </div>
"""

with open('why-quantum.html', 'r') as f:
    content = f.read()

# 1. Remove the misplaced mobile link from desktop navbar
content = re.sub(r'\s*<a href="why-quantum\.html" class="mobile-link.*?">Why Quantum\?</a>', '', content)

# 2. Insert the mobile menu immediately after </header>
if 'id="mobile-menu"' not in content:
    header_end = content.find('</header>') + len('</header>')
    content = content[:header_end] + "\n" + hardcoded_mobile_menu + "\n" + content[header_end:]

with open('why-quantum.html', 'w') as f:
    f.write(content)

print("Fixed why-quantum.html")
