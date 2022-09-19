import curses
from locale import currency
from src.colors import init_colors
from src import utilities 

menu = ["Time", "Back"]
time = ["", "Back"]

def time_menu(stdscr):
    stdscr.clear()
    tempo = utilities.get_setting_value("time")
    current_row = 0
    time[0] = f"<{tempo}>"
    print_menu(stdscr, current_row, time)
    
    while True: 
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1

        if current_row == 0:
            if key == curses.KEY_LEFT and tempo > 0:
                tempo -= 5
            elif key == curses.KEY_RIGHT:
                tempo += 5
            elif key == curses.KEY_ENTER or key in [10,13]:
                utilities.edit_setting_value("time", tempo)
                break
        elif current_row == 1:
            if key == curses.KEY_ENTER or key in [10,13]:
                break

        time[0] = f"<{tempo}>"
        print_menu(stdscr, current_row, time)

def print_menu(stdscr, selected_row, list):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(list):
        y = h//2 - len(list)//2 + idx - 1
        x = w//2 - len(row)//2 
        if idx == selected_row:
            stdscr.attron(curses.color_pair(4))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(4))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def settings(stdscr):
    curses.curs_set(0)
    init_colors()
    current_row = 0

    print_menu(stdscr, 0, menu)
    key = stdscr.getch()
    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10,13]:
            match current_row:
                case 0:
                    time_menu(stdscr)
                case 1:
                    break
    
        print_menu(stdscr, current_row, menu)