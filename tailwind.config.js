/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        tahack: '#4B5E51',
        tahackSecond : '#646A4E',
        tahackBg : '#F6F8F5',
    },
  },
  plugins: [],
}
}