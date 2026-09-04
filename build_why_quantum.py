import re
import os

with open('quantum-technology.html', 'r') as f:
    qt_content = f.read()

# Split around <main class="relative z-20" ...>
main_start = qt_content.find('<main class="relative z-20"')
main_end = qt_content.find('</main>') + len('</main>')

header_part = qt_content[:main_start]
footer_part = qt_content[main_end:]

# Wait, we need to replace the hero section inside header_part too!
hero_start = header_part.find('<!-- Premium Dark Hero -->')
hero_end = header_part.find('</header>') # wait, hero is after header.
# Let's find exactly where header ends
header_close = header_part.find('</header>') + len('</header>')
hero_actual = header_part[header_close:]

# Replace hero_actual with our new hero
new_hero = """
    <!-- Premium Dark Hero -->
    <div class="relative w-full min-h-[75vh] bg-black overflow-hidden flex items-center pt-32 pb-16">
        <div class="absolute inset-0 z-0">
            <div class="absolute top-0 right-0 w-[800px] h-[800px] bg-brand-orange/10 rounded-full blur-[120px] mix-blend-screen transform translate-x-1/3 -translate-y-1/4"></div>
            <div class="absolute bottom-0 left-0 w-[600px] h-[600px] bg-white/5 rounded-full blur-[100px] mix-blend-screen transform -translate-x-1/3 translate-y-1/4"></div>
        </div>
        <div class="absolute inset-0 bg-grid-pattern opacity-10 z-0"></div>

        <div class="w-full max-w-[1400px] mx-auto px-6 md:px-12 relative z-10 flex flex-col items-center text-center">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 mb-8 backdrop-blur-sm" data-aos="fade-up">
                <span class="w-2 h-2 rounded-full bg-brand-orange animate-pulse"></span>
                <span class="text-xs font-bold text-white/70 uppercase tracking-widest">Enterprise Briefing</span>
            </div>
            
            <h1 class="font-bank-gothic text-5xl md:text-7xl lg:text-8xl text-white mb-8 tracking-wide leading-tight" data-aos="fade-up" data-aos-delay="100">
                WHY <span class="text-brand-orange">QUANTUM?</span>
            </h1>
            
            <p class="text-xl md:text-2xl text-white/80 max-w-3xl font-light leading-relaxed mb-12" data-aos="fade-up" data-aos-delay="200">
                QUANTUM IS CHANGING THE ASSUMPTIONS BEHIND COMPUTING.
            </p>
            
            <div class="max-w-2xl text-white/60 text-base md:text-lg space-y-6 mb-16 font-sans leading-relaxed text-center" data-aos="fade-up" data-aos-delay="300">
                <p>For decades, modern digital infrastructure has depended on mathematical problems that are extremely difficult for classical computers to solve.</p>
                <p>Quantum computing changes that equation.</p>
                <p>The implications are larger than faster computers. They reach into the cryptography that protects digital communication, while opening new possibilities for problems that classical systems struggle to solve.</p>
            </div>

            <div class="p-6 border border-white/20 bg-white/5 backdrop-blur-sm rounded-xl max-w-3xl" data-aos="zoom-in" data-aos-delay="400">
                <p class="text-xl md:text-2xl font-bold text-white uppercase tracking-widest">
                    The question is no longer whether quantum matters.<br>
                    <span class="text-brand-orange">It is where it matters to your organization.</span>
                </p>
            </div>
        </div>
    </div>
"""

new_main = """
    <main class="relative z-20" style="background: radial-gradient(ellipse 100% 130% at 50% -30%, #c4d5e7 45%, #fdfbf7 85%, #f7f7f5); padding-bottom: 6rem;">
        
        <!-- SECTION: The Internet Runs on Mathematics -->
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 py-24">
            <h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-6" data-aos="fade-up">THE INTERNET RUNS ON MATHEMATICS.</h2>
            <h3 class="text-xl md:text-2xl font-bold text-brand-dark/70 uppercase tracking-widest mb-12" data-aos="fade-up" data-aos-delay="100">AND SOME OF THAT MATHEMATICS WILL NOT SURVIVE A CRYPTANALYTICALLY RELEVANT QUANTUM COMPUTER.</h3>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-16">
                <div class="space-y-6 text-brand-dark/80 text-lg leading-relaxed" data-aos="fade-right">
                    <p>Public-key cryptography sits underneath much of today's digital infrastructure.</p>
                    <p>It helps establish secure connections, authenticate systems, protect communications, secure certificates, and establish trust between organizations and machines.</p>
                    <p>Algorithms such as RSA and elliptic-curve cryptography derive their security from mathematical problems that are difficult for classical computers.</p>
                </div>
                <div class="space-y-6 text-brand-dark/80 text-lg leading-relaxed" data-aos="fade-left">
                    <p class="font-bold text-brand-dark">A sufficiently capable, fault-tolerant quantum computer could change that.</p>
                    <p>Shor's algorithm provides a theoretical path to efficiently solving the mathematical problems behind widely used public-key systems.</p>
                    <div class="bg-black text-white p-6 rounded-xl mt-8 shadow-xl border-l-4 border-brand-orange">
                        <p class="font-bold text-lg mb-2">The internet does not need to disappear for its security model to change.</p>
                        <p class="text-white/70 text-sm">The cryptographic assumptions underneath it do.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SECTION: Harvest Now -->
        <div class="w-full bg-black text-white py-24 relative overflow-hidden">
            <div class="absolute inset-0 bg-grid-pattern opacity-10"></div>
            <div class="max-w-[1400px] mx-auto px-6 md:px-12 relative z-10">
                <div class="text-center max-w-4xl mx-auto mb-16">
                    <h2 class="sharplink-h2 text-white text-4xl md:text-5xl mb-6" data-aos="fade-up">THE THREAT IS NOT WAITING FOR THE QUANTUM COMPUTER.</h2>
                    <div class="inline-block bg-brand-orange/20 text-brand-orange border border-brand-orange/30 px-6 py-2 rounded-full font-bold uppercase tracking-widest text-lg" data-aos="zoom-in">
                        HARVEST NOW. DECRYPT LATER.
                    </div>
                </div>
                
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                    <div class="space-y-6 text-white/80 text-lg leading-relaxed" data-aos="fade-right">
                        <p>Sensitive information does not necessarily need to be decrypted today to become a target today.</p>
                        <p>An adversary can capture encrypted traffic now, retain it, and attempt to decrypt it later when sufficiently capable quantum computing becomes available.</p>
                        <p>The risk is greatest for information whose confidentiality must survive for years or decades — <span class="text-white font-bold">intellectual property, strategic communications, personal information, financial records, credentials, research, and other long-lived data.</span></p>
                    </div>
                    <div class="bg-white/10 backdrop-blur-md border border-white/20 p-8 rounded-2xl" data-aos="fade-left">
                        <p class="text-sm text-white/60 uppercase tracking-widest mb-4">Regulatory Recognition</p>
                        <p class="text-white/90 italic mb-6">"The European Commission now explicitly identifies this risk, noting that data protected by quantum-vulnerable cryptography may already be at risk if it needs to remain confidential for a long period."</p>
                        <p class="font-bold text-brand-orange text-xl">The quantum threat therefore has a present-tense dimension.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SECTION: Salt Typhoon Case Study -->
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 py-24 border-b border-brand-dark/10">
            <h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-4 text-center" data-aos="fade-up">SALT TYPHOON SHOWED WHAT ACCESS LOOKS LIKE TODAY.</h2>
            <h3 class="text-xl md:text-2xl font-bold text-center text-brand-dark/70 uppercase tracking-widest mb-16" data-aos="fade-up" data-aos-delay="100">QUANTUM WAS NOT THE ATTACK. THE LESSON IS WHY DATA HAS VALUE BEFORE IT CAN BE DECRYPTED.</h3>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <div class="col-span-1 lg:col-span-2 space-y-6 text-brand-dark/80 text-lg leading-relaxed" data-aos="fade-right">
                    <p>The Salt Typhoon campaign demonstrated the strategic value of gaining access to telecommunications infrastructure.</p>
                    <p>U.S. government investigations found that the campaign compromised multiple telecommunications companies and resulted in the theft of call-data records, limited private communications involving identified victims, and other information.</p>
                    <p>The FBI described the activity as a broad campaign targeting telecommunications networks globally.</p>
                    <p class="font-bold text-brand-orange text-2xl uppercase tracking-widest mt-8">This was not a quantum attack.</p>
                    <p>That distinction matters.</p>
                </div>
                
                <div class="col-span-1 flex flex-col gap-6" data-aos="fade-left">
                    <div class="bg-[#f2f2f0] p-6 rounded-2xl border border-brand-dark/10 shadow-lg">
                        <p class="text-sm text-brand-dark/60 uppercase tracking-widest mb-2">The First Half</p>
                        <p class="font-bold text-brand-dark text-xl">DATA CAN BE COLLECTED TODAY.</p>
                    </div>
                    <div class="bg-brand-dark text-white p-6 rounded-2xl shadow-xl">
                        <p class="text-sm text-white/50 uppercase tracking-widest mb-2">The Second Half</p>
                        <p class="font-bold text-brand-orange text-xl">DATA THAT CANNOT BE DECRYPTED TODAY MAY NOT REMAIN SECURE FOREVER.</p>
                    </div>
                </div>
            </div>
            <p class="text-center text-xl font-bold text-brand-dark mt-16" data-aos="fade-up">That is why long-lived information deserves attention before a cryptographically relevant quantum computer exists.</p>
        </div>

        <!-- SECTION: The Computation Opportunity -->
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 py-24">
            <h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-4 text-center" data-aos="fade-up">BUT QUANTUM IS NOT ONLY A SECURITY STORY.</h2>
            <h3 class="text-xl md:text-2xl font-bold text-center text-brand-dark/70 uppercase tracking-widest mb-16" data-aos="fade-up" data-aos-delay="100">THE SAME TECHNOLOGY THAT CHALLENGES CRYPTOGRAPHY MAY OPEN NEW COMPUTATIONAL POSSIBILITIES.</h3>
            
            <p class="text-center text-lg text-brand-dark/80 max-w-4xl mx-auto mb-16" data-aos="fade-up">
                Quantum computers process information according to the principles of quantum mechanics. That does not make them universally faster than classical computers. Instead, quantum algorithms can provide fundamentally different approaches to particular classes of problems.
            </p>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
                <!-- Cards -->
                <div class="bg-white p-8 rounded-2xl shadow-xl border border-brand-dark/5 hover:-translate-y-2 transition-transform duration-300" data-aos="fade-up" data-aos-delay="100">
                    <h4 class="font-bold text-brand-dark text-lg mb-4">SIMULATION</h4>
                    <p class="text-sm text-brand-dark/70 leading-relaxed">Explore molecular and material systems that are difficult to model classically.</p>
                </div>
                <div class="bg-white p-8 rounded-2xl shadow-xl border border-brand-dark/5 hover:-translate-y-2 transition-transform duration-300" data-aos="fade-up" data-aos-delay="200">
                    <h4 class="font-bold text-brand-dark text-lg mb-4">OPTIMIZATION</h4>
                    <p class="text-sm text-brand-dark/70 leading-relaxed">Investigate complex combinations and decision spaces where better solutions can have meaningful economic value.</p>
                </div>
                <div class="bg-white p-8 rounded-2xl shadow-xl border border-brand-dark/5 hover:-translate-y-2 transition-transform duration-300" data-aos="fade-up" data-aos-delay="300">
                    <h4 class="font-bold text-brand-dark text-lg mb-4">CHEMISTRY & MATERIALS</h4>
                    <p class="text-sm text-brand-dark/70 leading-relaxed">Model systems whose quantum behaviour is difficult to reproduce efficiently using classical computation.</p>
                </div>
                <div class="bg-white p-8 rounded-2xl shadow-xl border border-brand-dark/5 hover:-translate-y-2 transition-transform duration-300" data-aos="fade-up" data-aos-delay="400">
                    <h4 class="font-bold text-brand-dark text-lg mb-4">FINANCIAL MODELLING</h4>
                    <p class="text-sm text-brand-dark/70 leading-relaxed">Explore specialised computational problems where quantum or hybrid methods may eventually provide an advantage.</p>
                </div>
            </div>
            
            <div class="text-center" data-aos="zoom-in">
                <p class="text-xl text-brand-dark mb-4">The opportunity is real. So is the uncertainty.</p>
                <p class="text-2xl font-bold text-brand-dark uppercase tracking-widest max-w-3xl mx-auto border-t border-b border-brand-dark/10 py-6">
                    Quantum should not be adopted because it is quantum.<br>
                    <span class="text-brand-orange">It should be adopted when it can solve a meaningful problem better.</span>
                </p>
            </div>
        </div>

        <!-- SECTION: One Technology Two Directions -->
        <div class="w-full bg-brand-dark text-white py-24">
            <div class="max-w-[1400px] mx-auto px-6 md:px-12 text-center">
                <h2 class="sharplink-h2 text-white text-4xl md:text-5xl mb-4" data-aos="fade-up">ONE TECHNOLOGY. TWO DIRECTIONS.</h2>
                <h3 class="text-xl md:text-2xl font-bold text-brand-orange uppercase tracking-widest mb-16" data-aos="fade-up" data-aos-delay="100">BREAK THE ASSUMPTIONS. EXPAND THE POSSIBILITIES.</h3>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-5xl mx-auto mb-16 text-left">
                    <div class="p-8 border border-white/20 rounded-2xl bg-white/5 backdrop-blur-sm" data-aos="fade-right">
                        <h4 class="font-bold text-2xl text-white mb-4">SECURITY</h4>
                        <p class="text-white/70 leading-relaxed mb-4">Quantum computing threatens widely deployed public-key cryptographic systems.</p>
                        <p class="text-white/70 leading-relaxed">RSA, Diffie-Hellman and elliptic-curve systems are among the cryptographic technologies that require migration planning for the quantum era.</p>
                    </div>
                    <div class="p-8 border border-white/20 rounded-2xl bg-white/5 backdrop-blur-sm" data-aos="fade-left">
                        <h4 class="font-bold text-2xl text-white mb-4">COMPUTATION</h4>
                        <p class="text-white/70 leading-relaxed mb-4">Quantum computing may provide new approaches to selected problems in simulation, optimization and other computational domains.</p>
                    </div>
                </div>
                
                <div class="bg-black/50 p-8 rounded-2xl max-w-4xl mx-auto border border-brand-orange/30 shadow-2xl shadow-brand-orange/10" data-aos="zoom-in">
                    <p class="text-sm text-white/50 uppercase tracking-widest mb-2">The Resulting Technology Transition:</p>
                    <p class="text-xl md:text-2xl font-bold text-white leading-relaxed">
                        Organizations need to prepare for what quantum could break —<br>
                        <span class="text-brand-orange">while discovering what quantum could make possible.</span>
                    </p>
                </div>
            </div>
        </div>

        <!-- SECTION: The Timelines -->
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 py-24">
            <div class="text-center max-w-4xl mx-auto mb-16">
                <h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-4" data-aos="fade-up">THE TIMELINES ARE ALREADY BEING SET.</h2>
                <h3 class="text-xl md:text-2xl font-bold text-brand-dark/70 uppercase tracking-widest mb-8" data-aos="fade-up" data-aos-delay="100">GOVERNMENTS ARE PLANNING YEARS AHEAD OF THE MACHINE.</h3>
                <p class="text-lg text-brand-dark/80" data-aos="fade-up" data-aos-delay="150">
                    In August 2024, NIST finalized its first three principal post-quantum cryptography standards: <br>
                    <span class="font-bold text-brand-dark">FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), and FIPS 205 (SLH-DSA)</span>.<br><br>
                    The transition has moved from algorithm research to infrastructure planning.
                </p>
            </div>
            
            <div class="overflow-x-auto shadow-2xl rounded-2xl border border-brand-dark/10 mb-16" data-aos="fade-up">
                <table class="w-full text-left bg-white text-sm md:text-base border-collapse">
                    <thead>
                        <tr class="bg-brand-dark text-white uppercase tracking-widest text-xs md:text-sm">
                            <th class="p-6 font-bold w-1/4 border-b border-white/20">REGION</th>
                            <th class="p-6 font-bold w-1/3 border-b border-white/20">CURRENT DIRECTION</th>
                            <th class="p-6 font-bold border-b border-white/20">KEY MILESTONES</th>
                        </tr>
                    </thead>
                    <tbody class="text-brand-dark/80 divide-y divide-brand-dark/10">
                        <tr class="hover:bg-[#f2f2f0] transition-colors">
                            <td class="p-6 font-bold text-brand-dark">United States</td>
                            <td class="p-6">Federal migration to NIST-approved PQC</td>
                            <td class="p-6">High-value/high-impact federal systems: PQC key establishment by <span class="font-bold text-brand-orange">2030</span>, digital signatures by <span class="font-bold text-brand-orange">2031</span>; broader transition continues toward <span class="font-bold text-brand-orange">2035</span></td>
                        </tr>
                        <tr class="hover:bg-[#f2f2f0] transition-colors">
                            <td class="p-6 font-bold text-brand-dark">United Kingdom</td>
                            <td class="p-6">NCSC national migration guidance</td>
                            <td class="p-6">Discovery & plan by <span class="font-bold text-brand-orange">2028</span> → priority migration by <span class="font-bold text-brand-orange">2031</span> → complete by <span class="font-bold text-brand-orange">2035</span></td>
                        </tr>
                        <tr class="hover:bg-[#f2f2f0] transition-colors">
                            <td class="p-6 font-bold text-brand-dark">European Union</td>
                            <td class="p-6">Coordinated EU PQC roadmap</td>
                            <td class="p-6">Member States transition by <span class="font-bold text-brand-orange">end-2026</span>; high-risk use cases by <span class="font-bold text-brand-orange">2030</span></td>
                        </tr>
                        <tr class="hover:bg-[#f2f2f0] transition-colors">
                            <td class="p-6 font-bold text-brand-dark">Australia</td>
                            <td class="p-6">ASD quantum-safe migration guidance</td>
                            <td class="p-6">Transition plan by <span class="font-bold text-brand-orange">2026</span> → migration underway by <span class="font-bold text-brand-orange">2028</span> → completion by <span class="font-bold text-brand-orange">2030</span></td>
                        </tr>
                        <tr class="hover:bg-[#f2f2f0] transition-colors">
                            <td class="p-6 font-bold text-brand-dark">India</td>
                            <td class="p-6">National Quantum-Safe Ecosystem roadmap</td>
                            <td class="p-6">Quantum resiliency for critical infrastructure by <span class="font-bold text-brand-orange">2029</span> → enterprise-wide PQC adoption by <span class="font-bold text-brand-orange">2033</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="text-center" data-aos="fade-up">
                <p class="text-lg text-brand-dark/70 mb-4">These are not identical regulatory mandates, and they should not be presented as though they are.</p>
                <p class="text-2xl font-bold text-brand-dark uppercase tracking-widest">
                    They represent something more important:<br>
                    <span class="text-brand-orange">The global direction is becoming increasingly clear.</span>
                </p>
            </div>
        </div>

        <!-- SECTION: Ecosystem & Early Movers -->
        <div class="w-full bg-[#f2f2f0] py-24 border-y border-brand-dark/10">
            <div class="max-w-[1400px] mx-auto px-6 md:px-12 grid grid-cols-1 lg:grid-cols-2 gap-16">
                
                <div data-aos="fade-right">
                    <h2 class="sharplink-h2 text-brand-dark text-4xl mb-4">WE HAVE SEEN THIS BEFORE.</h2>
                    <h3 class="text-xl font-bold text-brand-dark/70 uppercase tracking-widest mb-8">CRYPTOGRAPHY DOES NOT CHANGE WITH A SWITCH.</h3>
                    <div class="space-y-4 text-brand-dark/80 leading-relaxed mb-8">
                        <p>The move toward stronger cryptographic systems was never simply an algorithm replacement. New standards had to become protocols. Protocols had to become software.</p>
                        <p>Software had to work with certificates, hardware, identity systems, browsers, networks, and vendors.</p>
                        <p>Elliptic-curve cryptography illustrates the pattern. Over time, the technology moved from an emerging alternative to a widely deployed part of modern cryptographic infrastructure.</p>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow border border-brand-dark/5">
                        <p class="font-bold text-brand-dark">The lesson is not that RSA-to-ECC and PQC migration are identical. They are not.</p>
                        <p class="font-bold text-brand-orange text-xl mt-2">The lesson is that cryptographic transitions are ecosystem transitions.</p>
                    </div>
                </div>

                <div data-aos="fade-left">
                    <h2 class="sharplink-h2 text-brand-dark text-4xl mb-4">THE EARLY MOVERS.</h2>
                    <h3 class="text-xl font-bold text-brand-dark/70 uppercase tracking-widest mb-8">THE WEB IS TRANSITIONING BEFORE THE THREAT ARRIVES.</h3>
                    <div class="space-y-4 text-brand-dark/80 leading-relaxed mb-8">
                        <p>Google has been deploying post-quantum protections into Chrome's TLS stack. Chrome 116 introduced support for post-quantum key agreement.</p>
                        <p>Google later enabled the hybrid mechanism by default on desktop Chrome 124. The approach combines classical and post-quantum key exchange so that compatible connections can provide protection against future quantum decryption.</p>
                    </div>
                    <div class="bg-black text-white p-6 rounded-xl shadow-xl">
                        <p class="text-sm text-white/50 uppercase tracking-widest mb-2">An Important Signal</p>
                        <p class="font-bold text-brand-orange text-xl">Infrastructure is being adapted while the ecosystem is still developing.</p>
                    </div>
                </div>

            </div>
        </div>

        <!-- SECTION: Final Strategy & CTA -->
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 py-24 text-center">
            <h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-4" data-aos="fade-up">AWARENESS IS BECOMING PREPARATION.</h2>
            <h3 class="text-xl md:text-2xl font-bold text-brand-dark/70 uppercase tracking-widest mb-16" data-aos="fade-up" data-aos-delay="100">THE QUESTION IS MOVING FROM “IS QUANTUM REAL?” TO “WHERE ARE WE EXPOSED?”</h3>
            
            <p class="text-xl text-brand-dark max-w-3xl mx-auto mb-12" data-aos="fade-up">Organizations do not need to predict the exact year a cryptographically relevant quantum computer will appear. They need to understand the systems that would be affected if it does. That means knowing:</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-4xl mx-auto mb-16 text-left">
                <div class="bg-white p-6 rounded-xl shadow font-bold text-brand-dark uppercase tracking-wide border-l-4 border-brand-orange" data-aos="fade-up" data-aos-delay="100">What cryptography do we use?</div>
                <div class="bg-white p-6 rounded-xl shadow font-bold text-brand-dark uppercase tracking-wide border-l-4 border-brand-orange" data-aos="fade-up" data-aos-delay="150">Where is it used?</div>
                <div class="bg-white p-6 rounded-xl shadow font-bold text-brand-dark uppercase tracking-wide border-l-4 border-brand-orange" data-aos="fade-up" data-aos-delay="200">Which data must remain confidential — and for how long?</div>
                <div class="bg-white p-6 rounded-xl shadow font-bold text-brand-dark uppercase tracking-wide border-l-4 border-brand-orange" data-aos="fade-up" data-aos-delay="250">Which systems cannot be easily replaced?</div>
                <div class="bg-white p-6 rounded-xl shadow font-bold text-brand-dark uppercase tracking-wide border-l-4 border-brand-orange md:col-span-2" data-aos="fade-up" data-aos-delay="300">Which suppliers and technologies are part of the dependency chain?</div>
            </div>

            <div class="bg-brand-dark text-white p-12 rounded-3xl shadow-2xl max-w-4xl mx-auto" data-aos="zoom-in">
                <h3 class="text-2xl md:text-3xl font-bold mb-6">THIS IS WHY QUANTUM MATTERS NOW.</h3>
                <p class="text-white/80 text-lg mb-8 leading-relaxed">
                    Not because the quantum computer has arrived. Because the decisions required to prepare for it have. The organizations that understand their position early will have more choices later.
                </p>
                <div class="flex justify-center">
                    <a href="quantum-technology.html" class="inline-flex items-center gap-3 bg-brand-orange text-white px-8 py-4 rounded-full font-bold uppercase tracking-widest hover:bg-brand-orange/90 transition-all hover:scale-105 active:scale-95 text-sm md:text-base">
                        UNDERSTAND YOUR QUANTUM POSITION <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>
        </div>
    </main>
"""

# Let's replace the title and og:title tags
new_header = header_part[:header_close] + new_hero
new_header = new_header.replace('<title>Quantum Technology | Hadron Quantum Labs</title>', '<title>Why Quantum? | Hadron Quantum Labs</title>')
new_header = new_header.replace('content="Explore our post-quantum cryptography"', 'content="Understand why quantum computing is changing the assumptions behind digital infrastructure."')

full_new_page = new_header + new_main + footer_part

with open('why-quantum.html', 'w') as f:
    f.write(full_new_page)
print("Created why-quantum.html")

