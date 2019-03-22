# system libs
from sys import argv, exit

# another libs
from PIL import Image
from numpy import array

# code


def read_img(path: object) -> object:
    try:
        my_img = Image.open(path)
    except FileNotFoundError:
        print('File does`n exist. \nProgramm wil close.')
        exit(1)

    size_image = my_img.size
    print('{0} X {1} pixels.'.format(size_image[0], size_image[1]))
    pixel = my_img.load()
    grid = []
    for i in range(size_image[0]):
        for j in range(size_image[1]):
            if type(pixel[i, j]) == int:
                if pixel[i, j] == 0:
                    grid.append([i, j])
            elif len(pixel[i, j]) == 3 and pixel[i, j] == (0, 0, 0):
                grid.append([i, j])
            elif len(pixel[i, j]) == 4:
                temp = pixel[i, j]
                if temp[0] == 0 and temp[1] == 0 and temp[2] == 0:
                    grid.append([i, j])
    print('Image loaded.')

    grid_for_matplotlib = [[], []]
    for i in range(len(grid)):
        grid_for_matplotlib[0].append(grid[i][0])
        grid_for_matplotlib[1].append(grid[i][1])
    grid_for_matplotlib[0], grid_for_matplotlib[1] = array(grid_for_matplotlib[0]), array(grid_for_matplotlib[1])

    return grid_for_matplotlib, size_image


def check_grid(grid):
    if len(grid) == 0:
        print('Too less points.')
        exit(1)

    for i in range(len(grid[0]) - 1):
        for j in range(i + 1, len(grid[0])):
            if grid[0][i] == grid[0][j]:
                print('One X - one Y, no more.')
                exit(1)

    print('Errors not find.')


def main():
    exponent = -1
    # print(len(argv))
    if len(argv) == 2:
        # обычный вызов функции
        crop = []
    elif len(argv) == 3:
        # задана картинка и максимальная степень
        # crop = [argv[2]]
        exponent = int(argv[2])
    elif len(argv) == 4:
        # картинка, start_x и end_x
        crop = [argv[2], argv[3], argv[2], argv[3]]
    elif len(argv) == 6:
        # картинка, start_x, end_x, start_y, end_y
        crop = [argv[2], argv[3], argv[4], argv[5]]
    else:
        # какая-то ошибка с аргументами
        print('Check arguments!')
        exit(1)

    points, size = read_img(argv[1])

    if exponent == -1:
        exponent = len(size[0]) - 1
    # size_of_array
    # print(points)
    check_grid(grid=points)


if __name__ == '__main__':
    main()

'''
>>> X = [5, 5, 5, 6, 7, 8]
>>> Y = [10, 19, 3, 1, 2, 4]
>>>
>>> c = {}
>>> for x, y in zip(X, Y):
...     c.setdefault(x, []).append(y)
...
>>> X, Y = zip(*((x, sum(y)/len(y)) for x, y in c.items()))
>>> X
(5, 6, 7, 8)
>>> Y
(10.666666666666666, 1.0, 2.0, 4.0)
>>>
'''
