import curses #part of Python standard library, enables keyboard handling and screen painting in text based terminal 
from random import randint #allowing for random generation of items in game

#Initialisation and setting up window
curses.initscr() # initializes screen
window = curses.newwin(20, 60, 0, 0) #creating new window, specifying new lines and columns y coords first, x coords second
window.keypad(1) #enabling kepyad to be used to move the snake
curses.noecho() #ignores other input characters that we don't need
curses.curs_set(0) #hides cursor (no blinking cursors visible)
window.border(0) #setting up a window border for the game
window.nodelay(1) #sets it so the game is not waiting for further input before loop continues (allowing the "animation" of snake movement)


key = curses.KEY_RIGHT #initialising values
score = 0 #game score

#Snake and Fruit
snake = [(4, 10), (4, 9), (4, 8)] #using a list and tuple to create snake at initial coordinates
fruit = (10, 20) #fruit initial coordinates

window.addch(fruit[0], fruit[1], '*')  #prints the fruit

#Snake Game Logic
ESC = 27

while key != ESC:
    window.border(0)
    window.addstr(0, 2, 'Score: ' + str(score) + ' ') #adding score information to the top of the screen
    window.addstr(0, 23, ' Python Python ')  #adding game title to screen
    window.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120) #increasing speed of snake depending on it's length

    prev_key = key #starting game state, if no key pressed, loop continues as is
    event = window.getch()
    key = key if event == -1 else event

    if key == ord(' '):  #enable using space bar to pause game, press space again to continue
        key = -1
        while key != ord(' '):
            key = window.getch()
        key = prev_key
        continue

    #checking if a valid input key has been made
    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    #calculating next coordinates for snake's movements
    y = snake [0][0]
    x = snake [0][1]

    if key == curses.KEY_DOWN: 
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_RIGHT:
        x += 1
    if key == curses.KEY_LEFT: 
        x -= 1
    
    snake.insert(0, (y, x)) #appending list


    #check if snake collides with fruit, if true, then eats fruit and adds to body, generates new fruit on gameboard
    if snake[0] == fruit:
        score += 5
        fruit = ()
        while fruit == ():
            fruit = (randint(1, 18), randint(1,58)) # place fruit randomly on gameboard (1, 18) = y axis, (1,58) = x axis
            if fruit in snake: #checking if fruit's coord is within the snakes body, if yes repeat to place randomly elsewhere
                fruit = ()
        window.addch(fruit[0], fruit[1], '#') #prints new fruit
    #moving the snake
    else:
        snaketail = snake.pop()
        window.addch(snaketail[0], snaketail[1], ' ')

    #snake's body/appearance
    for snakebody in snake:
        window.addch(snakebody[0], snakebody[1], '*') #adding character at coordinates to place snake's body parts (coord[0] is the Y coord, coord[1] is the x coord, * will be the visible character of the snake's body)
    
    #fruit's appearance
    window.addch(snake[0][0], snake[0][1], '*')

    #checking if snake collides with game border (game over)
    if y == 0: 
        message = "You hit the wall! Game over!"
        message_score = (f"Final Score: {score}")
        window.addstr(9, 5, message)
        window.addstr(10, 5, message_score)
        window.nodelay(0)
        window.getch()
        break
    if y == 19: 
        message = "You hit the wall! Game over!"
        message_score = (f"Final Score: {score}")
        window.addstr(9, 5, message)
        window.addstr(10, 5, message_score)
        window.nodelay(0)
        window.getch()
        break
    if x == 0: 
        message = "You hit the wall! Game over!"
        message_score = (f"Final Score: {score}")
        window.addstr(9, 5, message)
        window.addstr(10, 5, message_score)
        window.nodelay(0)
        window.getch()
        break
    if x == 59:
        message = "You hit the wall! Game over!"
        message_score = (f"Final Score: {score}")
        window.addstr(9, 5, message)
        window.addstr(10, 5, message_score)
        window.nodelay(0)
        window.getch()
        break

    #check if snake collides with itself itself (game over)
    if snake [0] in snake[1:]: 
        message = "You can't eat yourself! Game Over!"
        message_score = (f"Final Score: {score}")
        window.addstr(9, 5, message)
        window.addstr(10, 5, message_score)
        window.nodelay(0)
        window.getch()
        break


    curses.endwin()
    print(f"Final score = {score}")#printing final score on screen



     # If snake crosses the boundaries, make it enter from the other side
    # if snake[0][0] == 0: snake[0][0] = 18
    # if snake[0][1] == 0: snake[0][1] = 58
    # if snake[0][0] == 19: snake[0][0] = 1
    # if snake[0][1] == 59: snake[0][1] = 1