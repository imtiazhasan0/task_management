/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",  //tamplates of root directory
    "./**/templates/**/*.html"//taplates of apps
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}