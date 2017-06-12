import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def set_text(imagefile, text):
    img = Image.open(imagefile)
    (img_x, img_y) = img.size

    # ttfont = ImageFont.truetype('/usr/share/fonts/noto/NotoSansCJK-Regular.ttc', int(img_y / 20))

    draw = ImageDraw.Draw(img)
    draw.text((int(img_x / 20), img_y - int((img_y * 1.3) / 20)), text, (0, 0, 0))

    img.save('target.jpg', 'jpeg')
