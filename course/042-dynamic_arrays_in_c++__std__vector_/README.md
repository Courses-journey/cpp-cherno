# Dynamic Arrays in C++ (std::vector)


- [Why it called vector?](https://stackoverflow.com/questions/581426/why-is-a-c-vector-called-a-vector)
- It should be called an `arrayList`
- unlike array this can resize
- [EASTL](https://github.com/electronicarts/EASTLs)
- to make one

```c++
struct Vertex {
  float x, y, z;
}
```

```c++
std::vector<Vertex> vertices;
```

- to add to it

```c++
vertices.push_back({1, 2, 3});
vertices.push_back({4, 5, 6});
vertices.push_back({7, 8, 9});
```

- to get size of elements in it
  - u can use `.size()

```c++
std::out<< vertices.size()<< "\n";
```

- range based loop

```c++
// this code make a copy of vertex in for loop scope
for (Vertex v: vertices)
{
  std::out<< v << "\n";
}

// to avoid that we use &
for (Vertex& v: vertices)
{
  std::out<< v << "\n";
}
```

- to clear it we use
  - `.clear()`

```c++
vertices.clear();
```

- to erase specific index
  - `.erase(iterator)

```c++
// to erase the second element | index 1
vertices.erase(vertices.begin() + 1);
```

