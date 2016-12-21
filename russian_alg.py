def russian(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z += y
        y <<= 1
        x >>= 1
    return z


print russian(20, 7)


def russian_rec(a, b):
    if a == 0:
        return 0
    if a % 2 == 0:
        return 2 * russian_rec(a / 2, b)
    return b + 2 * russian_rec((a - 1) / 2, b)
print russian_rec(20, 7)
