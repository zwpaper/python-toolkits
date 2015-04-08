#!/usr/bin/python2.7

from PIL import Image
import os
import time
import shutil

file_list = [f for f in os.listdir(".") if f.split(".")[1] == "JPG"]
# print file_list

i = 0
numbPics = len(file_list)
for f in file_list:
    print "mergePic: Dealing with " + f
    ori_im = Image.open(f)
    (x, y) = ori_im.size
    new_width = x * 2 + 125
    new_height = int(float(new_width) * float(842.0 / 595))

    if i == 0:
        name_time = time.strftime("%Y-%m-%d-%H-%M-%S")
        out_im = Image.new("RGB", (new_width, new_height), "white")
        os.mkdir(name_time)
    out_im.paste(ori_im, (50 + (x + 25) * (i % 2), 200 + (y + 10) * (i / 2)))
    shutil.move(f, name_time + "/" + f)
    i += 1
    if i == 8 or f == file_list[numbPics - 1]:
        print "mergePic: Done with " + name_time + "move to folder."
        out_im.save(name_time+".jpg", 'JPEG')
        i = 0









