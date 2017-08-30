def do_twice(f, v):
    f(v)
    f(v)

def print_twice(value):
    print value

do_twice(print_twice, "Jon")

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

do_four(print_twice, "Spam")


