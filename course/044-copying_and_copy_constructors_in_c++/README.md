# Copying and Copy Constructors in C++


- copy data `memory` from one place to another
- when copying object c++ take all parameters and assign it to the copied one
- c++ provide u a default copy constructor

```c++
Class_name(const Class_name& other);
```

```c++
Class_name(const Class_name& other)
{
  memcpy(this, &other, sizeof(Class_name));
}
```

- u can prevent copying by deleting this constructor

```c++
Class_name(const Class_name& other) = delete;
```

- always pass your object by const reference

