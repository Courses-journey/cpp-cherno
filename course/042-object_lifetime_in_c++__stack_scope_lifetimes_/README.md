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

