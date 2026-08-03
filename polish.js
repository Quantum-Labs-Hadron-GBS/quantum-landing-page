const fs = require('fs');

// ---- index.html ----
let html = fs.readFileSync('index.html', 'utf8');

// 1. SEO - Update title
html = html.replace(
  '<title>Hadron Quantum — Quantum-Inspired Infrastructure Optimization</title>',
  '<title>Hadron Quantum Labs | AI Infrastructure Optimization & PQC Security | Hadron GBS</title>'
);

// 2. SEO - Update meta description
html = html.replace(
  '<meta name="description" content="Operating above existing schedulers to maximize fleet-wide GPU utilization, minimize rack/cooling fragmentation, and prepare your enterprise for Post-Quantum Cryptography."/>',
  '<meta name="description" content="Hadron Quantum Labs is the quantum division of Hadron Global Business Solutions (GBS), delivering AI infrastructure optimization, fleet-wide GPU capacity planning, and Post-Quantum Cryptography (PQC) readiness audits for enterprise data centers."/>'
);

// 3. SEO - Update keywords
html = html.replace(
  '<meta name="keywords" content="Quantum-Inspired Optimization, AI Infrastructure, GPU Capacity Planning, PQC Readiness Audit, QUBO, Rack Placement"/>',
  '<meta name="keywords" content="Hadron Quantum Labs, Hadron GBS, Hadron Global Business Solutions, Quantum Division, AI Infrastructure Optimization, GPU Capacity Planning, PQC Readiness Audit, Post-Quantum Cryptography, QUBO Optimization, Rack Placement, Enterprise AI, Data Center Optimization, CERT-In, NIST, RBI Q-Safe"/>'
);

// 4. SEO - Update author/publisher
html = html.replace(
  '<meta name="author" content="Hadron Quantum"/>',
  '<meta name="author" content="Hadron GBS - Quantum Labs Division"/>'
);
html = html.replace(
  '<meta name="publisher" content="Hadron Quantum"/>',
  '<meta name="publisher" content="Hadron Global Business Solutions (GBS)"/>'
);

// 5. SEO - Update OG tags
html = html.replace(
  '<meta property="og:title" content="Hadron Quantum — Quantum-Inspired Infrastructure Optimization"/>',
  '<meta property="og:title" content="Hadron Quantum Labs | Quantum Division of Hadron GBS"/>'
);
html = html.replace(
  '<meta property="og:description" content="Maximize fleet-wide utilization and prepare enterprise infrastructure for Post-Quantum Cryptography."/>',
  '<meta property="og:description" content="Hadron Quantum Labs — AI infrastructure optimization and PQC security audits for enterprises. A division of Hadron Global Business Solutions."/>'
);
html = html.replace(
  '<meta name="twitter:title" content="Hadron Quantum — Infrastructure Optimization"/>',
  '<meta name="twitter:title" content="Hadron Quantum Labs | Quantum Division of Hadron GBS"/>'
);
html = html.replace(
  '<meta name="twitter:description" content="Quantum-Inspired AI Infrastructure Planning &amp; Fabric Optimization."/>',
  '<meta name="twitter:description" content="AI infrastructure optimization & PQC readiness audits. Quantum division of Hadron GBS."/>'
);

// 6. SEO - Fix broken favicon refs + add inline SVG favicon + add JSON-LD structured data + canonical
html = html.replace(
  '<link rel="shortcut icon" href="/favicon-16x16.png"/>',
  `<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⚛</text></svg>"/>
        <link rel="canonical" href="https://quantum.hadrongbs.com/"/>
        <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@type": "Organization",
          "name": "Hadron Quantum Labs",
          "alternateName": "Hadron GBS Quantum Division",
          "description": "Quantum-inspired AI infrastructure optimization and Post-Quantum Cryptography readiness audits for enterprise data centers.",
          "url": "https://quantum.hadrongbs.com",
          "parentOrganization": {
            "@type": "Organization",
            "name": "Hadron Global Business Solutions",
            "alternateName": "Hadron GBS",
            "url": "https://hadrongbs.com"
          },
          "knowsAbout": [
            "Quantum-Inspired Optimization",
            "AI Infrastructure Planning",
            "Post-Quantum Cryptography",
            "GPU Capacity Planning",
            "Data Center Optimization"
          ]
        }
        <\/script>`
);

// 7. Remove broken favicon links
html = html.replace('<link rel="icon" href="/favicon.ico?favicon.0b3bf435.ico" sizes="256x256" type="image/x-icon"/>', '');
html = html.replace('<link rel="icon" href="/favicon.ico"/>', '');
html = html.replace('<link rel="apple-touch-icon" href="/apple-icon.png"/>', '');

// 8. Hero CTA & text - Fix stuck animation (remove filter:blur from CTA)
// Fix the CTA button stuck blur - change the inline style
html = html.replace(
  '<a href="contact.html" class="group relative cursor-pointer inline-flex items-center max-[850px]:w-full" tabindex="0" style="opacity:0;filter:blur(8px);transform:scale(0.95)">',
  '<a href="contact.html" class="group relative cursor-pointer inline-flex items-center max-[850px]:w-full" tabindex="0" style="opacity:0;transform:scale(0.95)">'
);

// 9. Hero heading - change italic serif "Optimization" to a gradient accent span, no more serif font
html = html.replace(
  'Infrastructure <span class="italic font-serif text-accent">Optimization</span>',
  'Infrastructure <span class="text-accent">Optimization</span>'
);

// 10. Hero "Now Available" badge - small tweak to text
html = html.replace(
  'Now Available<span class="text-accent">✦</span>',
  'Now Available &nbsp;<span class="text-accent">✦</span>'
);

// 11. Hero Dashboard image - enhance fade with better multi-stop gradient
html = html.replace(
  'class="relative mix-blend-darken rounded-2xl overflow-hidden border border-neutral-200/50 shadow-2xl/5 mask-[linear-gradient(to_bottom,black_50%,transparent_100%)] [-webkit-mask-image:linear-gradient(to_bottom,black_50%,transparent_100%)]"',
  'class="relative mix-blend-darken rounded-2xl overflow-hidden border border-neutral-200/30 shadow-2xl/5 mask-[linear-gradient(to_bottom,black_30%,black_60%,transparent_100%)] [-webkit-mask-image:linear-gradient(to_bottom,black_30%,black_60%,transparent_100%)]"'
);

// Also add a subtle top glow/overlay to make the dashboard look premium
html = html.replace(
  'class="w-full h-auto contrast-125 opacity-90" style="color:transparent"  src="https://res.cloudinary.com/djxbxhgat/image/upload/v1785144026/149de2ff-a4e9-48e5-a223-c7572a43ef38.png"',
  'class="w-full h-auto contrast-110 opacity-95 brightness-110" style="color:transparent" src="https://res.cloudinary.com/djxbxhgat/image/upload/v1785144026/149de2ff-a4e9-48e5-a223-c7572a43ef38.png"'
);

// 12. LogoLoop - Fix: increase items to 4 for seamless scroll, add separator dots, fix gap
const oldLogoLoop = `<ul class="flex items-center" aria-hidden="false">
    <li class="flex-none mr-[var(--logo-gap)] text-[length:var(--logo-height)] leading-none">
        <span class="inline-flex items-center gap-4">
            <img alt="Hadron" loading="lazy" class="h-[1.25em] w-auto" src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png"/>
            <span class="text-lg font-medium tracking-wide text-white/90" style="margin-left: 10px;">Quantum Labs — Pioneering the Future of Enterprise AI & Security</span>
        </span>
    </li>
    <li class="flex-none mr-[var(--logo-gap)] text-[length:var(--logo-height)] leading-none">
        <span class="inline-flex items-center gap-4">
            <img alt="Hadron" loading="lazy" class="h-[1.25em] w-auto" src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png"/>
            <span class="text-lg font-medium tracking-wide text-white/90" style="margin-left: 10px;">Quantum Labs — Pioneering the Future of Enterprise AI & Security</span>
        </span>
    </li>
</ul>
<ul class="flex items-center" aria-hidden="true">
    <li class="flex-none mr-[var(--logo-gap)] text-[length:var(--logo-height)] leading-none">
        <span class="inline-flex items-center gap-4">
            <img alt="Hadron" loading="lazy" class="h-[1.25em] w-auto" src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png"/>
            <span class="text-lg font-medium tracking-wide text-white/90" style="margin-left: 10px;">Quantum Labs — Pioneering the Future of Enterprise AI & Security</span>
        </span>
    </li>
    <li class="flex-none mr-[var(--logo-gap)] text-[length:var(--logo-height)] leading-none">
        <span class="inline-flex items-center gap-4">
            <img alt="Hadron" loading="lazy" class="h-[1.25em] w-auto" src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png"/>
            <span class="text-lg font-medium tracking-wide text-white/90" style="margin-left: 10px;">Quantum Labs — Pioneering the Future of Enterprise AI & Security</span>
        </span>
    </li>
</ul>`;

const logoItem = (ariaHidden) => `<ul class="flex items-center gap-16" aria-hidden="${ariaHidden}">
    <li class="flex-none flex items-center gap-5">
        <img alt="Hadron Quantum Labs" loading="lazy" class="h-5 w-auto opacity-80" src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png"/>
        <span class="text-sm font-medium tracking-widest text-white/60 uppercase">Quantum Labs</span>
        <span class="text-white/20 text-xl">·</span>
        <span class="text-sm font-light tracking-wide text-white/50">Pioneering the Future of Enterprise AI &amp; Security</span>
        <span class="text-white/20 text-xl mx-8">✦</span>
    </li>
    <li class="flex-none flex items-center gap-5">
        <img alt="Hadron Quantum Labs" loading="lazy" class="h-5 w-auto opacity-80" src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png"/>
        <span class="text-sm font-medium tracking-widest text-white/60 uppercase">Quantum Labs</span>
        <span class="text-white/20 text-xl">·</span>
        <span class="text-sm font-light tracking-wide text-white/50">Pioneering the Future of Enterprise AI &amp; Security</span>
        <span class="text-white/20 text-xl mx-8">✦</span>
    </li>
    <li class="flex-none flex items-center gap-5">
        <img alt="Hadron Quantum Labs" loading="lazy" class="h-5 w-auto opacity-80" src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png"/>
        <span class="text-sm font-medium tracking-widest text-white/60 uppercase">Quantum Labs</span>
        <span class="text-white/20 text-xl">·</span>
        <span class="text-sm font-light tracking-wide text-white/50">Pioneering the Future of Enterprise AI &amp; Security</span>
        <span class="text-white/20 text-xl mx-8">✦</span>
    </li>
</ul>`;

const newLogoLoop = logoItem("false") + "\n" + logoItem("true");
html = html.replace(oldLogoLoop, newLogoLoop);

// Also update the CSS variables for the logo loop container
html = html.replace(
  'style="--logo-gap:124px;--logo-height:42px"',
  'style="--logo-gap:0px;--logo-height:20px"'
);

// And update the wrapper to use proper flex gap
html = html.replace(
  'class="flex will-change-transform select-none w-max"',
  'class="flex will-change-transform select-none w-max gap-0 animate-marquee"'
);

// Remove the old animate-marquee from inner div if any duplicate
html = html.replace(/class="flex will-change-transform select-none w-max gap-0 animate-marquee animate-marquee"/, 'class="flex will-change-transform select-none w-max gap-0 animate-marquee"');

// 13. Fix FAQ broken apostrophe entity
html = html.replace(
  "Can &#x27;t find the answer you &#x27;re looking for? Reach out!",
  "Can't find the answer you're looking for? Reach out to our team!"
);

// 14. Fix FAQ CTA buttons - link properly
html = html.replace(
  '<a href="#" class="inline-flex items-center rounded-xl bg-foreground px-6 py-2.5 text-sm font-semibold text-background transition-colors hover:bg-foreground/90" tabindex="0">Get Started</a>',
  '<a href="contact.html" class="inline-flex items-center rounded-xl bg-foreground px-6 py-2.5 text-sm font-semibold text-background transition-colors hover:bg-foreground/90" tabindex="0">Get in Touch</a>'
);
html = html.replace(
  '<a href="#" class="inline-flex items-center rounded-xl border border-border bg-frame px-6 py-2.5 text-sm font-semibold text-foreground transition-colors" tabindex="0">Contact Support</a>',
  '<a href="contact.html" class="inline-flex items-center rounded-xl border border-border bg-frame px-6 py-2.5 text-sm font-semibold text-foreground transition-colors" tabindex="0">Contact Support</a>'
);

// 15. Fix Workflow "Request Audit" link
html = html.replace(
  '<a href="#" class="mt-8 inline-flex items-center rounded-xl bg-foreground px-6 py-3 text-sm font-semibold text-background transition-colors hover:bg-foreground/90" tabindex="0">Request Audit</a>',
  '<a href="contact.html" class="mt-8 inline-flex items-center rounded-xl bg-foreground px-6 py-3 text-sm font-semibold text-background transition-colors hover:bg-foreground/90" tabindex="0">Request Audit</a>'
);

// 16. Fix Offerings card buttons - point to contact
html = html.replace(
  /<button class="mt-6 w-full rounded-xl py-3 text-sm font-semibold transition-colors bg-muted text-foreground hover:bg-muted\/80" tabindex="0">Model Portfolio<\/button>/g,
  '<a href="contact.html" class="mt-6 w-full rounded-xl py-3 text-sm font-semibold transition-colors bg-muted text-foreground hover:bg-muted/80 block text-center" tabindex="0">Get Started</a>'
);
html = html.replace(
  '<button class="mt-6 w-full rounded-xl py-3 text-sm font-semibold transition-colors bg-foreground text-background hover:bg-foreground/90" tabindex="0">Explore Optimizer</button>',
  '<a href="contact.html" class="mt-6 w-full rounded-xl py-3 text-sm font-semibold transition-colors bg-foreground text-background hover:bg-foreground/90 block text-center" tabindex="0">Explore Optimizer</a>'
);
html = html.replace(
  '<button class="mt-6 w-full rounded-xl py-3 text-sm font-semibold transition-colors bg-muted text-foreground hover:bg-muted/80" tabindex="0">Request Audit</button>',
  '<a href="contact.html" class="mt-6 w-full rounded-xl py-3 text-sm font-semibold transition-colors bg-muted text-foreground hover:bg-muted/80 block text-center" tabindex="0">Request Audit</a>'
);

// 17. Footer - Update copyright text and logo link
html = html.replace(
  '© 2026 Hadron Quantum Inc. All rights reserved.',
  '© 2026 Hadron Quantum Labs — A Division of Hadron Global Business Solutions (GBS). All rights reserved.'
);
html = html.replace(
  '<a href="#" class="flex items-center gap-3" aria-label="Hadron Quantum home">',
  '<a href="/" class="flex items-center gap-3" aria-label="Hadron Quantum home">'
);

// 18. Footer "Start building..." CTA - update button text
html = html.replace(
  'Join Waitlist',
  'Request Demo'
);

// 19. Footer "Start building" heading - differentiate from template
html = html.replace(
  'Start building something truly amazing today',
  'Ready to Optimize Your Enterprise Infrastructure?'
);

// 20. Add a "Back to top" remove the theme toggle button (floating disabled button looks bad)
html = html.replace(
  '<div class="fixed bottom-6 right-6 z-50">\n            <button class="w-12 h-12 rounded-full bg-foreground/10 opacity-30 cursor-not-allowed" aria-label="Toggle theme" disabled=""></button>\n        </div>',
  ''
);

fs.writeFileSync('index.html', html);
console.log('index.html updated successfully!');

// ---- contact.html ----
let contactHtml = fs.readFileSync('contact.html', 'utf8');

// 1. Fix title
contactHtml = contactHtml.replace(
  '<title>Hadron Quantum — Quantum-Inspired Infrastructure Optimization</title>',
  '<title>Contact Us | Hadron Quantum Labs — Quantum Division of Hadron GBS</title>'
);

// 2. Fix meta description
contactHtml = contactHtml.replace(
  /content="Operating above existing schedulers to maximize fleet-wide GPU utilization, minimize rack\/cooling fragmentation, and prepare your enterprise for Post-Quantum Cryptography\."/,
  'content="Contact Hadron Quantum Labs — the quantum division of Hadron GBS. Reach us for AI infrastructure optimization, CapEx planning, and PQC readiness audits."'
);

// 3. Fix favicon
contactHtml = contactHtml.replace(
  '<link rel="shortcut icon" href="/favicon-16x16.png"/>',
  `<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⚛</text></svg>"/>
        <link rel="canonical" href="https://quantum.hadrongbs.com/contact.html"/>`
);
contactHtml = contactHtml.replace('<link rel="icon" href="/favicon.ico?favicon.0b3bf435.ico" sizes="256x256" type="image/x-icon"/>', '');
contactHtml = contactHtml.replace('<link rel="icon" href="/favicon.ico"/>', '');
contactHtml = contactHtml.replace('<link rel="apple-touch-icon" href="/apple-icon.png"/>', '');

// 4. Fix nav links in contact.html to go back to index.html
contactHtml = contactHtml.replace(
  '<a href="#solutions"',
  '<a href="index.html#solutions"'
);
contactHtml = contactHtml.replace(
  '<a href="#workflow"',
  '<a href="index.html#workflow"'
);
contactHtml = contactHtml.replace(
  '<a href="#pricing"',
  '<a href="index.html#pricing"'
);
contactHtml = contactHtml.replace(
  '<a href="#faq-accordion"',
  '<a href="index.html#faq-accordion"'
);

// 5. Fix logo link in contact.html header to go back to home
contactHtml = contactHtml.replace(
  '<a href="#" class="flex items-center gap-2 ml-4 max-[850px]:ml-0">',
  '<a href="index.html" class="flex items-center gap-2 ml-4 max-[850px]:ml-0">'
);

// 6. Remove the redundant homepage sections from contact.html (keep only form + footer)
// Remove the massive hero+all sections except form and footer
const mainStart = contactHtml.indexOf('<main id="main-content"');
const footerStart = contactHtml.indexOf('<footer id="contact"');
const formSectionStart = contactHtml.indexOf('<!-- Global Grid -->');
const formSectionEnd = contactHtml.indexOf('</section>', contactHtml.indexOf('<script>')) + '</section>'.length;

// We know the contact form section is correct, and the footer should follow directly
// Find the redundant duplicate homepage sections between the form and footer
// These are the scroll reveal text, solutions, workflow, pricing, FAQ sections
// Replace everything between form end and footer start with nothing

// The form ends with </section> after the script
// Find exact boundaries
const scriptEndInContact = contactHtml.indexOf('</script>\n            </section>') + ('</script>\n            </section>').length;
const footerInContact = contactHtml.indexOf('<footer id="contact"');

if (scriptEndInContact > 0 && footerInContact > scriptEndInContact) {
  const gapContent = contactHtml.substring(scriptEndInContact, footerInContact);
  // Replace massive gap with just a small spacer
  contactHtml = contactHtml.substring(0, scriptEndInContact) + '\n\n' + contactHtml.substring(footerInContact);
  console.log('Removed redundant sections from contact.html');
}

// 7. Fix footer copyright
contactHtml = contactHtml.replace(
  '© 2026 Hadron Quantum Inc. All rights reserved.',
  '© 2026 Hadron Quantum Labs — A Division of Hadron Global Business Solutions (GBS). All rights reserved.'
);

// 8. Fix footer "Start building" heading on contact page
contactHtml = contactHtml.replace(
  'Start building something truly amazing today',
  'Ready to Optimize Your Enterprise Infrastructure?'
);
contactHtml = contactHtml.replace(
  'Join Waitlist',
  'Request Demo'
);

// 9. Remove disabled theme toggle button
contactHtml = contactHtml.replace(
  '<div class="fixed bottom-6 right-6 z-50">\n            <button class="w-12 h-12 rounded-full bg-foreground/10 opacity-30 cursor-not-allowed" aria-label="Toggle theme" disabled=""></button>\n        </div>',
  ''
);

// 10. Fix footer logo link on contact.html
contactHtml = contactHtml.replace(
  '<a href="#" class="flex items-center gap-3" aria-label="Hadron Quantum home">',
  '<a href="index.html" class="flex items-center gap-3" aria-label="Hadron Quantum home">'
);

fs.writeFileSync('contact.html', contactHtml);
console.log('contact.html updated successfully!');

// ---- vercel.json - also allow vercel.live for preview feedback ----
let vercelJson = fs.readFileSync('vercel.json', 'utf8');
vercelJson = vercelJson.replace(
  "script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com",
  "script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com https://vercel.live"
);
fs.writeFileSync('vercel.json', vercelJson);
console.log('vercel.json updated successfully!');

console.log('\\n✅ All polish fixes applied!');
