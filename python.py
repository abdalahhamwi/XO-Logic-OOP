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
            