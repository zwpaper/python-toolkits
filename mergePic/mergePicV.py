#!/usr/bin/python2.7

'''
    Todo:   *   Using the Orientation and width height to detect the real orientation of Pics
                and then move to two temp dir to deal with different orientated pics
            *   Using os.path.isfile() to test if it is a file.
'''
from PIL import Image
from PIL.ExifTags import TAGS
import os
import time
import shutil


file_list = [f for f in os.listdir(".") if f.split(".")[1] == "JPG"]
# print file_list

i = 0
tags = {}
vertical_orientation = {
    1: 90,
    3: 270,
    6: 0,
    8: 180,
}

numbPics = len(file_list)
for f in file_list:
    print "mergePic: Dealing with " + f
    ori_im = Image.open(f)
    exif = ori_im._getexif()

    # get Exif info for the orientation
    for tag, v in exif.items():
        decoded = TAGS.get(tag, tag)
        tags[decoded] = v

    # get width and height info and rotate to the same direction
    (x, y) = ori_im.size
    ori_im = ori_im.rotate(vertical_orientation[tags["Orientation"]])
    if y > x:
        x, y = y, x

    # using the width to create a A4 radio pic
    if i == 0:
        name_time = time.strftime("%Y-%m-%d-%H-%M-%S")
        new_width = x * 2 + 125
        new_height = int(float(new_width) * float(842.0 / 595))
        out_im = Image.new("RGB", (new_width, new_height), "white")
        os.mkdir(name_time)

    out_im.paste(ori_im, (50 + (x + 25) * (i % 2), 200 + (y + 10) * (i / 2)))
    # there may be some pics less than 8 moved to the last folder
    shutil.move(f, name_time + "/" + f)
    i += 1
    if i == 8 or f == file_list[numbPics - 1]:
        print "mergePic: Done with " + name_time + "move to folder."
        out_im.save(name_time+".jpg", 'JPEG')
        i = 0









