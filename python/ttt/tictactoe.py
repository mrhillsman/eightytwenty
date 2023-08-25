from tkinter import *
import random

# Global variables
current_player = ""
symbol = ""
game_over = False
winner = ""
tie = False
move_count = 0
game_started = False


def initialize_game():
    current_player = ""
    symbol = ""
    game_over = False
    winner = ""
    tie = False
    move_count = 0
    game_started = False

    reset_gameboard()

    random.Random(random.seed(float)).random()




def reset_gameboard():
    pass


def switch_player():
    pass


def place_symbol():
    pass


def start_game():
    pass


def reset_game():
    pass


def update_gameboard():
    pass


def check_for_winner():
    def check_rows():
        pass

    def check_columns():
        pass

    def check_diagonals():
        pass

    check_rows()
    check_columns()
    check_diagonals()


root = Tk()

root.mainloop()