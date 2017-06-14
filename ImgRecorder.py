import exifread
import DateUtil
import ImageUtil
import os

img_dir = "sourceImg"


def process(image_file):
    tags = exifread.process_file(image_file)

    for tag in tags.keys():
        # print "key:%s, value:%s" % (tag, tags[tag])
        if tag == "Image DateTime":
            diff_str = DateUtil.get_days(tags[tag])
            ImageUtil.set_text(image_file, diff_str)


for root, dirs, files in os.walk(img_dir):
    for item_file in files:
        if item_file.endswith((".jpg", ".jpeg", "png")):
            img_path = os.path.join(root, item_file)
            f = open(img_path, 'rb')
            process(f)
