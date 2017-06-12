import exifread
import DateUtil
import ImageUtil

f = open("IMG_20170530_132435.jpg", 'rb')
tags = exifread.process_file(f)

for tag in tags.keys():
    # print "key:%s, value:%s" % (tag, tags[tag])
    if tag == "Image DateTime":
        diff_str = DateUtil.get_days(tags[tag])
        ImageUtil.set_text("IMG_20170530_132435.jpg", diff_str)
