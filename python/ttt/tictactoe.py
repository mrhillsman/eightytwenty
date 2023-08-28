import tkinter as tk
import random

# Create the window named "window" and disable resizing
window = tk.Tk()
window.minsize(800, 900)
window.resizable(False, False)

# Create the outer frame that will hold all other widgets
game = tk.Frame(master=window, background="#66B2FF")
game.pack(fill=tk.BOTH, expand=True)

# Global variables
current_player = ""
symbol = ""
game_over = False
winner = ""
tie = False
move_count = 0
game_started = False
game_status = tk.StringVar()


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
    print("Symbol placed")


def start_game(event):
    game_status.set("Game started")


def reset_game(event):
    game_status.set("Game reset")


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


def build_game():
    # frame for players
    players_frame = tk.Frame(master=game)
    players_frame.grid(row=0, column=1)
    oplayer = tk.Frame(master=players_frame, borderwidth=1)
    oplayer_label = tk.Label(master=oplayer, text="O", font=("Monospace", 40))
    oplayer_label.pack()
    oplayer.grid(row=0, column=0)

    xplayer = tk.Frame(master=players_frame, borderwidth=1)
    xplayer_label = tk.Label(master=xplayer, text="X", font=("Monospace", 40))
    xplayer_label.pack()
    xplayer.grid(row=0, column=2)

    # frame for gameboard
    gameboard_frame = tk.Frame(master=game, borderwidth=1)
    gameboard_frame.grid(row=1, column=0)
    for i in range(3):
        for j in range(3):
            gameboard = tk.Frame(master=gameboard_frame, borderwidth=1)
            gameboard.grid(row=i, column=j)
            gameboard_label = tk.Label(master=gameboard, text="X", font=("Monospace", 40))
            gameboard_label.pack()

    game_meta_frame = tk.Frame(master=game, borderwidth=1)
    game_meta_frame.grid(row=2, column=0)
    # frame for status and controls
    game_status_text = tk.Label(master=game_meta_frame, text="...")
    game_status_text.grid(row=1, column=1)
    game_status_text["textvariable"] = game_status

    start_button = tk.Button(master=game_meta_frame, text="Start Game")
    start_button.bind("<Button-1>", start_game)
    start_button.grid(row=2, column=0)

    reset_button = tk.Button(master=game_meta_frame, text="Reset Game")
    reset_button.bind("<Button-1>", reset_game)
    reset_button.grid(row=2, column=2)


build_game()

# Start the window's event loop
window.mainloop()
