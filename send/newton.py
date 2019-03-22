from sys import exit, argv
from copy import copy

from PIL import Image, ImageDraw
from math import nan, fabs
from numpy import zeros, array
from matplotlib.pyplot import *


def read_img(path: object) -> object:
    try:
        image = Image.open(path)
    except FileNotFoundError:
        print('File does`n exist. \nProgramm wil close.')
        exit(1)
    size_image = image.size
    print('{0} X {1} pixels.'.format(size_image[0], size_image[1]))
    pixel = image.load()
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
    return grid, size_image


def check_error(grid):
    if len(grid) <= 1:
        print('Not enough points. Need more, then 1.')
        exit(255)

    for i in range(len(grid) - 1):
        for j in range(i + 1, len(grid)):
            if grid[i][0] == grid[j][0]:
                print('One X - one Y, no more.')
                exit(254)

    print('Errors not find.')


def create_home(xy_set):
    home = zeros((len(xy_set), (len(xy_set)) + 1))
    home[home == 0] = nan

    for i in range(len(xy_set)):
        home[i, 0] = xy_set[i][0]
        home[i, 1] = xy_set[i][1]

    for i in range(len(home[0]) - 2):   # column
        for j in range(len(home) - i - 1):  # row
            home[j, i + 2] = (home[j + 1, i + 1] - home[j, i + 1]) / (home[i + j + 1, 0] - home[j, 0])
    print('Home created.')
    return home


def point_to_point(size_of_img, home):
    big_grid = []
    for pixel_x in range(size_of_img[0]):
        sorted_for_this = sort_for_random_y(pixel_x, home[:, 0])
        pixel_y = search_y(home=home, sorted_x=sorted_for_this, point=pixel_x)
        big_grid.append([pixel_x, pixel_y])
    print('All point found.')
    return big_grid


def search_y(home, sorted_x, point):
    p_from_x0 = 0
    back_sum = 0
    stroka = 0
    train = 1
    for i in range(len(sorted_x)):
        if sorted_x[i][2] == 'up+right':
            stroka -= 1

        if i == 0:
            p_from_x0 = home[sorted_x[i][0], i + 1]
            stroka = sorted_x[i][0]
        elif i == 1:
            train *= point - sorted_x[i - 1][1]
            back_sum = home[stroka, i + 1] * train
            p_from_x0 += back_sum
        else:
            train *= point - sorted_x[i - 1][1]
            now_sum = home[stroka, i + 1] * train
            if fabs(back_sum) <= fabs(now_sum):
                return p_from_x0
            else:
                p_from_x0 += now_sum
                pass
    return p_from_x0


def sort_for_random_y(point, array_set):
    sorted_set = []
    for i in range(len(array_set)):
        sorted_set.append([i, fabs(array_set[i] - point)])

    sorted_set.sort(key=sort_by_second_element)

    for i in range(len(sorted_set)):
        sorted_set[i] = [sorted_set[i][0], array_set[sorted_set[i][0]]]

    for i in range(len(sorted_set)):
        if i == 0 or point < sorted_set[i][1]:
            sorted_set[i].append('right')
        elif point > sorted_set[i][1]:
            sorted_set[i].append('up+right')
    return sorted_set


def sort_by_second_element(user_set):
    return user_set[1]


def normalizer(coord_array):
    for i in range(len(coord_array)):
        coord_array[i][1] = round(coord_array[i][1])
    print('Array normalized.')
    return coord_array


def painter(size, old_points, new_points, path_to_old_file, crop):
    new_img = Image.new(mode='RGB', size=(size[0], size[1]), color='black')
    ImageDraw.Draw(new_img)
    pixels = new_img.load()

    for i in range(len(new_points)):
        if 0 <= new_points[i][1] <= size[1]:
            pixels[i, new_points[i][1]] = (255, 0, 0)

    for i in range(len(old_points)):
        pixels[old_points[i][0], old_points[i][1]] = (43, 255, 0)

    if len(crop) == 2:
        new_img = new_img.crop((crop[0], 0, crop[1], size[1]))
    elif len(crop) == 4:
        new_img = new_img.crop((crop[0], crop[2], crop[1], crop[3]))

    new_img.show()
    new_img.save(path_to_old_file.replace('.bmp', '_new.bmp'))
    print('New image save.')


def matplotlib_painter(size, old_points, new_points, path_to_old_file, crop):
    array_x = []
    array_y = []
    for i in range(len(new_points)):
        array_x.append(new_points[i][0])
        if new_points[i][1] >= size[0]:
            array_y.append(size[0] - 1)
        elif new_points[i][1] <= 0:
            array_y.append(0 + 1)
        else:
            array_y.append(new_points[i][1])

    array_old_x = []
    array_old_y = []
    for i in range(len(old_points)):
        array_old_x.append(old_points[i][0])
        array_old_y.append(old_points[i][1])

    array_x, array_y = array(array_x), array(array_y)
    array_old_x, array_old_y = array(array_old_x), array(array_old_y)

    if len(crop) != 0:
        kx = (crop[0] - crop[1]) / (0 - size[0])
        bx = crop[0]
        ky = (crop[2] - crop[3]) / (0 - size[1])
        by = crop[2]

        array_x = kx * array_x + bx
        array_y = ky * array_y + by
        array_old_x = kx * array_old_x + bx
        array_old_y = ky * array_old_y + by

        plot([bx, bx], [by, size[1] * ky + by], 'r')
        plot([bx, size[0] * kx + bx], [by, by], 'r')
        plot([bx, size[0] * kx + bx], [size[1] * ky + by, size[1] * ky + by], 'r')
        plot([size[0] * kx + bx, size[0] * kx + bx], [by, size[1] * ky + by], 'r')

    plot(array_x, array_y)
    if len(crop) == 0:
        plot([0, 0], [0, size[1]], 'k')
        plot([0, size[0]], [0, 0], 'k')
        plot([0, size[0]], [size[1], size[1]], 'k')
        plot([size[0], size[0]], [0, size[1]], 'k')

    scatter(array_old_x, array_old_y)

    grid(True)  # Сетка

    savefig(path_to_old_file.replace('.bmp', '_new.png'))
    print('New image save.')

    show()  # Показать график
    pass


def newton(path_to_file, arguments):
    print('You used {0} file.'.format(path_to_file))

    grid_array, size = read_img(path=path_to_file)
    underbreakble_old_points = copy(grid_array)

    check_error(grid=grid_array)

    home_array = create_home(xy_set=grid_array)

    coord_of_line = point_to_point(size_of_img=size, home=home_array)

    if len(arguments) == 0:
        matplotlib_painter(
            size=size,
            old_points=underbreakble_old_points,
            new_points=coord_of_line,
            path_to_old_file=path_to_file,
            crop=[]
        )

    elif len(arguments) == 4:
        matplotlib_painter(
            size=size,
            old_points=underbreakble_old_points,
            new_points=coord_of_line,
            path_to_old_file=path_to_file,
            crop=arguments
        )


def cut_the_grid(array, grid):
    to_remove = []
    for i in range(len(grid)):
        if array[0] < grid[i][0] < array[1] or array[3] < grid[i][1] < array[4]:
            pass
        else:
            to_remove.append(grid[i])

    for i in range(len(to_remove)):
        grid.remove(to_remove[i])

    return grid


def main():
    pass


if __name__ == '__main__':
    a = 0
    if len(argv) == 2:
        print('Standart image.')
        newton(path_to_file=argv[1], arguments=[])
    elif len(argv) == 4:
        print(
            'Start x={0}, end x={1}. \nStart y and end y the same.'.format(
                int(argv[2]),
                int(argv[3])
            )
        )
        if int(argv[2]) >= int(argv[3]):
            print('Check start/end of x!')
            exit(1)

        # newton(path_to_file=argv[1], arguments=[int(argv[2]), int(argv[3])])
        # print('Start x {0},\nEnd x {1}.'.format(int(argv[2]), int(argv[3])))
        newton(path_to_file=argv[1],
               arguments=[int(argv[2]),
                          int(argv[3]),
                          int(argv[2]),
                          int(argv[3])]
               )

    elif len(argv) == 6:
        if int(argv[2]) >= int(argv[3]):
            print('Check start/end of x!')
            exit(1)
        elif int(argv[4]) >= int(argv[5]):
            print('Check start/end of y!')
            exit(1)

        print(
            'Start x={0}, end x={1}. \nStart y={2}, end y={3}.'.format(
                int(argv[2]),
                int(argv[3]),
                int(argv[4]),
                int(argv[5])
            )
        )

        newton(path_to_file=argv[1],
               arguments=[int(argv[2]),
                          int(argv[3]),
                          int(argv[4]),
                          int(argv[5])]
               )

    else:
        print('Dismiss arguments.')
