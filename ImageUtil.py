# coding=utf-8
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_FOLDER = "targetImg"


def set_text(image_file, text):
    img = Image.open(image_file)
    (img_x, img_y) = img.size

    font = ImageFont.truetype('msyh.ttc', int(img_y / 20))

    draw = ImageDraw.Draw(img)
    draw.text((int(img_x / 20), img_y - int((img_y * 3) / 20)), unicode(text, "UTF-8"), (74, 74, 170), font=font)

    target_name = os.path.basename(image_file.name)
    target_dir = os.path.join(ROOT_DIR, TARGET_FOLDER)
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    target_file = os.path.join(target_dir, target_name)
    img.save(target_file, 'jpeg')
