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

# POINTERS in C++

- We have two type

  - raw pointers
  - smart pointers

- What is a pointer?

  - It's as integer
  - store a memory address

- Memory is 1 dimensional line

  - a long blob

- Example of memory

  - like a long line street in a city each house have an address
  - every house is one byte of memory

- Zero is not a vaild memory address

  - we can't read or write for memory address of zero
  - if u do that the programme will crash
  - Zero mean `NULL` also u can use `nullptr` from c++ 11 and above

- When making pointers type is meaningless

- U can get address of any variable by prefix it with ambersand `&`

```c++
int a = 5;
void* c = &a;
```

- Pointers just like any others vars but instead holding a value it hold
  a memory address
- memory address is just a value it's an integer value

  - its size depend on serveral things
  - could be [16bits - 32bits - 64bit] integer

- Types not matter and are meainingless

```c++
int a = 5;
void* c = &a;
// same as void*
int* d = &a;
// same as void*
double* d = (double*)&a;
```

## Dereferencing pointer

- By prefixing pointer with asterisk `*` we dereferencing it
  - Now we can read and write to it

```c++
int a = 5;
void* c = &a;

// write
*c = 5; //error
```

- now when we dereferencing pointer to write the type of pointer matter u can't for example write integer for void type.

```c++
int a = 5;
int* c = &a;

// write
*c = 5;
```

## To Know

- Some people says that pointers point to a block of memory

  - But this is not accurate

- Memory

  - Heap | Stack

- to allocate meomery without declaring var

  - ```c++
    // 8 byte of data
    char* buffer = new char[8];
    ```
  - Because we used `new` keyword this will store in Heap
  - This will make eight byte of memory and get a pointer to the begging of that block

- `memset()` fill the memory with data we specfied

  - take a pointer
  - take a value
  - take a size => how many bytes you want to fill
  - ```c++
    // 8 byte of data
    char* buffer = new char[8];
    memset(buffer,0,8);
    ```

- Because we used `new` keyword this will store in Heap

  - we should delete the data when we are done with it.
  - To delete we can use `delete`
  - `char* buffer` as the data is an array
    - we will use `[]` array operator
    - then type the namr of it
  - ```c++
    // 8 byte of data
    char* buffer = new char[8];
    memset(buffer,0,8);

    delete[] buffer;
    ```

- pointers the selve are just a variable

  - and are also stored in memory
  - so we can have a pointer to a pointer and u can go deeper with that
  - ```c++
    // 8 byte of data
    char* buffer = new char[8];
    memset(buffer,0,8);

    char** ptr = &buffer;

    delete[] buffer;
    ```

- 32bits application

  - pointers are 4bytes in memory.

- Because of endianness the pointer address could be in revesrse order
- Endianness refers to the order in which bytes are stored in computer memory. There are two main types of endianness: big-endian and little-endian.

# REFERENCES in C++

- Pointers and References are pretty much the same as far what the computer will do with them

## pointers and References

- Semantically they have subtle diffrences
- Reference is a way to refrence **existing data**
- With Pointer u could create new pointer variable and set it to `nullptr` or `NULL` OR `0`
- This cannot done with References as it must refrence existing var

## References

- Reference not a new variable and don't occupy memory
- U can define one by
  - write the type of data u want to reference
  - follow type with ambersand `&`
  - ```c++
    int a = 5;
    int& ref = a;
    ```
  - We just now created somthing called alias
  - the `ref` variable is not really a variable
  - It just a variable that exsit in our source code not in memory like noraml variables
  - We can use `ref` as it `a` we can read and write to `ref` directly

## usecases

- If u want for example to pass a variable to function and u want to manipulate this variable directly from function

- In function u can passe
  - By value
  - By pointer
  - By reference

```c++
#include <iostream>

int increaseByValue(int a)
{
	return a++;
}

int increaseByPointer(int* a)
{
	/* The wrong way
	* As it will increase the address first
	* and then derefrence it
	*/
	// return *a++;

	/* The right way
	* Derefrence first
	* then add value
	*/
	return (*a)++;
}

int increaseByRef(int& a)
{
	return a++;
}

int main()
{
	int a = 5;

	increaseByValue(a);
	std::cout << a << "\n"; // 5

	increaseByPointer(&a);
	std::cout << a << "\n"; // 6

	increaseByRef(a);
	std::cout << a << "\n"; // 7
}
```

## Note

- Any thing u can do with references you can do with pointers
- Pointers are more powerful and moreuseful in general
- When u make a reference u cannot change what it references.
- U can change pointer

  - ```c++
    int a = 5;
    int b = 5;

    int* ptr = &a;
    *ptr = 7; // a = 7

    ptr = &b;
    *ptr = 8 // b = 8

    ```

# CLASSES in C++

- classes are a way to group data and functionality together
- class are a new variable type we called it `object`
- the new object variable we called `instance`

```c++
class Player
{
  int x,y;
  int speed;
};

Player player; // instantiated a player object

// set var of player
player.x = 1;       // error as it private
player.y = 5;       // error as it private
player.speed = 50;  // error as it private
```

- By default class make everything private
- To make it public to access we have to sepecify that by `public:`

```c++
class Player
{
  public:
    int x,y;
    int speed;
};
```

- To write a function we could define it separtely outside the class like

```c++
class Player
{
  public:
    int x,y;
    int speed;
};

// Player& player as we want to change player
void move(Player& player,int xa,int ya)
{
  player.x = xa * player.speed;
  player.y = ya * player.speed;
}

int main(){
  Player player; // instantiated a player object

  // set var of player
  player.x = 1;
  player.y = 5;
  player.speed = 50;

  move(player, -1, 1);
}
```

- We can move functions inside classes
- Functions in classes are called methods

```c++
class Player
{
  public:
    int x,y;
    int speed;

    void move(int xa,int ya)
    {
      x = xa * player.speed;
      y = ya * player.speed;
    }
};


int main(){
  Player player; // instantiated a player object

  // set var of player
  player.x = 1;
  player.y = 5;
  player.speed = 50;

  player.move( -1, 1);
}
```

- Anything u can do with classes u can do without classes.
  - They just make our life easier
  - Syntax sugar ^\_^

# CLASSES vs STRUCTS in C++

- class private by default
- struct public by default

## so why it exist in c++?

- Because of backward compatibility with `c`

## when to use one of them?

- if u want all members to be public use struct

## Cherno

- `pod`=> plain old data
- use struct when i need to represent a punch/group of data
- ```c++
  struct Vec2{
    float x,y;
  }
  ```
- U could also add functions for example

  - ```c++
    struct Vec2{
      float x,y;

      Vec2 add(const Vec2& other)
      {
        x += other.x;
        y += other.y;
      }
    }
    ```

  - it all just about manipulating vec data

- Use classes with inhertance
- Some compilers will give u warnings in case

  - u have class A and struct B.
  - struct B inhert from class A.
  - it just warnings and code will work.
  - some compilers won't show these error.

- If u want something filloff functionlity go with class
- U can use struct whenever u use class

## some comments on video

```
Reydriel | 10 months ago (edited)

To elaborate more on what Cherno says in this video,

structs are a legacy feature from C which can group together variables into a user-defined type,

BUT CANNOT contain functions
(because C did not have OOP features such as methods).

This is why it's common in C++ to use structs for "classes with no methods", because that was how they were used in C.
```

```
It Cracks! | 5 years ago (edited)

The C++ Core Guidelines C.2 states:
"Use class if the class has an invariant;
use struct if the data members can vary independently."

So if you don't have any preexisting style, your best bet is to stick to that.
```

```
Matthijs van Duin | 2 years ago
The difference in default access also applies to inheritance:
struct Foo : Bar  // Bar is a public base class of Foo
class Foo : Bar  // Bar is a private base class of Foo
```

# How to Write a C++ Class

- use `m_` with private variable in class
  - stand for member variable
  - it just a better way to get the member of class
- Separate public function from public variable from public static variable

```c++
class Foo
{
  public:
    // static variables

  public:
    // variables

  public:
    // functions
}
```

# Static in C++

- Two means

  - Out of struct or class
  - Inside of struct or class

- static out of struct or class

  - means that the linkage of that symbol that you declared to be static is going to be internal meaning it's going to be visible only to that transaltion unit you've defined it in

- static Inside of struct or class
  - means that variable is actually going to share memory with all of the instances of the class
  - means whatever how many struct or class u have created it will be one instance of that static variable

## static out of struct or class

- U cannot have global variable with same name in diffrent files

  - u can make them static `means that they will be private in that file`
  - u can refrenec one of them using `extern` keyword
    ```c++
    extern int b;
    ```

- u can use static variable in headerfiles so when u import them in translation units each file will have its own static var
- use static all times u won't the variable to be global
- global variables are bad

# Static for Classes and Structs in C++

- In all programming langs static
  - with variables means it will be one instance of that variable across all instances
  - with method u can access this method without create an instance of the class

```c++
struct Entity
{
  int x,y;
  print()
  {
    std::cout<< x << ", " << y << std::endl;
  }
}
```

- when u define variable as static u should declare them outside to make compiler link them
  - ```c++
      variableType NameOfClassOrStruct::nameOfStaticVariable;
    ```
  - u can read and write them
  - u can consider it like a variable in namespace

```c++
struct Entity
{
  static int x,y;
  print()
  {
    std::cout<< x << ", " << y << std::endl;
  }
}
// To write Entity::x = 5;
// To read  cout<< Entity::x ;
int Entity::x;
// To write Entity::y = 7;
// To read  cout<< Entity::y;
int Entity::y;
```

- to call static function without creating instance of class or struct u can use
  - ```c++
    NameOfClassOrStruct::nameOfFunction();
    ```
- or u can create instance and call it with `.` as normal way

## Note

- static method cannot access non static variables
