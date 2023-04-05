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

