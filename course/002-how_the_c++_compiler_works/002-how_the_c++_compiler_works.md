# How the C++ Compiler Works


- Steps

  - Compiling
  - Linking

## Compiling

- Take text file and convert it to intermediate file called `obj`

- Steps

  - All pre-processor statement evaluated first
  - tokenizing and parsing
  - Abstract syntax tree
  - All of the code must be at the end either constant data or instruction

- `cpp` files are called translation units
- cpp doesn't care about files
- files have no meaning
- Not necessary that num `.cpp` files equal translation units
  - u may make some `.cpp` files but include all these file in one `.cpp`

## Pre-processing Statements

- `include`
  - include look for file u want open it and read all its data and then copy it to file u call it form
- `define`
  - take the name following it and replace it with whatever follows
- `if` `endif`
  - use to include or exclude code based on given condition
- `ifdef`
- `pragma`

