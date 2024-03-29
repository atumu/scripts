#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/31
# @Author  : zhangl


from pprint import pprint
from pymediainfo import MediaInfo

media_info = MediaInfo.parse("4-6 三大平台扬帆起航.mp4")
for track in media_info.tracks:
    if track.track_type == "Video":
        print("Bit rate: {t.bit_rate}, Frame rate: {t.frame_rate}, "
              "Format: {t.format}".format(t=track)
        )
        print("Duration (raw value):", track.duration)
        print("Duration (other values:")
        pprint(track.other_duration)
    elif track.track_type == "Audio":
        print("Track data:")
        pprint(track.to_data())