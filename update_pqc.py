import re

with open('pqc-security.html', 'r') as f:
    content = f.read()

old_content = r'''<h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-6" data-aos="fade-up">ServiceNow\s*Orchestration</h2>\s*<p class="sharplink-body text-brand-dark/70 mb-6">\s*ServiceNow can serve as an important implementation and operationalization layer for our\s*QaaS offerings\. We turn PQC readiness from a one-time assessment into an ongoing enterprise\s*program\.\s*</p>\s*<ul class="space-y-6 mt-8">\s*<li class="flex items-start gap-4">\s*<div\s*class="w-8 h-8 rounded-full bg-brand-dark text-white font-bold flex items-center justify-center shrink-0 text-sm mt-1">\s*1</div>\s*<div>\s*<h4 class="font-bold text-brand-dark">Discover & Assess</h4>\s*<p class="text-sm text-brand-dark/60 mt-1">Identify cryptographic assets and\s*determine algorithm, certificate, key, and system exposure\.</p>\s*</div>\s*</li>\s*<li class="flex items-start gap-4">\s*<div\s*class="w-8 h-8 rounded-full bg-brand-dark text-white font-bold flex items-center justify-center shrink-0 text-sm mt-1">\s*2</div>\s*<div>\s*<h4 class="font-bold text-brand-dark">Prioritize & Create</h4>\s*<p class="text-sm text-brand-dark/60 mt-1">Rank assets based on risk and\s*criticality, then generate remediation tasks and migration activities\.</p>\s*</div>\s*</li>\s*<li class="flex items-start gap-4">\s*<div\s*class="w-8 h-8 rounded-full bg-brand-orange text-white font-bold flex items-center justify-center shrink-0 text-sm mt-1">\s*3</div>\s*<div>\s*<h4 class="font-bold text-brand-dark">Orchestrate & Track</h4>\s*<p class="text-sm text-brand-dark/60 mt-1">Route activities to security,\s*infrastructure, application, and vendor teams and monitor remediation progress\.\s*</p>\s*</div>\s*</li>\s*</ul>'''

new_content = '''<h2 class="sharplink-h2 text-brand-dark text-4xl md:text-5xl mb-6" data-aos="fade-up">Enterprise<br>Security Integrations</h2>
                        <p class="sharplink-body text-brand-dark/70 mb-6">
                            A post-quantum strategy cannot exist in a vacuum. We integrate our cryptographic discovery and remediation workflows directly into the tools your security, infrastructure, and compliance teams already rely on.
                        </p>
                        <ul class="space-y-6 mt-8">
                            <li class="flex items-start gap-4" data-aos="fade-up" data-aos-delay="100">
                                <div class="w-8 h-8 rounded-full bg-brand-dark text-white font-bold flex items-center justify-center shrink-0 text-sm mt-1">1</div>
                                <div>
                                    <h4 class="font-bold text-brand-dark">Asset Management (CMDB)</h4>
                                    <p class="text-sm text-brand-dark/60 mt-1">Integrate cryptographic discovery into your existing configuration management databases for unified visibility.</p>
                                </div>
                            </li>
                            <li class="flex items-start gap-4" data-aos="fade-up" data-aos-delay="150">
                                <div class="w-8 h-8 rounded-full bg-brand-dark text-white font-bold flex items-center justify-center shrink-0 text-sm mt-1">2</div>
                                <div>
                                    <h4 class="font-bold text-brand-dark">SIEM & SOAR</h4>
                                    <p class="text-sm text-brand-dark/60 mt-1">Route cryptographic vulnerabilities and migration alerts into your existing security operations workflows.</p>
                                </div>
                            </li>
                            <li class="flex items-start gap-4" data-aos="fade-up" data-aos-delay="200">
                                <div class="w-8 h-8 rounded-full bg-brand-orange text-white font-bold flex items-center justify-center shrink-0 text-sm mt-1">3</div>
                                <div>
                                    <h4 class="font-bold text-brand-dark">Key Management & PKI</h4>
                                    <p class="text-sm text-brand-dark/60 mt-1">Align post-quantum certificate generation and crypto-agility with your established KMS and HSM infrastructure.</p>
                                </div>
                            </li>
                        </ul>'''

if re.search(old_content, content, re.DOTALL):
    content = re.sub(old_content, new_content, content, flags=re.DOTALL)
    with open('pqc-security.html', 'w') as f:
        f.write(content)
    print("Successfully replaced content.")
else:
    print("Could not find content to replace.")

