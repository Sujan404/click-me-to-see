/** @type {import('tailwindcss').Config} */
import flowbitePlugin  from "flowbite/plugin"
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    fontFamily:{
      'roboto': ["Roboto Mono", "monospace"]
    },
    extend: {},
  },
  plugins: [
    flowbitePlugin 
  ], 
}




