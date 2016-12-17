import math

count = 50


def time(n):
    """ Return the number of steps
    necessary to calculate
    `print countdown(n)`"""
    # steps = 0
    steps = 3 + 2 * math.ceil(n / 5)
    return steps


def countdown(x):
    y = 0
    while x > 0:
        x -= 5
        y += 1
    print y


print countdown(count)
print time(count)
