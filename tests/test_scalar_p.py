
from numpy import array, dot


def scalar_composition(point, x_or_fx, array_x_or_fx):
    composition = 0
    array_x_or_fx = array_x_or_fx * x_or_fx
    for i in array_x_or_fx:
        composition += i * point
    scalar_composition_full = composition * 1 / len(array_x_or_fx)
    return scalar_composition_full


def with_dot(point, array_x_or_fx):
    answer = dot(point, array_x_or_fx)
    if type(answer) == 'numpy.ndarray':
        return answer.sum()
    else:
        return answer


def main():
    array_x = array([-3, -2, -1, 0, 1, 2, 3])
    array_fx = array([0, -2, -2, 0, 4, 10, 18])
    print(scalar_composition(point=1, x_or_fx=1, array_x_or_fx=array_x))
    # print(with_dot(point=))


if __name__ == '__main__':
    main()
