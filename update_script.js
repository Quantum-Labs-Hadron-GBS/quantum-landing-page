const fs = require('fs');

try {
  let contactHtml = fs.readFileSync('contact.html', 'utf8');

  // Replace everything inside <main> and before <footer> with our Contact Form
  const mainStartRegex = /(<main id="main-content" class="flex-1 relative overflow-hidden">)[\s\S]*?(<footer id="contact" class="relative mt-48 mx-2\.5 max-\[850px\]:mx-0">)/;

  const contactFormHTML = `
            <!-- Global Grid -->
            <div class="absolute inset-0 pointer-events-none -z-20 bg-background overflow-hidden" aria-hidden="true">
                <div class="absolute inset-0 bg-[linear-gradient(to_right,rgba(255,159,43,0.03)_1px,transparent_1px),linear-gradient(to_bottom,rgba(255,159,43,0.03)_1px,transparent_1px)] bg-[size:64px_64px]"></div>
                <div class="absolute inset-0 bg-[linear-gradient(to_right,rgba(255,159,43,0.08)_1px,transparent_1px),linear-gradient(to_bottom,rgba(255,159,43,0.08)_1px,transparent_1px)] bg-[size:256px_256px]"></div>
                <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,transparent_40%,#000000_100%)] opacity-80"></div>
                <div class="absolute top-0 w-full h-[600px] bg-[linear-gradient(to_bottom,rgba(255,159,43,0.1),transparent)]"></div>
            </div>

            <section class="flex flex-col relative py-32 px-6" style="color-scheme:light; min-height: 80vh;">
                <div class="max-w-2xl mx-auto w-full z-10 bg-frame/80 backdrop-blur-md p-8 md:p-12 rounded-3xl border border-white/10 shadow-2xl mt-12">
                    <h1 class="text-4xl md:text-5xl font-medium tracking-tight mb-4 text-white text-center">Contact Us</h1>
                    <p class="text-muted-foreground text-center mb-8">Reach out to the Hadron Quantum team. We're here to help.</p>

                    <form id="contact-page-form" class="space-y-6">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div class="space-y-2">
                                <label for="name" class="text-sm font-medium text-foreground">Name <span class="text-accent">*</span></label>
                                <input type="text" id="name" name="name" required class="w-full bg-background border border-border rounded-xl px-4 py-3 text-foreground placeholder:text-muted-foreground focus:outline-none focus:border-accent/50 transition-colors" placeholder="John Doe">
                            </div>
                            <div class="space-y-2">
                                <label for="email" class="text-sm font-medium text-foreground">Email <span class="text-accent">*</span></label>
                                <input type="email" id="email" name="email" required class="w-full bg-background border border-border rounded-xl px-4 py-3 text-foreground placeholder:text-muted-foreground focus:outline-none focus:border-accent/50 transition-colors" placeholder="john@company.com">
                            </div>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div class="space-y-2">
                                <label for="organization" class="text-sm font-medium text-foreground">Organization</label>
                                <input type="text" id="organization" name="organization" class="w-full bg-background border border-border rounded-xl px-4 py-3 text-foreground placeholder:text-muted-foreground focus:outline-none focus:border-accent/50 transition-colors" placeholder="Acme Corp">
                            </div>
                            <div class="space-y-2">
                                <label for="service" class="text-sm font-medium text-foreground">Interested Service</label>
                                <select id="service" name="service" class="w-full bg-background border border-border rounded-xl px-4 py-3 text-foreground focus:outline-none focus:border-accent/50 transition-colors appearance-none">
                                    <option value="" disabled selected>Select a Service</option>
                                    <option value="Capacity & AI Infrastructure Optimizer">Capacity & AI Infrastructure Optimizer</option>
                                    <option value="Enterprise CapEx Optimizer">Enterprise CapEx Optimizer</option>
                                    <option value="PQC Readiness Audit">PQC Readiness Audit</option>
                                    <option value="Other">Other</option>
                                </select>
                            </div>
                        </div>

                        <div class="space-y-2">
                            <label for="description" class="text-sm font-medium text-foreground">Description</label>
                            <textarea id="description" name="description" rows="4" class="w-full bg-background border border-border rounded-xl px-4 py-3 text-foreground placeholder:text-muted-foreground focus:outline-none focus:border-accent/50 transition-colors resize-none" placeholder="How can we help you?"></textarea>
                        </div>

                        <div id="form-status" class="hidden text-sm font-medium p-4 rounded-xl text-center"></div>

                        <button type="submit" id="submit-btn" class="w-full bg-foreground text-background font-semibold py-4 rounded-xl hover:bg-foreground/90 transition-colors flex justify-center items-center gap-2">
                            Send Message
                            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                        </button>
                    </form>
                </div>
            </section>
            
            <script>
                document.getElementById('contact-page-form').addEventListener('submit', async (e) => {
                    e.preventDefault();
                    const btn = document.getElementById('submit-btn');
                    const statusEl = document.getElementById('form-status');
                    btn.disabled = true;
                    btn.innerHTML = 'Sending...';
                    
                    const formData = {
                        name: document.getElementById('name').value,
                        email: document.getElementById('email').value,
                        organization: document.getElementById('organization').value,
                        service: document.getElementById('service').value,
                        description: document.getElementById('description').value
                    };

                    try {
                        const response = await fetch('/api/contact', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify(formData)
                        });
                        
                        const result = await response.json();
                        
                        statusEl.classList.remove('hidden', 'bg-red-500/10', 'text-red-500');
                        statusEl.classList.add('bg-green-500/10', 'text-green-500');
                        statusEl.innerText = 'Thank you! Your message has been sent successfully.';
                        document.getElementById('contact-page-form').reset();
                    } catch (error) {
                        statusEl.classList.remove('hidden', 'bg-green-500/10', 'text-green-500');
                        statusEl.classList.add('bg-red-500/10', 'text-red-500');
                        statusEl.innerText = 'Sorry, there was an error sending your message. Please try again.';
                    } finally {
                        btn.disabled = false;
                        btn.innerHTML = 'Send Message <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>';
                    }
                });
            </script>
`;

  contactHtml = contactHtml.replace(mainStartRegex, '$1\n' + contactFormHTML + '\n$2');

  // We also need to update the top Nav contact link
  contactHtml = contactHtml.replace(/<a href="#contact" class="flex items-center rounded-full bg-white p-1 pr-1 pl-4 h-10 gap-2 transition-transform hover:scale-105 group">/g, '<a href="contact.html" class="flex items-center rounded-full bg-white p-1 pr-1 pl-4 h-10 gap-2 transition-transform hover:scale-105 group">');

  fs.writeFileSync('contact.html', contactHtml);
  console.log('Modified contact.html');

  let indexHtml = fs.readFileSync('index.html', 'utf8');

  // Update Top Contact Link
  indexHtml = indexHtml.replace(/<a href="#contact" class="flex items-center rounded-full bg-white p-1 pr-1 pl-4 h-10 gap-2 transition-transform hover:scale-105 group">/g, '<a href="contact.html" class="flex items-center rounded-full bg-white p-1 pr-1 pl-4 h-10 gap-2 transition-transform hover:scale-105 group">');
  // Update Hero Contact Button
  indexHtml = indexHtml.replace(/<a href="#contact" class="group relative cursor-pointer inline-flex items-center/g, '<a href="contact.html" class="group relative cursor-pointer inline-flex items-center');

  // Update Marquee in Hero section
  const marqueeRegex = /<ul class="flex items-center" aria-hidden="false">[\s\S]*?<\/ul>[\s\S]*?<ul class="flex items-center" aria-hidden="true">[\s\S]*?<\/ul>/;

  const newMarqueeInner = `
<ul class="flex items-center" aria-hidden="false">
    <li class="flex-none mr-[var(--logo-gap)] text-[length:var(--logo-height)] leading-none">
        <span class="inline-flex items-center gap-4">
            <img alt="Hadron" loading="lazy" class="h-[2em] w-auto" src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png"/>
            <span class="text-2xl font-medium tracking-wide text-white/90" style="margin-left: 10px;">Quantum Labs — Pioneering the Future of Enterprise AI & Security</span>
        </span>
    </li>
    <li class="flex-none mr-[var(--logo-gap)] text-[length:var(--logo-height)] leading-none">
        <span class="inline-flex items-center gap-4">
            <img alt="Hadron" loading="lazy" class="h-[2em] w-auto" src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png"/>
            <span class="text-2xl font-medium tracking-wide text-white/90" style="margin-left: 10px;">Quantum Labs — Pioneering the Future of Enterprise AI & Security</span>
        </span>
    </li>
</ul>
<ul class="flex items-center" aria-hidden="true">
    <li class="flex-none mr-[var(--logo-gap)] text-[length:var(--logo-height)] leading-none">
        <span class="inline-flex items-center gap-4">
            <img alt="Hadron" loading="lazy" class="h-[2em] w-auto" src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png"/>
            <span class="text-2xl font-medium tracking-wide text-white/90" style="margin-left: 10px;">Quantum Labs — Pioneering the Future of Enterprise AI & Security</span>
        </span>
    </li>
    <li class="flex-none mr-[var(--logo-gap)] text-[length:var(--logo-height)] leading-none">
        <span class="inline-flex items-center gap-4">
            <img alt="Hadron" loading="lazy" class="h-[2em] w-auto" src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png"/>
            <span class="text-2xl font-medium tracking-wide text-white/90" style="margin-left: 10px;">Quantum Labs — Pioneering the Future of Enterprise AI & Security</span>
        </span>
    </li>
</ul>`;

  indexHtml = indexHtml.replace(marqueeRegex, newMarqueeInner);

  fs.writeFileSync('index.html', indexHtml);
  console.log('Modified index.html');

} catch (e) {
  console.error(e);
}
