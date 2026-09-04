import re

with open('why-quantum.html', 'r') as f:
    content = f.read()

# Find bounds
start_marker = '<!-- Premium Dark Hero -->'
end_marker = '<!-- How We Deliver Section -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find markers!")
    exit(1)

head = content[:start_idx]
tail = content[end_idx:]

new_body = """<!-- Premium Dark Hero -->
    <div class="relative w-full min-h-[90vh] bg-black overflow-hidden flex items-center pt-32 pb-24">
        <div class="absolute inset-0 z-0">
            <div class="absolute top-0 right-0 w-[800px] h-[800px] bg-brand-orange/10 rounded-full blur-[120px] mix-blend-screen transform translate-x-1/3 -translate-y-1/4"></div>
            <div class="absolute bottom-0 left-0 w-[600px] h-[600px] bg-white/5 rounded-full blur-[100px] mix-blend-screen transform -translate-x-1/3 translate-y-1/4"></div>
        </div>
        <div class="absolute inset-0 bg-grid-pattern opacity-10 z-0"></div>

        <div class="w-full max-w-[1400px] mx-auto px-6 md:px-12 relative z-10 flex flex-col justify-center h-full">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 mb-12 backdrop-blur-sm self-start" data-aos="fade-up">
                <span class="w-2 h-2 rounded-full bg-brand-orange animate-pulse"></span>
                <span class="text-[11px] md:text-[13px] font-bold text-white/70 uppercase tracking-widest">Enterprise Briefing</span>
            </div>
            
            <h1 class="font-bank-gothic text-4xl md:text-5xl lg:text-6xl text-brand-orange mb-8 tracking-wide uppercase" data-aos="fade-up" data-aos-delay="100">
                WHY QUANTUM?
            </h1>
            
            <h2 class="text-[clamp(3rem,6vw,7rem)] font-bold text-white leading-[0.95] tracking-tight max-w-6xl mb-12" data-aos="fade-up" data-aos-delay="200" style="font-family: 'Archivo', sans-serif;">
                QUANTUM IS CHANGING<br>THE ASSUMPTIONS<br>BEHIND COMPUTING.
            </h2>
            
            <div class="max-w-2xl text-white/60 text-lg md:text-xl font-light leading-relaxed border-l-2 border-brand-orange/50 pl-6" data-aos="fade-up" data-aos-delay="300">
                <p>For decades, modern digital infrastructure has depended on mathematical problems that are extremely difficult for classical computers to solve. The implications of quantum reach deep into the cryptography that protects digital communication, while opening new possibilities for problems classical systems struggle to solve.</p>
            </div>
        </div>
    </div>

    <!-- SCENE 02: THE INTERNET (LIGHT) -->
    <main class="relative z-20" style="background: radial-gradient(ellipse 100% 130% at 50% -30%, #c4d5e7 45%, #fdfbf7 85%, #f7f7f5);">
        
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 py-32 md:py-48 flex flex-col">
            <h2 class="text-[clamp(4rem,9vw,9rem)] font-black text-brand-dark leading-[0.85] tracking-tighter mb-8" data-aos="fade-up" style="font-family: 'Archivo', sans-serif;">
                THE INTERNET<br>RUNS ON MATH.
            </h2>
            
            <h3 class="text-xl md:text-3xl font-medium text-brand-dark/60 max-w-4xl mb-24 leading-snug" data-aos="fade-up" data-aos-delay="100">
                Some of that mathematics may not survive a cryptographically relevant quantum computer.
            </h3>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-16 max-w-6xl">
                <div class="space-y-6 text-brand-dark/80 text-lg leading-relaxed" data-aos="fade-right">
                    <p>Public-key cryptography sits underneath much of today's digital infrastructure. It helps establish secure connections, authenticate systems, protect communications, and establish trust between organizations and machines.</p>
                </div>
                <div class="space-y-6 text-brand-dark/80 text-lg leading-relaxed" data-aos="fade-left">
                    <p>Algorithms such as RSA and elliptic-curve cryptography derive their security from mathematical problems that are difficult for classical computers. Shor's algorithm provides a theoretical path to efficiently solving those exact problems.</p>
                </div>
            </div>
        </div>

    </main>

    <!-- SCENE 03, 04, 05: THE THREAT & DUALITY (DARK) -->
    <div class="w-full bg-black text-white relative overflow-hidden">
        <div class="absolute inset-0 bg-grid-pattern opacity-10"></div>
        
        <!-- Scene 03: Harvest Now -->
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 py-32 md:py-48 relative z-10 border-b border-white/10">
            <p class="text-[12px] md:text-[14px] text-brand-orange uppercase tracking-widest font-bold mb-8" data-aos="fade-right">THE THREAT IS NOT WAITING.</p>
            
            <h2 class="text-[clamp(4.5rem,10vw,11rem)] font-black text-white leading-[0.85] tracking-tighter mb-16" data-aos="fade-up" style="font-family: 'Archivo', sans-serif;">
                HARVEST NOW.<br>DECRYPT LATER.
            </h2>
            
            <div class="max-w-3xl text-white/70 text-lg md:text-xl leading-relaxed" data-aos="fade-up" data-aos-delay="100">
                <p>Sensitive information does not necessarily need to be decrypted today to become a target today. An adversary can capture encrypted traffic now, retain it, and attempt to decrypt it later when sufficiently capable quantum computing becomes available. The risk is greatest for information whose confidentiality must survive for decades.</p>
            </div>
        </div>

        <!-- Scene 04: Salt Typhoon -->
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 py-32 md:py-40 relative z-10 border-b border-white/10">
            <h3 class="text-3xl md:text-5xl font-medium text-white/50 mb-4" data-aos="fade-up" style="font-family: 'Archivo', sans-serif;">
                <span class="text-white font-bold">SALT TYPHOON</span> wasn't a quantum attack.
            </h3>
            
            <h2 class="text-[clamp(4rem,8vw,8rem)] font-black text-brand-orange leading-[0.9] tracking-tighter mb-12" data-aos="fade-up" data-aos-delay="100" style="font-family: 'Archivo', sans-serif;">
                THAT'S THE POINT.
            </h2>
            
            <div class="max-w-3xl text-white/60 text-lg mb-16" data-aos="fade-up" data-aos-delay="150">
                <p>Salt Typhoon demonstrated something simpler: valuable data can be collected long before anyone can decrypt it.</p>
            </div>

            <div class="flex flex-col gap-8 max-w-4xl" data-aos="fade-up" data-aos-delay="200">
                <p class="text-2xl md:text-4xl font-bold text-white tracking-wide">DATA CAN BE COLLECTED TODAY.</p>
                <div class="w-1 h-12 bg-white/20 ml-4 rounded-full"></div>
                <p class="text-2xl md:text-4xl font-bold text-brand-orange tracking-wide">DATA MAY BE DECRYPTED TOMORROW.</p>
            </div>
        </div>

        <!-- Scene 05: Duality -->
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 py-32 md:py-48 relative z-10">
            <p class="text-[12px] md:text-[14px] text-brand-orange uppercase tracking-widest font-bold mb-8 text-center md:text-left" data-aos="fade-right">ONE TECHNOLOGY. TWO DIRECTIONS.</p>
            
            <div class="flex flex-col gap-6 md:gap-2 mb-24">
                <h2 class="text-[clamp(3.5rem,8vw,8rem)] font-black text-white leading-[0.9] tracking-tighter" data-aos="fade-up" style="font-family: 'Archivo', sans-serif;">
                    BREAK THE ASSUMPTIONS.
                </h2>
                <h2 class="text-[clamp(3.5rem,8vw,8rem)] font-black text-white/30 leading-[0.9] tracking-tighter" data-aos="fade-up" data-aos-delay="100" style="font-family: 'Archivo', sans-serif;">
                    EXPAND THE POSSIBILITIES.
                </h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-16 max-w-5xl">
                <div class="border-t-2 border-white/20 pt-8" data-aos="fade-up" data-aos-delay="200">
                    <h4 class="font-bold text-2xl md:text-3xl text-white mb-4 tracking-wide">SECURITY</h4>
                    <p class="text-white/60 text-lg leading-relaxed">What quantum could break. Cryptographic systems like RSA and elliptic-curve require migration planning today to survive the quantum era tomorrow.</p>
                </div>
                <div class="border-t-2 border-brand-orange/40 pt-8" data-aos="fade-up" data-aos-delay="300">
                    <h4 class="font-bold text-2xl md:text-3xl text-brand-orange mb-4 tracking-wide">COMPUTATION</h4>
                    <p class="text-white/60 text-lg leading-relaxed">What quantum could enable. New approaches to problems in simulation, materials, and optimization where classical compute stalls.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- SCENE 06 & 07: TIMELINE & CHROME (LIGHT) -->
    <div class="w-full relative py-32 md:py-40" style="background: radial-gradient(ellipse 100% 130% at 50% -30%, #fdfbf7 45%, #e8edf2 85%, #f7f7f5);">
        
        <!-- Scene 06: Timeline -->
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 mb-40">
            <h2 class="text-[clamp(3.5rem,7vw,7rem)] font-black text-brand-dark leading-[0.9] tracking-tighter mb-20" data-aos="fade-up" style="font-family: 'Archivo', sans-serif;">
                THE CLOCK IS ALREADY MOVING.
            </h2>
            
            <div class="flex flex-wrap md:flex-nowrap items-start gap-8 md:gap-4 lg:gap-12" data-aos="fade-up" data-aos-delay="100">
                
                <!-- 2026 -->
                <div class="flex flex-col min-w-[120px]">
                    <span class="text-4xl md:text-[clamp(3rem,4vw,4rem)] font-black text-brand-dark mb-4">2026</span>
                    <span class="text-sm font-bold text-brand-dark/60 uppercase tracking-widest border-l-2 border-brand-orange pl-3 py-1">EU<br>AUSTRALIA</span>
                </div>
                
                <div class="hidden md:flex items-center self-start mt-6 text-brand-dark/20"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
                
                <!-- 2028 -->
                <div class="flex flex-col min-w-[120px]">
                    <span class="text-4xl md:text-[clamp(3rem,4vw,4rem)] font-black text-brand-dark mb-4">2028</span>
                    <span class="text-sm font-bold text-brand-dark/60 uppercase tracking-widest border-l-2 border-brand-orange pl-3 py-1">UK<br>AUSTRALIA</span>
                </div>
                
                <div class="hidden md:flex items-center self-start mt-6 text-brand-dark/20"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
                
                <!-- 2029 -->
                <div class="flex flex-col min-w-[120px]">
                    <span class="text-4xl md:text-[clamp(3rem,4vw,4rem)] font-black text-brand-dark mb-4">2029</span>
                    <span class="text-sm font-bold text-brand-dark/60 uppercase tracking-widest border-l-2 border-brand-orange pl-3 py-1">INDIA</span>
                </div>

                <div class="hidden lg:flex items-center self-start mt-6 text-brand-dark/20"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
                
                <!-- 2030 -->
                <div class="flex flex-col min-w-[120px]">
                    <span class="text-4xl md:text-[clamp(3rem,4vw,4rem)] font-black text-brand-dark mb-4">2030</span>
                    <span class="text-sm font-bold text-brand-dark/60 uppercase tracking-widest border-l-2 border-brand-orange pl-3 py-1">US<br>EU<br>AUSTRALIA</span>
                </div>
                
                <div class="hidden md:flex items-center self-start mt-6 text-brand-dark/20"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
                
                <!-- 2031 -->
                <div class="flex flex-col min-w-[120px]">
                    <span class="text-4xl md:text-[clamp(3rem,4vw,4rem)] font-black text-brand-dark mb-4">2031</span>
                    <span class="text-sm font-bold text-brand-dark/60 uppercase tracking-widest border-l-2 border-brand-orange pl-3 py-1">UK<br>US</span>
                </div>

                <div class="hidden md:flex items-center self-start mt-6 text-brand-dark/20"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>

                <!-- 2033 -->
                <div class="flex flex-col min-w-[120px]">
                    <span class="text-4xl md:text-[clamp(3rem,4vw,4rem)] font-black text-brand-dark mb-4">2033</span>
                    <span class="text-sm font-bold text-brand-dark/60 uppercase tracking-widest border-l-2 border-brand-orange pl-3 py-1">INDIA</span>
                </div>
                
                <div class="hidden md:flex items-center self-start mt-6 text-brand-dark/20"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>

                <!-- 2035 -->
                <div class="flex flex-col min-w-[120px]">
                    <span class="text-4xl md:text-[clamp(3rem,4vw,4rem)] font-black text-brand-dark mb-4">2035</span>
                    <span class="text-sm font-bold text-brand-dark/60 uppercase tracking-widest border-l-2 border-brand-orange pl-3 py-1">US<br>UK</span>
                </div>

            </div>
        </div>

        <!-- Scene 07: Chrome Movers -->
        <div class="max-w-[1400px] mx-auto px-6 md:px-12">
            <h3 class="text-2xl md:text-3xl font-bold text-brand-dark/40 uppercase tracking-widest mb-4" data-aos="fade-up">WE HAVE SEEN THIS BEFORE.</h3>
            <h2 class="text-[clamp(3rem,6vw,6rem)] font-black text-brand-dark leading-[0.9] tracking-tighter mb-20" data-aos="fade-up" data-aos-delay="100" style="font-family: 'Archivo', sans-serif;">
                THE WEB IS ALREADY ADAPTING.
            </h2>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 max-w-5xl">
                <div data-aos="fade-up" data-aos-delay="200">
                    <h4 class="text-[clamp(3rem,5vw,5rem)] font-bold text-brand-dark leading-none tracking-tight mb-6">CHROME 116</h4>
                    <p class="text-xl text-brand-dark/70 font-medium border-l-4 border-brand-dark/10 pl-4 py-1">Post-quantum key agreement support introduced into the web stack.</p>
                </div>
                <div data-aos="fade-up" data-aos-delay="300">
                    <h4 class="text-[clamp(3rem,5vw,5rem)] font-bold text-brand-dark leading-none tracking-tight mb-6">CHROME 124</h4>
                    <p class="text-xl text-brand-dark/70 font-medium border-l-4 border-brand-orange pl-4 py-1">Hybrid post-quantum key exchange enabled by default on desktop.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- SCENE 08: CTA (DARK) -->
    <div class="w-full bg-black text-white relative py-32 md:py-48 flex flex-col items-center text-center">
        <div class="absolute inset-0 bg-grid-pattern opacity-10 z-0"></div>
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 relative z-10 flex flex-col items-center">
            
            <h2 class="text-2xl md:text-4xl font-medium text-white/50 uppercase tracking-widest mb-4" data-aos="fade-up" style="font-family: 'Archivo', sans-serif;">
                THE QUESTION IS NO LONGER
            </h2>
            <h3 class="text-2xl md:text-4xl font-light italic text-white/40 mb-16" data-aos="fade-up" data-aos-delay="100">
                "Is quantum real?"
            </h3>
            
            <h1 class="text-[clamp(4rem,9vw,9rem)] font-black text-brand-orange leading-[0.85] tracking-tighter mb-16" data-aos="fade-up" data-aos-delay="200" style="font-family: 'Archivo', sans-serif;">
                WHERE ARE<br>WE EXPOSED?
            </h1>
            
            <p class="text-xl md:text-2xl text-white/70 max-w-3xl font-light leading-relaxed mb-16" data-aos="fade-up" data-aos-delay="300">
                Organizations that understand their position early will have more choices later.
            </p>

            <div data-aos="zoom-in" data-aos-delay="400">
                <a href="contact.html" class="inline-flex items-center justify-center bg-white text-black px-10 py-5 rounded-full text-lg font-bold uppercase tracking-widest hover:bg-brand-orange hover:text-white transition-all hover:scale-105 active:scale-95 shadow-[0_0_40px_rgba(255,255,255,0.1)] hover:shadow-[0_0_40px_rgba(255,159,43,0.3)]">
                    FIND YOUR EXPOSURE
                </a>
            </div>
        </div>
    </div>

    """

with open('why-quantum.html', 'w') as f:
    f.write(head + new_body + tail)

print("Rewrote why-quantum.html")
