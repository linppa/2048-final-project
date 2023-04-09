import turtle
import random

'''
Linda Quach
CS 5001 - Spring 2023
Project - 2048

This program contains the functions used in the 2048 game. It utilizes Python's
Turtle and Random libraries.

The game of 2048 is
a simple 1-player board game, comprising of a 4x4 grid of numbers. The player
starts with two numbers (2 or 4) on the board, and in each turn, the player can
move the numbers up, down, left, or right. If two numbers are of the same value,
the numbers merge into one, and the value of the new number is the sum of the
two, essentially "sliding" the numbers together. The numbers can only slide in a
direction to occupy the farthest blank cell without jumping over another number.

The player's goal is to obtain the number 2048 on the board. The game ends when
this is obtained, or the board is full and no more moves can be made.

Resources:
https://cs111.wellesley.edu/labs/lab02/colors
https://www.geeksforgeeks.org/2048-game-in-python/#
https://www.geeksforgeeks.org/turtle-shape-function-in-python/

'''
# revisions to do
# delete print statements
# check lines not longer than 80 characters


# ---- GLOBAL VARIABLES ----
global_score = 0
global_game_board = []
GRID_SIZE = 4

# ---- GLOBAL INTERFACE ----
screen = turtle.Screen()
screen.tracer(0, 0)
score = turtle.Turtle()
grid = turtle.Turtle()
game_over = turtle.Turtle()
win = turtle.Turtle()
font = ('courier', 12, 'normal')
font2 = ('courier', 20, 'normal')


# ---- TURTLE SETUP ----

def start_window():
    '''
    start_window is a helper function that presents the window setup, including
    initial grid, score, & menu options. Also calls key bindings for controls.
    '''
    screen.setup(600, 630)
    screen.title('CS5001 2048 :D')
    screen.bgcolor('seashell2')
    draw_grid()
    # text & score
    display_score()
    display_menu()
    # key bindings
    key_binding()
    # continue run window
    turtle.mainloop()


def draw_grid():
    '''
    draw_grid creates blocks from square turtles, & stamps them on the game
    board. Numbers are written on top of the blocks if they are not 0.
    '''
    grid.hideturtle()
    grid.clear()
    grid.speed(0)
    grid.penup()
    grid.shape('square')
    grid.shapesize(4, 4, 10)

    color_dictionary = {0: 'AntiqueWhite4', 2: 'AntiqueWhite3', 4: 'wheat3', 8: 'goldenrod3', 
                        16: 'DarkGoldenrod2', 32: 'goldenrod1', 64: 'sienna3', 128: 'sienna2', 
                        256: 'sienna4', 512: 'DarkSeaGreen4', 1024: 'DarkSeaGreen3', 2048: 'CadetBlue3'}

    y_coordinate = 120
    for row in range(GRID_SIZE):
        # strange bug where a rougue turtle visible, so i hide it with grid
        x_coordinate = -144
        for column in range(GRID_SIZE):
            grid.goto(x_coordinate, y_coordinate)
            # colors
            if global_game_board[row][column] in color_dictionary:
                grid.color(color_dictionary[global_game_board[row][column]])
            else:
                grid.color('AntiqueWhite4')
            grid.stamp()
            if global_game_board[row][column] != 0:
                number = turtle.Turtle()
                number.hideturtle()
                number.color('white')
                number.penup()
                number.goto(x_coordinate, y_coordinate - 15)
                number.write(str(global_game_board[row][column]), align = 'center', font=("courier", 25, "bold"))
            x_coordinate += 100
        y_coordinate -= 100


# ---- SCORE FUNCTIONS & DISPLAY TEXTS ----
# update score
def update_score(add_points: int):
    global global_score
    global_score += add_points
    return global_score

# display & refresh current score
def display_score():
    global global_score
    score.clear()
    score.hideturtle()
    score.penup()
    score.goto(-250, 222)
    score.color('sienna')
    score.write(f"Score:{global_score}", font = font)

# print game board to terminal
def print_stacked_list(game_board):
    for row in game_board:
        print(row)
    print('')
    
# display options to restart & close game
def display_menu():
    menu = turtle.Turtle()
    menu.hideturtle()
    menu.penup()
    menu.goto(-250, 250)
    menu.color('AntiqueWhite4')
    menu.write(f"To end game, press 'E'\n"
               f"To restart,  press 'R'", font = font)

# game over text
def display_game_over():
    game_over.hideturtle()
    game_over.penup()
    game_over.goto(-250, 165)
    game_over.color('firebrick2')
    game_over.write(f"GAME OVER!\n", font = font2)

# check game over
def check_game_over():
    global global_game_board
    # check if board is full
    for row in global_game_board:
        for number in row:
            if number == 0:
                return False
    # check if there are any adjacent matching numbers
    # check rows
    for row in global_game_board:
        for i in range(GRID_SIZE - 1):
            if row[i] == row[i+1]:
                return False
    # check columns
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE - 1):
            if global_game_board[j][i] == global_game_board[j+1][i]:
                return False
    display_game_over()
    print('GAME OVER!')
    return True

def display_win():
    win.hideturtle()
    win.penup()
    win.goto(-250, 165)
    win.color('PaleGreen4')
    win.write(f"YOU WIN!\n", font = font2)
    
    print('Thank you for playing 2048! \n& for helping us learn '
          'throughout the semester, \n'
          'to make this game possible! :)\n')
    win.goto(-250, -285)
    win.color('PaleGreen4')
    win.write(f'Thank you for playing 2048! \n& for helping us learn '
                     'throughout the semester, \n'
                     'to make this game possible! :)', font = font)
    
def check_win():
    global global_game_board
    for row in global_game_board:
        for number in row:
            if number == 2048:
                display_win()
                print('YOU WIN!')
                return True
    return False


# ---- KEY BINDINGS ----
# listen for key presses
def key_binding():
    turtle.listen()
    turtle.onkey(move_up, 'Up')
    turtle.onkey(move_down, 'Down')
    turtle.onkey(move_left, 'Left')
    turtle.onkey(move_right, 'Right')
    turtle.onkey(restart_game, 'r')
    turtle.onkey(screen.bye, 'e')
    
    # bind error function to all other keys - yikes
    for key in ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3',
                '4', '5', '6', '7', '8', '9', '0', 'space',
                'Return', 'Escape', 'BackSpace', 'Tab', 'Caps_Lock',
                'Shift_L', 'Shift_R', 'Control_L', 'Control_R',
                'Alt_L', 'Alt_R', 'Pause', 'Scroll_Lock', 'Home',
                'Insert', 'Delete', 'End', 'Page_Up', 'Page_Down',
                'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8',
                'F9', 'F10', 'F11', 'F12', '<', '>', '?', '/',
                ':', ';', '"', "'", '[', ']', '{', '}', '|',
                '+', '-', '*', '=', '_', '(', ')', '&', '^',
                '%', '$', '#', '@', '!', '~', '`', 'comma', 'period']:
        turtle.onkey(key_error, key)
    
def key_error():
    print('Invalid key!')
    key_error = turtle.Turtle()
    key_error.hideturtle()
    key_error.penup()
    key_error.goto(50, -250)
    key_error.color('firebrick2')
    key_error.write(f"Invalid key! Please try again.", font = font)
    turtle.ontimer(key_error.clear, 500)

# restart game, clear screen, and start new game
def restart_game():
    global global_game_board, global_score
    global_game_board = []
    global_score = 0
    game_over.clear()
    win.clear()
    global_game_board = start_board()
    start_window()
    return global_game_board, global_score

# move left
def move_left():
    global global_game_board
    print('left:')
    # check if move was made
    valid_move = False
    for row in global_game_board:
        # combine adjacent matching numbers
        for i in range(GRID_SIZE - 1, 0, -1):
            if row[i] != 0:
                for j in range(i-1, -1, -1):
                    if row[j] != 0:
                        if row[i] == row[j]:
                            row[i], row[j] = (row[i] * 2), 0
                            update_score((row[i]))
                            valid_move = True
                        break
        # shift all non-zero numbers to the left
        # new list of non-zero numbers row
        non_zero_numbers = [number for number in row if number != 0]
        # empty spaces in row
        empty_spaces = GRID_SIZE - len(non_zero_numbers)
        # new list of zeroes with length = to number of empty space
        zeroes = [0] * empty_spaces
        new_row = non_zero_numbers + zeroes
        # if rows are different, move was made
        if row != new_row:
            valid_move = True
        row[:] = new_row
        
    if valid_move == True:
        add_new_number()
        display_score()
    else:
        print("Invalid move!")
    
    check_game_over()
    check_win()

    draw_grid()
    print_stacked_list(global_game_board)
    return global_game_board

# move right
def move_right():
    global global_game_board
    print('right:')
    # check if move was made
    valid_move = False
    for row in global_game_board:
        # combine adjacent matching numbers
        for i in range(GRID_SIZE - 1):
            if row[i] != 0:
                for j in range(i+1, GRID_SIZE):
                    if row[j] != 0:
                        if row[i] == row[j]:
                            row[i], row[j] = (row[i] * 2), 0
                            update_score((row[i]))
                            valid_move = True
                        break
        # shift all non-zero numbers to the right
        # new list containing all non-zero numbers in the current row
        non_zero_numbers = [number for number in row if number != 0]
        # empty spaces in row
        empty_spaces = GRID_SIZE - len(non_zero_numbers)
        # new list of zeroes with length = to number of empty space
        zeroes = [0] * empty_spaces
        new_row = zeroes + non_zero_numbers
        # if rows are different, move was made
        if row != new_row:
            valid_move = True
        row[:] = new_row

    if valid_move == True:
        add_new_number()
        display_score()
    else:
        print("Invalid move!")
    
    check_game_over()
    check_win()
    
    draw_grid()
    print_stacked_list(global_game_board)
    return global_game_board

# move up
def move_up():
    global global_game_board
    print('up:')
    # check if move was made
    valid_move = False
    for column in range(GRID_SIZE):
        # combine adjacent matching numbers
        for i in range(GRID_SIZE - 1, 0, -1):
            if global_game_board[i][column] != 0:
                for j in range(i-1, -1, -1):
                    if global_game_board[j][column] != 0:
                        if global_game_board[i][column] == global_game_board[j][column]:
                            global_game_board[i][column], global_game_board[j][column] = (global_game_board[i][column] * 2), 0
                            update_score((global_game_board[i][column]))
                            valid_move = True
                        break
        # shift all non-zero numbers up
        # new list containing all non-zero numbers in the current column
        non_zero_numbers = [number for number in [row[column] for row in global_game_board] if number != 0]
        # empty spaces in column
        empty_spaces = GRID_SIZE - len(non_zero_numbers)
        # new list of zeroes with length = to number of empty space
        zeroes = [0] * empty_spaces
        new_column = non_zero_numbers + zeroes
        # if columns are different, move was made
        if [row[column] for row in global_game_board] != new_column:
            valid_move = True
        # update columns
        for i in range(GRID_SIZE):
            global_game_board[i][column] = new_column[i]
    
    if valid_move == True:
        add_new_number()
        display_score()
    else:
        print("Invalid move!")
    
    check_game_over()
    check_win()
    
    draw_grid()
    print_stacked_list(global_game_board)
    return global_game_board

# move down
def move_down():
    global global_game_board
    print('down:')
    # check if move was made
    valid_move = False
    for column in range(GRID_SIZE):
        # combine adjacent matching numbers
        for i in range(GRID_SIZE - 1):
            if global_game_board[i][column] != 0:
                for j in range(i+1, GRID_SIZE):
                    if global_game_board[j][column] != 0:
                        if global_game_board[i][column] == global_game_board[j][column]:
                            global_game_board[i][column], global_game_board[j][column] = (global_game_board[i][column] * 2), 0
                            update_score((global_game_board[i][column]))
                            valid_move = True
                        break
        # shift all non-zero numbers down
        # new list containing all non-zero numbers in the current column
        non_zero_numbers = [number for number in [row[column] for row in global_game_board] if number != 0]
        # empty spaces in column
        empty_spaces = GRID_SIZE - len(non_zero_numbers)
        # new list of zeroes with length = to number of empty space
        zeroes = [0] * empty_spaces
        new_column = zeroes + non_zero_numbers
        # if columns are different, move was made
        if [row[column] for row in global_game_board] != new_column:
            valid_move = True
        # update columns
        for i in range(GRID_SIZE):
            global_game_board[i][column] = new_column[i]
            
    if valid_move == True:
        add_new_number()
        display_score()
    else:
        print("Invalid move!")
    
    check_game_over()
    check_win()
    
    draw_grid()
    print_stacked_list(global_game_board)
    return global_game_board
    

# ---- GAME FUNCTIONS ----
# create game board
def initialize_board():
    global global_game_board
    # iterate through 4 rows
    for size in range(GRID_SIZE):
        # create a list of 4 zeros
        global_game_board.append([0] * GRID_SIZE)
    
    # add two numbers to the board
    add_new_number()
    add_new_number()

    return global_game_board

# starting board ready with 2 numbers
def start_board():
    global global_game_board
    global_game_board = initialize_board()
    print_stacked_list(global_game_board)
    return global_game_board

# add a new number to the board
def add_new_number():
    global global_game_board
    
    check_game_over()
    check_win()
    
    print(f'new number added:')
    
    while True:
        # pick a random row and column
        random_row = random.randint(0, GRID_SIZE - 1)
        random_column = random.randint(0, GRID_SIZE - 1)
        # if the cell is empty, add a 2 or 4
        if global_game_board[random_row][random_column] == 0:
            break
    
    global_game_board[random_row][random_column] = random.choice([2, 4])
    return global_game_board