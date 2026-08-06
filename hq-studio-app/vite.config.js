import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    tailwindcss()
  ],
  base: '/studio/', // Ensure Vercel serves assets from /studio/
  build: {
    outDir: '../studio', // Build directly into the parent repository's /studio folder
    emptyOutDir: true,
  }
})
