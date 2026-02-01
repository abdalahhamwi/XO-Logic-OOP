# XO-Logic-OOP

## Class Diagram

```mermaid
classDiagram
    class Game {
        -board : Board
        -current_player : Player
        +play()
        +switch_player()
        +check_winner() bool
        +is_draw() bool
    }

    class Board {
        -cells : list
        +display()
        +update_cell(position, symbol)
        +is_full() bool
        +check_lines() str
    }

    class Player {
        -symbol : str
        +make_move() int
    }

    Game --> Board
    Game --> Player
