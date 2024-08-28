import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueJsx(),
    vueDevTools(),
  ],
  // server:{
  //   proxy:{
  //     '/media':{
  //       target: 'http://127.0.0.1:8000',  // URL of your Django backend
  //       // target:"C:\laragon\www\vue-django\backend",
  //       changeOrigin: true,
  //       rewrite: (path) => path.replace(/^\/media/, '/media'),
  //     }
  //   }
  // },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
