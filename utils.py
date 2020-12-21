from PIL import Image


def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst


def calculate_length(encoded_image) -> float:
    length = 0

    x, y = encoded_image.shape
    for i in range(x):
        for j in range(y):
            length += len(encoded_image[i][j])

    return length


def calculate_average_length(encoded_image) -> float:
    length = 0

    x, y = encoded_image.shape
    for i in range(x):
        for j in range(y):
            length += len(encoded_image[i][j])

    return length / encoded_image.size
