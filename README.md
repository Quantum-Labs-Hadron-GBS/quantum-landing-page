# Hadron Quantum Labs — Architecture & Operations Documentation

This document serves as the comprehensive technical reference for the **Hadron Quantum Labs** landing page (`quantum.hadrongbs.com`). It details the architecture, external integrations, deployment pipeline, and operational workflows required to maintain and scale the platform.

---

## 1. System Architecture Overview

The Hadron Quantum Landing Page is designed as a **statically generated frontend** powered by **serverless edge functions** for backend operations. This hybrid architecture ensures maximum global performance, flawless SEO indexability, and secure API handling without the overhead of a dedicated backend server.

### Technical Stack
- **Frontend Core:** Vanilla HTML5, CSS3, JavaScript (ES6+).
- **Styling:** Tailwind CSS (via CDN) with custom CSS variables for themes and glassmorphic UI elements.
- **Backend API:** Node.js (Vercel Serverless Functions).
- **Email Delivery:** Resend API.
- **Asset Delivery:** Cloudinary (Global CDN for images/media).
- **Hosting & CI/CD:** Vercel.
- **DNS & Edge Security:** Cloudflare.
- **Analytics:** Vercel Web Analytics & Speed Insights.

---

## 2. Infrastructure & Integrations

### A. Vercel (Hosting & Serverless Compute)
Vercel acts as the primary hosting provider and CI/CD pipeline.
- **Static Hosting:** All `.html`, `.css`, and frontend `.js` files are cached and served globally via Vercel's Edge Network.
- **Serverless API (`/api/contact.js`):** Vercel automatically maps the `api/` directory to Node.js serverless functions. The contact form submits a `POST` request to this endpoint.
- **Environment Variables:** Secure keys (like `RESEND_API_KEY`) are stored in the Vercel Dashboard and injected into the serverless function securely at runtime.
- **Security Headers:** The `vercel.json` file dictates strict Content-Security-Policy (CSP) headers, allowing external resources like Google Maps iframes and Cloudinary assets while blocking malicious injections.

### B. Resend (Transactional Email)
The "Contact Us" and "Request Audit" forms rely on the **Resend API** to process and deliver emails.
- **Workflow:** When a user submits the form, the frontend sends a JSON payload to `/api/contact.js`. The serverless function constructs an HTML email template and sends it via Resend to `info@quantum.lab`.
- **Authentication:** Authenticated via the `RESEND_API_KEY` environment variable.

### C. Cloudinary (Asset Management)
To ensure the site loads instantly, all heavy media assets (hero backgrounds, logos, OG preview images) are hosted on Cloudinary.
- Cloudinary automatically serves the most optimized format (e.g., WebP/AVIF) based on the user's browser, significantly reducing bandwidth and improving Core Web Vitals.

### D. Cloudflare (DNS & Edge Security)
Cloudflare sits in front of Vercel to manage the custom subdomain (`quantum.hadrongbs.com`).
- **DNS Management:** Cloudflare routes traffic to Vercel's servers using CNAME/A records.
- **SSL/TLS:** End-to-end encryption is managed between Cloudflare and Vercel.
- **DDoS Protection:** Cloudflare proxying (the "orange cloud") provides an initial layer of bot mitigation and DDoS protection before traffic hits Vercel.

---

## 3. SEO & Discoverability

The platform is heavily optimized for search engine crawlers and social sharing:
- **Semantic HTML & Meta Tags:** Standard title, description, and canonical tags are implemented across all pages.
- **Open Graph & Twitter Cards:** Fully configured to display premium preview images (hosted on Cloudinary) when links are shared on LinkedIn, X, Slack, or WhatsApp.
- **JSON-LD Structured Data:**
  - `Organization` schema is injected on `index.html` to help Google understand the entity relationship with Hadron GBS.
  - `ContactPage` schema is injected on `contact.html`.
- **Crawlability:** `sitemap.xml` and `robots.txt` are explicitly defined in the root directory. `robots.txt` is configured to allow crawling of pages while disallowing indexing of the `/api/` endpoints.

---

## 4. Local Development Workflow

To run and test the project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Quantum-Labs-Hadron-GBS/quantum-landing-page.git
   cd quantum-landing-page
   ```

2. **Frontend Testing:**
   Since the frontend is vanilla HTML/JS, you can use any local server (like VS Code Live Server or Python `http.server`) to view the site:
   ```bash
   npx serve .
   ```

3. **Testing the Serverless API (Contact Form):**
   To test the contact form locally, you must use Vercel's CLI, which simulates the serverless environment and injects environment variables.
   
   - Install Vercel CLI: `npm i -g vercel`
   - Link the project: `vercel link`
   - Pull environment variables: `vercel env pull .env.local`
   - Start the local dev server: `vercel dev`
   - The site will be available at `localhost:3000`, and form submissions will successfully hit `/api/contact` and trigger Resend (provided you pulled the valid API key).

---

## 5. Deployment Pipeline

The CI/CD pipeline is fully automated via GitHub and Vercel.

- **Staging/Preview:** Any branch pushed to GitHub (e.g., `test/orange-cards`) automatically triggers a Preview Build in Vercel. A unique preview URL is generated for testing without affecting production.
- **Production:** Merging a branch into `main` automatically triggers a Production Build. Once built, Vercel instantly invalidates the edge cache and deploys the updates to `quantum.hadrongbs.com`.

---

## 6. Maintenance & Troubleshooting

- **Form Failing (500 Error):** Check the Vercel Function Logs in the Vercel Dashboard. Ensure the `RESEND_API_KEY` is valid and the recipient email address (`info@quantum.lab`) is verified in the Resend dashboard.
- **Assets Not Loading:** Ensure the Cloudinary URLs are correct. If updating the background, replace the `https://res.cloudinary.com/...` link directly in the HTML.
- **Google Maps Not Rendering:** If the map iframe is blank, verify that `frame-src` in `vercel.json`'s Content-Security-Policy includes `https://maps.google.com/`. 

---
*Maintained by the Hadron Quantum Engineering Team.*
