import re

# ==========================================
# 1. AI Infrastructure Updates
# ==========================================
with open('ai-infrastructure.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Hero
html = html.replace(
    '''Turn computing infrastructure into a measurable optimization opportunity through better utilization, lower cost, and improved operational efficiency.''',
    '''Turn GPU capacity into productive capacity. AI infrastructure represents a significant investment. Hadron helps organizations improve how that infrastructure is utilized — intelligently scheduling workloads, allocating resources, and reducing idle or underutilized capacity. The objective is simple: increase productive usage without proportionally increasing infrastructure spend.'''
)

# Update "How We Approach It" section
# The current HTML has a 6-grid system.
# We will replace it with a 4-grid system for the new flow + trust copy
old_workflow_block = re.search(r'<!-- How We Approach It Section -->.*?</div>\s*</div>\s*</div>', html, flags=re.DOTALL)
if old_workflow_block:
    new_workflow_block = '''<!-- How We Deliver Section -->
        <div class="w-full relative border-y border-brand-dark/10 bg-white/20">
            <div class="absolute inset-0 bg-brand-light bg-grid-pattern z-0 opacity-10"></div>
            <div class="max-w-[1400px] mx-auto px-6 md:px-12 py-24 relative z-10">
                <h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-12 text-center" data-aos="fade-up">How We Deliver</h2>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-12">
                    <div class="flex flex-col items-center text-center p-6 bg-white rounded-3xl shadow-lg border border-black/5 relative" data-aos="zoom-in" data-aos-delay="50">
                        <div class="w-12 h-12 bg-brand-orange text-white rounded-full flex items-center justify-center font-bold text-xl mb-6 shadow-xl shadow-brand-orange/30">1</div>
                        <h4 class="font-bold text-xl text-brand-dark mb-3">Understand Fleet</h4>
                        <p class="text-brand-dark/60 text-sm">Analyze existing capacity, hardware investments, and current utilization rates.</p>
                    </div>
                    <div class="flex flex-col items-center text-center p-6 bg-white rounded-3xl shadow-lg border border-black/5 relative" data-aos="zoom-in" data-aos-delay="100">
                        <div class="w-12 h-12 bg-brand-dark text-white rounded-full flex items-center justify-center font-bold text-xl mb-6 shadow-xl">2</div>
                        <h4 class="font-bold text-xl text-brand-dark mb-3">Model Workloads</h4>
                        <p class="text-brand-dark/60 text-sm">Map operational requirements, dependencies, constraints, and scheduling bottlenecks.</p>
                    </div>
                    <div class="flex flex-col items-center text-center p-6 bg-white rounded-3xl shadow-lg border border-black/5 relative" data-aos="zoom-in" data-aos-delay="150">
                        <div class="w-12 h-12 bg-brand-dark text-white rounded-full flex items-center justify-center font-bold text-xl mb-6 shadow-xl">3</div>
                        <h4 class="font-bold text-xl text-brand-dark mb-3">Optimize Utilization</h4>
                        <p class="text-brand-dark/60 text-sm">Deploy intelligent allocation and scheduling to extract more value from existing resources.</p>
                    </div>
                    <div class="flex flex-col items-center text-center p-6 bg-white rounded-3xl shadow-lg border border-black/5 relative" data-aos="zoom-in" data-aos-delay="200">
                        <div class="w-12 h-12 bg-brand-dark text-white rounded-full flex items-center justify-center font-bold text-xl mb-6 shadow-xl">4</div>
                        <h4 class="font-bold text-xl text-brand-dark mb-3">Measure Improvement</h4>
                        <p class="text-brand-dark/60 text-sm">Validate the increase in productive capacity against baseline metrics.</p>
                    </div>
                </div>

                <div class="max-w-3xl mx-auto text-center" data-aos="fade-up" data-aos-delay="250">
                    <p class="text-lg md:text-xl text-brand-dark/80 font-medium">
                        Improve productive GPU utilization and infrastructure efficiency without treating additional hardware as the default answer.
                    </p>
                </div>
            </div>
        </div>'''
    html = html.replace(old_workflow_block.group(0), new_workflow_block)

with open('ai-infrastructure.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated ai-infrastructure.html")

# ==========================================
# 2. PQC Security Updates
# ==========================================
with open('pqc-security.html', 'r', encoding='utf-8') as f:
    pqc = f.read()

# Since pqc-security doesn't have a workflow section yet, we need to inject it.
# We will inject it right before the new CTA section.
new_pqc_workflow = '''
    <!-- How We Deliver Section -->
    <div class="w-full relative border-y border-brand-dark/10 bg-white/20">
        <div class="absolute inset-0 bg-brand-light bg-grid-pattern z-0 opacity-10"></div>
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 py-24 relative z-10">
            <h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-12 text-center" data-aos="fade-up">How We Deliver</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-12">
                <div class="flex flex-col items-center text-center p-6 bg-white rounded-3xl shadow-lg border border-black/5 relative" data-aos="zoom-in" data-aos-delay="50">
                    <div class="w-12 h-12 bg-brand-orange text-white rounded-full flex items-center justify-center font-bold text-xl mb-6 shadow-xl shadow-brand-orange/30">1</div>
                    <h4 class="font-bold text-xl text-brand-dark mb-3">Your Environment</h4>
                    <p class="text-brand-dark/60 text-sm">Establish the operational bounds, compliance mandates, and required isolation protocols.</p>
                </div>
                <div class="flex flex-col items-center text-center p-6 bg-white rounded-3xl shadow-lg border border-black/5 relative" data-aos="zoom-in" data-aos-delay="100">
                    <div class="w-12 h-12 bg-brand-dark text-white rounded-full flex items-center justify-center font-bold text-xl mb-6 shadow-xl">2</div>
                    <h4 class="font-bold text-xl text-brand-dark mb-3">Assessment</h4>
                    <p class="text-brand-dark/60 text-sm">Discover and map cryptographic dependencies across business-critical systems.</p>
                </div>
                <div class="flex flex-col items-center text-center p-6 bg-white rounded-3xl shadow-lg border border-black/5 relative" data-aos="zoom-in" data-aos-delay="150">
                    <div class="w-12 h-12 bg-brand-dark text-white rounded-full flex items-center justify-center font-bold text-xl mb-6 shadow-xl">3</div>
                    <h4 class="font-bold text-xl text-brand-dark mb-3">Migration Priorities</h4>
                    <p class="text-brand-dark/60 text-sm">Determine which systems require immediate attention based on vulnerability and impact.</p>
                </div>
                <div class="flex flex-col items-center text-center p-6 bg-white rounded-3xl shadow-lg border border-black/5 relative" data-aos="zoom-in" data-aos-delay="200">
                    <div class="w-12 h-12 bg-brand-dark text-white rounded-full flex items-center justify-center font-bold text-xl mb-6 shadow-xl">4</div>
                    <h4 class="font-bold text-xl text-brand-dark mb-3">Controlled Implementation</h4>
                    <p class="text-brand-dark/60 text-sm">Execute the transition reliably while maintaining confidentiality and business continuity.</p>
                </div>
            </div>

            <div class="max-w-3xl mx-auto text-center" data-aos="fade-up" data-aos-delay="250">
                <p class="text-lg md:text-xl text-brand-dark/80 font-medium">
                    Designed around controlled environments, security requirements, applicable regulatory considerations, and the teams responsible for your infrastructure.
                </p>
            </div>
        </div>
    </div>
'''
pqc = pqc.replace('<!-- New CTA Section -->', new_pqc_workflow + '\n    <!-- New CTA Section -->')
with open('pqc-security.html', 'w', encoding='utf-8') as f:
    f.write(pqc)
print("Updated pqc-security.html")

# ==========================================
# 3. Quantum Technology Updates
# ==========================================
with open('quantum-technology.html', 'r', encoding='utf-8') as f:
    qt = f.read()

# Inject workflow section before CTA
new_qt_workflow = '''
    <!-- How We Deliver Section -->
    <div class="w-full relative border-y border-brand-dark/10 bg-white/20">
        <div class="absolute inset-0 bg-brand-light bg-grid-pattern z-0 opacity-10"></div>
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 py-24 relative z-10">
            <h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-12 text-center" data-aos="fade-up">How We Deliver</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6 mb-12">
                <div class="flex flex-col items-center text-center p-6 bg-white rounded-3xl shadow-lg border border-black/5 relative" data-aos="zoom-in" data-aos-delay="50">
                    <div class="w-10 h-10 bg-brand-orange text-white rounded-full flex items-center justify-center font-bold text-lg mb-4 shadow-xl shadow-brand-orange/30">1</div>
                    <h4 class="font-bold text-lg text-brand-dark mb-2">Identify Problem</h4>
                    <p class="text-brand-dark/60 text-xs">Find operational challenges suited for advanced computing.</p>
                </div>
                <div class="flex flex-col items-center text-center p-6 bg-white rounded-3xl shadow-lg border border-black/5 relative" data-aos="zoom-in" data-aos-delay="100">
                    <div class="w-10 h-10 bg-brand-dark text-white rounded-full flex items-center justify-center font-bold text-lg mb-4 shadow-xl">2</div>
                    <h4 class="font-bold text-lg text-brand-dark mb-2">Assess Suitability</h4>
                    <p class="text-brand-dark/60 text-xs">Determine if quantum or quantum-inspired methods offer an advantage.</p>
                </div>
                <div class="flex flex-col items-center text-center p-6 bg-white rounded-3xl shadow-lg border border-black/5 relative" data-aos="zoom-in" data-aos-delay="150">
                    <div class="w-10 h-10 bg-brand-dark text-white rounded-full flex items-center justify-center font-bold text-lg mb-4 shadow-xl">3</div>
                    <h4 class="font-bold text-lg text-brand-dark mb-2">Evaluate Approaches</h4>
                    <p class="text-brand-dark/60 text-xs">Test the most effective hardware and software ecosystems.</p>
                </div>
                <div class="flex flex-col items-center text-center p-6 bg-white rounded-3xl shadow-lg border border-black/5 relative" data-aos="zoom-in" data-aos-delay="200">
                    <div class="w-10 h-10 bg-brand-dark text-white rounded-full flex items-center justify-center font-bold text-lg mb-4 shadow-xl">4</div>
                    <h4 class="font-bold text-lg text-brand-dark mb-2">Validate</h4>
                    <p class="text-brand-dark/60 text-xs">Measure results against classical baselines and business KPIs.</p>
                </div>
                <div class="flex flex-col items-center text-center p-6 bg-white rounded-3xl shadow-lg border border-black/5 relative" data-aos="zoom-in" data-aos-delay="250">
                    <div class="w-10 h-10 bg-brand-dark text-white rounded-full flex items-center justify-center font-bold text-lg mb-4 shadow-xl">5</div>
                    <h4 class="font-bold text-lg text-brand-dark mb-2">Scale</h4>
                    <p class="text-brand-dark/60 text-xs">Transition proven models into production workflows.</p>
                </div>
            </div>

            <div class="max-w-3xl mx-auto text-center" data-aos="fade-up" data-aos-delay="300">
                <p class="text-lg md:text-xl text-brand-dark/80 font-medium">
                    Hadron coordinates the technical and business requirements needed to make quantum exploration practical.
                </p>
            </div>
        </div>
    </div>
'''
qt = qt.replace('<!-- New CTA Section -->', new_qt_workflow + '\n    <!-- New CTA Section -->')
with open('quantum-technology.html', 'w', encoding='utf-8') as f:
    f.write(qt)
print("Updated quantum-technology.html")
