# cpp-cherno

The Cherno youtube channel

## [c++ course](https://www.youtube.com/playlist?list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb)

# How C++ Works

## Some

- `#include <iostream>`

  - preprossecer statement it means this statement will be processed first before compilation
  - `include <iostream>` it will look for file called `iostream` and paste it the file u called in

- `<<`

  - Overloaded operator
  - operator are just functions

- `int main()`

  - sepcial case it assume it return `0`

- `cin.get()`

  - await user press enter before programe end

- **After compilation finish there will be `.obj` file for all `.cpp` files**

## Declaration and Definition

- Declaration is the header of function like

```c++
void log(const char* message);
```

- Definition is the implementation of Declaration
  - or declaration with body

```c++
void log(const char* message)
{
  std::cout<<message<<std::endl;
}
```

- U can ignore param name in Declaration for example

```c++
void log(const char*);
```
