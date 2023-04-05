# Constructors in C++


- Special type of method which run every time when we instantiate an object
- doesn't have return type
- it's name must match the of the class
- there is always a default constructor

```c++
class Entity
{
public:
	float X, Y;

	Entity() {
		X = 0;
		Y = 0;
	};

	Entity(float x,float y) {
		X = x;
		Y = y;
	};
};
```

- To crate instance u can use

```c++
Entity e; // Entity()
Entity e1(10.f,20.f); // Entity(float x,float y)
```

- U can prevent users from create instance of class by two way

  - make constructor private
  - ```c++
    class Log
    {
    private:
      Log(){};

    public:
      Write(const char* msg) {
      };
    };
    ```

  - assign constructor to delete
  - ```c++
    class Log
    {
    public:
      Log() = delete;
      Write(const char* msg) {
      };
    };
    ```

- There are special type of constructor such
  - copy constructor
  - move constructor

