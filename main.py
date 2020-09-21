import curses
import threading
import basics
import text
import files
import frills
import time

def color(screen, buffer, position, top):
    h = screen.getmaxyx()[0]
    x = "for"
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    while 1:
        for i, b in enumerate(buffer):
           if x in b:
               screen.addstr(i + top, b.index(x), x, curses.color_pair(1))
               screen.addstr(position[0], 0, buffer[top + position[0]][:position[1]])

def main(screen):
    h = screen.getmaxyx()[0]
    buffer = files.open_file()
    top = basics.set_top(screen, buffer)
    position = [0, 0]
    buffer, position, top = basics.redraw_screen(screen, buffer, position, top)

#    color_thread = threading.Thread(target=color, args=(screen, buffer, position, top))
#    color_thread.start()
    while 1:
        key = screen.getch()
        if key == curses.KEY_UP or key == curses.KEY_DOWN or key == curses.KEY_RIGHT or key == curses.KEY_LEFT:
            buffer, position, top= basics.move(screen, buffer, position, top, key)
        elif key == curses.KEY_BACKSPACE or key == 127:
            buffer, position, top = text.backspace(screen, buffer, position, top)
        elif key == curses.KEY_ENTER or key == 10:
            buffer, position, top = text.enter(screen, buffer, position, top)
        elif key == 27:
            files.save_file(buffer)
            return
        else:
            buffer, position = text.text(screen, buffer, position, top, chr(key))




if __name__ == "__main__":
    curses.wrapper(main)