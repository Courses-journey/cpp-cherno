# The Arrow Operator in C++


- a shortcut for dereferencing

```c++
class Entity
{
  public:
    void Print() const
    {
      std::cout << "Hello!" << std::endl;
    }
};
```

```c++
int main()
{
  Entity e;
  e.Print();

  Entity* ptr = &e;

  Entity& entity = *ptr;
  entity.Print();

  (*ptr).Print();
}
```

- with arrow operator

```c++
int main()
{
  Entity e;
  e.Print();

  Entity* ptr = &e;

  ptr->Print();
}
```

- u can override it same as any operator

```c++
class Entity
{
  public:
    void Print() const
    {
      std::cout << "Hello!" << std::endl;
    }

    Entity* operator-> () const
    {
      return /**/;
    }

    const Entity* operator-> () const
    {
      return /**/;
    }
};
```

- u can use it to get offset of each member in memory
  - useful when serializing data into a stream of bytes and u want to figure out offset of cretin things

```c++
struct Vector3
{
  float x, y, z; // the order of declaration will be the same in memory
}

int main()
{
  // start from zero
  //  using 0 or nullptr
  int offsetX = (int)&((Vector3*)0)->x ;
}
```

