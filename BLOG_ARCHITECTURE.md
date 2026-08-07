# Hadron Quantum Labs – Blog Portal & HQ Studio Architecture

This document provides a comprehensive overview of the architecture, technologies, frameworks, and workflows implemented to build the Hadron Quantum Labs Blog Portal and the underlying HQ Studio Content Management System (CMS).

## 1. System Overview
The platform is designed as a decoupled architecture consisting of two primary interfaces:
1. **The Public Blog Portal**: A blazing-fast, static-first HTML/JS frontend that fetches content dynamically at runtime to ensure maximum SEO compatibility and performance.
2. **HQ Studio**: A secure, React-based Single Page Application (SPA) that serves as the editorial command center for creating, managing, and publishing content.

## 2. Technology Stack & Frameworks

### Frontend (Public Portal)
* **Framework**: Vanilla HTML5, CSS3, and modern ES6 JavaScript. No heavy frameworks (React/Angular) are loaded on the client side, ensuring near-instant page loads.
* **Styling**: Tailwind CSS (via CDN) for rapid, utility-first styling, featuring custom Tailwind configurations (`tailwind.config`) injected at runtime.
* **Typography**: Custom-written `.prose` CSS rules mimicking Tailwind Typography to ensure beautiful, readable formatting for headings, blockquotes, code blocks, and tables.

### Frontend (HQ Studio CMS)
* **Framework**: React.js 18
* **Build Tool**: Vite (Lightning-fast HMR and optimized production bundling).
* **Routing**: `react-router-dom` for handling dashboard and editor routes.
* **Icons**: `lucide-react` for clean, consistent SVG iconography.
* **Rich Text Editor**: **Tiptap** headless editor framework.
  * *Extensions used*: `@tiptap/starter-kit`, `@tiptap/extension-image`, `@tiptap/extension-table`, `tiptap-markdown`.
  * *Capabilities*: Markdown parsing, inline image rendering, complex table manipulation (add/remove rows/cols).

### Backend, Database & Storage
* **Backend-as-a-Service (BaaS)**: **Supabase**
  * Serves as the primary Postgres database and REST API layer.
* **Database Schema**: 
  * Table: `documents`
  * Key Columns: `id`, `slug`, `title`, `type_id` (Category), `status_id` (Draft/Published), `html`, `markdown`, `cover_image`, `published_at`.
  * **JSONB Storage**: The `seo_metadata` column is heavily utilized to store flexible document attributes such as `author`, `excerpt`, and `seo_description` without requiring constant schema migrations.
* **Asset Storage / CDN**: 
  * **Cloudinary** (External App) is the standard for hosting cover images, author avatars, and inline article images, providing optimized delivery.

---

## 3. Core Features & Implementation Details

### The Public Blog Feed (`blogs.html`)
* **Hero Section**: An edge-to-edge, immersive hero image with dark gradients designed to maintain visual parity with the main Hadron homepage.
* **Featured Carousel**: A JavaScript-driven auto-rotating carousel that cycles through the top 3 featured/latest articles every few seconds.
* **Masonry Layout**: A dynamic CSS grid layout for the "All Updates" feed, allowing uneven card heights based on the presence/absence of cover images.
* **Category Filtering**: Interactive "pill" buttons that execute real-time DOM filtering based on the `type_id` (e.g., CASE STUDY, BLOG, RESEARCH).

### The Individual Article View (`article.html`)
* **Dual-Column Layout**: A premium 12-column grid that allocates the main text to the left and a sticky utility sidebar to the right.
* **Dynamic Table of Contents (ToC)**: JavaScript parses the rendered HTML for `<h2>`, `<h3>`, and `<h4>` tags, automatically generating anchor links and building the hierarchical ToC in the sidebar.
* **IntersectionObserver Scrollspy**: As the user scrolls, the observer detects which header is currently in the viewport and animates a vertical progress bar in the ToC to highlight the active section.
* **Read-Time Calculator**: A script dynamically strips HTML tags, counts the raw words, and calculates an estimated reading time (assuming ~220 words per minute).
* **Related Articles Engine**: A secondary Supabase API call fetches the 2 most recently published articles (excluding the current one) and renders them as mini-cards to maximize reader retention.

### HQ Studio Editor (`hq-studio-app`)
* **Live Markdown Synchronization**: The Tiptap editor seamlessly converts between WYSIWYG visual editing and raw Markdown. Both HTML and Markdown formats are saved to the database.
* **Document Settings Sidebar**: A comprehensive slide-out menu allowing admins to inject Cover Images, Excerpts, SEO Meta Descriptions, Category tags, and Author Names directly into the `seo_metadata` JSONB.
* **Production Build Pipeline**: Changes made in the React app (`src/`) are compiled via `npm run build` directly into the root `/studio` folder, allowing the static web server to serve the React app effortlessly.

---

## 4. Development Workflow & Routing
1. Admins navigate to `/studio` to launch the React application.
2. The Dashboard (`Dashboard.jsx`) queries Supabase for all documents and renders them in a management table.
3. Clicking an article opens `/studio/editor/:id` (`Editor.jsx`), loading the `markdown` payload into Tiptap.
4. Upon clicking **Publish**, the `status_id` is updated to `3`, instantly pushing it to the live `/blogs.html` feed.
5. Readers click an article card on `/blogs.html`, which routes them to `/article.html?slug=article-slug`, where Vanilla JS fetches and paints the article layout on the fly.
