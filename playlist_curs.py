import curses


screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

screen.addstr("PRESS F2 FOR HELP", curses.A_REVERSE)

curses.noecho()
curses.curs_set(0)
screen.keypad(1)
top_pos = 3
left_pos = 30
screen.addstr(top_pos, left_pos, "PLAYLIST NAME\n", curses.A_BOLD)

while True:
    event = screen.getch()
    if event == curses.KEY_BACKSPACE:
        break
    if event == curses.KEY_F2:
        screen.clear()
        screen.addstr("PAUSE = down arrow\n", curses.color_pair(1))
        screen.addstr("PLAY = p\n", curses.color_pair(1))
        screen.addstr("NEXT SONG = right arrow\n", curses.color_pair(1))
        screen.addstr("QUIT = backspace", curses.color_pair(1))
    elif event == curses.KEY_RIGHT:
        screen.addstr("next song\n", curses.color_pair(3))
    elif event == ord("p"):
        screen.addstr("play\n", curses.color_pair(2))
    elif event == curses.KEY_DOWN:
        screen.addstr("pause\n", curses.color_pair(4))

curses.endwin()
