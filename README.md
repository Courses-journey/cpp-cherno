# cpp-cherno

The Cherno youtube channel

## [c++ course](https://www.youtube.com/playlist?list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb)

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
