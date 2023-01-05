#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/25
# @Author  : zhangl

from pydub import AudioSegment

m4a_audio = AudioSegment.from_file("C:/T/youtube/郭老师相声/001.m4a", format="raw",
                                   frame_rate=44100, channels=2, sample_width=2)

m4a_audio.export("audio1.mp3", format="mp3")