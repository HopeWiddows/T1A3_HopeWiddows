import curses #part of Python standard library, enables keyboard handling and screen painting in text based terminal 
from curses import textpad #simple textbox editing widget

#Initialisation
#screen = curses.initscr() # initializes screen

#main game 
def main(stdscr):
     #screen setup
    curses.curs_set(0) #disabling the blinking cursor
    screen_height, screen_width = stdscr.getmaxyx() #allowing screen height and width
    box = [[3,3], [screen_height-3, screen_width-3]] #setting up a box with coordinates for game screen
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1]) #setting up the rectangle for game play on screen
    
    #stdscr.refresh() #will update screen with any new changes
    #stdscr.getch() #waits for user input before exiting

    #initial state of snake
    snake_body = [[screen_height//2, screen_width//2+1], [screen_height//2, screen_width//2], [screen_height//2, screen_width//2-1]] #snake starts with three parts to it's body and uses x axis to startin center of game screen
    direction = curses.KEY_RIGHT #snake will start moving right at game start

    for y, x in snake_body:
        stdscr.addstr(y, x, '#')

    stdscr.getch() #waits for user input before exiting




curses.wrapper(main)


