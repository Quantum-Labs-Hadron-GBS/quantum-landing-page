import re

with open('quantum-technology.html', 'r') as f:
    content = f.read()

# 1. Hero Section
content = re.sub(
    r'<h1 class="text-4xl md:text-6xl lg:text-7xl font-medium tracking-tight mb-6 leading-\[1\.05\] text-white"([^>]+)>\s*YOUR BUSINESS<br>IS ALREADY ON<br><span class="text-brand-orange">A QUANTUM CLOCK\.</span>\s*</h1>\s*<p class="text-white/80 text-sm md:text-lg mb-8 font-medium leading-relaxed max-w-xl">.*?</p>\s*<div class="flex gap-4" data-aos="fade-up">\s*<a href="contact\.html"\s*class="sl-btn sl-btn--light bg-brand-orange hover:bg-orange-600 text-black border-none">ASSESS\s*YOUR QUANTUM RISK</a>\s*</div>',
    '''<h1 class="text-4xl md:text-6xl lg:text-7xl font-medium tracking-tight mb-6 leading-[1.05] text-white"\\1>
                    QUANTUM IS BECOMING A<br><span class="text-brand-orange">BUSINESS QUESTION.</span>
                </h1>
                <p class="text-white/80 text-sm md:text-lg mb-8 font-medium leading-relaxed max-w-xl">
                    Quantum computing is evolving. The important question for your organization is where it matters — across security, technology, operations, and future opportunities.<br><br>Hadron helps you understand where to look, what matters, and what to do next.
                </p>
                <div class="flex gap-4" data-aos="fade-up">
                    <a href="contact.html"
                        class="sl-btn sl-btn--light bg-brand-orange hover:bg-orange-600 text-black border-none">EXPLORE YOUR QUANTUM POSITION</a>
                </div>''',
    content, flags=re.DOTALL
)

# 2. Assessment Section (Intro)
content = re.sub(
    r'<div class="max-w-3xl mb-16">\s*<h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-6" data-aos="fade-up">THE PROBLEM ISN\'T\s*QUANTUM\.<br>IT\'S WHAT YOU DON\'T KNOW ABOUT YOUR EXPOSURE\.\s*</h2>.*?</div>\s*<!-- Glass Cards Grid -->\s*<h3 class="text-xl font-bold font-bank-gothic text-brand-dark mb-2">Assessment Areas</h3>\s*<p class="text-brand-dark/70 font-medium mb-8">YOU DO NOT NEED TO MIGRATE EVERYTHING AT ONCE\. YOU NEED TO\s*KNOW WHAT MATTERS FIRST\.</p>',
    '''<div class="max-w-3xl mb-16">
                <h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-6" data-aos="fade-up">WHERE QUANTUM MATTERS</h2>
                <p class="sharplink-body text-brand-dark/70 mb-12">
                    Quantum affects different organizations in different ways. We identify the areas that matter to your business — from cryptographic dependencies and technology exposure to opportunities for advanced computation.
                </p>
                <div class="flex flex-wrap items-center gap-4 md:gap-8 text-xl md:text-2xl font-bold text-brand-dark uppercase tracking-widest" data-aos="fade-up" data-aos-delay="100">
                    <span>RISK</span>
                    <span class="text-brand-orange">|</span>
                    <span>VISIBILITY</span>
                    <span class="text-brand-orange">|</span>
                    <span>IMPACT</span>
                    <span class="text-brand-orange">|</span>
                    <span>READINESS</span>
                </div>
            </div>''',
    content, flags=re.DOTALL
)

# 2b. Assessment Cards
content = re.sub(
    r'<h4 class="text-lg font-bold text-brand-dark mb-3">QUANTUM EXPOSURE</h4>\s*<p class="text-sm text-brand-dark/70 leading-relaxed">Identify where quantum developments could\s*create meaningful risk across your security, technology, data and business environment\. Focus on\s*what matters to the organization — not on theoretical risk alone\.</p>',
    '''<h4 class="text-lg font-bold text-brand-dark mb-3">QUANTUM EXPOSURE</h4>
                    <p class="font-semibold text-brand-dark mb-2">Where could quantum matter?</p>
                    <p class="text-sm text-brand-dark/70 leading-relaxed">Identify where quantum developments create risk or opportunity across your environment.</p>''',
    content, flags=re.DOTALL
)

content = re.sub(
    r'<h4 class="text-lg font-bold text-brand-dark mb-3">CRYPTOGRAPHIC VISIBILITY</h4>\s*<p class="text-sm text-brand-dark/70 leading-relaxed">Understand where encryption, certificates,\s*keys, signatures and other cryptographic dependencies exist across applications, infrastructure\s*and data\. You cannot prioritize migration without first knowing what you have\.</p>',
    '''<h4 class="text-lg font-bold text-brand-dark mb-3">CRYPTOGRAPHIC VISIBILITY</h4>
                    <p class="font-semibold text-brand-dark mb-2">What depends on cryptography today?</p>
                    <p class="text-sm text-brand-dark/70 leading-relaxed">Map your encryption, keys, and certificates. You cannot migrate what you cannot see.</p>''',
    content, flags=re.DOTALL
)

content = re.sub(
    r'<h4 class="text-lg font-bold text-brand-dark mb-3">BUSINESS IMPACT</h4>\s*<p class="text-sm text-brand-dark/70 leading-relaxed">Not every system deserves the same priority\.\s*We assess business criticality, data sensitivity, exposure, dependency and longevity to identify\s*where quantum-related change could matter most\.</p>',
    '''<h4 class="text-lg font-bold text-brand-dark mb-3">BUSINESS IMPACT</h4>
                    <p class="font-semibold text-brand-dark mb-2">Which systems matter most?</p>
                    <p class="text-sm text-brand-dark/70 leading-relaxed">Assess criticality, data sensitivity, and exposure to prioritize where change is actually required.</p>''',
    content, flags=re.DOTALL
)

content = re.sub(
    r'<h4 class="text-lg font-bold text-brand-dark mb-3">READINESS</h4>\s*<p class="text-sm text-brand-dark/70 leading-relaxed">Assess how prepared your organization is to\s*respond — from visibility and governance to technology dependencies, cryptographic agility,\s*skills and migration complexity\.</p>',
    '''<h4 class="text-lg font-bold text-brand-dark mb-3">READINESS</h4>
                    <p class="font-semibold text-brand-dark mb-2">How prepared are you to respond?</p>
                    <p class="text-sm text-brand-dark/70 leading-relaxed">Evaluate your governance, technology agility, and migration complexity.</p>''',
    content, flags=re.DOTALL
)


# 3. Use Case Development (Left column)
content = re.sub(
    r'<div>\s*<h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-6" data-aos="fade-up">QUANTUM\s*SHOULD ANSWER A BUSINESS QUESTION\.</h2>\s*<p class="sharplink-body text-brand-dark/70 mb-6">\s*The wrong question is: <em>"Where can we use quantum\?"</em>\s*</p>\s*<p class="sharplink-body text-brand-dark/70 mb-6">\s*The better question is: <em>"Which problems are expensive, complex or difficult to solve\s*with the approaches we use today\?"</em>\s*</p>\s*<p class="text-brand-dark/60 text-sm leading-relaxed mb-8">\s*Quantum is not a strategy by itself\. A business problem is\. We identify high-value problems\s*where optimization, simulation or other advanced computational approaches could create\s*measurable value — and determine whether quantum, quantum-inspired, hybrid or classical\s*approaches make the most sense\.\s*</p>\s*</div>',
    '''<div>
                        <div data-aos="fade-up">
                            <span class="text-sm font-bold text-brand-dark/50 tracking-widest uppercase mb-2 block">THE WRONG QUESTION</span>
                            <h2 class="text-4xl md:text-5xl font-medium text-brand-dark/40 mb-12" style="font-family: 'Archivo', sans-serif;">
                                "WHERE CAN WE USE QUANTUM?"
                            </h2>
                        </div>
                        <div data-aos="fade-up" data-aos-delay="100">
                            <span class="text-sm font-bold text-brand-orange tracking-widest uppercase mb-2 block">THE BETTER QUESTION</span>
                            <h2 class="text-4xl md:text-5xl font-medium text-brand-dark mb-8" style="font-family: 'Archivo', sans-serif;">
                                "WHICH PROBLEMS ARE WORTH SOLVING BETTER?"
                            </h2>
                            <p class="text-brand-dark/70 text-lg leading-relaxed max-w-lg">
                                We identify high-value problems where optimization, simulation, or advanced computation could create measurable value — and determine whether classical, quantum-inspired, hybrid, or quantum approaches make the most sense.
                            </p>
                        </div>
                    </div>''',
    content, flags=re.DOTALL
)

# 3b. Use Case 4 Steps
content = re.sub(
    r'<p class="text-sm text-brand-dark/60 mt-1">Identify the operational or strategic\s*problem where better computation could create meaningful value\.</p>',
    '<p class="text-sm text-brand-dark/60 mt-1">Identify where better computation creates meaningful value.</p>',
    content, flags=re.DOTALL
)
content = re.sub(
    r'<p class="text-sm text-brand-dark/60 mt-1">Evaluate business value, computational\s*complexity, available data, constraints and feasibility before investing in a\s*quantum approach\.</p>',
    '<p class="text-sm text-brand-dark/60 mt-1">Evaluate feasibility before investing in a quantum approach.</p>',
    content, flags=re.DOTALL
)
content = re.sub(
    r'<p class="text-sm text-brand-dark/60 mt-1">Translate the real-world problem into a\s*structured model that can be tested, compared and optimized\.</p>',
    '<p class="text-sm text-brand-dark/60 mt-1">Translate the real-world problem into a testable, optimizable model.</p>',
    content, flags=re.DOTALL
)
content = re.sub(
    r'<p class="text-sm text-brand-dark/60 mt-1">Compare classical, heuristic,\s*quantum-inspired, quantum and hybrid approaches where appropriate\. The objective\s*is not to use quantum\. The objective is to find the approach that creates the\s*strongest business case\.</p>',
    '<p class="text-sm text-brand-dark/60 mt-1">Compare approaches to find the strongest business case.</p>',
    content, flags=re.DOTALL
)

# 4. Implementation Accordion
content = re.sub(
    r'<div class="max-w-\[1400px\] mx-auto px-6 md:px-12 py-24">\s*<h2 class="sharplink-h2 text-brand-dark text-3xl md:text-4xl mb-6 text-center" data-aos="fade-up">FROM\s*ASSESSMENT TO ACTION</h2>\s*<p class="text-center text-brand-dark/60 max-w-2xl mx-auto mb-16">\s*A quantum strategy is only useful if it can become part of the way an organization actually operates\.\s*Where appropriate, Hadron can help translate findings into enterprise workflows, governance, technology\s*programs and decision-making processes — so quantum readiness does not remain a report sitting on a\s*shelf\.\s*</p>\s*<div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">\s*<div class="bg-white/40 backdrop-blur-md border border-white/60 p-8 rounded-2xl shadow-xl shadow-brand-dark/5"\s*data-aos="fade-up" data-aos-delay="100">\s*<h3 class="text-2xl font-bold text-brand-dark mb-4">MAKE QUANTUM READINESS OPERATIONAL</h3>\s*<p class="text-sm text-brand-dark/70 leading-relaxed">Turn quantum-risk findings into trackable\s*enterprise work\. Relevant risks, dependencies, remediation priorities and readiness activities\s*can be incorporated into existing IT, security and operational workflows\.</p>\s*</div>\s*<div class="bg-white/40 backdrop-blur-md border border-white/60 p-8 rounded-2xl shadow-xl shadow-brand-dark/5"\s*data-aos="fade-up" data-aos-delay="100">\s*<h3 class="text-2xl font-bold text-brand-dark mb-4">CONNECT QUANTUM TO BUSINESS DECISIONS</h3>\s*<p class="text-sm text-brand-dark/70 leading-relaxed">Bring quantum initiatives into the broader\s*business context — from strategic priorities and opportunity tracking to executive visibility\s*and investment decisions\.</p>\s*</div>',
    '''<div class="max-w-[1400px] mx-auto px-6 md:px-12 py-24">
            <h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-6 text-center" data-aos="fade-up">TURN INSIGHT INTO ACTION.</h2>
            <p class="text-center text-brand-dark/70 text-lg max-w-2xl mx-auto mb-16" data-aos="fade-up">
                Insights only matter when they lead to action. We translate findings into enterprise workflows, governance, and technology programs.
            </p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">
                <div class="bg-white/40 backdrop-blur-md border border-white/60 p-8 rounded-2xl shadow-xl shadow-brand-dark/5"
                    data-aos="fade-up" data-aos-delay="100">
                    <h3 class="text-xl font-bold text-brand-dark mb-4">MAKE READINESS OPERATIONAL</h3>
                    <p class="text-sm text-brand-dark/70 leading-relaxed">Turn findings into trackable enterprise work. Incorporate relevant risks, dependencies, and remediation priorities into existing IT and security workflows.</p>
                </div>
                <div class="bg-white/40 backdrop-blur-md border border-white/60 p-8 rounded-2xl shadow-xl shadow-brand-dark/5"
                    data-aos="fade-up" data-aos-delay="150">
                    <h3 class="text-xl font-bold text-brand-dark mb-4">INFORM BUSINESS DECISIONS</h3>
                    <p class="text-sm text-brand-dark/70 leading-relaxed">Bring initiatives into the broader business context — from strategic priorities to executive visibility and investment decisions.</p>
                </div>''',
    content, flags=re.DOTALL
)

# 5. How We Deliver
content = re.sub(
    r'<h4 class="font-bold text-lg text-brand-dark mb-2">Identify Problem</h4>',
    '<h4 class="font-bold text-lg text-brand-dark mb-2">IDENTIFY</h4>',
    content
)
content = re.sub(
    r'<h4 class="font-bold text-lg text-brand-dark mb-2">Assess Suitability</h4>',
    '<h4 class="font-bold text-lg text-brand-dark mb-2">ASSESS</h4>',
    content
)
content = re.sub(
    r'<h4 class="font-bold text-lg text-brand-dark mb-2">Evaluate Approaches</h4>',
    '<h4 class="font-bold text-lg text-brand-dark mb-2">EVALUATE</h4>',
    content
)
content = re.sub(
    r'<h4 class="font-bold text-lg text-brand-dark mb-2">Validate</h4>',
    '<h4 class="font-bold text-lg text-brand-dark mb-2">VALIDATE</h4>',
    content
)
content = re.sub(
    r'<h4 class="font-bold text-lg text-brand-dark mb-2">Scale</h4>',
    '<h4 class="font-bold text-lg text-brand-dark mb-2">SCALE</h4>',
    content
)

# 6. Final CTA
content = re.sub(
    r'<h2 class="text-4xl md:text-6xl font-medium tracking-tight mb-8 text-center max-w-4xl px-4 text-brand-dark"\s*style="font-family: \'Archivo\', sans-serif;">\s*DO YOU KNOW WHERE<br>YOUR BUSINESS STANDS\?\s*</h2>\s*<p class="text-brand-dark/70 mb-8 max-w-2xl text-center text-lg">You don\'t need to predict when quantum becomes\s*practical\. You need to understand what it could mean for your organization — and what deserves attention\s*before it becomes urgent\.</p>\s*<a href="contact\.html"\s*class="bg-\[#111\] text-white px-8 py-4 rounded-full text-sm font-semibold hover:bg-black/80 transition-transform hover:scale-105 shadow-xl mb-12 relative z-10">\s*FIND YOUR QUANTUM EXPOSURE\s*</a>\s*<p class="text-brand-dark/50 text-sm mt-4 font-medium mb-12 relative z-10">Start with visibility\. Then decide\s*what comes next\.</p>',
    '''<h2 class="text-4xl md:text-6xl font-medium tracking-tight mb-8 text-center max-w-4xl px-4 text-brand-dark"
            style="font-family: 'Archivo', sans-serif;">
            KNOW WHERE YOU STAND.<br>KNOW WHAT COMES NEXT.
        </h2>
        <p class="text-brand-dark/70 mb-8 max-w-2xl text-center text-lg">Start with visibility. Then decide what deserves attention before it becomes urgent.</p>

        <a href="contact.html"
            class="bg-[#111] text-white px-8 py-4 rounded-full text-sm font-semibold hover:bg-black/80 transition-transform hover:scale-105 shadow-xl mb-12 relative z-10">
            FIND YOUR QUANTUM EXPOSURE
        </a>''',
    content, flags=re.DOTALL
)

with open('quantum-technology.html', 'w') as f:
    f.write(content)

print("Done")
