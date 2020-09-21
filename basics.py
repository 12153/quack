import curses

functions_list = ["hello"]

def set_top(screen, buffer):
    h = screen.getmaxyx()[0]
    if len(buffer) > h:
        return len(buffer) - h
    else:
        return 0

def redraw_screen(screen, buffer, position, top):
    global functions_list
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    words = [["for ", "while ", "in ","if ", "else:", "elif " "return ", "with ", "not ", "import "],
    ["len", "range", "enumerate", "print"],
    ["def "], functions_list]
    h = screen.getmaxyx()[0]
    screen.clear()
    if top < 0:
        top = 0
    if len(buffer) > h:
        for i in range(top, top + h):
            screen.addstr(i - top, 0, buffer[i%h])
    else:
        for i in range(top, len(buffer)):
            screen.addstr(i - top, 0, buffer[i])
            if buffer[i][:3] == "def" and buffer[i][-1] == ":":
                if "(" in buffer[i]:
                    functions_list += [buffer[i][4:buffer[i].index("(")]]
            for y, line in enumerate(words):
                for w in line:
                    if w in buffer[i]:
                        screen.addstr(i - top, buffer[i].index(w), w, curses.color_pair(y+1))
    screen.addstr(position[0], 0, buffer[top + position[0]][:position[1]])
    return buffer, position, top

def move(screen, buffer, position, top, key):
    h = screen.getmaxyx()[0]
    if key == curses.KEY_UP:
        if position[0] == 0 and top > 0:
            top -= 1
        elif position[0] > 0:
            position[0] -= 1
        if len(buffer[position[0] + top]) < position[1]:
            position[1] = len(buffer[position[0] + top])
    elif key == curses.KEY_DOWN:
        if position[0] == h - 1 and (h + top) < len(buffer):
            top += 1
        elif position[0] < h - 1 and position[0]+top+1 < len(buffer):
            position[0] += 1
        if len(buffer[position[0] + top]) < position[1]:
            position[1] = len(buffer[position[0] + top])
    elif key == curses.KEY_RIGHT:
        if position[1] < len(buffer[position[0] + top]):
            position[1] += 1
    elif key == curses.KEY_LEFT:
        if position[1] > 0:
            position[1] -= 1
    buffer, position, top = redraw_screen(screen, buffer, position, top)
    return buffer, position, top