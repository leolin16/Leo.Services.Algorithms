# Typescript

## benefits

1. static types (variables, parameters, return types, etc.)
2. organization (classes, namespaces, modules, interfaces)
3. Tooling (static type analysis, instant errors, detect unused data/unreachable code, source maps - debug directly in TypeScript, inspect external modules)

## Installation

1. method1: www.typescriptlang.org
2. method2: `npm install -g typescript` to install globally
3. method3: `npm install typescript --save-dev` to install locally
4. extra: `npm install -g ts-node typescript` to install globally, this way, tsconfig.json is needed to substitute the necessity of --lib parameter, etc.

### get extension for vscode

1. Prettier extension
2. ESLint extension
### method1: www.typescriptlang.org

### method2

1. `npm install -g typescript ts-node jest` to install globally
2. `npm install --save-dev typescript jest ts-jest @types/jest @types/node`
3. `tsc --init` to create tsconfig.json

### method3
1. `npm install typescript --save-dev` to install locally

## Compile

> tsc ???.ts
<<<<<<< HEAD
> ts-node ???.ts
=======

## test

1. `npm init` to create package.json
2. `jest --init` to create jest.config.js and config package.json
3. config jest.config.js

   ```js
    module.exports = {
        transform: {
            '^.+\\.tsx?$': 'ts-jest',
        },
        testRegex: '(/__tests__/.*|(\\.|/)(test|spec))\\.(jsx?|tsx?)$',
        moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node'],
    }
   ```

4. `jest {some_sub_folder}(/{some_test.js}) --watch`
5. ctrl + C to exit
>>>>>>> 21ac8b167a093d106fcca8d22f843a5bca1c4003
