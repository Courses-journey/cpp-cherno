# CLASSES vs STRUCTS in C++


- class private by default
- struct public by default

## so why it exist in c++?

- Because of backward compatibility with `c`

## when to use one of them?

- if u want all members to be public use struct

## Cherno

- `pod`=> plain old data
- use struct when i need to represent a punch/group of data
- ```c++
  struct Vec2{
    float x,y;
  }
  ```
- U could also add functions for example

  - ```c++
    struct Vec2{
      float x,y;

      Vec2 add(const Vec2& other)
      {
        x += other.x;
        y += other.y;
      }
    }
    ```

  - it all just about manipulating vec data

- Use classes with inheritance
- Some compilers will give u warnings in case

  - u have class A and struct B.
  - struct B inherit from class A.
  - it just warnings and code will work.
  - some compilers won't show these error.

- If u want something fill of functionality go with class
- U can use struct whenever u use class

## some comments on video

- **Reydriel | 10 months ago (edited)**
  <br>
  To elaborate more on what Cherno says in this video,
  <br>
  structs are a legacy feature from C which can group together variables into a user-defined type,
  <br>
  BUT CANNOT contain functions
  (because C did not have OOP features such as methods).
  <br>
  This is why it's common in C++ to use structs for "classes with no methods", because that was how they were used in C.

- **It Cracks! | 5 years ago (edited)**
  <br>
  The C++ Core Guidelines C.2 states:
  "Use class if the class has an invariant;
  use struct if the data members can vary independently."
  <br>
  So if you don't have any preexisting style, your best bet is to stick to that.

- **Matthijs van Duin | 2 years ago**
  <br>
  The difference in default access also applies to inheritance:
  <br>
  struct Foo : Bar // Bar is a public base class of Foo
  <br>
  class Foo : Bar // Bar is a private base class of Foo

