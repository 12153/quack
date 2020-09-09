import curses

def set_top(screen, buffer):
    h = screen.getmaxyx()[0]
    if len(buffer) > h:
        return len(buffer) - h
    else:
        return 0

def redraw_screen(screen, buffer, position, top):
    h = screen.getmaxyx()[0]
    screen.clear()
    if top < 0:
        top = 0
    if len(buffer) > h:
        for i in range(top, top + h):
            screen.addstr(i - top, 0, buffer[i])
    else:
        for i in range(top, len(buffer)):
            screen.addstr(i - top, 0, buffer[i])
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