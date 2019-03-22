from PIL import Image
from numpy import array, dot


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

    grid_for_matplotlib = [[], []]
    for i in range(len(grid)):
        grid_for_matplotlib[0].append(grid[i][0])
        grid_for_matplotlib[1].append(grid[i][1])
    grid_for_matplotlib[0], grid_for_matplotlib[1] = array(grid_for_matplotlib[0]), array(grid_for_matplotlib[1])

    return grid_for_matplotlib, size_image


def create_q(var_x, exponent):
    # exponent = -1
    if exponent == -1:
        pass

    list_of_q = []
    for i in range(exponent):
        if i == 0:
            list_of_q.append(1)
        elif i == 1:
            list_of_q.append(var_x - dot(var_x, list_of_q[i - 1]) / dot(list_of_q[i - 1], list_of_q[i - 1]))
        else:
            q_last = list_of_q[i - 1]
            q_2last = list_of_q[i - 2]
            one = var_x * q_last
            two = (-1) * dot(var_x * q_last, q_last) / dot(q_last, q_last) * q_last
            three = (-1) * dot(var_x * q_last, q_2last) / dot(q_2last, q_2last)
            # q_next = var_x * q_last - dot(var_x * q_last, q_last) / dot(q_last, q_last) * q_last - dot(var_x * q_last, q_2last) / dot(q_2last, q_2last )
            q_this = one + two + three
            list_of_q.append(q_this)
        # pass
    return list_of_q


if __name__ == '__main__':
    more_q = create_q(var_x=10, exponent=5)
    print(more_q[len(more_q) - 1])
    pass
