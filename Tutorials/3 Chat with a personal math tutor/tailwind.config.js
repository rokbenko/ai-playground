/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx}',
    './src/components/**/*.{js,ts,jsx,tsx}',
    './src/app/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        "gray-700": 'rgb(64,65,78)',
        "gray-800": "rgba(52,53,65,1)",
        "gray-900": 'rgb(32,33,35)',
      },
      width: {
        '280': '280px',
      },
      backgroundImage: {
        'vert-dark-gradient': 'linear-gradient(180deg, rgba(53, 55, 64, 0), #353740 58.85%)',
      }
    },
  },
  plugins: [],
}
