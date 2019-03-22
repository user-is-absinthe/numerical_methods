from PIL import Image

image = Image.open('black.bmp')
size_image = image.size
print(size_image)
pixel = image.load()
print(pixel[89, 39])
