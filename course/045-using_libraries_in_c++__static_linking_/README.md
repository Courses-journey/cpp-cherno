# Using Libraries in C++ (Static Linking)


- `include` directory is a bunch of header files
  - function we going to use from the prebuilt binaries
- `lib` directory is the prebuilt binaries

  - dynamic libraries
  - static libraries

- some libraries have both static and dynamic and u can choose which one to choose

- static mean that library will put in your executable
- dynamic link at runtime
  - u can choose to link on the fly
  - link at program launch
- `cherno` use static linking as possible

  - better that dynamic
  - compiler can do optimization with linking

## `.dll` `.dll.lib` `.lib`

- `.dll` dynamic link library
- `.dll.lib` kind of static library we use with `.dll`
  - contains all of the locations of the functions and symbols in `.dll`
  - if we don't have this file we will need to call function by name from `.dll`
- `.lib` static library this is what we link if we don't want compile time linking

  - and we won't need `.dll` to be with our executable at runtime

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
- go to additional Dependencies add `.lib` file
  - for example `glfw3.lib`
  - separate between multiple with semicolon `;`
- Now you are ready to go.

## Note

- code written in c in c++

```c++
extern "C" _function_signature()
```

