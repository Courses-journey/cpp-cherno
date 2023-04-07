# Using Dynamic Libraries in C++


- dynamic linking happen in runtime
- static linking happen in compile time
  - u can link it in executable
  - or u can make as dynamic library

## How to setup

- make `Dependencies` directory at project directory
  - make folder with name of the library
- open project properties
- make sure of configuration and target
- go to c++/c
  - if not exist make sure that there is `.cpp` file in your solution
- go to general
- go to additional include add `include` path of the library
  - make path relative to project folder
  - user `$(SolutionDir)Dependencies\library_name\include\`
- go to linker
- go to general
- go to additional library directories add `lib` folder of the library
  - make path relative to project folder
  - user `$(SolutionDir)Dependencies\library_name\lib\`
- now go to input
- go to additional Dependencies add `.dll.lib` file
  - for example `glfw3.dll.lib`
  - separate between multiple with semicolon `;`
- u must provide `.dll` to the output folder of your executable to work
- Now you are ready to go.

## comment

- 洪鹏圳 | 1 year ago
  <br>
  If you use lib + dll，you don't need `**declspec(dllimport)` because all the functions or variables you wan't to import have defined in lib as pointer;but if you use LoadLibrary API to import dll, with `**declspec(dllimport)` you can tell the compiler which function or variable you want to import, it will reduce the import time

- Agent M | 5 years ago
  <br>
  Because you already linked the static library that came with the dll with all the declarations of functions within the dll, it knows where to look for them, except it's maybe slightly less efficient.

