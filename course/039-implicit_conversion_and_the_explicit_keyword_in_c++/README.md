# Implicit Conversion and the Explicit Keyword in C++


- Implicit mean automatic
- c++ do one implicit conversion on your code

```c++
using String = std::string;

class Entity
{
private:
	String m_name;
  int m_age;
public:
	Entity()
  : m_name("none") {};

	Entity(const String& name)
  : m_name(name), m_age(-1) {};

	Entity(int age)
  : m_name("none"), m_age(age) {};

	const String& GetName() const{
		return m_name;
	}
};
```

- Implicit init

```c++
Entity e("Ali");
Entity b(23);

// u can do like this

Entity e = "Ali";
Entity b = 23;
```

```c++
void printEntity(const Entity& e)
{
  // code
}

printEntity(23);

/*
* won't work because it expect to provide std::string
* and "ali" is a char array
* so it need first converted to std::string
* then need to be converted to Entity with the string constructor
* c++ do one implicit conversion so it won't work
*/
// printEntity("Ali");

// here will do one implicit from std::string to Entity
printEntity(std::string("Ali"));
// here will do one implicit from char array to std::string
printEntity(Entity("Ali"));
```

## explicit

- prevent implicit conversion mean u should explicitly make the calling

```c++
using String = std::string;

class Entity
{
private:
	String m_name;
  int m_age;
public:
	Entity()
  : m_name("none") {};

	Entity(const String& name)
  : m_name(name), m_age(-1) {};

	explicit Entity(int age)
  : m_name("none"), m_age(age) {};

	const String& GetName() const{
		return m_name;
	}
};
```

now we can't do that

```c++
Entity a = 22; // wrong code
```

what u can do now is

```c++
Entity a(22); // valid | normal init
Entity a = Entity(22); // valid | normal init

Entity a = (Entity)22; // valid | casting
```

- cherno usually use
  - in math library
  - low level wrapper

