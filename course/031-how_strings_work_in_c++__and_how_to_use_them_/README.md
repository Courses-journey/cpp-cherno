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

