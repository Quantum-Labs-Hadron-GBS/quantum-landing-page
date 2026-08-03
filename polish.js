const fs = require('fs');

// ---- index.html ----
let html = fs.readFileSync('index.html', 'utf8');

// 1. Boost orange gradients by ~40% (increase opacity values)
// Minor grid: 0.03 → 0.042
html = html.replaceAll('rgba(255,159,43,0.03)', 'rgba(255,159,43,0.05)');
// Major grid: 0.08 → 0.112
html = html.replaceAll('rgba(255,159,43,0.08)', 'rgba(255,159,43,0.12)');
// Hero top bleed: 0.1 → 0.14
html = html.replace('rgba(255,159,43,0.1),transparent', 'rgba(255,159,43,0.15),transparent');
// Section glows: 0.25 → 0.35
html = html.replaceAll('rgba(255,159,43,0.25)', 'rgba(255,159,43,0.35)');
// Section glows: 0.3 → 0.42
html = html.replaceAll('rgba(255,159,43,0.3)', 'rgba(255,159,43,0.42)');
// Value props border: accent/15 stays, but boost slightly
// Logo hover accent/15 stays
// FAQ hover accent/30 → accent/42
html = html.replaceAll('hover:border-accent/30', 'hover:border-accent/45');

// 2. Navbar logo: h-6 → h-[1.44rem] (approx 20% bigger, h-6 = 1.5rem, 1.5*1.2=1.8rem → use h-7 which is 1.75rem)
html = html.replace(
  '<img src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png" alt="Hadron" class="h-6 w-auto" />',
  '<img src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png" alt="Hadron" class="h-[1.8rem] w-auto" />'
);

// 3. Navbar logo link: redirect to www.hadrongbs.com
html = html.replace(
  '<a href="#" class="flex items-center gap-2 ml-4 max-[850px]:ml-0">',
  '<a href="https://www.hadrongbs.com" target="_blank" rel="noopener" class="flex items-center gap-2 ml-4 max-[850px]:ml-0">'
);

fs.writeFileSync('index.html', html);
console.log('index.html updated');

// ---- contact.html ----
let contact = fs.readFileSync('contact.html', 'utf8');

// 1. Replace the background grid section with the boosted version + richer gradients
const oldBg = `        <!-- Background Grid -->
        <div class="absolute inset-0 pointer-events-none -z-20 bg-background overflow-hidden" aria-hidden="true">
            <div class="absolute inset-0 bg-[linear-gradient(to_right,rgba(255,159,43,0.03)_1px,transparent_1px),linear-gradient(to_bottom,rgba(255,159,43,0.03)_1px,transparent_1px)] bg-[size:64px_64px]"></div>
            <div class="absolute inset-0 bg-[linear-gradient(to_right,rgba(255,159,43,0.07)_1px,transparent_1px),linear-gradient(to_bottom,rgba(255,159,43,0.07)_1px,transparent_1px)] bg-[size:256px_256px]"></div>
            <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,transparent_40%,#000000_100%)] opacity-80"></div>
            <div class="absolute top-0 w-full h-[500px] bg-[linear-gradient(to_bottom,rgba(255,159,43,0.08),transparent)]"></div>
        </div>`;

const newBg = `        <!-- Background Grid + Gradients -->
        <div class="absolute inset-0 pointer-events-none -z-20 bg-background overflow-hidden" aria-hidden="true">
            <div class="absolute inset-0 bg-[linear-gradient(to_right,rgba(255,159,43,0.05)_1px,transparent_1px),linear-gradient(to_bottom,rgba(255,159,43,0.05)_1px,transparent_1px)] bg-[size:64px_64px]"></div>
            <div class="absolute inset-0 bg-[linear-gradient(to_right,rgba(255,159,43,0.12)_1px,transparent_1px),linear-gradient(to_bottom,rgba(255,159,43,0.12)_1px,transparent_1px)] bg-[size:256px_256px]"></div>
            <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,transparent_40%,#000000_100%)] opacity-80"></div>
            <!-- Top orange bleed -->
            <div class="absolute top-0 w-full h-[600px] bg-[linear-gradient(to_bottom,rgba(255,159,43,0.15),transparent)]"></div>
            <!-- Top-right radial glow -->
            <div class="absolute top-0 right-0 w-full max-w-[900px] h-[800px] bg-[radial-gradient(ellipse_at_top_right,rgba(255,159,43,0.35)_0%,transparent_65%)] pointer-events-none"></div>
            <!-- Bottom-left radial glow -->
            <div class="absolute bottom-0 left-0 w-full max-w-[700px] h-[600px] bg-[radial-gradient(ellipse_at_bottom_left,rgba(255,159,43,0.30)_0%,transparent_65%)] pointer-events-none"></div>
        </div>`;

contact = contact.replace(oldBg, newBg);

// 2. Navbar logo: h-6 → h-[1.8rem]
contact = contact.replace(
  '<img src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png" alt="Hadron" class="h-6 w-auto" />',
  '<img src="https://res.cloudinary.com/djxbxhgat/image/upload/v1784806399/hadron_logo_white_jsl37p.png" alt="Hadron" class="h-[1.8rem] w-auto" />'
);

// 3. Navbar logo link → www.hadrongbs.com
contact = contact.replace(
  '<a href="index.html" class="flex items-center gap-2 ml-4 max-[850px]:ml-0" aria-label="Hadron Quantum home">',
  '<a href="https://www.hadrongbs.com" target="_blank" rel="noopener" class="flex items-center gap-2 ml-4 max-[850px]:ml-0" aria-label="Hadron Quantum home">'
);

fs.writeFileSync('contact.html', contact);
console.log('contact.html updated');
console.log('\n✅ All changes applied!');
