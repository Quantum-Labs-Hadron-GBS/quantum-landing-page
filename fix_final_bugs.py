def fix():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix maxTranslate for horizontal scroll
    # 1. First occurrence (around line 1559)
    target1 = 'const maxTranslate = qTrack.scrollWidth - wh;'
    replacement1 = 'const maxTranslate = qTrack.scrollWidth - window.innerWidth;'
    html = html.replace(target1, replacement1)

    # 2. Fix the blog cards being hidden on mobile
    target_blog1 = 'if (index === 1) classes = "group hidden md:flex flex-col gap-6 pt-0 has-pin has-pin--tr bg-white border border-black/5 p-4 shadow-sm hover:shadow-md transition-shadow";'
    replacement_blog1 = 'if (index === 1) classes = "group flex flex-col gap-6 pt-0 has-pin has-pin--tr bg-white border border-black/5 p-4 shadow-sm hover:shadow-md transition-shadow";'
    
    target_blog2 = 'if (index === 2) classes = "group hidden lg:flex flex-col gap-6 pt-0 has-pin has-pin--tr bg-white border border-black/5 p-4 shadow-sm hover:shadow-md transition-shadow";'
    replacement_blog2 = 'if (index === 2) classes = "group flex flex-col gap-6 pt-0 has-pin has-pin--tr bg-white border border-black/5 p-4 shadow-sm hover:shadow-md transition-shadow";'
    
    html = html.replace(target_blog1, replacement_blog1)
    html = html.replace(target_blog2, replacement_blog2)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

fix()
print("Fixed bugs")
