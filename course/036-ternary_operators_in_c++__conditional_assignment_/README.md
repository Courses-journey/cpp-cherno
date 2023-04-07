# Ternary Operators in C++ (Conditional Assignment)


- summary syntax for if else

- Ternary syntax

```c++
condition ? if_true : if_false
```

- Example

```c++
if(temp > 30)
  status = "hot";
else
  status = "cold";
```

```c++
status = temp > 30 ? "hot" : "cold";
```

## comments

- **Jon Snow | 2 years ago**
  <br>
  A better way to write this kind of nested conditional at 4:50 is:

```c++
s_speed = s_level > 10 ?  15 :
          s_level >  5 ?  10 :
                            5;
```

An old school C trick that with proper indentation makes the nested ternary assignment very nice to read and more readable than if...else if...else

- **Andrew Esh | 3 years ago**
  <br>
  You missed my favorite use of the ternary operator: conditional argument passing. You can use the ternary in the list of arguments to a function or method call like this:

```c++
SetSpeed(s_Level > 5 ? 10 : 5);
```

So the ternary is not just a replacement for an if statement. It can be used in places an if statement can not.

