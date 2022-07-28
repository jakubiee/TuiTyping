import curses
from curses import wrapper
import random
import json
import time
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Terminal Type Tester.")
    parser.add_argument("-t", 
                        default=15, 
                        dest="tempo", 
                        type=int, 
                        help="Test duration")
    return parser.parse_args()

def get_size_of_terminal():
    screen = curses.initscr()
    y, x = screen.getmaxyx()
    return y, x

def get_text(number_of_words):
    with open('english.json') as json_file:
        words = json.load(json_file)['words']
        x = 1
        target_text = []
        while x < number_of_words:
            target_text.append(random.choice(words))
            x+=1
        return target_text

def get_ten_words_from_text(text, tens):
    listToStr = ' '.join([str(element) for element in text[10*(tens-1):10*tens]]) 
    return listToStr


def display(stdscr, target, line, max_y, max_x):
    middle_row = int(max_y / 2)
    x_position = int((max_x / 2) - (len(target)) / 2)
    stdscr.addstr(middle_row+line, x_position, target)

def display_test(stdscr, target, current, max_y, max_x):
    middle_row = int(max_y / 2) - 1
    x_position = int((max_x / 2) - (len(target)) / 2)
    
    stdscr.addstr(middle_row, x_position, target)
    total = 0
    for i in target:
        total += 1

    for i, char in enumerate(current):
        if i == total:
            stdscr.clear()
            return True
        correct_char = target[i]
        stdscr.addstr(middle_row, x_position+i, correct_char, curses.color_pair(1))
        if char != correct_char:
            stdscr.addstr(middle_row, x_position+i, correct_char, curses.color_pair(2))
            if correct_char ==  " ":
                stdscr.addstr(middle_row, x_position+i, char, curses.color_pair(2))
        
def countdown_timer(stdscr, time_elapsed, max_y, max_x):
    middle_row = int(max_y / 2) - 5
    x_position = int((max_x / 2) - 1)
    stdscr.addstr(middle_row, x_position, str(time_elapsed))

def statistic_window(stdscr, wpm, max_y, max_x):
    stdscr.clear()
    middle_row = int(max_y / 2)
    x_position = int((max_x / 2))
    stdscr.addstr(middle_row-4, x_position-int(7/2), f"WPM {str(wpm)}")
    stdscr.addstr(middle_row-2, x_position-int(23/2), "PRESS ENTER TO CONTINUE")
    stdscr.nodelay(False)
    while True:
        key = stdscr.getkey()
        if key in ("\x0A"):
            main(stdscr)
        elif key in ("\x1b"):
            break
        
def test(stdscr, tempo):
    test_text = get_text(1000)
    test_text_string = ' '.join([str(element) for element in test_text])  
    current_text = []
    all_characters = []
    max_y, max_x = get_size_of_terminal()
    n = 0
    wpm = 0
    stdscr.nodelay(True)
    start_time = time.time()

    while True:
        time_elapsed = round(max(time.time() - start_time, 1))
        wpm = round((len(all_characters) / (time_elapsed / 60)) / 5 )
        if time_elapsed == tempo:
            break
        stdscr.refresh()
        if display_test(stdscr, get_ten_words_from_text(test_text, 1+n), current_text, max_y, max_x) == True:
            current_text = []
            n += 1
            display_test(stdscr, get_ten_words_from_text(test_text, 1+n), current_text, max_y, max_x)
        
        display(stdscr, get_ten_words_from_text(test_text, 2+n), 0, max_y, max_x)
        display(stdscr, get_ten_words_from_text(test_text, 3+n), 1, max_y, max_x)
        countdown_timer(stdscr, time_elapsed, max_y, max_x)
        
        try:
            key = stdscr.getkey()
        except:
            continue

        if key in ("\x1b"):
            break
        elif key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
                all_characters.pop()
        elif len(current_text) < len(test_text_string):
            current_text.append(key)
            all_characters.append(key)

    statistic_window(stdscr, wpm, max_y, max_x)

def main(stdscr):
    args = get_args()
    tempo = args.tempo
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.curs_set(0)
    stdscr.clear()
    
    test(stdscr, tempo)

if __name__ == "__main__":
    wrapper(main)