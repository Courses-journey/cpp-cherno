# Visibility in C++


- Concept that is related to OOP
- How visible certain members or methods of a class actually are
- Visible mean who can see them oe call them or use them

## Three basic visibility modifiers in c++

- private
- protected
- public

## private

- mean members can be only access inside class or struct scope
  - `friend` keyword u can label class or a function as friend and u can access private member
- default in class | `public` default in struct

## protected

- mean members can be only access inside class or struct scope and subclasses that inherits from this class

  - `friend` keyword u can label class or a function as friend and u can access private member

