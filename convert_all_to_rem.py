import os
import re
import glob

def px_to_rem(match):
    px_val = float(match.group(1))
    if px_val == 0:
        return "[0px]"
    rem_val = px_val / 16.0
    rem_str = f"{rem_val:g}"
    return f"[{rem_str}rem]"

def px_style_to_rem(match):
    prop = match.group(1)
    px_val = float(match.group(2))
    if px_val == 0:
        return f"{prop}: 0px"
    rem_val = px_val / 16.0
    rem_str = f"{rem_val:g}"
    return f"{prop}: {rem_str}rem"

# Read styles.css and append the global rule if not present
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

fluid_rule = """
/* Proportional Scaling for Desktop (Base 1512px) */
@media (min-width: 1024px) {
    html {
        font-size: clamp(10px, calc(100vw / 1512 * 16), 24px);
    }
}
"""

if "font-size: clamp(10px, calc(100vw / 1512 * 16), 24px);" not in css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write("\n" + fluid_rule)

# Process all HTML files
html_files = glob.glob('*.html')

injected_style_block = """    <style>
        /* Proportional Scaling for Desktop (Base 1512px) */
        @media (min-width: 1024px) {
            html {
                font-size: clamp(10px, calc(100vw / 1512 * 16), 24px);
            }
        }
    </style>
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Clean up the previously injected style block from index.html
    html = html.replace(injected_style_block, "")

    # Replace Tailwind classes like [1400px] -> [87.5rem]
    html = re.sub(r'\[(\d+(?:\.\d+)?)px\]', px_to_rem, html)

    # Replace inline styles like min-height: 500px -> min-height: 31.25rem
    # Only targeting specific properties safely to avoid replacing px in URLs or other non-CSS places
    html = re.sub(r'(width|height|min-width|min-height|max-width|max-height|top|bottom|left|right|margin|padding|margin-top|margin-bottom|margin-left|margin-right|padding-top|padding-bottom|padding-left|padding-right):\s*(-?\d+(?:\.\d+)?)px', px_style_to_rem, html)

    # Some old styles might have 0rem from previous replace. Convert them back to 0px just to be safe for JS.
    html = html.replace('max-height: 0rem;', 'max-height: 0px;')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print(f"Processed {len(html_files)} HTML files and updated styles.css")
