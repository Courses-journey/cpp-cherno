# String Literals in C++


- A series of characters in between two double quotes

```c++
"string"; // const char* | length 7 because of null termination
```

- `strlen()` get string length

## note

```c++
const char* txt01 = "string"; // utf8
const char* txt02 = u8"string";
```

## from c++ 11 and above

```c++
const wchar_t* txt03 = L"string";  // 2 byte per  | differ depend on compiler
const char16_t* txt04 = u"string"; // 2 byte per char | utf16
const char32_t* txt05 = U"string"; // 4 byte per char | utf32
```

## from c++ 14

- `""s` => `s` operator function return a standard string

```c++
using namespace std::string_literals;

// std::string txt = "first" + "second" //error
std::string txt = "first"s + "second"
```

## `R""` => ignore escape character

- we can for example make multiline string

In C++, the R"txt" syntax is called a raw string literal. The R stands for "raw", which means that the string is interpreted literally without any special meaning to escape sequences such as \n or \". This can be useful when you want to include special characters or escape sequences within a string without having to escape them manually.

```c++
const char* txt = R"";
const char* txt2 = R"
01- .....
02- .....
03- .....
04- .....
";
// alternative
const char* txt2 = "01- .....\n"
"02- .....\n"
"03- .....\n"
"04- .....";
```

## ..

- String Literals always stored in readonly memory

- [watch this video again ^\_^](https://www.youtube.com/watch?v=FeHZHF0f2dw&list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb&index=33)

