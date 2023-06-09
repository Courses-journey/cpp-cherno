cpp-cherno | The Cherno youtube channel

- [c++ course](https://www.youtube.com/playlist?list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb)

# Welcome to C++

# How to Setup C++ on Windows

# How to Setup C++ on Mac

# How to Setup C++ on Linux

# How C++ Works

## Some

- `#include <iostream>`

  - pre-processor statement it means this statement will be processed first before compilation
  - `include <iostream>` it will look for file called `iostream` and paste it the file u called in

- `<<`

  - Overloaded operator
  - operator are just functions

- `int main()`

  - special case it assume it return `0`

- `cin.get()`

  - await user press enter before program end

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

# Variables in C++

- All programmes are about data and manipulating data.

- Data stored in memory either in stack or heap

## Primitives data type

- The only difference is the size that type occupy in memory
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
- As int store negative and positive numbers so it need some way to store negative
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
  - when typing decimal in c++ it considered as double
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

- Avoid code duplication

- Has inputs and output

- Take parameters

- `void` to make it return nothing

- Use Functions only to reduce code

- Too many function can affects performance

- Function declaration written in `.h` files
- Function definition written in translation unit `.cpp` files

# C++ Header Files

- Used for

  - declare certain type of function

- When define function in another file c++ won't know that it even exist when compiling the file

  - So we need a common place to make declaration in it.

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

- file without extension at the end like `iostream` are c++ STDL
- file with `.h` extension at the end like `stdlib.h` are c STDL

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

# CONDITIONS and BRANCHES in C++ (if statements)

- If make programme move from place to another in memory depend on condition and start execute commands from that place in memory.
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

- `i` doesn't have to be zero and doesn't have to be an integer
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

- Primarily used in loops and used in switch statement.
- Function
  - Get out of the loop | end the loop

## return

- U can say it's the most powerful
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

- Zero is not a valid memory address

  - we can't read or write for memory address of zero
  - if u do that the programme will crash
  - Zero mean `NULL` also u can use `nullptr` from c++ 11 and above

- When making pointers type is meaningless

- U can get address of any variable by prefix it with ampersand `&`

```c++
int a = 5;
void* c = &a;
```

- Pointers just like any others vars but instead holding a value it hold
  a memory address
- memory address is just a value it's an integer value

  - its size depend on several things
  - could be [16bits - 32bits - 64bit] integer

- Types not matter and are meaningless

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

- to allocate memory without declaring var

  - ```c++
    // 8 byte of data
    char* buffer = new char[8];
    ```
  - Because we used `new` keyword this will store in Heap
  - This will make eight byte of memory and get a pointer to the begging of that block

- `memset()` fill the memory with data we specified

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
    - then type the name of it
  - ```c++
    // 8 byte of data
    char* buffer = new char[8];
    memset(buffer,0,8);

    delete[] buffer;
    ```

- pointers themselves are just a variable

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

- Because of endianness the pointer address could be in reverse order
- Endianness refers to the order in which bytes are stored in computer memory. There are two main types of endianness: big-endian and little-endian.

# REFERENCES in C++

- Pointers and References are pretty much the same as far what the computer will do with them

## pointers and References

- Semantically they have subtle differences
- Reference is a way to reference **existing data**
- With Pointer u could create new pointer variable and set it to `nullptr` or `NULL` OR `0`
- This cannot done with References as it must reference existing var

## References

- Reference not a new variable and don't occupy memory
- U can define one by
  - write the type of data u want to reference
  - follow type with ampersand `&`
  - ```c++
    int a = 5;
    int& ref = a;
    ```
  - We just now created something called alias
  - the `ref` variable is not really a variable
  - It just a variable that exist in our source code not in memory like normal variables
  - We can use `ref` as it `a` we can read and write to `ref` directly

## use cases

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
	* and then dereference it
	*/
	// return *a++;

	/* The right way
	* Dereference first
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
- Pointers are more powerful and more useful in general
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
- To make it public to access we have to specify that by `public:`

```c++
class Player
{
  public:
    int x,y;
    int speed;
};
```

- To write a function we could define it separately outside the class like

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

- Use classes with inheritance
- Some compilers will give u warnings in case

  - u have class A and struct B.
  - struct B inherit from class A.
  - it just warnings and code will work.
  - some compilers won't show these error.

- If u want something fill of functionality go with class
- U can use struct whenever u use class

## some comments on video

- **Reydriel | 10 months ago (edited)**
  <br>
  To elaborate more on what Cherno says in this video,
  <br>
  structs are a legacy feature from C which can group together variables into a user-defined type,
  <br>
  BUT CANNOT contain functions
  (because C did not have OOP features such as methods).
  <br>
  This is why it's common in C++ to use structs for "classes with no methods", because that was how they were used in C.

- **It Cracks! | 5 years ago (edited)**
  <br>
  The C++ Core Guidelines C.2 states:
  "Use class if the class has an invariant;
  use struct if the data members can vary independently."
  <br>
  So if you don't have any preexisting style, your best bet is to stick to that.

- **Matthijs van Duin | 2 years ago**
  <br>
  The difference in default access also applies to inheritance:
  <br>
  struct Foo : Bar // Bar is a public base class of Foo
  <br>
  class Foo : Bar // Bar is a private base class of Foo

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

  - means that the linkage of that symbol that you declared to be static is going to be internal meaning it's going to be visible only to that translation unit you've defined it in

- static Inside of struct or class
  - means that variable is actually going to share memory with all of the instances of the class
  - means whatever how many struct or class u have created it will be one instance of that static variable

## static out of struct or class

- U cannot have global variable with same name in different files

  - u can make them static `means that they will be private in that file`
  - u can reference one of them using `extern` keyword
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

# ENUMS in C++

- Enums is a shortcut for enumeration and basically all it is a set of values
- Give a name to value
- Define set of values
- Limit which value assign to what
- A way to name values
- It just an integer
- By default it a zero based index
  - first value zero and increment 0 1 2 ...
- U can specify the value if u want
  - If u define first one as 5 and level others
  - it will be 5 6 7 8 ...
- By default enums is 32bit integer and u can change that
  - it must be integer
- There is an enum class
- U can access by `::` example `EnumName::Info`
  - or directly using `Info`

```c++
// example
const int A = 0;
const int B = 1;
const int C = 2;

// Enum way
enum Hamada
{
  A, B, C
};

enum HamadaTani
{
  A = 9, B = 7, C = 3
};

enum HamadaFoo : unsigned char
{
  A = 9, B = 7, C = 3
};

int main()
{
  // int x = A;

  Hamada y = A; // B | C
  // Hamada y = D; // Error

  int x = Hamada::A;
}

```

# Constructors in C++

- Special type of method which run every time when we instantiate an object
- doesn't have return type
- it's name must match the of the class
- there is always a default constructor

```c++
class Entity
{
public:
	float X, Y;

	Entity() {
		X = 0;
		Y = 0;
	};

	Entity(float x,float y) {
		X = x;
		Y = y;
	};
};
```

- To crate instance u can use

```c++
Entity e; // Entity()
Entity e1(10.f,20.f); // Entity(float x,float y)
```

- U can prevent users from create instance of class by two way

  - make constructor private
  - ```c++
    class Log
    {
    private:
      Log(){};

    public:
      Write(const char* msg) {
      };
    };
    ```

  - assign constructor to delete
  - ```c++
    class Log
    {
    public:
      Log() = delete;
      Write(const char* msg) {
      };
    };
    ```

- There are special type of constructor such
  - copy constructor
  - move constructor

# Destructors in C++

- run when u destroy an object
- In Constructors u can initialize any variable or any thing u want
- In Destructors u uninitialized any variable or clean any memory that you've used
- Applies to both stack and heap allocated objects
- to make one create a method with object name and prefix it with Tilde `~`

  - ```c++
    class Entity
    {
    public:
      float X, Y;

      Entity() {
        X = 0;
        Y = 0;
      };


      Entity(float x,float y) {
        X = x;
        Y = y;
      };

      ~Entity() {
        X = 0;
        Y = 0;
      };
    };
    ```

# Inheritance in C++

- Base class that have common functionality
  - Branch it and add more to it
- Avoid code duplication
- A way to extend existing class and new functionality to it

```c++
class Entity
{
public:
	float X, Y;
};

class Player : public Entity
{
public :
	const char* Name;
};

```

# Virtual Functions in C++

- Virtual Functions allow us to override methods in subclasses
- U can define same functions name and parameters in base and subclass
  - it will work as expected until u assign subclass instance to base pointer
  - when u do that the function in base will be called not the one in base
  - Here come virtual functions

```c++
class Entity
{
public:
	float X, Y;
	void GetName(){
		std::cout<<"Entity"<<"\n";
	}
};

class Player : public Entity
{
public :
	const char* Name;
	void GetName() {
		std::cout << "Player" << "\n";
	}
};
```

- Normal instance

```c++
  Entity e;
  e.GetName(); // Entity

  Player p;
  p.GetName(); // Player

  // -------------
  std::cout << "================" << "\n";
  // -------------
```

- Pointer instance

```c++
  Entity* e1 = new Entity();
  e1->GetName(); // Entity

  Player* p1 = new Player();
  p1->GetName(); // Player

  // -------------
  std::cout << "================" << "\n";
  // -------------
```

- Pointer instance and assign subclass to base pointer

```c++
  Entity* entity = e1;
  entity->GetName(); // Entity

  entity = p1;
  entity->GetName(); // Entity | not as expected | we expected to return Player
```

- virtual function reduce something called dynamic dispatch
  - compiled typically implemented by our vtable
- vtable is a table that contains mapping for all the virtual functions

- so to wrap it up all we need now to make function in base class as `virtual`
- c++ 11 introduce `override` keyword
  - it's not required but make code more readable
  - Reduce bugs
    - wrong writing method name in subclass for example
    - override non virtual method

```c++
class Entity
{
public:
	float X, Y;
	virtual void GetName(){
		std::cout<<"Entity"<<"\n";
	}
};

class Player : public Entity
{
public :
	const char* Name;
	void GetName() override{
		std::cout << "Player" << "\n";
	}
};
```

- Virtual function aren't free
  - two runtime costs
    - additional memory required to store vtable
    - every time we call function we go to that table to know which function to actually map to.
    - `cherno` use them all-time
      - May considered not use them in **embedded systems** which have terrible performance and every cpu slice account

## vtable

- In C++, virtual functions are used to achieve runtime polymorphism, which allows code to work with objects of different classes without knowing their exact type at compile time.

- When a virtual function is called on an object through a pointer or reference to the base class, the correct version of the function for the actual type of the object is called.

- This process is called dynamic dispatch, and it is typically implemented by using a vtable to store the addresses of the virtual functions for each class in the inheritance hierarchy.

- While virtual functions have some performance overhead compared to non-virtual functions, they allow for more flexible and extensible code.

## Notes | Difference between `.` and `->`

- In C++, the dot operator (.) is used to access

  - methods and properties of an object when it is accessed directly,

- whereas the arrow operator (->) is used to access

  - methods and properties of an object when it is accessed through a pointer.

```c++
// Accessing object method using dot operator
MyObject obj;
obj.doSomething();

// Accessing object method using arrow operator through a pointer
MyObject* pObj = new MyObject();
pObj->doSomething();

// Accessing object property using dot operator
int x = obj.value;

// Accessing object property using arrow operator through a pointer
int y = pObj->value;
```

## comments

### Juan Ortiz | 3 years ago

Brief explanation of uncovered topics (yet) in this video:

- Since strings is not a primitive type of C++ we need to import the header

```c++
#include <string>
// To use string without namespace std is like this:
std::string MyString("hello")
// This is equivalent to:
std::string MyString = "Hello"
```

- Pointer instances: new keyword returns a pointer

```c++
std::string* MyString = new std::string("Hello")
// And if is a pointer you access their properties with -> instead of a dot (.)
std::cout << MyString->length() << std::endl;
```

# Interfaces in C++ (Pure Virtual Functions)

- allow us to define virtual function in our base class that have no implementation and impl it in subclasses
- force subclasses to impl there own impl to that virtual function
- in programming it's common to have classes that have unimplemented method called `interface class`
  - it's not possible for us to instantiate this class
- to make virtual function a pure virtual function
  - we assign it to 0

```c++
class Entity
{
public:
	float X, Y;
  // pure virtual function
	virtual void GetName() = 0;
};
```

- c++ doesn't have a keyword called `interface` it just a class with pure virtual function
- U cannot make instances of base class that have pure virtual functions
- U cannot make instances of subclass class that extend base class that have pure virtual functions until u impl all pure functions in it

# Visibility in C++

- Concept that is related to OOP
- How visible certain members or methods of a class actually are
- Visible mean who can see them oe call them or use them

## Three basic visibility modifiers in c++

- private
- protected
- public

## private

- mean members can be only access inside class or struct scope
  - `friend` keyword u can label class or a function as friend and u can access private member
- default in class | `public` default in struct

## protected

- mean members can be only access inside class or struct scope and subclasses that inherits from this class

  - `friend` keyword u can label class or a function as friend and u can access private member

# Arrays in C++

- Pointers are the basis of how arrays work in c++

```c++
type array_name[array_size];
```

- Zero based index
- u can write to it

```c++
type array_name[array_size];
array_name[index] = value;
```

- If u print `array_name` it self it will give u the memory address

  - as it actually a pointer type

- If u try to access an index which not exist or out the array size

  - that will cause something called a memory access violation

- array store data contiguously store data in a row

- again array is just an integer pointer
  - access array by index is just offset the pointer by this value
  - the number u add to offset is depend on array type
  - for the array of int example when offset by 2 and when the int is 4 byte `2*4`
  - u can directly deal with bytes by some casting

```c++
int list[5];
list[2] = 3;

int* ptr = list;
*(ptr + 2) = 3;

// using bytes
/* since u want to deal with byte
*  u must cast it to a data type with 1 byte size like [char]
*  now u must modify offset to be 8
*
*  Then as u want to assign value 3 which is integer
*  u must cast pointer again to an integer pointer
*/
*(int*)((char*)ptr + 8) = 3;
```

- u can create array on heap using `new` keyword
  - can cause indirect
  - ..

```c++
int* list = new int[5];
```

- create your array on the stack
- c++ 11 introduce standard array
  - includes bounds checking
  - keep tracking size of the array
- raw array is faster and dangerous
- standard array are safer

# How Strings Work in C++ (and how to use them)

## char

- char | 1 Byte
  - cast pointer to a char pointer so you can do pointer arithmetic in term of bytes
  - allocating memory buffers for example if you want to allocate one kilobyte of memory u can allocate 1024 char
  - strings and text

## string

- array of char
- c style

```c++
const char* name = "Hello";
```

- despite we use `char*` we don't need to `delete`

  - don't `delete` when u doesn't use `new` keyword

- null termination character

  - to know that string has ended
  - `0`
  - `'\0'`

- `''` char
- `""` char pointer

### standard library

- class called `string`
- `basic string` template class
- `std::string` templated version of `basic string` class
  - templated with char
  - char is the underline data for each character
- `wstring` for wide string

```c++
#include <iostream> // contain definition for string
#include <string>  // impl << | and have functions
```

## string manipulating

- to add string to another
  - ```c++
    std::string name = std::string("first") + "second";
    ```
  - ```c++
    std::string name = "first" ;
    name += "second";
    ```
- check if string contain char or word

  - ```c++
    bool contains = name.find("st") != std::string::npos;
    ```
  - `name.find("st")` return position of "st"
  - `std::string::npos` illegal position

- [c++ string](https://cplusplus.com/reference/string/string/)
- when u pass string to function using `printMe(std::string text)` u make a copy of that string
  - meaning anything u do to string won't affect the original one
  - less faster

```c++
void printMe(std::string text)
{
  std::cout<<text<<"\n";
}
```

- if u want to make the string as readonly pass it using const reference

```c++
void printMe(const std::string& text)
{
  std::cout<<text<<"\n";
}
```

## pointer arithmetic

Pointer arithmetic is a way to perform arithmetic operations on pointers in C++ and other programming languages that support pointers.

Pointer arithmetic allows you to manipulate the memory addresses stored in pointers, which can be useful for traversing arrays, manipulating linked lists, and other operations that involve accessing memory.

Pointer arithmetic in C++ is based on the size of the data type that the pointer is pointing to. When you perform pointer arithmetic, the address stored in the pointer is incremented or decremented by a certain number of bytes, depending on the size of the data type. For example, if you have a pointer to an integer, incrementing the pointer will cause its value to increase by the size of an integer (typically 4 bytes on most systems).

Here's an example of how pointer arithmetic can be used to access elements of an array:

```c++
int arr[] = {1, 2, 3, 4, 5};
int *p = arr; // p points to the first element of arr

for(int i = 0; i < 5; i++) {
    cout << *p << " "; // print the value pointed to by p
    p++; // increment p to point to the next element of arr
}

```

## comments on video

- Василь Зорич | 4 years ago (edited)
  <br>
  Please what is the difference between:

```c++
char* a = "Cherno";
a[2] = 'a';
// output is:error
```

and

```c++
char* a = "Cherno";
a = "Charno";
std::cout << a;
// output is:Charno
```

- Mario Galindo Queralt | 4 years ago (edited)
  <br>
  `Стефан Рибак` In the second alternative, you aren't changing the memory the pointer "a" points to. You are changing the value of the pointer "a" to point to other place that contains other char string (with the same letters). I think this could seems difficult, so I'll try to explain better:

```c++
char* a = "Cherno";
// creates a pointer "a" that points to a memory that contains the letters "Cherno".
```

```c++
a = "Cherno";
// change the value of the pointer "a" to point to other memory that also contains the letters "Cherno".
```

So, later you can also do

```c++
a = "A big string like this";
// and it will work too, because "a" will point now to a new memory.
// The old memories with "Cherno" will remain unchanged somewhere in memory.
```

You must not change any value of the C-String-Literal! - But I did. or not
Thanks

# String Literals in C++

- A series of characters in between two double quotes

```c++
"string"; // const char* | length 7 because of null termination
```

- `strlen()` get string length

## note

```c++
const char* txt01 = "string"; // utf8
const char* txt02 = u8"string";
```

## from c++ 11 and above

```c++
const wchar_t* txt03 = L"string";  // 2 byte per  | differ depend on compiler
const char16_t* txt04 = u"string"; // 2 byte per char | utf16
const char32_t* txt05 = U"string"; // 4 byte per char | utf32
```

## from c++ 14

- `""s` => `s` operator function return a standard string

```c++
using namespace std::string_literals;

// std::string txt = "first" + "second" //error
std::string txt = "first"s + "second"
```

## `R""` => ignore escape character

- we can for example make multiline string

In C++, the R"txt" syntax is called a raw string literal. The R stands for "raw", which means that the string is interpreted literally without any special meaning to escape sequences such as \n or \". This can be useful when you want to include special characters or escape sequences within a string without having to escape them manually.

```c++
const char* txt = R"";
const char* txt2 = R"
01- .....
02- .....
03- .....
04- .....
";
// alternative
const char* txt2 = "01- .....\n"
"02- .....\n"
"03- .....\n"
"04- .....";
```

## ..

- String Literals always stored in readonly memory

- [watch this video again ^\_^](https://www.youtube.com/watch?v=FeHZHF0f2dw&list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb&index=33)

# CONST in C++

- A fake keyword
- It just a promise that u won't change this data
  - but u can bypass that
  - u can break that promise ^\_^

## const with pointers

- const before pointer `before asterisk *`
  - u can't change the value `content in that address`
  - but u can change the pointer itself `change what pointer refer to`

```c++
// first way
const type* var_name

// second way
type const* var_name
```

```c++
const int b = 5;
const int* a = new int;
*a = 7; //not valid code
a = &b; //valid code
```

- const after pointers type
  - u can change the value `content in that address`
  - but u can't change the pointer itself `change what pointer refer to`

```c++
type* const var_name
```

```c++
const int b = 5;
const int* a = new int;
*a = 7; //valid code
a = &b; //not valid code
```

## const with method and classes

### in classes

- when u mark method as const
  - I promise that this method won't change any member of this class
  - readonly method
  - useful with getter method as it only read data from class
  - u can call this method when it passed to `const reference`
    - this why u can see two version of getter one with const and one without
  - always `always` mark your method as const when it doesn't change the class or if they not supposed to modify the class

```c++
return_type method_name() const
{

}
```

```c++
class Entity{
  private:
  int m_x,m_y;
  public:
  int GetX() const
  {
    // m_x = 7 ; // u can't do that
    return m_x;
  }
}
```

- what if I need to change a variable of the class from const method?
  - u can mark this variable as `mutable`

```c++
class Entity{
  private:
  int m_x,m_y;
  mutable int var;
  public:
  int GetX() const
  {
    // m_y = 8; // not valid
    var = 7 ; // valid
    return m_x;
  }
}
```

- when member of class is pointer

```c++
class Entity{

  private:

  int* m_x,m_y;

  public:

  /*
  * this mean this function will
  * return a constant pointer
  * its content won't change
  * the pointer itself won't change
  * this method won't change any thing of this class member
  * it's a readonly method
  */
  const int* const GetX() const
  {
    // m_x = 7 ; // u can't do that
    return m_x;
  }
}
```

- Be aware

```c++
  /*
  * this mean m_x is an int pointer
  * m_y is a normal int
  */
  int* m_x,m_y;

  /*
  * this mean both m_x and m_y is an int pointer
  */
  int* m_x,*m_y;
```

# The Mutable Keyword in C++

- Two uses
  - with const
  - with lambda

## mutable with const

```c++
class Entity{

  private:
  std::string m_name;
  mutable int var;

  public:
  const std::string& GetName() const
  {
    var = 7 ; // valid
    return m_name;
  }
}
```

## mutable with lambda

- lambda is a little throwaway function u can write and assign to variable quickly

  - `[capture method]` u can pass variables from current scope to lambda from`[]`
  - `[a]` => passing a by value
  - `[&a]` => passing a by reference
  - `[=]` => passing all variables in scope by value
  - `[&]` => passing all variables in scope by reference

- when passing variables by value u can't change them in lambda
  - and here come `mutable` keyword `[=]() mutable`
  - this mean u can now change the variables passing by value
  - this applied if u want to make it `pass by value` otherwise u can `pass by reference` and u don't need `mutable`

```c++
int main()
{
  int a = 0;
  auto func = []()
  {
    std::cout<< "I'm a lambda"<<"\n";
  };

  func();
}
```

# Member Initializer Lists in C++ (Constructor Initializer List)

- It's all about initialize class members
- there are two ways to do that in c++

## normal way

```c++
class Entity{

  private:
  std::string m_name;

  public:

  Entity(){
    m_name = "None";
  }

  Entity(const std::string& name){
    m_name = name;
  }

  const std::string& GetName() const
  {
    return m_name;
  }
}
```

## Member Initializer Lists

- always list member list in order of class members declaration order
- use them everywhere `why?`

  - because when using normal way the member created two time on from init and the other from constructor `not the case in primitive type`
  - but using member initializer list it created once

- comments

  - **Charisma | 5 years ago**
    <br>
    Also you cant initialize const members without using "Member initializer".
  - **Josh Stephenson | 5 years ago**
    <br>
    Don't forget Member Initializer Lists can also be used for initializing const member variables as well!

  - **Delta Rambo | 2 years ago**
    <br>
    Basically, all data-members which should be initialized at time of declaration, such as const , references, etc., must be included in the constructor's initializer list.

```c++
class Entity{

  private:
  std::string m_name; // first
  int m_score;        // second

  public:
  Entity()
      :m_name("None"),m_score(0)
  {
  }

  Entity(const std::string& name,int& score)
      :m_name(name),m_score(score)
  {
  }

  const std::string& GetName() const
  {
    return m_name;
  }
}
```

# Ternary Operators in C++ (Conditional Assignment)

- summary syntax for if else

- Ternary syntax

```c++
condition ? if_true : if_false
```

- Example

```c++
if(temp > 30)
  status = "hot";
else
  status = "cold";
```

```c++
status = temp > 30 ? "hot" : "cold";
```

## comments

- **Jon Snow | 2 years ago**
  <br>
  A better way to write this kind of nested conditional at 4:50 is:

```c++
s_speed = s_level > 10 ?  15 :
          s_level >  5 ?  10 :
                            5;
```

An old school C trick that with proper indentation makes the nested ternary assignment very nice to read and more readable than if...else if...else

- **Andrew Esh | 3 years ago**
  <br>
  You missed my favorite use of the ternary operator: conditional argument passing. You can use the ternary in the list of arguments to a function or method call like this:

```c++
SetSpeed(s_Level > 5 ? 10 : 5);
```

So the ternary is not just a replacement for an if statement. It can be used in places an if statement can not.

# How to CREATE/INSTANTIATE OBJECTS in C++

- we have to option to instantiate our object
  - it depend on which memory it's going to occupy
- At least when need one byte of memory for class even if we have an empty class

```c++
class Entity
{
private:
	String m_name;
public:
	Entity(): m_name("none") {};

	Entity(const String& name): m_name(name) {};

	const String& GetName() const{
		return m_name;
	}

};
```

## stack and heap

- there are other section in memory for example where our source code live

### stack objects

- have automatic lifespan
- their lifetime controlled by the scope that they declared
- as soon as the variable go out of the scope the memory is free `stack pops`

- How to init on stack?

```c++
/*
* this way we create the object entity on stack
* don't think this is not initialized it does
* because we have a default constructor [e] was initialized using it
* so it's a valid code
*/
Entity e;

// u can also make this way and it's the same
Entity e1 = Entity();

// =======================

// If u want to specify parameters
// u can make this
Entity e2("AA");

// or this way and it's the same
Entity e3 = Entity("AA");
```

- when not to init on stack?
  - when object is too large
  - when we have too many objects
  - stack is usually smaller it is `1megabyte` or `2megabyte`
    - depend on platform and compiler

### Heap

- a bit big mysteries place
- if u create object in heap it will set there until u decide to free it
- How to init on heap?
  - `new` keyword => return a `pointer` to object in heap

```c++
Entity* e = new Entity();

// or | we don't need to make () for default constructor
Entity* e1 = new Entity;

// =======================

// If u want to specify parameters
// u can make this
Entity* e2 = new Entity("AA");
```

- cons
  - allocating on heap take longer than allocating in stack
  - u have free memory manually when u finish with it
    - ```c++
      delete var_name;
      ```

## Note

- when using string don't use

  ```c++
  using namespace std;
  ```

  - use
    ```c++
    using String = std::string;
    ```

- differences between `using` and `#define`

```c++
 using String = std::string;
//  is a type alias that creates a new name for an existing type,
```

while

```c++
#define String std::string;
// is a macro that replaces all occurrences of String with std::string;
// and can have some potential drawbacks.
```

## scope

- can be a function

```C++
type name(){
  // CODE
}
```

- If statement

```C++
if(/*condition*/)
{
  // CODE
}
```

- for loop

```C++
for(;;)
{
  // CODE
}
```

- empty scope

```c++
{
  // CODE
}
```

so scope not just a function

## wrap up

- Is object is too big?
- Do i want explicitly control the life time of the object?
- If your answer no => allocate on the stack
  - it's way better
  - it's automated
  - it's faster
- If your answer yes => allocate on the heap
  - u have manually free memory with delete
  - if u forget to free can cause memory leak
  - u can use `smart pointers`

# The NEW Keyword in C++

- The main purpose of `new` is to allocate memory on the heap specifically
- `new` is just an operator like `+` or `*` etc..
- u can overload operators or change its behavior
- usually what `new` does underline is calling the c function `malloc(size)` to allocate memory
  - calling constructor
- Don't forget to call `delete` to free memory
  - what `delete` does underline is calling the c function `free(var);`
  - it also calling destructor
  - if u use `new` with `[]` => `var = new Object[]` use `delete[] var`
- `new` support something called placement
  - which is a way to construct an object in a pre-allocated memory block.
  - `new(pointer) Object()`

## So How it do that?

1. Based on what u have write it determines the necessary size of the allocation in bytes
2. And then is ask the operating system `I want this size of memory`
3. Now we need to find a contiguous block of memory of that size
   - it doesn't search all memory where this size exist
   - there is something called `free list` which maintain addresses that have bytes free
4. When it find that place it return a pointer for that address

```c++
int a = 5; // allocate 4 bytes on stack

// =======================================

int* b = new int; // allocate 4 bytes on heap
int* c = new int[50]; // allocate 50*4 = 200 bytes on heap

// =======================================

/*
* allocate the size of Entity on heap
* we not just allocating that memory
* we also call the default constructor
*/
Entity* d = new Entity;
Entity* d1 = new Entity();

// purely allocating the memory without calling the default constructor
Entity* d2 = (Entity*)malloc(sizeof(Entity));

// =======================================

// allocate 50 times the size of Entity on heap
// don't allocate like that in c++
Entity* e = new Entity[50];

// =======================================

delete a;
delete b;
delete[] c;
delete d;
delete d1;
delete d2;
delete[] e;
```

# Implicit Conversion and the Explicit Keyword in C++

- Implicit mean automatic
- c++ do one implicit conversion on your code

```c++
using String = std::string;

class Entity
{
private:
	String m_name;
  int m_age;
public:
	Entity()
  : m_name("none") {};

	Entity(const String& name)
  : m_name(name), m_age(-1) {};

	Entity(int age)
  : m_name("none"), m_age(age) {};

	const String& GetName() const{
		return m_name;
	}
};
```

- Implicit init

```c++
Entity e("Ali");
Entity b(23);

// u can do like this

Entity e = "Ali";
Entity b = 23;
```

```c++
void printEntity(const Entity& e)
{
  // code
}

printEntity(23);

/*
* won't work because it expect to provide std::string
* and "ali" is a char array
* so it need first converted to std::string
* then need to be converted to Entity with the string constructor
* c++ do one implicit conversion so it won't work
*/
// printEntity("Ali");

// here will do one implicit from std::string to Entity
printEntity(std::string("Ali"));
// here will do one implicit from char array to std::string
printEntity(Entity("Ali"));
```

## explicit

- prevent implicit conversion mean u should explicitly make the calling

```c++
using String = std::string;

class Entity
{
private:
	String m_name;
  int m_age;
public:
	Entity()
  : m_name("none") {};

	Entity(const String& name)
  : m_name(name), m_age(-1) {};

	explicit Entity(int age)
  : m_name("none"), m_age(age) {};

	const String& GetName() const{
		return m_name;
	}
};
```

now we can't do that

```c++
Entity a = 22; // wrong code
```

what u can do now is

```c++
Entity a(22); // valid | normal init
Entity a = Entity(22); // valid | normal init

Entity a = (Entity)22; // valid | casting
```

- cherno usually use
  - in math library
  - low level wrapper

# OPERATORS and OPERATOR OVERLOADING in C++

- `OPERATOR` symbol that we use instead of function to do something

  - `->` `*` `<<` `>>` `&` `+=` `new` `delete` etc..
  - `,` `()`

- overloading is to change the way this operator work or give it a new meaning

- [Operators Reference](https://en.cppreference.com/w/cpp/language/operators)

- If other go to your definition of operator overloading u have use it wrong

- How to implement it?
  - write the operator u want after `operator` keyword => for example `operator*` `operator+`

```c++
  returnType operator+ (params)
  {
    // code
  }
```

- implementation
  - cherno recommended style

```c++
struct Vector2
{
  float x,y;

  Vector2(float x, float y)
      : x(x), y(y) {}

  Vector2 Add (const Vector2& other) const
  {
    return Vector2(x + other.x , y + other.y);
  }

  Vector2 operator+ (const Vector2& other) const
  {
    return Add(other);
  }
}
```

- In the the previous code the + operator call the add method
- U can do the opposite to make the add function to call plus operator

- with `this` keyword

```c++
struct Vector2
{
  float x,y;

  Vector2(float x, float y)
      : x(x), y(y) {}

  Vector2 Add (const Vector2& other) const
  {
    return *this + other;
  }

  Vector2 operator+ (const Vector2& other) const
  {
    return Vector2(x + other.x , y + other.y);
  }
}
```

- with address operator plus like a function

```c++
struct Vector2
{
  float x,y;

  Vector2(float x, float y)
      : x(x), y(y) {}

  Vector2 Add (const Vector2& other) const
  {
    return operator+(other);
  }

  Vector2 operator+ (const Vector2& other) const
  {
    return Vector2(x + other.x , y + other.y);
  }
}
```

- Same way u can implement multiply

```c++
struct Vector2
{
  float x,y;

  Vector2(float x, float y)
      : x(x), y(y) {}

  Vector2 Add (const Vector2& other) const
  {
    return Vector2(x + other.x , y + other.y);
  }

  Vector2 operator+ (const Vector2& other) const
  {
    return Add(other);
  }

  Vector2 Multiply (const Vector2& other) const
  {
    return Vector2(x * other.x , y * other.y);
  }

  Vector2 operator* (const Vector2& other) const
  {
    return Multiply(other);
  }
}
```

## How to use

```c++
Vector2 pos(10.f, 20.f);
Vector2 speed(5.f, 5.f);
Vector2 powerUp(1.1f, 1.1f);

Vector2 result01 = pos.Add(speed.Multiply(powerUp)); // with functions
Vector2 result02 = pos +   speed *        powerUp;   // with operator overload
```

## `<<` left shift operator | to print to console

- `ostream` output stream

```c++
/*
* [std::ostream&] original definition to left shift operator
* [stream] reference to cout
*
*/
std::ostream& operator<< (std::ostream& stream, const Vector2& other)
{
  steam << other.x << ", " << other.y;
  return stream;
}
```

## `==` equality operator

```c++
/*
* [std::ostream&] original definition to left shift operator
* [stream] reference to cout
*
*/
{

  bool operator== (const Vector2& other) const
  {
    return x = other.x && y = other.y;
  }

  bool operator!= (const Vector2& other) const
  {
    // return !operator==(other); // looks weird
    return !(*this == other);
  }

}
```

## Note

- `this` keyword is a pointer for the class

# The "this" keyword in C++

- only accessible through a member function
  - a function that belong to a class
- `this` pointer to current object instance that the method belongs to

```c++
class Entity
{
  public:
   int x,y;

   Entity(int x, int y)
   {
    Entity* e = this;
    // Entity* const e = this;
    e->x = x;
    e->y = y;
   }
}
```

```c++
class Entity
{
  public:
   int x,y;

   Entity(int x, int y)
   {
    this->x = x;
    this->y = y;
   }
}
```

```c++
class Entity
{
  public:
   int x,y;

   Entity(int x, int y)
   {
    (*this).x = x;
    (*this).y = y;
   }
}
```

- In const method `this` not only a pointer to the instance but a const pointer
  - because in const function we aren't allowed to change class member
  - and by being a const pointer we now aren't able to change the content of it

```c++
{
  int GetX() const
  {
    // Entity* e = this; // error
    const Entity* e = this;
  }
}
```

- `this` useful when we for example want to pass the current instance to function from outside our class

```c++
void doSomething(const Entity& entity)
{
  // code
}

void doSomethingElse(Entity* entity)
{
  // code
}

class Entity
{
  public:
   int x,y;

   Entity(int x, int y)
      : x(x), y(y)
   {
    doSomething (*this);
    doSomethingElse (this);
   }
}
```

# Object Lifetime in C++ (Stack/Scope Lifetimes)

- Lifetime for stack based variables

```
  _______________
  |  Stack 03   | <== write data to the stack
  _______________
  |  Stack 02   |
  _______________
  |  Stack 01   |
___________________
|                 |
```

- when the app terminated all memory become free

- when the stack variable out of its scope its memory free

```c++
int* createArray()
{
  int array[50];
  return array; // wrong code
}
// solution
int* createArray()
{
  int* array = new int[50]; // allocate it on heap
  return array;
}


int main()
{
  int* a = createArray(); // it will fail
}
```

- [watch the video](https://www.youtube.com/watch?v=iNuTwvD6ciI&list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb&index=43)

## remember again scope

- can be a function

```C++
type name(){
  // CODE
}
```

- If statement

```C++
if(/*condition*/)
{
  // CODE
}
```

- for loop

```C++
for(;;)
{
  // CODE
}
```

- empty scope

```c++
{
  // CODE
}
```

- class also have a scope

```c++
class Entity
{
  private:
    int x;
}
```

so scope not just a function

## use cases

- timer
- mutex locking

# SMART POINTERS in C++ (std::unique_ptr, std::shared_ptr, std::weak_ptr)

- `new` allocate on heap and then by calling `delete` it free the memory

  - smart pointers came to automate that process
  - when u call `new` u don't have to call `delete`
  - also in many cases u don't even need to call `new`

- include `memory`

```c++
#include <memory>
```

## unique pointer

- scoped pointer when the scope end it will free the memory
- they have to be unique
- u can't copy a unique pointer
- `std::unique_ptr<template_Arg>`

```c++
{
  std::unique_ptr<Entity> entity(new Entity());
  // std::unique_ptr<Entity> entity = new Entity(); // not allowed as it explicit constructor
}
```

- the preferred way
  - due to exception safety
  - if the constructor throw an exception u won't end up having a dangling pointer with no reference and cause memory leak

```c++
{
  std::unique_ptr<Entity> entity = std::make_unique<Entity>();
}
```

- stack allocated pointer
- the problem with this u can'y copy or share or pass to a function

```c++
{
  std::unique_ptr<Entity> entity = std::make_unique<Entity>();

  /*
  * in [unique_ptr] class the definition of assign was deleted
  * u can't copy instances
  */
  // std::unique_ptr<Entity> entity1 = entity; // not allowed
}
```

## shared pointer

- use something called reference counting
  - u keep tracking of how many references u have to your pointer
  - as soon as this count reach there it gets deleted
- `std::shared_ptr<template_Arg>`

- shared pointer not just allocate our object but also allocate a control block to track references count
  - when u call `std::make_shared` it allocate our object and the control block together which is a lot more efficient

```c++
/*
* If u init like that
* it will allocate your object
* then it will allocate the control block
* and this is two allocation
*/
std::make_shared<Entity> entity(new Entity());
```

```c++
std::shared_ptr<Entity> entity = std::make_shared<Entity>();
```

- when u copy shared pointer to another shared pointer the `references count` increase by one

## weak pointer

- when u assign shared pointer to weak pointer it won't increase the references count

```c++
std::shared_ptr<Entity> entity = std::make_shared<Entity>();
std::weak_ptr<Entity> e = entity;
```

- this is good if u won't to take ownership of the entity
  - check if it's alive
  - it won't keep it alive

```c++
int main(){
  {
    std::weak_ptr<Entity> e0;
    {
      std::shared_ptr<Entity> entity = std::make_shared<Entity>();
      entity = e0;
    } // e0 will be died after exist the first scope
  }
}
```

## use cases of pointer

- u should try use them all the time
  - they automate the memory management
  - prevent memory leaking by forgetting to call delete
- shared pointer have overhead as it has counting system

# Copying and Copy Constructors in C++

- copy data `memory` from one place to another
- when copying object c++ take all parameters and assign it to the copied one
- c++ provide u a default copy constructor

```c++
Class_name(const Class_name& other);
```

```c++
Class_name(const Class_name& other)
{
  memcpy(this, &other, sizeof(Class_name));
}
```

- u can prevent copying by deleting this constructor

```c++
Class_name(const Class_name& other) = delete;
```

- always pass your object by const reference

# The Arrow Operator in C++

- a shortcut for dereferencing

```c++
class Entity
{
  public:
    void Print() const
    {
      std::cout << "Hello!" << std::endl;
    }
};
```

```c++
int main()
{
  Entity e;
  e.Print();

  Entity* ptr = &e;

  Entity& entity = *ptr;
  entity.Print();

  (*ptr).Print();
}
```

- with arrow operator

```c++
int main()
{
  Entity e;
  e.Print();

  Entity* ptr = &e;

  ptr->Print();
}
```

- u can override it same as any operator

```c++
class Entity
{
  public:
    void Print() const
    {
      std::cout << "Hello!" << std::endl;
    }

    Entity* operator-> () const
    {
      return /**/;
    }

    const Entity* operator-> () const
    {
      return /**/;
    }
};
```

- u can use it to get offset of each member in memory
  - useful when serializing data into a stream of bytes and u want to figure out offset of cretin things

```c++
struct Vector3
{
  float x, y, z; // the order of declaration will be the same in memory
}

int main()
{
  // start from zero
  //  using 0 or nullptr
  int offsetX = (int)&((Vector3*)0)->x ;
}
```

# Dynamic Arrays in C++ (std::vector)

- [Why it called vector?](https://stackoverflow.com/questions/581426/why-is-a-c-vector-called-a-vector)
- It should be called an `arrayList`
- unlike array this can resize
- [EASTL](https://github.com/electronicarts/EASTLs)
- to make one

```c++
struct Vertex {
  float x, y, z;
}
```

```c++
std::vector<Vertex> vertices;
```

- to add to it

```c++
vertices.push_back({1, 2, 3});
vertices.push_back({4, 5, 6});
vertices.push_back({7, 8, 9});
```

- to get size of elements in it
  - u can use `.size()

```c++
std::out<< vertices.size()<< "\n";
```

- range based loop

```c++
// this code make a copy of vertex in for loop scope
for (Vertex v: vertices)
{
  std::out<< v << "\n";
}

// to avoid that we use &
for (Vertex& v: vertices)
{
  std::out<< v << "\n";
}
```

- to clear it we use
  - `.clear()`

```c++
vertices.clear();
```

- to erase specific index
  - `.erase(iterator)

```c++
// to erase the second element | index 1
vertices.erase(vertices.begin() + 1);
```

# Optimizing the usage of std::vector in C++

- Know your environment

- When push back element to vector by init directly when make a copy of it
- as we push back to vector it keep resizing to fit elements and this way we copying element each time vector extend

```c++
int main(){
  std::vector<Vertex> vertices;
  vertices.push_back(Vertex(1, 2, 3)); // init vertex copying to vertices | copying to resize
  vertices.push_back(Vertex(4, 5, 6)); // init vertex copying to vertices | copying to resize
  vertices.push_back(Vertex(7, 8, 9)); // init vertex copying to vertices | copying to resize
}
```

- so if we somehow tell vector that I'm going to push back 3 elements I'll prevent these copies
- we can do that using `.reserve(size)`

```c++
int main(){
  std::vector<Vertex> vertices;
  vertices.reserve(3);
  vertices.push_back(Vertex(1, 2, 3)); // init vertex copying to vertices
  vertices.push_back(Vertex(4, 5, 6)); // init vertex copying to vertices
  vertices.push_back(Vertex(7, 8, 9)); // init vertex copying to vertices
}
```

- now I want to pass vertex to vertices vector without copying
- u can use `emplace_back` this take parameters of vertex and tell vector to construct a vertex

```c++
int main(){
  std::vector<Vertex> vertices;
  vertices.reserve(3);
  vertices.emplace_back(1, 2, 3);
  vertices.emplace_back(4, 5, 6);
  vertices.emplace_back(7, 8, 9);
}
```

# Local Static in C++

- `static` keyword in local scope
- We have two things to take in consideration
  - first is the lifetime which mean how long our variable we be in memory before deleted
  - second is the scope which mean the accessability og the variable
- we mark variable as static in a scope this mean that the variable will have the lifetime of our program but can only accessed from that scope

```c++
void Test(){
  static int count_call = 0;
  count_call++;
  std::cout<<count_call<< std::endl;
}

// ====================================

Test(); // 1
Test(); // 2
Test(); // 3
```

- is the same if u do that
  - but now u can call count anywhere

```c++
int count_call = 0;

void Test(){
  count_call++;
}

// ====================================

Test(); // 1
Test(); // 2
Test(); // 3
```

```c++
int count_call = 0;

void Test(){
  count_call++;
}

// ====================================

Test(); // 1
count_call = 10;
Test(); // 11
Test(); // 12
```

- Make singleton class without static in scope

```c++
class Singleton
{
  private:
    static Singleton* s_Instance;

  public:
    static Singleton& Get()
    {
      return s_Instance;
    }

    void Hello(){}
};

Singleton* Singleton::s_Instance = nullptr;

int main(){
  Singleton::Get().Hello();
}
```

- Make singleton class with static in scope

```c++
class Singleton
{
  public:
    static Singleton& Get()
    {
        static Singleton instance;
        return instance;
    }

    void Hello(){}
};

int main(){
  Singleton::Get().Hello();
}
```

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

# Making and Working with Libraries in C++ (Multiple Projects in Visual Studio)

- Create game solution
- Create Engine Solution
- Make `src` folder ro each project
- For all platforms and targets
  - configure `engine` output to static library for
  - configure `game` output to `.exe` for windows

## How to link

- Add path of our engine `src` to game properties
  - go to c++/c
    - if not exist make sure that there is `.cpp` file in your solution
  - go to general
  - go to additional include add `include` path of the library
    - make path relative to project folder
- U can use relative path to include files `#include "../../----"` instead of pervious step but don't do that
- Now we need to link `.lib` from engine project
- u can do this from
  - `Using Libraries in C++ (Static Linking)`
- But the beat way as this project inside our solution is to add reference to `engine` to `game` project
  - right click
  - add
  - add reference
  - mark engine solution
- this is the best approach as it will rebuild engine project if it has changes

# How to Deal with Multiple Return Values in C++

- make a struct with things u want to return
- pass output by reference to the function
  - Prefix parameters with `out`
- pass output by pointer to the function
  - Prefix parameters with `out`
- if returned value have the same type u can go with
  - string list `std::string[2]`
  - standard array `std::array<std::string,2>` => include `<array>`
  - vector `std::vector<std::string>` => include `<vector>`
- u can use tuples
  - include `<utility>`
  - include `<functional>`
  - `std::tuple<std::string, std::string>`
  - `std::make_pair(a, b)`
  - `std::get<index>(tuple)`

## comment

- AlguienMasRaro | 1 year ago
  <br>
  For anyone reading recently, there's a better way with structured binding since c++17:
  <br>
  Return a tuple of your choice and return it as per the video:

```c++
std::tuple<std::string, std::string, int> getData() {
    return { "One", "two", 3 };
}
```

Retrieve values using structured binding:

```c++
auto [str1, str2, number] = getData();
```

# Templates in C++

Templates in C++ are a powerful feature that allows you to write generic code that can work with different data types. A template is a blueprint or a pattern that is used to create a generic class or function.

```c++
void print(int val)
{
  std::cout<< val << std::endl;
}

void print(std::string val)
{
  std::cout<< val << std::endl;
}

void print(float val)
{
  std::cout<< val << std::endl;
}
```

```c++
int main(){
  print(3);
  print("hi");
  print(3.5f);
}
```

- with templates

```c++
template <typename T>
void print(T val)
{
  std::cout<< val << std::endl;
}
```

```c++
int main(){
  print(3);
  print("hi");
  print(3.5f);

  // ==================
  print<int>(3);
  print<std::string>("hi");
  print<float>(3.5f);
}
```

- Template is not exist until u call it
- Template is not limited to types or functions

```c++
template<int N>
class Array{
  private:
    int m_Array[N];
  public:
    int GetSize(){return N;}
}
```

```c++
Array<5> arr;
```

- you shouldn't go so far with it

## use cases

- for example
  - logging system
  - material system for rendering graphics

# Stack vs Heap Memory in C++

- stack has predefined size usually 2mb
- heap also kind have a predefined value but can grow and change as application go
- Both stack and heap are in ram
- the difference is how they allocate that memory

```c++
// Stack
int val = 5;

// Heap
int* hVal = new int;
*hVal = 5;
```

```c++
// Stack
int array[5];
array[0] = 1;
array[1] = 1;
array[2] = 1;
array[3] = 1;
array[4] = 1;

// Heap
int* hArray = new int[5];
hArray[0] = 1;
hArray[1] = 1;
hArray[2] = 1;
hArray[3] = 1;
hArray[4] = 1;
```

```c++
struct Vector3
{
  float x, y, z;

  Vector3()
      : x(10), y(11), z(12) {}
}

// Stack
Vector3 vec3;

// Heap
Vector3* hVec3 = new Vector3();
```

- with stack we stack values on each other in memory
  - one cpu instruction
  - move stack backwards with bytes and return pointer to the beginning of that location
  - in stack variable next to each others
- if u use smart pointers it will call `new` for you
- don't forget to call delete for heap allocated variables
  - smart pointers do that for you
- allocation on heap is a cost while stack is one cpu instruction
- allocate on stack as u can

[For more | Youtube video](https://www.youtube.com/watch?v=wJ1L2nSIV1s&list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb&index=54)

## comment

- The Cherno | 5 years ago
  <br>
  Hope you guys enjoyed the video! A few notes:
  - to be clear, each program/process on our computer has its own stack/heap
  - each thread will create its own stack when it gets created, whereas the heap is shared amongst all threads

# Macros in C++

- first stage before compiler is the `preprocessor`
  - any statement with hash `#`
- and then the code passed to compiler for actual compilation

- the preprocessor stage is basically a text editing stage
  - we make some macros that replaces text in our code with something else
  - preform find and replace
  - can have parameters and arguments not just a basic find and replace
- `;` semicolon if dose't have statement before it considered it has an empty statement

```c++
{
  ; //empty statement
}
```

- using params

```c++
#define LOG(x) std::cout<< x << std::endl

int main()
{
  LOG("Hello");
}
```

- Logging take time
- To add preprocessor

  1. open project properties
  2. go to c++/c
  3. go to preprocessor
  4. preprocessor definitions
  5. for example add `PR_DEBUG` in debug mode or u can do this way `PR_DEBUG=1`
     - don't make spaces between like that `PR_DEBUG = 1` this is wrong

- u could for example add preprocessor one in debug and one in release
  - and use that in your code to modify behavior depend on the mode your are in

```c++
#ifdef PR_DEBUG // valid but not the best
#define LOG(x) std::cout << x << std::endl
#else
#define LOG(x)
#endif

int main()
{
  LOG("Hello"); // debug to console in debug mode only
}
```

- recommended

```c++
#if PR_DEBUG == 1 // recommended
#define LOG(x) std::cout << x << std::endl
#else
#define LOG(x)
#endif

int main()
{
  LOG("Hello"); // debug to console in debug mode only
}
```

- u can also use else if

```c++
#if PR_DEBUG == 1 // recommended
#define LOG(x) std::cout << x << std::endl
#elif defined(PR_RELEASE)
#define LOG(x)
#endif

int main()
{
  LOG("Hello"); // debug to console in debug mode only
}
```

- u can also customize `PR_DEBUG` directly from code by using `#define`

```c++
#define PR_DEBUG 1 // or make it 0
```

- u can also use `#if` to disable a block of code like this

```c++
#if 0

// any code u want
// any code in this scope will be dead
// :(

#endif
```

- u can use backslash to multiline macros

```c++

// for example this code
int main()
{
  std::cout << "Hello" << std::endl;
  std::cin.get();
}

// u can write like that
#define MAIN int main()\
{\
  std::cout << "Hello" << std::endl;\
  std::cin.get();\
}

MAIN // call it
```

- u can use macro with `new` to get size of allocation in which line and in what file

```c++
| 01 |  #include <iostream>
| 02 |
| 03 |  #define NEW(size) \
| 04 |      (std::cout << "Allocating " << size << " bytes in " << __FILE__ << " at line " << __LINE__ << "\n", \
| 05 |      new char[size])
| 06 |
| 07 |  int main() {
| 08 |      char* p = NEW(100);
| 09 |      return 0;
| 10 |  }
```

```c++
// out
// Allocating 100 bytes in test.cpp at line 8
```

# The "auto" keyword in C++

- Make compiler to deduce variable ot return type for you

```c++
int a = 5;
auto b = a; // b is an int type
```

```c++
std::string val(){
  return "Value";
}

auto name = val(); // name is std::string type
```

- u can use it with long type

```c++
std::vector<std::string> val(){
  return "Value";
}

std::vector<std::string>  name = val(); // name is std::string type

// using auto
auto  name0 = val(); //

// using using
using nameVector = std::vector<std::string>;
nameVector name = val();

// using typedef
typedef std::vector<std::string> nameVectorT;
nameVectorT name = val();
```

- if u use `auto` with reference you must type `&`
  - if you don't it will make a copy of that variable

```c++
auto& var = somethingReturnTypeReference();
auto var0 = somethingReturnTypeReference(); // make copy
```

- c++14 u can use `auto` with return type in functions

```c++
auto name()
{
  return "name";
}
```

c++ 11

```c++
auto name() -> char*
{
  return "name";
}
```

# Static Arrays in C++ (std::array)

- static array that won't grow

```c++
#include <array>
```

- `std::array<type, size>`

```c++
std::array<int, 5> data01;

// c style array
int data02[5];
```

- u can use std::array with all algorithm in std
- both array and std::array allocated on stack
- std::array has a bounds checking optionally
  - in debug only
- USE std::array instead c style array
  - has no cost compared to c style
  - bounds check
  - layers of debugging

## comments

- Khatharr Malkavian | 1 year ago

It's worth noting that the size() function is also `constexpr`, so it doesn't actually return 5, but rather the compiler will just replace the function call itself with 5, so something like:

```c++
int s = ary.size();

// literally becomes

int s = 5;

// with no function call at runtime.
```

## constexpr

constexpr is a keyword in C++ that was introduced in C++11. It allows the evaluation of expressions at compile-time, rather than run-time.

A constexpr function is a function that can be evaluated at compile time. It is declared using the constexpr keyword in the function signature.

For example, consider the following code:

```c++
constexpr int square(int x) {
    return x * x;
}

int main() {
    constexpr int y = square(5);
    static_assert(y == 25, "Incorrect result");
}
```

In this code, the square function is declared as constexpr, which means that it can be evaluated at compile time. The y variable is also declared as constexpr, which means that its value is known at compile time. The static_assert statement is used to ensure that the value of y is equal to 25 at compile time.

constexpr is very useful for writing efficient code that can be evaluated at compile-time, which can reduce the time and resources required for program execution.

# Function Pointers in C++

- when use parentheses with function we call this function `func()`
- but if we call function without parentheses we getting the function pointer`&func`
- functions are cpu instruction and are stored somewhere

```c++
void func(){
  std::cout << "I was called"<< std::endl;
}
```

```c++
int main(){
  // calling
  // auto test = func(); // error as the return type is void

  // get function pointer
  auto test = func;

  test(); // calling it
  test(); // calling it
  test(); // calling it
}
```

- what the type look like?

```c++
void(*test)() = func;
```

- so can either use auto or make an alias for it

```c++
typedef void(*funcFunction)()
funcFunction test = func;
```

- how it works with functions with params?

```c++
void func(int a){
  std::cout << "I was called | param is "<< a << std::endl;
}
```

```c++
typedef void(*funcFunction)(int)
funcFunction test = func;

test(8);
```

- a real world example may be if u want to pass function to another function

```c++
void PrintValue(int val)
{
  std::cout << val << std::endl;
}

void ForEach (const std::vector<int>& list,  void(*print)(int))
{
  for(int val: list)
    print(val);
}
```

```c++
int main()
{
  std::vector<int> values = {1,2,3,4,5,6,7};

  ForEach(values,PrintValue);

  std::cin.get();
}
```

- we can define our function directly with lambda

```c++
[](params){
  /*code*/
}
```

```c++
int main()
{
  std::vector<int> values = {1,2,3,4,5,6,7};

  ForEach(values, [](int val){
    std::cout << val << std::endl;
  });

  std::cin.get();
}
```

`[]` captcha method which how we pass variable from outside

# Lambdas in C++

- a way to make anonymous
  - a quick disposable function
- whenever you have a pointer function u can use lambda function

```c++
void ForEach (const std::vector<int>& list,  void(*print)(int))
{
  for(int val: list)
    print(val);
}
```

```c++
int main()
{
  std::vector<int> values = {1, 2, 3, 4, 5, 6, 7};

  auto lambda  = [](int val){
      std::cout << val << std::endl;
    };

  ForEach(values, lambda);

  std::cin.get();
}
```

- [cpp reference](https://en.cppreference.com/w/cpp/language/lambda)

## mutable with lambda

- lambda is a little throwaway function u can write and assign to variable quickly

  - `[capture method]` u can pass variables from current scope to lambda from`[]`
  - `[a]` => passing a by value
  - `[&a]` => passing a by reference
  - `[=]` => passing all variables in scope by value
  - `[&]` => passing all variables in scope by reference

- when passing variables by value u can't change them in lambda
  - and here come `mutable` keyword `[=]() mutable`
  - this mean u can now change the variables passing by value
  - this applied if u want to make it `pass by value` otherwise u can `pass by reference` and u don't need `mutable`

```c++
int main()
{
  int a = 0;
  auto func = []()
  {
    std::cout<< "I'm a lambda"<<"\n";
  };

  func();
}
```

# Why I don't "using namespace std"

- avoid using `using namespace` with standard library as u can
- u can use it with long name namespace
- u can use `using namespace` inside scope instead of the header if your `.cpp` files

  - so if u want to use namespace in certain scope just make it in this scope

- `Comments`
  - You don't have to bring the entire std namespace. I mostly use:

```c++
#include <iostream>

using std::cout;
using std::endl;

int main() {
  int number = 10;
  cout << "The value of number is: " << number << endl;
  cout << "Hello, world!" << endl;
  return 0;
}
```

## Don't ever never use `using namespace` in header files

# Namespaces in C++

- with this u can define same symbols in different namespaces
  - symbols like classes functions variables ..etc
- the main purpose is to avoid naming conflicts
- `::` u can call it a namespace operator
  - u can access namespaces symbols
  - also u can access static method in classes using it
    - u can consider classes as namespace on its own
- what `using namespace ?` mean?
  - include every thing from `?` to not to use `?::` every time u use it

```c++
using namespace ?
```

- u can define certain method `using ?::method` so u can use `method` without namespace but u must provided it with other methods

```c++
using ?::method
method();
?::other();
```

- u can make alias for namespace

```c++
namespace name = ?
name::method(); // instead of using ?::method();
```

- u can nest namespaces

```c++
namespace first {
  namespace second {
    void func(){

    }
  }
}
```

call nested functions

```c++
first::second::func();
```

u can use `using`

```c++
using namespace first::second;
```

or u can separate the like that

```c++
using namespace first;
using namespace second;
```

- c++ 17

```c++
namespace first::second {
    void func(){

    }
}
```

## comments

- Katleho Komeke | 4 years ago

  The `::` is called the scope resolution operator.

# Threads in C++

- CPUs now a days have multi core
- we can do operations in parallel
- first include `thread`

```c++
#include <thread>
```

```c++
std::thread worker(/*function pointer*/);
```

u can wait the thread to finish using `join`

```c++
worker.join();
```

- [watch video for more](https://www.youtube.com/watch?v=wXBcwHwIt_I&list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb&index=62)
