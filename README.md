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

# How the C++ Compiler Works

- Steps

  - Compiling
  - Linking

## Compiling

- Take text file and convert it to intermediate file called `obj`

- Steps

  - All preprocessors statement evaluated first
  - tokenizing and parsing
  - Abstract syntax tree
  - All of the code must be at the end either constatnt data or instruction

- `cpp` files are called translation units
- cpp dosenot care about files
- files have no meaning
- Not nessecary that num `.cpp` files equal translation units
  - u may make some `.cpp` files but include all these file in one `.cpp`

## Pre-processing Statements

- `include`
  - include look for file u want open it and read all its data and then copy it to file u call it form
- `define`
  - take the name follwing it and replace it with whatever follows
- `if` `endif`
  - use to include or exclude code based on given condition
- `ifdef`
- `pragma`

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

- Declared function won't be compiled or linked utill you call them in your code
- Function definition will compiled and linked even if u never call them as they could be used in another file
- If u define function by word `static` this mean that function only used in the translation unit u defined into

## Avoid linking errors

- `static`

  - all files will have its own version of function

- `inline`

  - will replace call with the function body

- Move to third translation unit

# Variables in C++

- All programmes are about data and manipulating data.

- Data stored in memory either in stack or heap

## Premitives data type

- The only diffrence is the size that type occpuy in memory
- The size for same type differ depend on the complier u are using

- How to define variables?

```c++
type var_name_00;
type var_name_01 = 5;
```

## int size

- `int` is 4 Bytes
- 1 Byte have 8 Bits
- 1 Bits can store 2 values `0` or `1`
- So int can store 2 ^ (4\*8) = `2 ^ 32`
- int can accept number form `-2^31` to `+2^31` But why?
- As int store negative and positive numbers so it need some way to store negatve
- To store negative it take one bit from `32bits`
- If u want to store positive numbers only u can use `unsigned` keyword this mean int now can store double the amount number form `-2^32` to `+2^32`

## Type

- **Basic 5**

| Type      | size           |
| --------- | -------------- |
| char      | 1 Byte         |
| short     | 2 Byte         |
| int       | 4 Byte         |
| long      | 4 Byte usually |
| long long | 8 Byte         |

- **To store decimal**
  - when typing decimal in c++ it considerd as double
  - We use `f` or `F` to make number as float for example `2.2f`

| Type   | size   |
| ------ | ------ |
| float  | 4 Byte |
| double | 8 Byte |

- **Boolean**
  - Zero `0` mean => false
  - Any number else is => true

| Type | size   |
| ---- | ------ |
| bool | 1 Byte |

- There is no way to address individual bits
- We could only address bytes
- For all the above `bool` is one byte not bit
- **U can store up to `8 bool` in one byte**

- To get size of type u can use `sizeof()`
  - `sizeof(bool)`
  - `sizeof bool`

## Pointers and References

- U have the ability to convert any type to pointers or references

- `Pointers`

  - Define with `*` after type like `bool* var = false;`

- `References`
  - Define with `&` after type like `bool& var = false;`
