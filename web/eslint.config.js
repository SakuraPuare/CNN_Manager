import globals from "globals";
import pluginJs from "@eslint/js";
import tseslint from "typescript-eslint";
import pluginVue from "eslint-plugin-vue";
import pluginPrettierRecommendedConfigs from "eslint-plugin-prettier/recommended";

export default [
  {
    languageOptions: {
      globals: {
        ...globals.browser,
        ...globals.es2020,
        ...globals.node,
      },
      ecmaVersion: 2020,
      // parser: parserVue,
      parserOptions: {
        parser: tseslint.parser,
      },
    },
  },
  pluginPrettierRecommendedConfigs,
  pluginJs.configs.recommended,
  ...tseslint.configs.recommended,
  ...pluginVue.configs["flat/essential"],
];
