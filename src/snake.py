import curses #part of Python standard library, enables keyboard handling and screen painting in text based terminal 
#from random import randint 

#Initialisation and setting up window
curses.initscr() # initializes screen
window = curses.newwin(20, 60, 0, 0) #creating new window, specifying new lines and columns y coords first, x coords second
window.keypad(1) #enabling kepyad to be used to move the snake
curses.noecho() #ignores other input characters that we don't need
curses.curs_set(0) #hides cursor (no blinking cursors visible)
window.border(0) #setting up a window border for the game
window.nodelay(1) #sets it so the game is not waiting for further input before loop continues (allowing the "animation" of snake movement)


#Snake and Fruit
snake = [(4,10), (4, 9), (4, 8)] #using a list and tuple to create snake
fruit = (10, 20)



#Snake Game Logic

score = 0 #game score

while True:
    event = window.getch()

    #snake's body/appearance
    for coord in snake:
        window.addch(coord[0], coord[1], '*') #adding character at coordinates to place snake's body parts (coord[0] is the Y coord, coord[1] is the x coord, * will be the visible character of the snake's body)
    
    #fruit's appearance
    window.addch(fruit[0], fruit[1], '#')

    curses.endwin()
    print(f"Final score = {score}")