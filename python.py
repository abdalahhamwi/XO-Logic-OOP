class Player:
    def __ini__(self):
        self.name = ""
        self.symbol = ""
        
    def choose_name(self):
        while True:
            name = input ("Enter your name (letters only): ")
            if name.isalpha():
              self.name = name
              break
            print("Invalid name. please use letters only. ")
            
    def choose_symbol(self):
        while True :
            symbol = input(f"{self.name} Choose your symbol (a single letters):")
            if symbol.isalpha() and len (symbol) == 1 :
                self.symbol = symbol.upper()
                break
            print("Invalid symbol. please choose a single letters.")
            
class Menu:
    def display_main_menu(self):
        while True :
            print("Welcome to X-O Game!")
            print("1. Start Game")
            print("2. Quit Game")
            choice = input("Enter your choice (1 or 2): ")
            if choice == "1" or choice == "2":
             return choice
            break
        print("Invalid choice. Please enter 1 or 2.")
        
    def display_endgame_menu(self):
        while True:
            print("Game Over!")
            print("1. Restart Game")
            print("2. Quit Game")
            choice = input("Enter your choice (1 or 2): ")
            if choice == "1" or choice == "2":
                return choice
            print("Invalid choice. Please enter 1 or 2.")
            
class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
        
    def display_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 5)
                
    def update_board(self, choice, symbol): 
        if self.is_vaild_move (choice):
            self.board[choice-1] = symbol
            return True
        return False
                
    def is_vaild_move(self, choice):
      return self.board[choice-1].isdigit()
      
    def rest_board(self):
        self.board = [str(i) for i in range(1, 10)]
          
class Game:
    def __init__(self):
        self.player = [ Player(), Player() ]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0
        
    def start_game(self):
            choice = self.menu.display_main_menu()
            if choice == "1":
                self.setup_players()
                self.play_game()
            else:
               self.quit_game()
               
    def setup_players(self):
        for number, player in enumerate(self.player, start=1):
            print(f"Player {number}, Enter your details:.")
            player.choose_name()
            player.choose_symbol()
            
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_winner() or self.check_draw():
              choice = self.menu.display_endgame_menu()
              if choice == "1":
                  self.restart_game()
              else:
                  self.quit_game()