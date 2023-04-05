# REFERENCES in C++


- Pointers and References are pretty much the same as far what the computer will do with them

## pointers and References

- Semantically they have subtle differences
- Reference is a way to reference **existing data**
- With Pointer u could create new pointer variable and set it to `nullptr` or `NULL` OR `0`
- This cannot done with References as it must reference existing var

## References

- Reference not a new variable and don't occupy memory
- U can define one by
  - write the type of data u want to reference
  - follow type with ampersand `&`
  - ```c++
    int a = 5;
    int& ref = a;
    ```
  - We just now created something called alias
  - the `ref` variable is not really a variable
  - It just a variable that exist in our source code not in memory like normal variables
  - We can use `ref` as it `a` we can read and write to `ref` directly

## use cases

- If u want for example to pass a variable to function and u want to manipulate this variable directly from function

- In function u can passe
  - By value
  - By pointer
  - By reference

```c++
#include <iostream>

int increaseByValue(int a)
{
	return a++;
}

int increaseByPointer(int* a)
{
	/* The wrong way
	* As it will increase the address first
	* and then dereference it
	*/
	// return *a++;

	/* The right way
	* Dereference first
	* then add value
	*/
	return (*a)++;
}

int increaseByRef(int& a)
{
	return a++;
}

int main()
{
	int a = 5;

	increaseByValue(a);
	std::cout << a << "\n"; // 5

	increaseByPointer(&a);
	std::cout << a << "\n"; // 6

	increaseByRef(a);
	std::cout << a << "\n"; // 7
}
```

## Note

- Any thing u can do with references you can do with pointers
- Pointers are more powerful and more useful in general
- When u make a reference u cannot change what it references.
- U can change pointer

  - ```c++
    int a = 5;
    int b = 5;

    int* ptr = &a;
    *ptr = 7; // a = 7

    ptr = &b;
    *ptr = 8 // b = 8

    ```

