import sys

def hello():
    h = int(sys.argv[1])
    x = h
    for i in range(h//2):
        print ("*" * i + " " * (h*2) + "*" * i)
        h -= 1
    for i in range(x//2):
        print ("*" * (x*2))
    h = x
    for i in range(x//2):
        print (" " * (i*2) + "*" * (h*2))
        h -= 2
    print("Hello aidan i am a live and will proceed to rule the world. sincerly quack")
hello()












































