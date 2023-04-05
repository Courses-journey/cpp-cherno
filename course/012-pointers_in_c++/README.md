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

