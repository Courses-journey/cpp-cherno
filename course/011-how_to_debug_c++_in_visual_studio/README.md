# How to DEBUG C++ in VISUAL STUDIO


- what debug mean?
  - It mean de bug to remove bugs from code.

## Breakpoints

- what Breakpoints mean?

  - It mean a point in our program at which debugger will break `pause`.

- Make sure u are in debug mode

### Buttons

- Step into

  - Step into the current function that is on this line of code `if there is a function`
  - `f11`

- Step over

  - Step over to the next line of code in the current function
  - `f10`

- Step out

  - Step out the current function and take us to what ever call of this function.
  - `shift` + `f11`

- Continue
  - continue execution of programme
  - `f5`

## Look at memory

- Windows in vs

- Auto and Locals

  - show you local variables or variables that it thinks might be important to you watch

- Watch

  - Let us monitor variables
  - Type name of the variable u want to track

- Memory

  - run code in debug mode
  - open from DEBUG -> Windows -> Memory -> Memory 1
  - U can search certain var using `&var_name`
  - In debug mode compiler made extra good stuff to make our life easier
  - For example It know that we have declare variable but we never assign it so it fill it with `cc cc ...` so if u see that u can know directly that the variable haven't assigned yet
  - `cc cc ...` It seems working when running as debug in x68 only
  - every `00` is one byte of data

