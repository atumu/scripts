#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/25
# @Author  : zhangl

from moviepy.editor import *

input = "C:\T\youtube\郭老师相声"
output = "mp3"

if len(input) == 0:
    input = os.getcwd()

audioclip = None
videoClip = None

for root, dirs, files in os.walk(input):
    for name in files:
        try:
            old = os.path.join(root, name)
            # mp3_file = "{}.mp3".format(name.split(".")[0])
            mp3_file = "{}.mp3".format(name)
            videoClip = VideoFileClip(old)
            audioclip = videoClip.audio
            audioclip.write_audiofile(output + os.sep + mp3_file)
        except NameError:
            exit(
                "You either didn't install the moviepy library, or you didn't put the correct name! Be sure to include mp4")
        except OSError:
            exit(
                "You either didn't install the moviepy library, or you didn't put the correct name! Be sure to include .mp4 after the song name!")

audioclip.close()
videoClip.close()
