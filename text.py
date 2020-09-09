import curses
import basics 

def text(screen, buffer, position, top, key):
    buffer[position[0] + top] = buffer[position[0] + top][:position[1]] + key + buffer[position[0] + top][position[1]:]
    position[1] += 1
    screen.addstr(position[0], 0, buffer[top + position[0]])
    screen.addstr(position[0], 0, buffer[top + position[0]][:position[1]])
    return buffer, position

def backspace(screen, buffer, position, top):
    w = screen.getmaxyx()[1]
    if position[1] > 0:    
        buffer[position[0] + top] = buffer[position[0] + top][:position[1] - 1] + buffer[position[0] + top][position[1]:]
        position[1] -= 1
        screen.addstr(position[0], 0, " " * w)
        screen.addstr(position[0], 0, buffer[top + position[0]])
        screen.addstr(position[0], 0, buffer[top + position[0]][:position[1]])
    elif position[1] == 0 :
        if position[0] == 0:
            screen.addstr(20,10,"z"*15)
            if top > 0:
                top -= 1
            basics.redraw_screen(screen, buffer, position, top)
            return buffer, position, top
        temp = buffer[position[0] + top][position[1]:]
        position[0] -= 1
        position[1] = len(buffer[position[0] + top])
        buffer[position[0] + top] += temp 
        buffer = buffer[:position[0] + top + 1] + buffer[position[0] + top + 2:]
        basics.redraw_screen(screen, buffer, position, top)
    return buffer, position, top

def enter(screen, buffer, position, top):
    h = screen.getmaxyx()[0]
    temp = buffer[position[0] + top][position[1]:]
    buffer[position[0] + top] = buffer[position[0] + top][:position[1]]
    if position[0] + 1 == h and (h + top) < len(buffer):
        top += 1
    elif position[0] < h - 1:
        position[0] += 1
    buffer = buffer[:position[0] + top] + [temp] + buffer[position[0] + top:]
    position[1] = 0
    basics.redraw_screen(screen, buffer, position, top)
    return buffer, position, top