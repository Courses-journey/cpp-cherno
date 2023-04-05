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

