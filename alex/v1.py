# import PIL
import sys
from PIL import Image, ImageDraw
import os


EX_PATH = '/Users/owl/Desktop/Образец переименовывания/!_example3.png'
NEW_PATH = '/Users/owl/Desktop/Образец переименовывания/!_save/'
PATH = '/Users/owl/Desktop/Образец переименовывания/'


# (237, 237, 237)


def get_to_change(path=EX_PATH):
    image = Image.open(path)
    size_image = image.size
    # print('{0} X {1} pixels.'.format(size_image[0], size_image[1]))
    pixel = image.load()

    # print('End.')

    to_change = list()

    for i in range(size_image[0]):
        for j in range(size_image[1]):
            # print(pixel[i, j])
            if pixel[i, j] == (0, 0, 0, 0):
                # print('This!')
                # pixel[i, j] == (255, 255, 255)
                to_change.append((i, j))

    return to_change


def open_img(path):
    try:
        image = Image.open(path)
    except FileNotFoundError:
        print('File does`n exist. \nProgramm wil close.')
        sys.exit(1)

    size_image = image.size
    # print('{0} X {1} pixels.'.format(size_image[0], size_image[1]))
    pixel = image.load()

    # print('End.')

    # to_change = list()
    #
    # for i in range(size_image[0]):
    #     for j in range(size_image[1]):
    #         # print(pixel[i, j])
    #         if pixel[i, j] == (0, 0, 0, 0):
    #             print('This!')
    #             # pixel[i, j] == (255, 255, 255)
    #             to_change.append((i, j))

    to_change = get_to_change()

    new_img = Image.new(mode='RGBA', size=(size_image[0], size_image[1]))
    ImageDraw.Draw(new_img)
    new_pixels = new_img.load()
    flag = False
    for i in range(size_image[0]):
        for j in range(size_image[1]):
            if (i, j) == to_change[0]:
                # new_pixels[i, j] = pixel[i, j]
                # new_pixels[i, j] = (255, 255, 255, 0)
                new_pixels[i, j] = (0, 0, 0, 0)
                del to_change[0]
                if len(to_change) == 0:
                    flag = True
                    break
            else:
                # new_pixels[i, j] = (0, 0, 0, 0)
                new_pixels[i, j] = pixel[i, j]

        if flag:
            break
    new_img.save(path.replace('переименовывания/', 'переименовывания/!_save/').replace('.jpg', '.png'))

    # print('End?')
    pass


if __name__ == '__main__':
    # path = '/Users/owl/Desktop/Образец переименовывания/202.jpg'
    # open_img(path)

    in_dir = os.listdir(PATH)
    in_dir.remove('!_example.PNG')
    in_dir.remove('!_example2.PNG')
    in_dir.remove('!_example3.PNG')
    in_dir.remove('!_save')

    for number, img in enumerate(in_dir):
        try:
            open_img(PATH + img)
            print('{0}/{1} ({2}) done.'.format(number + 1, len(in_dir), img))
        except OSError:
            pass
    print('That`s all!')
