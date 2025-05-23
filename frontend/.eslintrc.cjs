/* eslint-env node */
module.exports = {
  root: true,
  extends: [
    "plugin:vue/vue3-essential",
    "eslint:recommended"
  ],
  parserOptions: {
    ecmaVersion: 'latest'
  },
  rules: {
    // allow console.log during development
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    // allow debugger during development
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
    // vue specific rules
    "vue/multi-word-component-names": "off", // Or "warn" or "error" if you want to enforce it
    "vue/no-unused-vars": "warn"
  }
}
