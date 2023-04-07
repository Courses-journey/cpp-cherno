# SMART POINTERS in C++ (std::unique_ptr, std::shared_ptr, std::weak_ptr)


- `new` allocate on heap and then by calling `delete` it free the memory

  - smart pointers came to automate that process
  - when u call `new` u don't have to call `delete`
  - also in many cases u don't even need to call `new`

- include `memory`

```c++
#include <memory>
```

## unique pointer

- scoped pointer when the scope end it will free the memory
- they have to be unique
- u can't copy a unique pointer
- `std::unique_ptr<template_Arg>`

```c++
{
  std::unique_ptr<Entity> entity(new Entity());
  // std::unique_ptr<Entity> entity = new Entity(); // not allowed as it explicit constructor
}
```

- the preferred way
  - due to exception safety
  - if the constructor throw an exception u won't end up having a dangling pointer with no reference and cause memory leak

```c++
{
  std::unique_ptr<Entity> entity = std::make_unique<Entity>();
}
```

- stack allocated pointer
- the problem with this u can'y copy or share or pass to a function

```c++
{
  std::unique_ptr<Entity> entity = std::make_unique<Entity>();

  /*
  * in [unique_ptr] class the definition of assign was deleted
  * u can't copy instances
  */
  // std::unique_ptr<Entity> entity1 = entity; // not allowed
}
```

## shared pointer

- use something called reference counting
  - u keep tracking of how many references u have to your pointer
  - as soon as this count reach there it gets deleted
- `std::shared_ptr<template_Arg>`

- shared pointer not just allocate our object but also allocate a control block to track references count
  - when u call `std::make_shared` it allocate our object and the control block together which is a lot more efficient

```c++
/*
* If u init like that
* it will allocate your object
* then it will allocate the control block
* and this is two allocation
*/
std::make_shared<Entity> entity(new Entity());
```

```c++
std::shared_ptr<Entity> entity = std::make_shared<Entity>();
```

- when u copy shared pointer to another shared pointer the `references count` increase by one

## weak pointer

- when u assign shared pointer to weak pointer it won't increase the references count

```c++
std::shared_ptr<Entity> entity = std::make_shared<Entity>();
std::weak_ptr<Entity> e = entity;
```

- this is good if u won't to take ownership of the entity
  - check if it's alive
  - it won't keep it alive

```c++
int main(){
  {
    std::weak_ptr<Entity> e0;
    {
      std::shared_ptr<Entity> entity = std::make_shared<Entity>();
      entity = e0;
    } // e0 will be died after exist the first scope
  }
}
```

## use cases of pointer

- u should try use them all the time
  - they automate the memory management
  - prevent memory leaking by forgetting to call delete
- shared pointer have overhead as it has counting system

