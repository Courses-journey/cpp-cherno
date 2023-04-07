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
