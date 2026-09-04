import os
import re

desktop_style_str = 'style="background:rgba(255,159,43,0.1); color:#ff9f2b !important; border-color:rgba(255,159,43,0.2) !important;"'
desktop_style_str2 = ' style="background:rgba(255,159,43,0.1); color:#ff9f2b !important; border-color:rgba(255,159,43,0.2) !important;"'
mobile_style_str = 'style="color:#ff9f2b;"'
mobile_style_str2 = ' style="color:#ff9f2b;"'

js_snippet = """
    <!-- Dynamic Active Nav Script -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const currentPath = window.location.pathname.split('/').pop() || 'index.html';
            
            // Desktop Nav
            document.querySelectorAll('#header-nav .nav-link, #header-nav a:not(.nav-link)').forEach(link => {
                const href = link.getAttribute('href');
                if (!href || href === 'javascript:void(0)') return;
                
                // If the link matches exactly, or if we are on article.html and the link is blogs.html
                if (href === currentPath || (currentPath.startsWith('article.html') && href === 'blogs.html')) {
                    if (link.classList.contains('nav-link')) {
                        link.style.background = 'rgba(255,159,43,0.1)';
                        link.style.setProperty('color', '#ff9f2b', 'important');
                        link.style.setProperty('border-color', 'rgba(255,159,43,0.2)', 'important');
                    } else {
                        link.style.color = '#ff9f2b';
                    }
                } else {
                    link.style.background = '';
                    link.style.color = '';
                    link.style.borderColor = '';
                }
            });

            // Mobile Menu
            document.querySelectorAll('#mobile-menu a').forEach(link => {
                const href = link.getAttribute('href');
                if (!href || href === 'javascript:void(0)') return;
                
                if (href === currentPath || (currentPath.startsWith('article.html') && href === 'blogs.html')) {
                    link.style.setProperty('color', '#ff9f2b', 'important');
                } else {
                    link.style.color = '';
                }
            });
        });
    </script>
"""

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in html_files:
    if f.startswith('old_') or f.startswith('previous_') or f.startswith('google'):
        continue
        
    with open(f, 'r') as file:
        content = file.read()
        
    # Remove existing hardcoded styles
    content = content.replace(desktop_style_str2, '')
    content = content.replace(desktop_style_str, '')
    content = content.replace(mobile_style_str2, '')
    content = content.replace(mobile_style_str, '')
    
    # Remove existing dynamic nav script if we ran this before
    if "<!-- Dynamic Active Nav Script -->" in content:
        content = re.sub(r'\s*<!-- Dynamic Active Nav Script -->.*?<\/script>\n', '\n', content, flags=re.DOTALL)
        
    # Inject before </body>
    content = content.replace('</body>', js_snippet + '</body>')
    
    with open(f, 'w') as file:
        file.write(content)
        
    print(f"Updated {f}")
