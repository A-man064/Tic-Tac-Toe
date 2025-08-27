import check_input
import random
import sys

'''Displays the main menu for the player to pick a game mode of view scores'''
def menu():
    print("TIC-TAC-TOE\n")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    print("3. View Scores")
    user_input = check_input.get_int_range("Select an option (1-3): ", 1, 3)
    if user_input == 1:
        return 1
    elif user_input == 2:
        return 2
    elif user_input == 3:
        return 3




def main():
    menu()
    

main()
    

    