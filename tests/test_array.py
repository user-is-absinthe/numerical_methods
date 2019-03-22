from numpy import empty, hsplit, vsplit

array = empty((3, 3))
print(array)
print(type(array))

horizontal = hsplit(array, (1, 1))
print(horizontal)

vertical = vsplit(array, 1)
print(vertical)
