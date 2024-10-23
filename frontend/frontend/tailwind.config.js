/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    fontFamily:{
      'display': ['Oswald'],
      'body': ["Open Sans"],
    },
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

