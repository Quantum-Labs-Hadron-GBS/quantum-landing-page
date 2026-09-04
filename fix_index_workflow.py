import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Current text:
# <h2 class="text-4xl md:text-5xl lg:text-6xl text-brand-dark font-medium leading-tight tracking-tight mb-6" style="font-family: 'Inter', system-ui, sans-serif;">
#    Technology Is Not The Starting Point
# </h2>
# <p class="text-lg md:text-xl text-brand-dark/70 max-w-2xl leading-relaxed font-normal">
#    We do not force organizational problems into quantum architectures. We evaluate business operations, identify computational bottlenecks, and apply the right computing approach—classical, quantum-inspired, or quantum—to solve them.
# </p>

html = html.replace(
    '''Technology Is Not The Starting Point''',
    '''A CLEAR PATH FROM QUESTION TO ACTION.'''
)

html = html.replace(
    '''We do not force organizational problems into quantum architectures. We evaluate business operations, identify computational bottlenecks, and apply the right computing approach—classical, quantum-inspired, or quantum—to solve them.''',
    '''Every engagement follows a structured process designed to turn complex technology questions into practical decisions.'''
)

# Insert the CTA button right after the paragraph.
# Wait, the paragraph is followed by:
# </div>
# <!-- Desktop Layout (Sticky Cards) -->
# I can just insert it right after the paragraph tag.

button_html = '''
                        <div class="mt-8" data-aos="fade-up">
                            <a href="how-we-work.html" class="inline-flex items-center gap-2 text-sm font-bold tracking-widest uppercase text-brand-orange hover:text-[#e08920] transition-colors group">
                                EXPLORE OUR APPROACH
                                <svg class="w-4 h-4 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                            </a>
                        </div>
'''

html = re.sub(
    r'(Every engagement follows a structured process designed to turn complex technology questions into practical decisions\.\s*</p>)',
    r'\1' + button_html,
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index workflow teaser.")
