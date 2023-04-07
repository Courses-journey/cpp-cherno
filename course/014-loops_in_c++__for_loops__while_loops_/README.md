# Loops in C++ (for loops, while loops)


## for loop

```c++
for(int i = 0; i < 5; i++)
{

}
```

- `i` doesn't have to be zero and doesn't have to be an integer
- condition
- `i++` called before next iteration of for loop

  - `i += 1`
  - `i = i + 1`

- You can separate all for loop stuff like code below

```c++
int i = 0;
for(; ;)
{
  // code
 i++;

 if(/*condition*/){
    break;
 }
}
```

- Use when u have number of iterations

## while loop

```c++
int i = 0;
while(/*condition*/)
{
  // code
  i++;
}
```

- Use when u have condition

## do while loop

```c++
int i = 0;
do
{
  // code
}while( /*condition*/ )
```

- The main difference from `while` that do will execute at least one time no matter what is the condition

