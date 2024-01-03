import os

from PIL import Image


def toto_debug(*args):
    print(f'toto debug ===', *args)


image_index = 0

root_path = os.path.dirname(__file__)
image_save_path = os.path.join(root_path, "image_save")
if not os.path.exists(image_save_path):
    os.makedirs(image_save_path)


def reset_image_index():
    global image_index
    image_index = 0


def save_image_np(np, name=None):
    global image_index
    image_index += 1
    image = Image.fromarray(np)
    if name is None:
        image_name = f"{image_index}_unnamed.jpg"
    else:
        image_name = f"{image_index}_{name}.jpg"
    image.save(os.path.join(image_save_path, image_name))


def save_image(image: Image, name=None):
    global image_index
    image_index += 1
    if name is None:
        image_name = f"{image_index}_unnamed.jpg"
    else:
        image_name = f"{image_index}_{name}.jpg"
    image.save(os.path.join(image_save_path, image_name))
