

x = [-3, 2, 5]
y = []
y_f = []
for i in x:
    y.append(i ** 3 + 5 * i - 7)
    y_f.append(-1.2*i**2 + 1.82*i + 38.01)
    print('x = {0}, f(x) = {1}, f\'(x) = {2}.'.format(i, i ** 3 + 5 * i - 7, -1.2*i**2 + 1.82*i + 38.01))
print('\n')
print('x =', x)
print('y =', y)
print('y\' =', y_f)

# a = 0
# b = 0
# for i in range(len(x)):
#     a = (x[i] - 41/27*x[i] - 862/27) * y[i]
#     b += a
#     print(a, b)
# print(b/3)
#
# print('\n\n\n')
#
# a1 = 0
# b1 = 0
# for i in range(len(x)):
#     a1 = (x[i] - 41/27*x[i] - 862/27) * (x[i] - 41/27*x[i] - 862/27)
#     b1 += a1
#     print(a1, b1)
# print(b1/3)
#
# print(b/b1)