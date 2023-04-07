# Optimizing the usage of std::vector in C++


- Know your environment

- When push back element to vector by init directly when make a copy of it
- as we push back to vector it keep resizing to fit elements and this way we copying element each time vector extend

```c++
int main(){
  std::vector<Vertex> vertices;
  vertices.push_back(Vertex(1, 2, 3)); // init vertex copying to vertices | copying to resize
  vertices.push_back(Vertex(4, 5, 6)); // init vertex copying to vertices | copying to resize
  vertices.push_back(Vertex(7, 8, 9)); // init vertex copying to vertices | copying to resize
}
```

- so if we somehow tell vector that I'm going to push back 3 elements I'll prevent these copies
- we can do that using `.reserve(size)`

```c++
int main(){
  std::vector<Vertex> vertices;
  vertices.reserve(3);
  vertices.push_back(Vertex(1, 2, 3)); // init vertex copying to vertices
  vertices.push_back(Vertex(4, 5, 6)); // init vertex copying to vertices
  vertices.push_back(Vertex(7, 8, 9)); // init vertex copying to vertices
}
```

- now I want to pass vertex to vertices vector without copying
- u can use `emplace_back` this take parameters of vertex and tell vector to construct a vertex

```c++
int main(){
  std::vector<Vertex> vertices;
  vertices.reserve(3);
  vertices.emplace_back(1, 2, 3);
  vertices.emplace_back(4, 5, 6);
  vertices.emplace_back(7, 8, 9);
}
```

