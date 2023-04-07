# Making and Working with Libraries in C++ (Multiple Projects in Visual Studio)


- Create game solution
- Create Engine Solution
- Make `src` folder ro each project
- For all platforms and targets
  - configure `engine` output to static library for
  - configure `game` output to `.exe` for windows

## How to link

- Add path of our engine `src` to game properties
  - go to c++/c
    - if not exist make sure that there is `.cpp` file in your solution
  - go to general
  - go to additional include add `include` path of the library
    - make path relative to project folder
- U can use relative path to include files `#include "../../----"` instead of pervious step but don't do that
- Now we need to link `.lib` from engine project
- u can do this from
  - `Using Libraries in C++ (Static Linking)`
- But the beat way as this project inside our solution is to add reference to `engine` to `game` project
  - right click
  - add
  - add reference
  - mark engine solution
- this is the best approach as it will rebuild engine project if it has changes

