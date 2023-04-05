# Static in C++


- Two means

  - Out of struct or class
  - Inside of struct or class

- static out of struct or class

  - means that the linkage of that symbol that you declared to be static is going to be internal meaning it's going to be visible only to that translation unit you've defined it in

- static Inside of struct or class
  - means that variable is actually going to share memory with all of the instances of the class
  - means whatever how many struct or class u have created it will be one instance of that static variable

## static out of struct or class

- U cannot have global variable with same name in different files

  - u can make them static `means that they will be private in that file`
  - u can reference one of them using `extern` keyword
    ```c++
    extern int b;
    ```

- u can use static variable in headerfiles so when u import them in translation units each file will have its own static var
- use static all times u won't the variable to be global
- global variables are bad

