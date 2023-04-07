# OPERATORS and OPERATOR OVERLOADING in C++


- `OPERATOR` symbol that we use instead of function to do something

  - `->` `*` `<<` `>>` `&` `+=` `new` `delete` etc..
  - `,` `()`

- overloading is to change the way this operator work or give it a new meaning

- [Operators Reference](https://en.cppreference.com/w/cpp/language/operators)

- If other go to your definition of operator overloading u have use it wrong

- How to implement it?
  - write the operator u want after `operator` keyword => for example `operator*` `operator+`

```c++
  returnType operator+ (params)
  {
    // code
  }
```

- implementation
  - cherno recommended style

```c++
struct Vector2
{
  float x,y;

  Vector2(float x, float y)
      : x(x), y(y) {}

  Vector2 Add (const Vector2& other) const
  {
    return Vector2(x + other.x , y + other.y);
  }

  Vector2 operator+ (const Vector2& other) const
  {
    return Add(other);
  }
}
```

- In the the previous code the + operator call the add method
- U can do the opposite to make the add function to call plus operator

- with `this` keyword

```c++
struct Vector2
{
  float x,y;

  Vector2(float x, float y)
      : x(x), y(y) {}

  Vector2 Add (const Vector2& other) const
  {
    return *this + other;
  }

  Vector2 operator+ (const Vector2& other) const
  {
    return Vector2(x + other.x , y + other.y);
  }
}
```

- with address operator plus like a function

```c++
struct Vector2
{
  float x,y;

  Vector2(float x, float y)
      : x(x), y(y) {}

  Vector2 Add (const Vector2& other) const
  {
    return operator+(other);
  }

  Vector2 operator+ (const Vector2& other) const
  {
    return Vector2(x + other.x , y + other.y);
  }
}
```

- Same way u can implement multiply

```c++
struct Vector2
{
  float x,y;

  Vector2(float x, float y)
      : x(x), y(y) {}

  Vector2 Add (const Vector2& other) const
  {
    return Vector2(x + other.x , y + other.y);
  }

  Vector2 operator+ (const Vector2& other) const
  {
    return Add(other);
  }

  Vector2 Multiply (const Vector2& other) const
  {
    return Vector2(x * other.x , y * other.y);
  }

  Vector2 operator* (const Vector2& other) const
  {
    return Multiply(other);
  }
}
```

## How to use

```c++
Vector2 pos(10.f, 20.f);
Vector2 speed(5.f, 5.f);
Vector2 powerUp(1.1f, 1.1f);

Vector2 result01 = pos.Add(speed.Multiply(powerUp)); // with functions
Vector2 result02 = pos +   speed *        powerUp;   // with operator overload
```

## `<<` left shift operator | to print to console

- `ostream` output stream

```c++
/*
* [std::ostream&] original definition to left shift operator
* [stream] reference to cout
*
*/
std::ostream& operator<< (std::ostream& stream, const Vector2& other)
{
  steam << other.x << ", " << other.y;
  return stream;
}
```

## `==` equality operator

```c++
/*
* [std::ostream&] original definition to left shift operator
* [stream] reference to cout
*
*/
{

  bool operator== (const Vector2& other) const
  {
    return x = other.x && y = other.y;
  }

  bool operator!= (const Vector2& other) const
  {
    // return !operator==(other); // looks weird
    return !(*this == other);
  }

}
```

## Note

- `this` keyword is a pointer for the class

