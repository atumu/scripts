#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 18:45
# @Author  : ZhangL
from moviepy.editor import *

video = VideoFileClip('13-5 Kafka 零拷贝原理分析.mp4')
audio = video.audio
audio.write_audiofile('13-5 Kafka 零拷贝原理分析.wav')
