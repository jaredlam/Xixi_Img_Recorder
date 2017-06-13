import exifread
import DateUtil
import ImageUtil

source_img = "IMG_20170407_221436.jpg"

f = open(source_img, 'rb')
tags = exifread.process_file(f)

for tag in tags.keys():
    # print "key:%s, value:%s" % (tag, tags[tag])
    if tag == "Image DateTime":
        diff_str = DateUtil.get_days(tags[tag])
        ImageUtil.set_text(source_img, diff_str)
