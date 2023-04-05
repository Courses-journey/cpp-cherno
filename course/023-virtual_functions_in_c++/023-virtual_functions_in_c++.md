# Virtual Functions in C++


- Virtual Functions allow us to override methods in subclasses
- U can define same functions name and parameters in base and subclass
  - it will work as expected until u assign subclass instance to base pointer
  - when u do that the function in base will be called not the one in base
  - Here come virtual functions

```c++
class Entity
{
public:
	float X, Y;
	void GetName(){
		std::cout<<"Entity"<<"\n";
	}
};

class Player : public Entity
{
public :
	const char* Name;
	void GetName() {
		std::cout << "Player" << "\n";
	}
};
```

- Normal instance

```c++
  Entity e;
  e.GetName(); // Entity

  Player p;
  p.GetName(); // Player

  // -------------
  std::cout << "================" << "\n";
  // -------------
```

- Pointer instance

```c++
  Entity* e1 = new Entity();
  e1->GetName(); // Entity

  Player* p1 = new Player();
  p1->GetName(); // Player

  // -------------
  std::cout << "================" << "\n";
  // -------------
```

- Pointer instance and assign subclass to base pointer

```c++
  Entity* entity = e1;
  entity->GetName(); // Entity

  entity = p1;
  entity->GetName(); // Entity | not as expected | we expected to return Player
```

- virtual function reduce something called dynamic dispatch
  - compiled typically implemented by our vtable
- vtable is a table that contains mapping for all the virtual functions

- so to wrap it up all we need now to make function in base class as `virtual`
- c++ 11 introduce `override` keyword
  - it's not required but make code more readable
  - Reduce bugs
    - wrong writing method name in subclass for example
    - override non virtual method

```c++
class Entity
{
public:
	float X, Y;
	virtual void GetName(){
		std::cout<<"Entity"<<"\n";
	}
};

class Player : public Entity
{
public :
	const char* Name;
	void GetName() override{
		std::cout << "Player" << "\n";
	}
};
```

- Virtual function aren't free
  - two runtime costs
    - additional memory required to store vtable
    - every time we call function we go to that table to know which function to actually map to.
    - `cherno` use them all-time
      - May considered not use them in **embedded systems** which have terrible performance and every cpu slice account

## vtable

- In C++, virtual functions are used to achieve runtime polymorphism, which allows code to work with objects of different classes without knowing their exact type at compile time.

- When a virtual function is called on an object through a pointer or reference to the base class, the correct version of the function for the actual type of the object is called.

- This process is called dynamic dispatch, and it is typically implemented by using a vtable to store the addresses of the virtual functions for each class in the inheritance hierarchy.

- While virtual functions have some performance overhead compared to non-virtual functions, they allow for more flexible and extensible code.

## Notes | Difference between `.` and `->`

- In C++, the dot operator (.) is used to access

  - methods and properties of an object when it is accessed directly,

- whereas the arrow operator (->) is used to access

  - methods and properties of an object when it is accessed through a pointer.

```c++
// Accessing object method using dot operator
MyObject obj;
obj.doSomething();

// Accessing object method using arrow operator through a pointer
MyObject* pObj = new MyObject();
pObj->doSomething();

// Accessing object property using dot operator
int x = obj.value;

// Accessing object property using arrow operator through a pointer
int y = pObj->value;
```

## comments

### Juan Ortiz | 3 years ago

Brief explanation of uncovered topics (yet) in this video:

- Since strings is not a primitive type of C++ we need to import the header

```c++
#include <string>
// To use string without namespace std is like this:
std::string MyString("hello")
// This is equivalent to:
std::string MyString = "Hello"
```

- Pointer instances: new keyword returns a pointer

```c++
std::string* MyString = new std::string("Hello")
// And if is a pointer you access their properties with -> instead of a dot (.)
std::cout << MyString->length() << std::endl;
```

