# Local Static in C++


- `static` keyword in local scope
- We have two things to take in consideration
  - first is the lifetime which mean how long our variable we be in memory before deleted
  - second is the scope which mean the accessability og the variable
- we mark variable as static in a scope this mean that the variable will have the lifetime of our program but can only accessed from that scope

```c++
void Test(){
  static int count_call = 0;
  count_call++;
  std::cout<<count_call<< std::endl;
}

// ====================================

Test(); // 1
Test(); // 2
Test(); // 3
```

- is the same if u do that
  - but now u can call count anywhere

```c++
int count_call = 0;

void Test(){
  count_call++;
}

// ====================================

Test(); // 1
Test(); // 2
Test(); // 3
```

```c++
int count_call = 0;

void Test(){
  count_call++;
}

// ====================================

Test(); // 1
count_call = 10;
Test(); // 11
Test(); // 12
```

- Make singleton class without static in scope

```c++
class Singleton
{
  private:
    static Singleton* s_Instance;

  public:
    static Singleton& Get()
    {
      return s_Instance;
    }

    void Hello(){}
};

Singleton* Singleton::s_Instance = nullptr;

int main(){
  Singleton::Get().Hello();
}
```

- Make singleton class with static in scope

```c++
class Singleton
{
  public:
    static Singleton& Get()
    {
        static Singleton instance;
        return instance;
    }

    void Hello(){}
};

int main(){
  Singleton::Get().Hello();
}
```

