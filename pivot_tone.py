import re

def update_tone():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Hero Headline
    html = html.replace(
        'YOUR BUSINESS<br>IS ALREADY ON<br><span class="text-brand-orange">A QUANTUM CLOCK.</span>',
        'QUANTUM IS BECOMING A<br><span class="text-brand-orange">BUSINESS QUESTION.</span>'
    )

    # 2. Hero Subtext
    html = html.replace(
        '''Quantum may still feel like a future technology problem. For your business, some of the decisions cannot wait that long. Your data, applications, infrastructure, and cryptographic systems may contain dependencies that become harder to secure, replace, or understand as quantum computing advances.<br><br><span class="font-bold uppercase tracking-wider text-[11px]">You don't need to become a quantum expert. You need to know where you stand.</span>''',
        '''From securing what matters today to discovering what becomes possible tomorrow, organizations need a practical way to understand where quantum fits.<br><br><span class="font-bold uppercase tracking-wider text-[11px]">Hadron helps you find the answer.</span>'''
    )

    # 3. Why Hadron Title
    html = html.replace(
        '''The Problem Is Not<br>The Technology.''',
        '''A New Strategic<br>Challenge.'''
    )

    # 4. Why Hadron Text
    html = html.replace(
        '''The problem is visibility. Your organization already depends on technologies that quantum computing could change. The difficult question is not whether quantum exists—it is knowing exactly where it affects your business today.''',
        '''Knowing where to start isn't always straightforward. Quantum opportunities are highly problem-specific, while quantum risk can be buried across systems, applications, data, and cryptographic dependencies.'''
    )

    # 5. Transition Title
    html = html.replace(
        '''You Cannot Protect <br>What You Cannot See''',
        '''Where Quantum <br>Matters.'''
    )

    # 6. Transition Text
    html = html.replace(
        '''A quantum strategy cannot be built from headlines alone. It requires understanding the dependencies your business relies on today.''',
        '''The question isn't whether your business needs quantum today. It's where quantum matters — and what you should do about it.'''
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Tone update complete.")

if __name__ == '__main__':
    update_tone()
