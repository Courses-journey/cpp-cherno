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

