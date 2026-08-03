const fs = require('fs');
let h = fs.readFileSync('index.html', 'utf8');

// Inject home button between the logo </a> and <nav> in the header
// The exact sequence: logo img /> \r </a> \r <nav
const TARGET = 'class="h-[1.8rem] w-auto" />\r                </a>\r                <nav';
const REPLACEMENT = 'class="h-[1.8rem] w-auto" />\r                </a>\r                <a href="index.html" aria-label="Home" title="Hadron Quantum Labs — Home" class="flex items-center justify-center w-8 h-8 rounded-full bg-white/[0.06] hover:bg-white/[0.12] border border-white/[0.08] transition-colors">\r                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>\r                </a>\r                <nav';

if (h.includes(TARGET)) {
    h = h.replace(TARGET, REPLACEMENT);
    console.log('Home button injected ✅');
} else {
    console.error('Target not found ❌ — checking alternatives...');
    // Try with \n instead of \r
    const T2 = 'class="h-[1.8rem] w-auto" />\n                </a>\n                <nav';
    if (h.includes(T2)) {
        const R2 = 'class="h-[1.8rem] w-auto" />\n                </a>\n                <a href="index.html" aria-label="Home" title="Hadron Quantum Labs — Home" class="flex items-center justify-center w-8 h-8 rounded-full bg-white/[0.06] hover:bg-white/[0.12] border border-white/[0.08] transition-colors">\n                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>\n                </a>\n                <nav';
        h = h.replace(T2, R2);
        console.log('Home button injected (LF variant) ✅');
    }
}

fs.writeFileSync('index.html', h);
console.log('Saved ✅');
