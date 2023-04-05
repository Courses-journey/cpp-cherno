# CONST in C++


- A fake keyword
- It just a promise that u won't change this data
  - but u can bypass that
  - u can break that promise ^\_^

## const with pointers

- const before pointer `before asterisk *`
  - u can't change the value `content in that address`
  - but u can change the pointer itself `change what pointer refer to`

```c++
// first way
const type* var_name

// second way
type const* var_name
```

```c++
const int b = 5;
const int* a = new int;
*a = 7; //not valid code
a = &b; //valid code
```

- const after pointers type
  - u can change the value `content in that address`
  - but u can't change the pointer itself `change what pointer refer to`

```c++
type* const var_name
```

```c++
const int b = 5;
const int* a = new int;
*a = 7; //valid code
a = &b; //not valid code
```

## const with method and classes

### in classes

- when u mark method as const
  - I promise that this method won't change any member of this class
  - readonly method
  - useful with getter method as it only read data from class
  - u can call this method when it passed to `const reference`
    - this why u can see two version of getter one with const and one without
  - always `always` mark your method as const when it doesn't change the class or if they not supposed to modify the class

```c++
return_type method_name() const
{

}
```

```c++
class Entity{
  private:
  int m_x,m_y;
  public:
  int GetX() const
  {
    // m_x = 7 ; // u can't do that
    return m_x;
  }
}
```

- what if I need to change a variable of the class from const method?
  - u can mark this variable as `mutable`

```c++
class Entity{
  private:
  int m_x,m_y;
  mutable int var;
  public:
  int GetX() const
  {
    // m_y = 8; // not valid
    var = 7 ; // valid
    return m_x;
  }
}
```

- when member of class is pointer

```c++
class Entity{

  private:

  int* m_x,m_y;

  public:

  /*
  * this mean this function will
  * return a constant pointer
  * its content won't change
  * the pointer itself won't change
  * this method won't change any thing of this class member
  * it's a readonly method
  */
  const int* const GetX() const
  {
    // m_x = 7 ; // u can't do that
    return m_x;
  }
}
```

- Be aware

```c++
  /*
  * this mean m_x is an int pointer
  * m_y is a normal int
  */
  int* m_x,m_y;

  /*
  * this mean both m_x and m_y is an int pointer
  */
  int* m_x,*m_y;
```

