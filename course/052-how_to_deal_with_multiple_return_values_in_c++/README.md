# How to Deal with Multiple Return Values in C++


- make a struct with things u want to return
- pass output by reference to the function
  - Prefix parameters with `out`
- pass output by pointer to the function
  - Prefix parameters with `out`
- if returned value have the same type u can go with
  - string list `std::string[2]`
  - standard array `std::array<std::string,2>` => include `<array>`
  - vector `std::vector<std::string>` => include `<vector>`
- u can use tuples
  - include `<utility>`
  - include `<functional>`
  - `std::tuple<std::string, std::string>`
  - `std::make_pair(a, b)`
  - `std::get<index>(tuple)`

## comment

- AlguienMasRaro | 1 year ago
  <br>
  For anyone reading recently, there's a better way with structured binding since c++17:
  <br>
  Return a tuple of your choice and return it as per the video:

```c++
std::tuple<std::string, std::string, int> getData() {
    return { "One", "two", 3 };
}
```

Retrieve values using structured binding:

```c++
auto [str1, str2, number] = getData();
```

