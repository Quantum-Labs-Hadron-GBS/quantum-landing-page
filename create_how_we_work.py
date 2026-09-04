import re

with open('ai-infrastructure.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace <title> and meta
html = re.sub(r'<title>.*?</title>', '<title>How We Work | Hadron GBS</title>', html)
html = re.sub(r'<meta name="description" content=".*?" />', '<meta name="description" content="How Hadron turns complex technology questions into practical action through a structured methodology." />', html)

# Replace Hero
hero_pattern = r'<!-- Premium Dark Hero -->.*?<!-- Main Content -->'
hero_match = re.search(hero_pattern, html, flags=re.DOTALL)

new_hero = '''<!-- Premium Dark Hero -->
    <div class="relative w-full min-h-[60vh] bg-black overflow-hidden flex items-center pt-32 pb-16">
        <!-- Abstract gradient/video background -->
        <div class="absolute inset-0 bg-gradient-to-tr from-brand-orange/20 via-black to-black opacity-80"></div>
        <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_bottom_left,_var(--tw-gradient-stops))] from-brand-orange/20 via-transparent to-transparent opacity-60"></div>
        
        <div class="relative z-10 max-w-[1400px] w-full mx-auto px-6 md:px-12 grid grid-cols-1 lg:grid-cols-[1.2fr_1fr] gap-12 items-center">
            <div>
                <div class="mb-6 flex items-center gap-3">
                    <span class="px-3 py-1 rounded-full bg-brand-orange/20 text-brand-orange border border-brand-orange/30 text-xs font-bold tracking-widest uppercase">How We Work</span>
                </div>
                <h1 class="text-4xl md:text-6xl lg:text-7xl font-medium tracking-tight mb-6 leading-[1.05] text-white" style="font-family: 'Archivo', sans-serif;">
                    HOW WE TURN COMPLEXITY <br><span class="text-brand-orange">INTO ACTION.</span>
                </h1>
                <p class="text-white/80 text-sm md:text-lg mb-8 font-medium leading-relaxed max-w-xl">
                    Every engagement follows a structured process designed to move organizations from theoretical technology questions to practical, validated business decisions.
                </p>
                <div class="flex gap-4" data-aos="fade-up">
                    <a href="contact.html" class="sl-btn sl-btn--light bg-brand-orange hover:bg-orange-600 text-black border-none">Discuss Your Environment</a>
                </div>
            </div>
        </div>
    </div>
    <!-- Main Content -->'''
html = html.replace(hero_match.group(0), new_hero)

# Replace Main Content
main_content_pattern = r'<!-- Main Content -->.*?<!-- New CTA Section -->'
new_main_content = '''<!-- Main Content -->
    <main class="relative z-20" style="background: radial-gradient(ellipse 100% 130% at 50% -30%, #c4d5e7 45%, #fdfbf7 85%, #f7f7f5); padding-bottom: 6rem;">
        
        <!-- Methodology Section -->
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 pt-24 pb-16">
            <div class="max-w-3xl mb-16">
                <h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-6" data-aos="fade-up">A Structured Methodology</h2>
                <p class="sharplink-body text-brand-dark/70 mb-6">
                    Our workflow is consistent across all engagements, ensuring that technology exploration is always grounded in rigorous assessment, clear prioritization, and measurable action.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="bg-white/40 backdrop-blur-md border border-brand-dark/10 p-8 rounded-3xl shadow-xl hover:-translate-y-2 transition-all duration-300 relative overflow-hidden group">
                    <div class="w-12 h-12 rounded-full border border-brand-dark/20 flex items-center justify-center mb-6 bg-brand-dark group-hover:bg-brand-orange transition-colors duration-300">
                        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-brand-dark mb-4 uppercase tracking-widest text-sm">Understand</h3>
                    <p class="text-brand-dark/70 text-sm leading-relaxed">Map the environment, baseline current operations, and discover where vulnerabilities or computational bottlenecks actually exist.</p>
                </div>
                
                <div class="bg-white/40 backdrop-blur-md border border-brand-dark/10 p-8 rounded-3xl shadow-xl hover:-translate-y-2 transition-all duration-300 relative overflow-hidden group">
                    <div class="w-12 h-12 rounded-full border border-brand-dark/20 flex items-center justify-center mb-6 bg-brand-dark group-hover:bg-brand-orange transition-colors duration-300">
                        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-brand-dark mb-4 uppercase tracking-widest text-sm">Assess</h3>
                    <p class="text-brand-dark/70 text-sm leading-relaxed">Evaluate classical, heuristic, quantum-inspired, and true quantum approaches against the defined operational requirements.</p>
                </div>

                <div class="bg-white/40 backdrop-blur-md border border-brand-dark/10 p-8 rounded-3xl shadow-xl hover:-translate-y-2 transition-all duration-300 relative overflow-hidden group">
                    <div class="w-12 h-12 rounded-full border border-brand-dark/20 flex items-center justify-center mb-6 bg-brand-dark group-hover:bg-brand-orange transition-colors duration-300">
                        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-brand-dark mb-4 uppercase tracking-widest text-sm">Prioritize</h3>
                    <p class="text-brand-dark/70 text-sm leading-relaxed">Focus resources exclusively on workloads and security dependencies that offer the highest measurable value or highest vulnerability impact.</p>
                </div>

                <div class="bg-white/40 backdrop-blur-md border border-brand-dark/10 p-8 rounded-3xl shadow-xl hover:-translate-y-2 transition-all duration-300 relative overflow-hidden group">
                    <div class="w-12 h-12 rounded-full border border-brand-dark/20 flex items-center justify-center mb-6 bg-brand-orange transition-colors duration-300">
                        <svg class="w-5 h-5 text-black" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 13l4 4L19 7"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-brand-dark mb-4 uppercase tracking-widest text-sm">Act</h3>
                    <p class="text-brand-dark/70 text-sm leading-relaxed">Validate solutions against business KPIs and safely transition proven models and secured infrastructure into production.</p>
                </div>
            </div>
        </div>

        <!-- Core Principles Section -->
        <div class="w-full relative border-t border-brand-dark/10 pt-24 pb-16">
            <div class="max-w-[1400px] mx-auto px-6 md:px-12">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
                    <div data-aos="fade-right">
                        <h2 class="text-3xl md:text-5xl text-brand-dark font-medium leading-tight mb-6" style="font-family: 'Archivo', sans-serif;">
                            Technology is not<br>the starting point.
                        </h2>
                        <p class="text-lg md:text-xl text-brand-dark/70 leading-relaxed font-normal">
                            We do not force organizational problems into quantum architectures. We evaluate business operations, identify computational bottlenecks, and apply the right computing approach—classical, quantum-inspired, or quantum—to solve them.
                        </p>
                    </div>
                    <div data-aos="fade-left" data-aos-delay="100">
                        <h2 class="text-3xl md:text-5xl text-brand-dark font-medium leading-tight mb-6" style="font-family: 'Archivo', sans-serif;">
                            Built around<br><span class="text-brand-orange">your environment.</span>
                        </h2>
                        <p class="text-lg md:text-xl text-brand-dark/70 leading-relaxed font-normal">
                            Our work is designed to fit the way your organization operates. We work within the relevant technical, security, regulatory, and operational constraints — coordinating with the teams and technology partners required to move from assessment to execution.
                        </p>
                    </div>
                </div>
            </div>
        </div>

    </main>
    <!-- New CTA Section -->'''

html = re.sub(main_content_pattern, new_main_content, html, flags=re.DOTALL)

with open('how-we-work.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Created how-we-work.html")
