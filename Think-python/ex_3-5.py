def top():
    print "+",
    print "-" * 4,
    print "+",
    print "-" * 4,
    print "+"

def side():
    print "|",
    print " " * 4,
    print "|",
    print " " * 4,
    print "|"

def repeat(f, n):
    for i in range(n):
        f()

def draw_2x2():
    top()
    repeat(side, 4)
    top()
    repeat(side, 4)
    top()

draw_2x2()

def draw_4x4():
    top(), 
