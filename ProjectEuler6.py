def add():
    global s
    s = 0
    for x in range(101):
        s = s + x**2

    square()


def square():
    n = 0
    sq = 0
    for y in range(101):
        n = n + y
        sq = n**2
    difference = sq - s
    print(difference)

add()
