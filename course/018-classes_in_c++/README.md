# CLASSES in C++


- classes are a way to group data and functionality together
- class are a new variable type we called it `object`
- the new object variable we called `instance`

```c++
class Player
{
  int x,y;
  int speed;
};

Player player; // instantiated a player object

// set var of player
player.x = 1;       // error as it private
player.y = 5;       // error as it private
player.speed = 50;  // error as it private
```

- By default class make everything private
- To make it public to access we have to specify that by `public:`

```c++
class Player
{
  public:
    int x,y;
    int speed;
};
```

- To write a function we could define it separately outside the class like

```c++
class Player
{
  public:
    int x,y;
    int speed;
};

// Player& player as we want to change player
void move(Player& player,int xa,int ya)
{
  player.x = xa * player.speed;
  player.y = ya * player.speed;
}

int main(){
  Player player; // instantiated a player object

  // set var of player
  player.x = 1;
  player.y = 5;
  player.speed = 50;

  move(player, -1, 1);
}
```

- We can move functions inside classes
- Functions in classes are called methods

```c++
class Player
{
  public:
    int x,y;
    int speed;

    void move(int xa,int ya)
    {
      x = xa * player.speed;
      y = ya * player.speed;
    }
};


int main(){
  Player player; // instantiated a player object

  // set var of player
  player.x = 1;
  player.y = 5;
  player.speed = 50;

  player.move( -1, 1);
}
```

- Anything u can do with classes u can do without classes.
  - They just make our life easier
  - Syntax sugar ^\_^

