import sys
from PIL import Image, ImageDraw
import os

PATH_TO_SQUARE = 'C:\\Users\Worker\Desktop\работа на ИС\\lines.png'
PATH_TO_ENDS = 'C:\\Users\Worker\Desktop\работа на ИС\\angles.png'
PATH_TO_FOLDER = ''


def main():
    ends = read_example(PATH_TO_SQUARE)
    print(ends)
    crop_img('C:\\Users\Worker\Desktop\работа на ИС\\1 вид SIM-карты СНГ (без уголков)\\246_03.png', ends)

    pass


def read_example(path):
    image = Image.open(path)
    size_image = image.size
    pixel = image.load()
    to_change = list()
    for i in range(size_image[0]):
        for j in range(size_image[1]):
            if pixel[i, j] == (0, 0, 0, 0):
                to_change.append((i, j))
    return to_change


def crop_img(path, changelog):
    try:
        image = Image.open(path)
    except FileNotFoundError:
        print('File does`n exist. \nProgramm wil close.')
        sys.exit(1)

    size_image = image.size
    pixel = image.load()

    to_change = changelog.copy()

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
    new_img.save(path.replace('.png', '_new.png'))

    # print('End?')
    pass


if __name__ == '__main__':
    main()
