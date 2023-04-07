# How to CREATE/INSTANTIATE OBJECTS in C++


- we have to option to instantiate our object
  - it depend on which memory it's going to occupy
- At least when need one byte of memory for class even if we have an empty class

```c++
class Entity
{
private:
	String m_name;
public:
	Entity(): m_name("none") {};

	Entity(const String& name): m_name(name) {};

	const String& GetName() const{
		return m_name;
	}

};
```

## stack and heap

- there are other section in memory for example where our source code live

### stack objects

- have automatic lifespan
- their lifetime controlled by the scope that they declared
- as soon as the variable go out of the scope the memory is free `stack pops`

- How to init on stack?

```c++
/*
* this way we create the object entity on stack
* don't think this is not initialized it does
* because we have a default constructor [e] was initialized using it
* so it's a valid code
*/
Entity e;

// u can also make this way and it's the same
Entity e1 = Entity();

// =======================

// If u want to specify parameters
// u can make this
Entity e2("AA");

// or this way and it's the same
Entity e3 = Entity("AA");
```

- when not to init on stack?
  - when object is too large
  - when we have too many objects
  - stack is usually smaller it is `1megabyte` or `2megabyte`
    - depend on platform and compiler

### Heap

- a bit big mysteries place
- if u create object in heap it will set there until u decide to free it
- How to init on heap?
  - `new` keyword => return a `pointer` to object in heap

```c++
Entity* e = new Entity();

// or | we don't need to make () for default constructor
Entity* e1 = new Entity;

// =======================

// If u want to specify parameters
// u can make this
Entity* e2 = new Entity("AA");
```

- cons
  - allocating on heap take longer than allocating in stack
  - u have free memory manually when u finish with it
    - ```c++
      delete var_name;
      ```

## Note

- when using string don't use

  ```c++
  using namespace std;
  ```

  - use
    ```c++
    using String = std::string;
    ```

- differences between `using` and `#define`

```c++
 using String = std::string;
//  is a type alias that creates a new name for an existing type,
```

while

```c++
#define String std::string;
// is a macro that replaces all occurrences of String with std::string;
// and can have some potential drawbacks.
```

## scope

- can be a function

```C++
type name(){
  // CODE
}
```

- If statement

```C++
if(/*condition*/)
{
  // CODE
}
```

- for loop

```C++
for(;;)
{
  // CODE
}
```

- empty scope

```c++
{
  // CODE
}
```

so scope not just a function

## wrap up

- Is object is too big?
- Do i want explicitly control the life time of the object?
- If your answer no => allocate on the stack
  - it's way better
  - it's automated
  - it's faster
- If your answer yes => allocate on the heap
  - u have manually free memory with delete
  - if u forget to free can cause memory leak
  - u can use `smart pointers`

