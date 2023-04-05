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

