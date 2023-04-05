# Member Initializer Lists in C++ (Constructor Initializer List)


- It's all about initialize class members
- there are two ways to do that in c++

## normal way

```c++
class Entity{

  private:
  std::string m_name;

  public:

  Entity(){
    m_name = "None";
  }

  Entity(const std::string& name){
    m_name = name;
  }

  const std::string& GetName() const
  {
    return m_name;
  }
}
```

## Member Initializer Lists

- always list member list in order of class members declaration order
- use them everywhere `why?`

  - because when using normal way the member created two time on from init and the other from constructor `not the case in primitive type`
  - but using member initializer list it created once

- comments

  - **Charisma | 5 years ago**
    <br>
    Also you cant initialize const members without using "Member initializer".
  - **Josh Stephenson | 5 years ago**
    <br>
    Don't forget Member Initializer Lists can also be used for initializing const member variables as well!

  - **Delta Rambo | 2 years ago**
    <br>
    Basically, all data-members which should be initialized at time of declaration, such as const , references, etc., must be included in the constructor's initializer list.

```c++
class Entity{

  private:
  std::string m_name; // first
  int m_score;        // second

  public:
  Entity()
      :m_name("None"),m_score(0)
  {
  }

  Entity(const std::string& name,int& score)
      :m_name(name),m_score(score)
  {
  }

  const std::string& GetName() const
  {
    return m_name;
  }
}
```

