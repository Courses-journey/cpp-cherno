# Interfaces in C++ (Pure Virtual Functions)


- allow us to define virtual function in our base class that have no implementation and impl it in subclasses
- force subclasses to impl there own impl to that virtual function
- in programming it's common to have classes that have unimplemented method called `interface class`
  - it's not possible for us to instantiate this class
- to make virtual function a pure virtual function
  - we assign it to 0

```c++
class Entity
{
public:
	float X, Y;
  // pure virtual function
	virtual void GetName() = 0;
};
```

- c++ doesn't have a keyword called `interface` it just a class with pure virtual function
- U cannot make instances of base class that have pure virtual functions
- U cannot make instances of subclass class that extend base class that have pure virtual functions until u impl all pure functions in it

