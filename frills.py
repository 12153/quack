import curses
import time

def color(screen, buffer, position, top):
    h = screen.getmaxyx()[0]
    #while 1:
    #    time.sleep(0.1)
    for i, b in enumerate(buffer):
       if "for" in b:
           screen.addstr(i + top, 10, "z"*10)
           screen.addstr(position[0], 0, buffer[top + position[0]][:position[1]])
        