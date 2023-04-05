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

