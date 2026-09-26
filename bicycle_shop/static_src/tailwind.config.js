/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [],
  theme: {
    extend: {
      colors: {
        primary: {
          light: '#f0f9ff',
          DEFAULT: '#3b82f6',
          dark: '#1d4ed8',
        },
        secondary: {
          light: '#f8fafc',
          DEFAULT: '#64748b',
          dark: '#475569',
        },
        accent: {
          light: '#f0f2f5',
          DEFAULT: '#1e293b',
          dark: '#0f172a',
        },
        neo: {
          light: #ffffff,
          dark: #0f0f23,
          card: #ffffff,
          shadow: rgba(0, 0, 0, 0.1),
        },
      },
      boxShadow: {
        'neo': 'inset 0 2px 4px rgba(0,0,0,0.1), 0 4px 12px rgba(0,0,0,0.05)',
        'neo-hover': 'inset 0 2px 4px rgba(0,0,0,0.15), 0 8px 20px rgba(0,0,0,0.1)',
        'neo-active': 'inset 0 1px 2px rgba(0,0,0,0.1), 0 2px 4px rgba(0,0,0,0.05)',
      },
      borderRadius: {
        'neo': '1rem',
      },
    },
  },
  plugins: [],
}