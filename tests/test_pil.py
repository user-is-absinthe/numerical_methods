from PIL import Image
# from os import


def read_img(path):
    image = Image.open(path)
    size_image = image.size
    print('{0} X {1} pixels.'.format(size_image[0], size_image[1]))
    pixel = image.load()
    grid = []
    # print(pixel[0, 26])
    for i in range(size_image[0]):
        for j in range(size_image[1]):
            # print(pixel[i, j], type(pixel[i, j]), type(pixel[i, j][0]))
            if type(pixel[i, j]) == int:
                if pixel[i, j] == 0:
                    grid.append([i, j])
            elif len(pixel[i, j]) == 3 and pixel[i, j] == (0, 0, 0):
                grid.append([i, j])
            elif len(pixel[i, j]) == 4:
                temp = pixel[i, j]
                if temp[0] == 0 and temp[1] == 0 and temp[2] == 0:
                    grid.append([i, j])
            # if (255, 255, 255, 255) != pixel[i, j]:  # pixel[i, j] == (0, 0, 0, 0) or
            # if pixel[i, j] == 0 or pixel[i, j] == (0, 0, 0):
            #     # print('awdwdad')
            #     grid.append([i, j])
    # grid.remove(255)
    # # print((0, 0, 0, 255), 'never')
    print(grid, 'lmlm')
    return grid


if __name__ == '__main__':
    path_to_file = '/Users/owl/Pycharm/PycharmProjects/numerical_methods/img/RevInt5.bmp'
    # path_to_file = '/Users/owl/Pycharm/PycharmProjects/numerical_methods/img/Unknown.bmp'
    # path_to_file = '/Users/owl/Pycharm/PycharmProjects/numerical_methods/img/black.bmp'
    # path_to_file = '/Users/owl/Pycharm/PycharmProjects/numerical_methods/img/RevIntz.bmp'
    print('You used {0} file.'.format(path_to_file))
    read_img(path=path_to_file)
