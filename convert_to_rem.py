import re

def px_to_rem(match):
    px_val = float(match.group(1))
    rem_val = px_val / 16.0
    # Format to remove trailing zeros and dot if it's an integer
    rem_str = f"{rem_val:g}"
    return f"[{rem_str}rem]"

def px_style_to_rem(match):
    prop = match.group(1)
    px_val = float(match.group(2))
    rem_val = px_val / 16.0
    rem_str = f"{rem_val:g}"
    return f"{prop}: {rem_str}rem"

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Tailwind classes like [1400px] -> [87.5rem]
html = re.sub(r'\[(\d+(?:\.\d+)?)px\]', px_to_rem, html)

# Replace inline styles like min-height: 500px -> min-height: 31.25rem
# Only targeting specific properties safely to avoid replacing px in URLs or other non-CSS places
html = re.sub(r'(width|height|min-width|min-height|max-width|max-height|top|bottom|left|right|margin|padding|margin-top|margin-bottom|margin-left|margin-right|padding-top|padding-bottom|padding-left|padding-right):\s*(-?\d+(?:\.\d+)?)px', px_style_to_rem, html)

# Inject the root font size CSS
css_inject = """
    <style>
        /* Proportional Scaling for Desktop (Base 1512px) */
        @media (min-width: 1024px) {
            html {
                font-size: clamp(10px, calc(100vw / 1512 * 16), 24px);
            }
        }
    </style>
</head>
"""

html = html.replace('</head>', css_inject)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
