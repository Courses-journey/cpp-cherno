# CONDITIONS and BRANCHES in C++ (if statements)


- If make programme move from place to another in memory depend on condition and start execute commands from that place in memory.
- If u want a faster code try to avoid them.

```c++
if()
{
  // code
}else if()
{
  // code
}

// ----- same as -----
// It just like a shortcut

if ()
{
  // code
}
else
{
	if ()
	{
    // code
	}
}

```

- We can use `if` with pointers to check that they aren't `null`

```c++
const char* ptr = "hello";

if(ptr)
  cout<<"ptr not null"<<"\n";
else
  cout<<"ptr is null"<<"\n";

```

