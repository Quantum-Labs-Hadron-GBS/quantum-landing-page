const fs = require('fs');

const newFooterHTML = `
    <!-- RICH FOOTER -->
    <footer id="contact" class="relative overflow-hidden bg-[#080808] border-t border-white/[0.06]">
        
        <!-- Big BG Word -->
        <div aria-hidden="true" class="pointer-events-none absolute inset-x-0 bottom-0 flex justify-center overflow-hidden select-none">
            <span class="text-[clamp(80px,20vw,220px)] font-black tracking-tighter text-white/[0.025] leading-none pb-2 translate-y-6">HADRON</span>
        </div>

        <div class="relative z-10 max-w-7xl mx-auto px-6 pt-20 pb-8">

            <!-- Top Section CTA Banner -->
            <div class="relative rounded-3xl overflow-hidden mb-20">
                <div class="absolute inset-0 bg-center bg-no-repeat brightness-150 blur scale-125 hue-rotate-[-45deg] saturate-[1.2]" style="background-image:url('https://res.cloudinary.com/djxbxhgat/image/upload/v1785142156/BG_m1typg.jpg');background-size:150%" aria-hidden="true"></div>
                <div class="absolute inset-0 bg-black/30"></div>
                <div class="relative z-10 flex flex-col sm:flex-row items-center justify-between gap-6 px-8 py-10 sm:px-12">
                    <div>
                        <h2 class="text-2xl sm:text-3xl font-medium text-black tracking-tight">Ready to optimize your enterprise infrastructure?</h2>
                        <p class="text-black/60 mt-1 text-sm">Speak to the Hadron Quantum Labs team today.</p>
                    </div>
                    <a href="contact.html" class="shrink-0 inline-flex items-center gap-2 bg-black text-white px-6 py-3 rounded-xl text-sm font-semibold hover:bg-black/80 transition-colors">
                        Contact Us
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m7 7 10 10"/><path d="M17 7v10H7"/></svg>
                    </a>
                </div>
            </div>

            <!-- Main Footer Grid -->
            <div class="grid grid-cols-1 lg:grid-cols-[1.8fr_1fr_1.4fr] gap-12 lg:gap-8 mb-16">

                <!-- Col 1: Brand + Map -->
                <div>
                    <a href="https://www.hadrongbs.com" target="_blank" rel="noopener" class="inline-block mb-5">
                        <img src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png" alt="Hadron GBS" class="h-7 w-auto opacity-90" />
                    </a>
                    <p class="text-sm text-white/40 leading-relaxed mb-3 max-w-sm">
                        Hadron Quantum Labs is the quantum division of <a href="https://www.hadrongbs.com" target="_blank" rel="noopener" class="text-accent/70 hover:text-accent transition-colors">Hadron Global Business Solutions</a>, delivering AI infrastructure optimization and Post-Quantum Cryptography readiness audits for enterprise data centers worldwide.
                    </p>
                    <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-accent/10 border border-accent/20 text-accent text-xs font-medium mb-6">
                        <span class="w-1.5 h-1.5 rounded-full bg-accent animate-pulse"></span>
                        Quantum Division of Hadron GBS
                    </div>

                    <!-- Office Map Tabs -->
                    <div>
                        <p class="text-xs font-medium text-white/30 uppercase tracking-widest mb-3">Global Offices — Interactive Map</p>
                        <div class="flex flex-wrap gap-1.5 mb-3" id="map-tabs">
                            <button onclick="switchMap('pune','https://maps.google.com/maps?q=Pyramid+Axis,Baner,Pune&t=&z=14&ie=UTF8&iwloc=&output=embed')" class="map-tab map-tab-active px-3 py-1 rounded-lg text-xs font-medium transition-colors" data-office="pune">Pune</button>
                            <button onclick="switchMap('singapore','https://maps.google.com/maps?q=7+Temasek+Boulevard,Suntec+Tower,Singapore&t=&z=14&ie=UTF8&iwloc=&output=embed')" class="map-tab px-3 py-1 rounded-lg text-xs font-medium transition-colors" data-office="singapore">Singapore</button>
                            <button onclick="switchMap('dubai','https://maps.google.com/maps?q=Westburry+Tower+1,Business+Bay,Dubai&t=&z=14&ie=UTF8&iwloc=&output=embed')" class="map-tab px-3 py-1 rounded-lg text-xs font-medium transition-colors" data-office="dubai">Dubai</button>
                            <button onclick="switchMap('usa','https://maps.google.com/maps?q=8+The+Green,Dover,DE&t=&z=14&ie=UTF8&iwloc=&output=embed')" class="map-tab px-3 py-1 rounded-lg text-xs font-medium transition-colors" data-office="usa">USA</button>
                        </div>
                        <div class="rounded-xl overflow-hidden border border-white/[0.07]">
                            <iframe id="office-map" 
                                src="https://maps.google.com/maps?q=Pyramid+Axis,Baner,Pune&t=&z=14&ie=UTF8&iwloc=&output=embed"
                                width="100%" height="200" 
                                style="border:0;display:block;filter:grayscale(0.7) contrast(1.1) brightness(0.9);" 
                                allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade"
                                title="Hadron GBS Office Map">
                            </iframe>
                        </div>
                    </div>
                </div>

                <!-- Col 2: Quick Links + Contact -->
                <div class="flex flex-col gap-8">
                    <div>
                        <p class="text-xs font-medium text-white/30 uppercase tracking-widest mb-4">Quick Links</p>
                        <ul class="space-y-2.5">
                            <li><a href="index.html" class="text-sm text-white/55 hover:text-white transition-colors">Home</a></li>
                            <li><a href="index.html#solutions" class="text-sm text-white/55 hover:text-white transition-colors">Solutions</a></li>
                            <li><a href="index.html#workflow" class="text-sm text-white/55 hover:text-white transition-colors">Workflow</a></li>
                            <li><a href="index.html#pricing" class="text-sm text-white/55 hover:text-white transition-colors">Offerings</a></li>
                            <li><a href="index.html#faq-accordion" class="text-sm text-white/55 hover:text-white transition-colors">FAQ</a></li>
                            <li><a href="contact.html" class="text-sm text-white/55 hover:text-white transition-colors">Contact Us</a></li>
                            <li><a href="https://www.hadrongbs.com" target="_blank" rel="noopener" class="text-sm text-accent/70 hover:text-accent transition-colors flex items-center gap-1">Hadron GBS <svg xmlns="http://www.w3.org/2000/svg" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6"/><path d="M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/></svg></a></li>
                        </ul>
                    </div>
                    <div>
                        <p class="text-xs font-medium text-white/30 uppercase tracking-widest mb-4">Get In Touch</p>
                        <ul class="space-y-2.5">
                            <li>
                                <a href="mailto:quantum.labs@hadrongbs.com" class="text-sm text-white/55 hover:text-white transition-colors flex items-center gap-2">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-accent"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7"/></svg>
                                    quantum.labs@hadrongbs.com
                                </a>
                            </li>
                            <li>
                                <a href="mailto:info@hadrongbs.com" class="text-sm text-white/55 hover:text-white transition-colors flex items-center gap-2">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-accent"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7"/></svg>
                                    info@hadrongbs.com
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>

                <!-- Col 3: Global Offices -->
                <div>
                    <p class="text-xs font-medium text-white/30 uppercase tracking-widest mb-4">Global Offices</p>
                    <div class="space-y-5">
                        <div class="group">
                            <p class="text-xs font-semibold text-accent/80 uppercase tracking-widest mb-0.5">Pune — HQ</p>
                            <p class="text-xs font-medium text-white/60">Hadron Global Business Solutions Pvt Ltd</p>
                            <p class="text-xs text-white/35 leading-relaxed mt-0.5">Pyramid Axis 10th Floor, Veerbhadra Nagar, Baner, Pune, Maharashtra 411045</p>
                        </div>
                        <div class="group">
                            <p class="text-xs font-semibold text-accent/80 uppercase tracking-widest mb-0.5">Pune — Hinjewadi</p>
                            <p class="text-xs font-medium text-white/60">Hadron Global Business Solutions Pvt Ltd</p>
                            <p class="text-xs text-white/35 leading-relaxed mt-0.5">A 1004, High Mont, Phase 2, Hinjewadi, Pune, Maharashtra 411057</p>
                        </div>
                        <div class="group">
                            <p class="text-xs font-semibold text-accent/80 uppercase tracking-widest mb-0.5">Singapore</p>
                            <p class="text-xs font-medium text-white/60">Hadron GBS Pte Ltd</p>
                            <p class="text-xs text-white/35 leading-relaxed mt-0.5">7 Temasek Boulevard, Suntec Tower One, Singapore 038987</p>
                        </div>
                        <div class="group">
                            <p class="text-xs font-semibold text-accent/80 uppercase tracking-widest mb-0.5">Dubai, UAE</p>
                            <p class="text-xs font-medium text-white/60">Hadron Technologies LLC</p>
                            <p class="text-xs text-white/35 leading-relaxed mt-0.5">303, Westburry Tower 1, Business Bay, Dubai, UAE</p>
                        </div>
                        <div class="group">
                            <p class="text-xs font-semibold text-accent/80 uppercase tracking-widest mb-0.5">USA</p>
                            <p class="text-xs font-medium text-white/60">Hadron GBS Inc.</p>
                            <p class="text-xs text-white/35 leading-relaxed mt-0.5">8 The Green, Ste R, Dover, DE 19901, USA</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Divider -->
            <div class="border-t border-white/[0.06] mb-6"></div>

            <!-- Bottom Bar -->
            <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
                <p class="text-xs text-white/25 text-center sm:text-left">
                    © 2026 Hadron Quantum Labs — A Division of <a href="https://www.hadrongbs.com" target="_blank" rel="noopener" class="hover:text-white/50 transition-colors">Hadron Global Business Solutions (GBS)</a>. All rights reserved.
                </p>
                <!-- Social Links -->
                <div class="flex items-center gap-2">
                    <a href="https://x.com/HadronGBS" target="_blank" rel="noopener noreferrer" aria-label="X (Twitter)" class="w-8 h-8 rounded-lg bg-white/[0.05] hover:bg-white/[0.1] border border-white/[0.06] flex items-center justify-center text-white/40 hover:text-white transition-all text-xs font-bold">𝕏</a>
                    <a href="https://www.linkedin.com/company/hadron-gbs/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" class="w-8 h-8 rounded-lg bg-white/[0.05] hover:bg-white/[0.1] border border-white/[0.06] flex items-center justify-center text-white/40 hover:text-white transition-all text-xs font-bold">in</a>
                    <a href="https://www.youtube.com/@HadronGBS" target="_blank" rel="noopener noreferrer" aria-label="YouTube" class="w-8 h-8 rounded-lg bg-white/[0.05] hover:bg-white/[0.1] border border-white/[0.06] flex items-center justify-center text-white/40 hover:text-white transition-all text-xs">▶</a>
                    <a href="https://www.facebook.com/profile.php?id=61560719736422" target="_blank" rel="noopener noreferrer" aria-label="Facebook" class="w-8 h-8 rounded-lg bg-white/[0.05] hover:bg-white/[0.1] border border-white/[0.06] flex items-center justify-center text-white/40 hover:text-white transition-all text-xs font-bold">f</a>
                </div>
            </div>
        </div>

        <style>
            .map-tab {
                background: rgba(255,255,255,0.04);
                border: 1px solid rgba(255,255,255,0.07);
                color: rgba(255,255,255,0.4);
                cursor: pointer;
            }
            .map-tab:hover { background: rgba(255,255,255,0.08); color: rgba(255,255,255,0.7); }
            .map-tab-active { background: rgba(255,159,43,0.15) !important; border-color: rgba(255,159,43,0.3) !important; color: #ff9f2b !important; }
        </style>
        <script>
            function switchMap(office, url) {
                document.getElementById('office-map').src = url;
                document.querySelectorAll('.map-tab').forEach(btn => {
                    btn.classList.remove('map-tab-active');
                    if (btn.dataset.office === office) btn.classList.add('map-tab-active');
                });
            }
        </script>
    </footer>`;

// ---- index.html: Replace old footer ----
let html = fs.readFileSync('index.html', 'utf8');

// Remove old footer (from <footer id="contact" to </footer>)
const footerStart = html.indexOf('<footer id="contact"');
const footerEnd = html.indexOf('</footer>') + '</footer>'.length;
if (footerStart !== -1 && footerEnd > footerStart) {
    html = html.substring(0, footerStart) + newFooterHTML + html.substring(footerEnd);
    console.log('Replaced footer in index.html');
} else {
    console.error('Could not find footer in index.html');
}

fs.writeFileSync('index.html', html);

// ---- contact.html: Replace old footer ----
let contact = fs.readFileSync('contact.html', 'utf8');

// Contact footer is a plain <footer> tag
const cFooterStart = contact.indexOf('<footer');
const cFooterEnd = contact.indexOf('</footer>') + '</footer>'.length;
if (cFooterStart !== -1 && cFooterEnd > cFooterStart) {
    // Build contact version (CTA banner links back to index.html not contact.html)
    const contactFooter = newFooterHTML.replace(
        '<a href="contact.html" class="shrink-0',
        '<a href="index.html" class="shrink-0'
    );
    contact = contact.substring(0, cFooterStart) + contactFooter + contact.substring(cFooterEnd);
    console.log('Replaced footer in contact.html');
} else {
    console.error('Could not find footer in contact.html');
}

fs.writeFileSync('contact.html', contact);
console.log('\n✅ Rich footer injected into both pages!');
