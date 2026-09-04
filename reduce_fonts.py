import re

with open('why-quantum.html', 'r') as f:
    content = f.read()

replacements = {
    # Hero
    r'text-\[clamp\(3rem,6vw,7rem\)\]': r'text-[clamp(2.5rem,5vw,5.5rem)]',
    
    # Internet
    r'text-\[clamp\(4rem,9vw,9rem\)\]': r'text-[clamp(3rem,7vw,7rem)]',
    
    # Harvest Now
    r'text-\[clamp\(4\.5rem,10vw,11rem\)\]': r'text-[clamp(3.5rem,8vw,8.5rem)]',
    
    # Salt Typhoon & Duality max 8rem
    r'text-\[clamp\(4rem,8vw,8rem\)\]': r'text-[clamp(3rem,6.5vw,6.5rem)]',
    r'text-\[clamp\(3\.5rem,8vw,8rem\)\]': r'text-[clamp(2.75rem,6.5vw,6.5rem)]',
    
    # Timeline Header max 7rem
    r'text-\[clamp\(3\.5rem,7vw,7rem\)\]': r'text-[clamp(2.75rem,5.5vw,5.5rem)]',
    
    # Timeline Years max 4rem
    r'text-\[clamp\(3rem,4vw,4rem\)\]': r'text-[clamp(2.5rem,3.25vw,3.25rem)]',
    
    # Web adapting max 6rem
    r'text-\[clamp\(3rem,6vw,6rem\)\]': r'text-[clamp(2.5rem,4.75vw,4.75rem)]',
    
    # Chrome anchors max 5rem
    r'text-\[clamp\(3rem,5vw,5rem\)\]': r'text-[clamp(2.5rem,4vw,4rem)]',
    
    # Where are we exposed (re-uses 4rem,9vw,9rem logic so it is handled by the Internet one)
}

for old, new in replacements.items():
    content = re.sub(old, new, content)

with open('why-quantum.html', 'w') as f:
    f.write(content)

print("Fonts reduced by roughly 15-20%")
