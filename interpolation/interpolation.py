from sys import exit

from PIL import Image
from math import nan
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
        # for j in range(len(grid)):
        #     if range[i][]
    pass


def create_home(xy_set):
    home = zeros((len(xy_set), (len(xy_set)) + 1))
    home[home == 0] = nan

    for i in range(len(xy_set)):
        home[i, 0] = xy_set[i][0]
        home[i, 1] = xy_set[i][1]

    for i in range(len(home[0]) - 2):   # column
        for j in range(len(home) - i - 1):  # row
            home[j, i + 2] = (home[j + 1, i + 1] - home[j, i + 1]) / (home[i + j + 1, 0] - home[j, 0])
    '''
            % create home function:
        function home_array = create_home(array)
        array = array';
        temp_array = NaN(size(array, 1), size(array, 1) - 1);
        full_array = cat(2, array, temp_array);
        for i = 1:size(full_array, 2) - 2 % stb
            for j = 1:size(full_array, 1) - i % str
                full_array(j, i + 2) = (full_array(j + 1, i+1) - full_array(j, i + 1)) ...
                    / (full_array(i + j, 1) - full_array(j, 1));
            end
        end
        home_array = full_array;
        end
    '''
    # print(home)
    return home


def point_to_point(size_of_img, home):
    big_grid = []
    for pixel in range(size_of_img[0]):
        for i in range(len(home)):
            if pixel == home[i, 0]:
                big_grid.append([pixel, home[i, 1]])
    return big_grid


if __name__ == '__main__':

    path_to_file = '/Users/owl/Pycharm/PycharmProjects/numerical_methods/img/RevInt6.bmp'
    # path_to_file = '/Users/owl/Pycharm/PycharmProjects/numerical_methods/img/Unknown.bmp'
    # path_to_file = '/Users/owl/Pycharm/PycharmProjects/numerical_methods/img/black.bmp'
    # path_to_file = '/Users/owl/Pycharm/PycharmProjects/numerical_methods/img/RevIntz.bmp'

    print('You used {0} file.'.format(path_to_file))

    grid_array = read_img(path=path_to_file)
    print(grid_array[0])

    check_error(grid=grid_array)

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
    # print(create_home(xy_set=from_book))
    print(home_array)

    coord_of_line = point_to_point(size_of_img=grid_array[1], home=home_array)
    print(coord_of_line)
