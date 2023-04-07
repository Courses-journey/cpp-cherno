# Inheritance in C++


- Base class that have common functionality
  - Branch it and add more to it
- Avoid code duplication
- A way to extend existing class and new functionality to it

```c++
class Entity
{
public:
	float X, Y;
};

class Player : public Entity
{
public :
	const char* Name;
};

```

