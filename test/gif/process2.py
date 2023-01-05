#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 13:08
# @Author  : ZhangL


from PIL import Image, ImageSequence

# 读取GIF
im = Image.open("数组排序/快速排序.gif")
# GIF图片流的迭代器
iter = ImageSequence.Iterator(im)

index = 1
# 遍历图片流的每一帧
for frame in iter:
    if index % 20 == 0:
        print("image %d: mode %s, size %s" % (index, frame.mode, frame.size))
        frame.save("./数组排序/快速排序/%d.png" % index)
    index += 1

# frame0 = frames[0]
# frame0.show()

# 把GIF拆分为图片流
# imgs = [frame.copy() for frame in ImageSequence.Iterator(im)]
# # 把图片流重新成成GIF动图
# imgs[0].save('out.gif', save_all=True, append_images=imgs[1:])
#
# # 图片流反序
# imgs.reverse()
# # 将反序后的所有帧图像保存下来
# imgs[0].save('./reverse_out.gif', save_all=True, append_images=imgs[1:])
