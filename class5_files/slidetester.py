from slidepuzzle import *
import curses

def nicePrint(board):
    for y in range(BOARDHEIGHT):
        boxes = []
        for x in range(BOARDWIDTH):
            boxes.append(board[x][y])
        print(' '.join('{:4}'.format(k) for k in boxes))

def playTest(): 
    # get the curses screen window
    screen = curses.initscr()

    # turn off input echoing
    curses.noecho()

    # respond to keys immediately (don't wait for enter)
    curses.cbreak()

    # map arrow keys to special values
    screen.keypad(True)

    board = getStartingBoard()
    try:
        while True:
            screen.clear()           # clear screen
            for x in range(BOARDWIDTH):
                for y in range(BOARDHEIGHT):
                    if board[x][y] != None:
                        screen.addstr(y, x*5, '{:5}'.format(board[x][y]))
                    else:
                        screen.addstr(y, x*5, '    _')
            screen.addstr(BOARDHEIGHT+1, 0, "Move up/down/left/right, q to quit: ")
            char = screen.getch()    # read single key (character)
            x,y = getBlankPosition(board)
            if char == ord('q'):
                break
            elif char == curses.KEY_RIGHT:
                if (isValidMove(board, RIGHT)):
                    board[x][y], board[x-1][y] = board[x-1][y], board[x][y]
            elif char == curses.KEY_LEFT:
                if (isValidMove(board, LEFT)):
                    board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
            elif char == curses.KEY_UP:
                if (isValidMove(board, UP)):
                    board[x][y], board[x][y+1] = board[x][y+1], board[x][y]
            elif char == curses.KEY_DOWN:
                if (isValidMove(board, DOWN)):
                    board[x][y], board[x][y-1] = board[x][y-1], board[x][y]
    finally:
        # shut down cleanly
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()



