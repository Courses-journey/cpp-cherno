# How the C++ Linker Works


## what does?

- Linker find where each symbols and function is and link them together

## TO KNOW

- WHEN compile file in vs only compilation stage happen
- WHEN build or run the project both the stage happen compilation then linking

## Errors

- `error: C0000` mean it's a compilation error.
- `error: LNK0000` mean it's a linking error.

## T

- Declared function won't be compiled or linked until you call them in your code
- Function definition will compiled and linked even if u never call them as they could be used in another file
- If u define function by word `static` this mean that function only used in the translation unit u defined into

## Avoid linking errors

- `static`

  - all files will have its own version of function

- `inline`

  - will replace call with the function body

- Move to third translation unit

