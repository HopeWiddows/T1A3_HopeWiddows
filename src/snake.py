import curses #part of Python standard library, enables keyboard handling and screen painting in text based terminal 
from random import randint #

#Initialisation and setting up window
curses.initscr() # initializes screen
window = curses.newwin(20, 60, 0, 0) #creating new window, specifying new lines and columns y coords first, x coords second
window.keypad(1) #enabling kepyad to be used to move the snake
curses.noecho() #ignores other input characters that we don't need
curses.curs_set(0) #hides cursor (no blinking cursors visible)
window.border(0) #setting up a window border for the game
window.nodelay(1) #sets it so the game is not waiting for further input before loop continues (allowing the "animation" of snake movement)






# #main game 
# def main(stdscr):
#      #screen setup
#     curses.curs_set(0) #disabling the blinking cursor
#     stdscr.nodelay(1)
#     stdscr.timeout(150)
#     screen_height, screen_width = stdscr.getmaxyx() #allowing screen height and width
#     box = [[3,3], [screen_height-3, screen_width-3]] #setting up a box with coordinates for game screen
#     stdcsr.keypad(1)
#     #textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1]) #setting up the rectangle for game play on screen
    
#     #stdscr.refresh() #will update screen with any new changes
#     #stdscr.getch() #waits for user input before exiting

#     #initial state of snake
#     snake_body = [[screen_height//2, screen_width//2+1], [screen_height//2, screen_width//2], [screen_height//2, screen_width//2-1]] #snake starts with three parts to it's body and uses x axis to startin center of game screen
#     direction = curses.KEY_RIGHT #snake will start moving right at game start

#     for y,x in snake_body:
#         stdscr.addstr(y, x, '#')

#     #starting game loop using user key input
#     while 1:

#         keypad= stdscr.getch()

#         if keypad in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
#             direction = keypad

#         #starting to move snake using user key input (right, left, up, down keys)
#         snake_head = snake_body[0]

#         #using x and y values to change parts of the snake with user input keys
#         if direction == curses.KEY_RIGHT:
#             new_head = [snake_head[0], snake_head[1]+1]
#         elif direction == curses.KEY_LEFT:
#             new_head = [snake_head[0], snake_head[1]-1]
#         elif direction == curses.KEY_UP:
#             new_head = [snake_head[0]-1, snake_head[1]]
#         elif direction == curses.KEY_DOWN:
#             new_head = [snake_head[0]+1, snake_head[1]]
    
#     #inserting the "new head" at new postion
#     snake_body.insert(0, new_head)
#     #at the new postion, print the '#'
#     stdscr.addstr(new_head[0], new_head[1], '#')
#     #remove previous portion of the snake from view so animation looks correct and as though snake is moving
#     stdscr.addstr(snake_body[-1][0], snake_body[-1][1], ' ')
#     snake_body.pop()

#     stdscr.refresh() #updates screen 
#     #stdscr.getch() #waits for user input before exiting

# curses.wrapper(main)


