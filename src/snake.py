import curses #part of Python standard library, enables keyboard handling and screen painting in text based terminal 
from curses import textpad #simple textbox editing widget

#Initialisation
#screen = curses.initscr() # initializes screen

 #screen setup
def main(stdscr):
    curses.curs_set(0) #disabling the blinking cursor
    screen_height, screen_width = stdscr.getmaxyx() #allowing screen height and width
    box = [[3,3], [screen_height-3, screen_width-3]] #setting up a box with coordinates for game screen
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1]) #setting up the rectangle for game play on screen
    stdscr.refresh() #will update screen with any new changes
    stdscr.getch() #waits for user input before exiting

curses.wrapper(main)
