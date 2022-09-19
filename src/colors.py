import curses

def init_colors():
    # Default text
    curses.init_pair(1, curses.COLOR_WHITE, 0)
    # Green text
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # Red text
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    # Black text, white background
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)