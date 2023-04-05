# Destructors in C++


- run when u destroy an object
- In Constructors u can initialize any variable or any thing u want
- In Destructors u uninitialized any variable or clean any memory that you've used
- Applies to both stack and heap allocated objects
- to make one create a method with object name and prefix it with Tilde `~`

  - ```c++
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

      ~Entity() {
        X = 0;
        Y = 0;
      };
    };
    ```

