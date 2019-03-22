from sys import exit

from PIL import Image, ImageDraw
from math import nan, fabs
from numpy import zeros


def read_img(path: object) -> object:
    image = Image.open(path)
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


def create_home(xy_set):
    home = zeros((len(xy_set), (len(xy_set)) + 1))
    home[home == 0] = nan

    for i in range(len(xy_set)):
        home[i, 0] = xy_set[i][0]
        home[i, 1] = xy_set[i][1]

    for i in range(len(home[0]) - 2):   # column
        for j in range(len(home) - i - 1):  # row
            home[j, i + 2] = (home[j + 1, i + 1] - home[j, i + 1]) / (home[i + j + 1, 0] - home[j, 0])
    return home


def point_to_point(size_of_img, home):
    big_grid = []
    for pixel_x in range(size_of_img[0]):
        sorted_for_this = sort_for_random_y(pixel_x, home[:, 0])
        pixel_y = search_y(home=home, sorted_x=sorted_for_this, point=pixel_x)
        print(pixel_y)
        # exit(status=134)
        big_grid.append([pixel_x, pixel_y])
    return big_grid


def search_y(home, sorted_x, point):
    # flag = True
    p_from_x0 = 0
    back_sum = 0
    now_sum = 0
    stroka = 0
    train = 1
    for i in range(len(sorted_x)):
        if sorted_x[i][2] == 'up+right':
            stroka -= 1

        if i == 0:
            p_from_x0 = home[sorted_x[i][0], i + 1]
            stroka = sorted_x[i][0]
            # continue
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

        '''
        if i == 0:
            home_y = sorted_x[i][0]
            p_from_x0 += home[i + 1, home_y]
            continue
        elif i == 1:
            train *= point - sorted_x[i - 1][1]
            back_sum = home[i + 1, home_y] * train
            p_from_x0 += back_sum
        else:
            train *= point - sorted_x[i - 1][1]
            now_sum = home[i + 1, home_y] * train
            if fabs(back_sum) <= fabs(now_sum):
                return p_from_x0
            else:
                p_from_x0 += now_sum
                back_sum = now_sum
        '''



    return p_from_x0


def sort_for_random_y(point, array_set):
    # передаем координату искомого Х и массив с заданными Х
    # TODO: отсортировать заданные Х по модулю относительно искомого Х
    # для этого используем модуль fabs

    sorted_set = []
    for i in range(len(array_set)):
        sorted_set.append([i, fabs(array_set[i] - point)])
    # print(sorted_set)

    sorted_set.sort(key=sort_by_second_element)
    # print(sorted_set)

    for i in range(len(sorted_set)):
        sorted_set[i] = [sorted_set[i][0], array_set[sorted_set[i][0]]]
    # print(sorted_set)

    for i in range(len(sorted_set)):
        if i == 0 or point < sorted_set[i][1]:
            sorted_set[i].append('right')
        elif point > sorted_set[i][1]:
            sorted_set[i].append('up+right')
    # print(sorted_set)
    # exit(134)
    return sorted_set


def sort_by_second_element(user_set):
    return user_set[1]


def normalizer(coord_array):
    for i in range(len(coord_array)):
        coord_array[i][1] = round(coord_array[i][1])
    return coord_array


def painter(size, old_points, new_points, path_to_old_file):
    new_img = Image.new(mode='RGB', size=(size[0], size[1]), color='black')
    # color = (255, 255, 255)
    ImageDraw.Draw(new_img)
    pixels = new_img.load()

    for i in range(len(new_points)):
        if 0 <= new_points[i][1] <= size[1]:
            # PIL.ImageDraw.ImageDraw.point(xy, fill=None)
            # ImageDraw.ImageDraw.point(new_img, new_points[i], (43, 255, 0))
            pixels[i, new_points[i][1]] = (43, 255, 0)

    for i in range(len(old_points)):
        pixels[old_points[i][0], old_points[i][1]] = (255, 0, 0)

    new_img.save(path_to_old_file.replace('.bmp', '_new.bmp'))


path_to_file = '/Users/owl/Pycharm/PycharmProjects/numerical_methods/img/RevInt6.bmp'
# path_to_file = '/Users/owl/Pycharm/PycharmProjects/numerical_methods/img/Unknown.bmp'
# path_to_file = '/Users/owl/Pycharm/PycharmProjects/numerical_methods/img/black.bmp'
# path_to_file = '/Users/owl/Pycharm/PycharmProjects/numerical_methods/img/RevIntz.bmp'

print('You used {0} file.'.format(path_to_file))

grid_array = read_img(path=path_to_file)
print(grid_array[0])

check_error(grid=grid_array[0])

from_book = [
    [0, 0.5403],
    [0.2, 0.6831],
    [0.5, 0.8216],
    [0.9, 0.9185],
    [1.4, 0.9697],
    [2, 0.9909],
    [2.7, 0.9977],
    [4, 0.9998]
]

home_array = create_home(xy_set=grid_array[0])
# home_array = create_home(xy_set=from_book)
print(home_array)

coord_of_line = point_to_point(size_of_img=grid_array[1], home=home_array)
print(coord_of_line)

normal_coord_of_line = normalizer(coord_array=coord_of_line)
print(normal_coord_of_line)

painter(
    size=grid_array[1],
    old_points=grid_array[0],
    new_points=normal_coord_of_line,
    path_to_old_file=path_to_file)



# home_array = create_home(xy_set=from_book)
# x = 3.9
# sorted_for_this = sort_for_random_y(x, home_array[:, 0])
# pixel_y = search_y(home=home_array, sorted_x=sorted_for_this, point=x)
# print(sorted_for_this)
# print(pixel_y)
