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



def main():
    menu()
    


    
'''Prints a board with slots to be filled up by user or computer inputs'''
def print_board(slots):
    print("\n")
    print(" " + slots[0] + " | " + slots[1] + " | " + slots[2] + " ")
    print("---+---+---")
    print(" " + slots[3] + " | " + slots[4] + " | " + slots[5] + " ")
    print("---+---+---")
    print(" " + slots[6] + " | " + slots[7] + " | " + slots[8] + " ")
    print("\n")    

print_board([])

]