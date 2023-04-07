# The "this" keyword in C++


- only accessible through a member function
  - a function that belong to a class
- `this` pointer to current object instance that the method belongs to

```c++
class Entity
{
  public:
   int x,y;

   Entity(int x, int y)
   {
    Entity* e = this;
    // Entity* const e = this;
    e->x = x;
    e->y = y;
   }
}
```

```c++
class Entity
{
  public:
   int x,y;

   Entity(int x, int y)
   {
    this->x = x;
    this->y = y;
   }
}
```

```c++
class Entity
{
  public:
   int x,y;

   Entity(int x, int y)
   {
    (*this).x = x;
    (*this).y = y;
   }
}
```

- In const method `this` not only a pointer to the instance but a const pointer
  - because in const function we aren't allowed to change class member
  - and by being a const pointer we now aren't able to change the content of it

```c++
{
  int GetX() const
  {
    // Entity* e = this; // error
    const Entity* e = this;
  }
}
```

- `this` useful when we for example want to pass the current instance to function from outside our class

```c++
void doSomething(const Entity& entity)
{
  // code
}

void doSomethingElse(Entity* entity)
{
  // code
}

class Entity
{
  public:
   int x,y;

   Entity(int x, int y)
      : x(x), y(y)
   {
    doSomething (*this);
    doSomethingElse (this);
   }
}
```

