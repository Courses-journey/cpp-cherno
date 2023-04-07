# C++ Header Files


- Used for

  - declare certain type of function

- When define function in another file c++ won't know that it even exist when compiling the file

  - So we need a common place to make declaration in it.

## `#pragma once`

- `pragma` is an instruction that sent to the compiler
- `pragma once` mean include this file once
- It called Header Guide

## `ifndef` `endif`

- The traditional `old` way

```c++
#ifndef _LOG_H
#define _LOG_H

void Log(cont char* msg);

#endif
```

## `#include <fileName>` and `#include "fileName"`

- `#include <fileName>` Compiler search for file in the system's standard include directories.

  - angle brackets
  - The file u search must in one of the includes directories
  - used only with includes directories

- `#include "fileName"` the compiler first searches for the header file in the current directory. If the header file is not found in the current directory, the compiler searches for it in the standard include directories

  - double quotes
  - relative to directory the project exist in `#include "..\file"`.
  - used everywhere

### Note in standard library

- file without extension at the end like `iostream` are c++ STDL
- file with `.h` extension at the end like `stdlib.h` are c STDL

