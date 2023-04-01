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

# Functions in C++

- Avoid code dupplication

- Has inputs and output

- Take parameters

- `void` to make it return nothing

- Use Functions only to reduce code

- Too many function can affects preformance

- Function declration written in `.h` files
- Function definiation written in translation unit `.cpp` files

# C++ Header Files

- Used for

  - declare ceratin type of function

- When define function in another file c++ won't know that it even exist when compiling the file

  - So we need a common place to make declartion in it.

## `#pragma once`

- `pragma` is an instruction that sent to the compiler
- `pragma once` mean include this file once
- It called Header Guide

## `ifndef` `endif`

- The traditional `old` way

```c++
#ifndef _LOG_H
#define _LOG_H

void Log(cont char* msg);

#endif
```

## `#include <fileName>` and `#include "fileName"`

- `#include <fileName>` Compiler search for file in the system's standard include directories.

  - angle brackets
  - The file u search must in one of the includes directories
  - used only with includes directories

- `#include "fileName"` the compiler first searches for the header file in the current directory. If the header file is not found in the current directory, the compiler searches for it in the standard include directories

  - double quotes
  - relative to directory the project exist in `#include "..\file"`.
  - used everywhere

### Note in standard library

- file without extension at the end like `iostram` are c++ STDL
- file with `.h` extension at the end like `stdlib.h` are c STDL

# How to DEBUG C++ in VISUAL STUDIO

- what debug mean?
  - It mean de bug to remove bugs from code.

## Breakpoints

- what Breakpoints mean?

  - It mean a point in our programe at which debugger will break `pause`.

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
  - continuse execution of programme
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
  - open from DEGUG -> Windows -> Memory -> Memory 1
  - U can search ceertin var using `&var_name`
  - In debug mode compiler made extra good stuff to make our life easier
  - For example It know that we have declare variable but we never assign it so it fill it with `cc cc ...` so if u see that u can know directly that the variable haven't assigned yet
  - `cc cc ...` It seems working when running as debug in x68 only
  - every `00` is one byte of data

# CONDITIONS and BRANCHES in C++ (if statements)

- If make programme move from place to antoher in memory depend on condition and start execute commands from that place in memory.
- If u want a faster code try to avoid them.

```c++
if()
{
  // code
}else if()
{
  // code
}

// ----- same as -----
// It just like a shortcut

if ()
{
  // code
}
else
{
	if ()
	{
    // code
	}
}

```

- We can use `if` with pointers to check that they aren't `null`

```c++
const char* ptr = "hello";

if(ptr)
  cout<<"ptr not null"<<"\n";
else
  cout<<"ptr is null"<<"\n";

```

# BEST Visual Studio Setup for C++ Projects!

- Output Dir:

  - `$(SolutionDir)bin\$(Platform)\$(Configuration)\`

- intermediates files:

  - `$(SolutionDir)bin\intermediates\$(Platform)\$(Configuration)\`

# Loops in C++ (for loops, while loops)

## for loop

```c++
for(int i = 0; i < 5; i++)
{

}
```

- `i` dosen't have to be zero and dosen't have to be an integer
- condition
- `i++` called before next iteration of for loop

  - `i += 1`
  - `i = i + 1`

- You can separate all for loop stuff like code below

```c++
int i = 0;
for(; ;)
{
  // code
 i++;

 if(/*condition*/){
    break;
 }
}
```

- Use when u have number of iterations

## while loop

```c++
int i = 0;
while(/*condition*/)
{
  // code
  i++;
}
```

- Use when u have condition

## do while loop

```c++
int i = 0;
do
{
  // code
}while( /*condition*/ )
```

- The main difference from `while` that do will execute at least one time no matter what is the condition

# Control Flow in C++ (continue, break, return)

## continue

- can only used in loop
- Function
  - Go to next iteration of this loop
  - Skip the current iteration

## break

- Primarly used in loops and used in switch statement.
- Function
  - Get out of the loop | end the loop

## return

- U can say it's the most powerfull
- Function
  - Get out of the entire function.
- Code below it is a dead code
