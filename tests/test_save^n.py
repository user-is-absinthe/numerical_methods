
from numpy import array, vstack


def crete_equation(degree=array([]), to_function=array([])):
    if len(degree) == 0:
        print('Null degree?')
        return 0
    elif len(to_function) == 0:
        print('Null x?')
        return 0

    # beautiful_line = ''
    # for i in range(len(degree)):
    #     line = '{0}x^{1}'.format(degree[i], len(degree) - i - 1)
    #     beautiful_line += line
    # print(beautiful_line)

    fx = []
    for this_x in to_function:
        this_fx = 0
        for i in range(len(degree)):
            this_fx += degree[i] * this_x ** (len(degree) - i - 1)
        fx.append(this_fx)

    fx = array(fx)

    to_print = vstack((to_function, fx))
    print(to_print)
    # print(fx)
    return fx


if __name__ == '__main__':
    number = array([6, 8, 10, -3, 9])
    x = array([-5, -3, -1, 0, 1, 3, 5])
    print(number)
    crete_equation(degree=number, to_function=x)
