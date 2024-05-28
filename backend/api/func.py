#!/usr/bin/python3
from os import makedirs, path
from PIL import Image

def allowed_images(extension):
    """ check the file extension """

    allowed_extension = ['png', 'jpeg', 'jpg']

    if extension in allowed_extension:
        return 1
    return None


def image_save(image, image_name):
    """ this functions saves images """

    folder = '/var/www/html/images'

    if not path.exists(folder):
        makedirs(folder)

    full_path = path.join(folder, image_name)
    img = Image.open(image)
    img.save(full_path)
