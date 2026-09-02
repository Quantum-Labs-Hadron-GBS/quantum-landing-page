import os
import re

css_to_add = """
        /* Dynamic Navbar Adaptability */
        .header-light-mode #header-logo { filter: invert(1) brightness(0) !important; }
        .header-light-mode #header-nav { background-color: rgba(0,0,0,0.05) !important; }
        .header-light-mode .nav-link { color: #0a0a0a !important; border-color: rgba(0,0,0,0.15) !important; }
        .header-light-mode #mobile-menu-btn { color: #0a0a0a !important; }
"""

def update_css(content):
    if "Dynamic Navbar Adaptability" not in content:
        # Before closing </style>
        content = content.replace("</style>", css_to_add + "\n    </style>", 1)
    return content

def update_header(content, active_page):
    # We will replace the entire <header id="main-header"...> ... </header> block
    start_str = '<header id="main-header"'
    end_str = '</header>'
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str, start_idx) + len(end_str)
    
    if start_idx == -1 or end_idx == -1:
        return content
        
    blogs_active = 'style="background:rgba(255,159,43,0.1); color:#ff9f2b !important; border-color:rgba(255,159,43,0.2) !important;"' if active_page == 'blogs' else ''
    contact_active = 'style="background:rgba(255,159,43,0.1); color:#ff9f2b !important; border-color:rgba(255,159,43,0.2) !important;"' if active_page == 'contact' else ''
    
    new_header = f'''<header id="main-header" class="fixed top-0 left-0 w-full z-[100] flex justify-center header-light-mode" style="transition: transform 0.3s ease;">
        <div class="w-full max-w-[1400px] flex items-center justify-between pl-6 md:pl-8 pr-0">
            <a href="/" class="flex items-center gap-2 py-3 md:py-4">
                <img id="header-logo" src="https://res.cloudinary.com/ax6dtcht/image/upload/v1786087098/Hadron_Quantum_Logo_Final_Monochrome_white-06_vbvvqu.png" alt="Hadron Quantum Labs"
                    class="h-9 md:h-10 w-auto" style="transition: filter 0.3s;" />
            </a>
            <nav class="hidden md:flex items-stretch text-xs font-bold tracking-wide text-white bg-white/10 backdrop-blur-md border-l border-white/20 transition-colors"
                style="height: 44px;" id="header-nav">
                <a href="/" class="nav-link flex items-center px-6 border-r border-white/20 hover:bg-white/20 transition-colors">HOME</a>
                <a href="/blogs.html" class="nav-link flex items-center px-6 border-r border-white/20 hover:bg-white/20 transition-colors" {blogs_active}>BLOGS</a>
                <a href="/#solutions" class="nav-link flex items-center px-6 border-r border-white/20 hover:bg-white/20 transition-colors">SOLUTIONS</a>
                <a href="/#workflow" class="nav-link flex items-center px-6 border-r border-white/20 hover:bg-white/20 transition-colors">WORKFLOW</a>
                <a href="/#pricing" class="nav-link flex items-center px-6 border-r border-white/20 hover:bg-white/20 transition-colors">OFFERINGS</a>
                <a href="/#faq-accordion" class="nav-link flex items-center px-6 border-r border-white/20 hover:bg-white/20 transition-colors">FAQ</a>
                <a href="/contact.html" class="nav-link flex items-center px-5 border-r border-white/20 hover:bg-white/20 transition-colors" {contact_active}>
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 12h14M12 5l7 7-7 7"></path></svg>
                </a>
            </nav>
            <button id="mobile-menu-btn" class="flex md:hidden items-center justify-center w-12 h-12 text-white absolute right-4 top-2 z-[60] transition-colors" aria-label="Open menu">
                <div class="w-6 h-3.5 relative flex flex-col justify-between cursor-pointer">
                    <span class="block h-0.5 w-full bg-current origin-center rounded-full transition-transform duration-300"></span>
                    <span class="block h-0.5 w-full bg-current origin-center rounded-full transition-transform duration-300"></span>
                </div>
            </button>
        </div>
    </header>'''
    
    return content[:start_idx] + new_header + content[end_idx:]

for filename, active in [('blogs.html', 'blogs'), ('article.html', 'blogs'), ('contact.html', 'contact')]:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = update_css(content)
    content = update_header(content, active)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

