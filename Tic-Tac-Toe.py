import check_input
import random
import sys

'''Displays the main menu for the player to pick a game mode of view scores'''
def menu():
    print("TIC-TAC-TOE\n")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    print("3. View Scores")
    
    #This function checks if the user input is valid and returns the corresponding option
    user_input = check_input.get_int_range("Select an option (1-3): ", 1, 3)
    if user_input == 1:
        return 1
    elif user_input == 2:
        return 2
    elif user_input == 3:
        return 3
    #My style of coding is to always return inputs to main function and have that act as an intermediary between functions

'''Sets up and monitors a player vs player game'''
def player_vs_player():
    game_board = board()
     
    #collects player names
    x_name = input("Player X, enter your name: ")
    o_name = input("Player O, enter your name: ")

    #While loop to keep the game running until a player wins or the game is a draw
    while True:
        game_board.print_board(game_board.slots)
        

    
'''Board class to both display board and keep track of game state'''
class board():
    def __init__(self):
        #code for slots is quite repetitive, but I wanted to keep it simple and easy to understand
        self.slot_1 = '1'
        self.slot_2 = '2'
        self.slot_3 = '3'
        self.slot_4 = '4'
        self.slot_5 = '5'
        self.slot_6 = '6'
        self.slot_7 = '7'
        self.slot_8 = '8'
        self.slot_9 = '9'
        self.slots = [self.slot_1, self.slot_2, self.slot_3, self.slot_4, self.slot_5, self.slot_6, self.slot_7, self.slot_8, self.slot_9]
    
    '''Prints a board with slots to be filled up by user or computer inputs'''
    def print_board(self, slots):
        print("\n")
        print(" " + slots[0] + " | " + slots[1] + " | " + slots[2] + " ")
        print("---+---+---")
        print(" " + slots[3] + " | " + slots[4] + " | " + slots[5] + " ")
        print("---+---+---")
        print(" " + slots[6] + " | " + slots[7] + " | " + slots[8] + " ")
        print("\n")    
    
    '''Updates the board with user or computer input, checks if the slot is already taken'''
    def update_board(self, slots, input, symbol):
        #Again, repetitive code but simple to understand
        if input == 1 and slots[0] != 'X' and slots[0] != 'O':
            slots[0] = symbol
        elif input == 2 and slots[1] != 'X' and slots[1] != 'O':
            slots[1] = symbol
        elif input == 3 and slots[2] != 'X' and slots[2] != 'O':
            slots[2] = symbol
        elif input == 4 and slots[3] != 'X' and slots[3] != 'O':
            slots[3] = symbol
        elif input == 5 and slots[4] != 'X' and slots[4] != 'O':
            slots[4] = symbol
        elif input == 6 and slots[5] != 'X' and slots[5] != 'O':
            slots[5] = symbol
        elif input == 7 and slots[6] != 'X' and slots[6] != 'O':
            slots[6] = symbol
        elif input == 8 and slots[7] != 'X' and slots[7] != 'O':
            slots[7] = symbol
        elif input == 9 and slots[8] != 'X' and slots[8] != 'O':
            slots[8] = symbol
        else:
            print("Error: Slot already taken")
            return False  
        return True
        
    '''checks if there is a winner after every turn'''
    def check_winner(self, slots):
        #Checks all possible winning combinations
        if slots[0] == slots[1] == slots[2]:
            return True
        elif slots[3] == slots[4] == slots[5]:
            return True
        elif slots[6] == slots[7] == slots[8]:
            return True
        elif slots[0] == slots[3] == slots[6]:
            return True
        elif slots[1] == slots[4] == slots[7]:
            return True
        elif slots[2] == slots[5] == slots[8]:
            return True
        elif slots[0] == slots[4] == slots[8]:
            return True
        elif slots[2] == slots[4] == slots[6]:
            return True
        else:
            return None
    
    '''checks if the game is a draw after every turn'''
    def check_draw(self, slots):
        
        #Increments a counter for every filled slot. If counter reaches 9, all slots are filled and game is a draw
        count = 0
        for slot in slots:
            if slot == 'X' or slot == 'O':
                count += 1
        if count == 9:
            return True
        else:
            return False
    

#Everything below here is just for testing purposes, will be removed in final version

game_board = board()
game_board.print_board(game_board.slots)
  
win = None
while win == None:
    while True:
        user_input = check_input.get_int_range("Select a slot (1-9): ", 1, 9)
        valid_update = game_board.update_board(game_board.slots, user_input, 'X')
        if valid_update == True:
            break
        else:
            continue
    

    game_board.print_board(game_board.slots)
    win = game_board.check_winner(game_board.slots)
print("Works")


def main():
    menu()
