# x = 5
# y = 3
# z = 0
#
# while x > 0:
#     z += y
#     x -= 1
# print z


# def clique(n):
#     count = 0
#     print "in a clique..."
#     count += 1
#     for j in range(n):
#         for i in range(j):
#             count += 1
#     print count
# clique(4)


def clique_check(n):
    return ((n * (n-1))/2) + (2 + n)

print clique_check(4)