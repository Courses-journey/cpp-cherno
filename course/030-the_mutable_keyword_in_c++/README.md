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

