import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"
import { VitePWA } from "vite-plugin-pwa"

export default defineConfig({

  plugins: [

    vue(),

    VitePWA({

        devOptions: {
          enabled: true,
        },

      registerType: "autoUpdate",

      includeAssets: [

        "favicon.ico",

        "apple-touch-icon.png",

        "icon-192.png",

        "icon-512.png"

      ],

      manifest: {

        name: "Placement Portal",

        short_name: "Placement",

        description: "Placement Management Portal",

        theme_color: "#0d6efd",

        background_color: "#ffffff",

        display: "standalone",

        start_url: "/",

        icons: [

          {

            src: "icon-192.png",

            sizes: "192x192",

            type: "image/png"

          },

          {

            src: "icon-512.png",

            sizes: "512x512",

            type: "image/png"

          }

        ]

      }

    })

  ]

})