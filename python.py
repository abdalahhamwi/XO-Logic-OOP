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