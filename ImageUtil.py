# coding=utf-8
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_FOLDER = "targetImg"


def set_text(image_file, text, date_str):
    img = Image.open(image_file)
    (img_x, img_y) = img.size

    day_font = ImageFont.truetype('hkw5.ttf', int(img_y / 30))
    date_font = ImageFont.truetype('hkw5.ttf', int(img_y / 40))
    background = Image.new('RGBA', (int(img_x), img_y / 20), (255, 255, 255))

    draw = ImageDraw.Draw(background, 'RGBA')
    # draw.text((int(img_x / 20), img_y - int((img_y * 3) / 20)), unicode(text, "UTF-8"), (74, 74, 170), font=font)

    alpha = background.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(0.5)
    background.putalpha(alpha)

    final_day_text = unicode(text, "UTF-8")
    final_date_text = unicode(date_str, "UTF-8")
    start_x = 80
    start_y = 20
    color = (255, 102, 102)

    draw.text((start_x, start_y), final_day_text, color, font=day_font)
    day_width, day_height = day_font.getsize(final_day_text)
    date_width, date_height = date_font.getsize(final_date_text)
    draw.text((start_x + day_width + 80, start_y + day_height - date_height), date_str, color, font=date_font)

    target_name = os.path.basename(image_file.name)
    target_dir = os.path.join(ROOT_DIR, TARGET_FOLDER)
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    target_file = os.path.join(target_dir, target_name)
    Image.composite(background, img, background).save(target_file, 'jpeg')
