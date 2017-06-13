# coding=utf-8
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def set_text(imagefile, text):
    img = Image.open(imagefile)
    (img_x, img_y) = img.size

    ttfont = ImageFont.truetype('msyh.ttc', int(img_y / 20))

    draw = ImageDraw.Draw(img)
    draw.text((int(img_x / 20), img_y - int((img_y * 3) / 20)), unicode(text, "UTF-8"), (74, 74, 170), font=ttfont)

    img.save('target.jpg', 'jpeg')
