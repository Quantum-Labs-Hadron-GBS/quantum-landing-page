import re
import os

files = [
    'how-we-work.html',
    'ai-infrastructure.html',
    'pqc-security.html',
    'quantum-technology.html'
]

old_js = """            const mainHeader = document.getElementById('main-header');
            window.addEventListener('scroll', () => {
                if (mainHeader) mainHeader.style.transform = window.scrollY > 50 ? 'translateY(10px)' : 'translateY(0)';
                const btt = document.getElementById('back-to-top');"""

new_js = """            const mainHeader = document.getElementById('main-header');
            window.addEventListener('scroll', () => {
                if (mainHeader) {
                    mainHeader.style.transform = window.scrollY > 50 ? 'translateY(10px)' : 'translateY(0)';
                    const hero = document.querySelector('.bg-black');
                    const threshold = hero ? hero.offsetHeight - 50 : window.innerHeight * 0.5;
                    if (window.scrollY > threshold) {
                        mainHeader.classList.add('header-light-mode');
                        mainHeader.classList.remove('header-dark-mode');
                    } else {
                        mainHeader.classList.add('header-dark-mode');
                        mainHeader.classList.remove('header-light-mode');
                    }
                }
                const btt = document.getElementById('back-to-top');"""

for file in files:
    if os.path.exists(file):
        with open(file, 'r') as f:
            content = f.read()
        
        if old_js in content:
            new_content = content.replace(old_js, new_js)
            with open(file, 'w') as f:
                f.write(new_content)
            print(f"Updated {file}")
        else:
            print(f"Pattern not found in {file}")
