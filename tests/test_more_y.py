from itertools import groupby

from numpy import array, vstack

points = [array([1, 1, 2, 3, 3, 4, 5, 5, 5]), array([1, 10, 2, 3, 8, 4, 5, 7, 9])]

xy_array = vstack((points[0], points[1]))

# for i in range(len(points[0])):
#
#     pass

# new = groupby(xy_array)
new = groupby(points[0], points[1])

#
# print(new)

# new = []
#
# for i in range(len(points[0])):
#     new.append((points[0][i], points[1][i]))
#
# print(new)
#
# new = groupby(new)

print(new)
