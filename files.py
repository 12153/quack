import curses
import random
import sys

def open_file():
    if len(sys.argv) == 2:
        try:
            f = open(sys.argv[1], 'r')
            lines = f.readlines()
            f.close()
            ret = []
            for l in lines:
                if l[-1] == '\n':
                    ret += [l[:-1]]
                else:
                    ret += [l]
            return ret
        except:
            f = open(sys.argv[1], 'w')
            f.close()
            return [' ']
    else:
        return [' ']

def save_file(buffer):
    stre = ''
    for b in buffer:
        stre += b + '\n'
    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'w')
    else:
        f = open("defualt_file"+str(random.randint(1000, 9999)), 'w')
    f.write(stre)
    f.close