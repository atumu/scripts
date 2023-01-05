#!/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 11:17
# @Author  : ZhangL
import time

from selenium.webdriver.common.action_chains import ActionChains


def sliding_code(driver):
    '''
    处理滑动验证码
    :param driver: 出现验证码的driver对象
    :return: True-->解决了
    '''
    print('开始处理滑动验证码！')
    # 发现验证码的部分就是一个iframe标签，切入frame
    print(driver.switch_to.frame(1))
    # 1、先找到滑块，鼠标点他，悬浮           滑块在xpath路径是滑块最外层
    # //*[@id="slideBlock"]
    slider = driver.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
    # slider = driver.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
    # print(slider)

    # 2、先找到滑动距离---任何一个问题解决思路--通过测量得到220

    # ActionChains(driver)：创建一个鼠标动作链---绑定driver（参数）上的
    # click_and_hold：点击并保持（参数表示点谁）
    # perform：悬浮

    # 3、点住他，水平移动（移动一定的距离）---距离到底是多少
    while True:
        ActionChains(driver).click_and_hold(on_element=slider).perform()
        # 滑动：先闪现100
        ActionChains(driver).move_by_offset(xoffset=150, yoffset=0).perform()
        # 剩余的123模拟加速后减速的过程
        tracks = get_tracks(30)
        # print(tracks)
        for s in tracks:
            ActionChains(driver).move_by_offset(xoffset=s, yoffset=0).perform()
        # 4、放开鼠标即可
        ActionChains(driver).release().perform()
        time.sleep(2)
        if driver.title != '登录豆瓣':
            break
        time.sleep(1)
        # 点击刷新图片
        driver.find_element_by_xpath('//*[@id="reload"]').click()
        time.sleep(1)
    # 网络恍惚了一下：滑动的太快了
    # 滑动要符合人的滑动习惯：先加速，后减速


def get_tracks(distance):
    '''
    模仿先加速后减速的过程
    :param distance: 移动的距离
    :return: 列表
    '''
    # 当前速度
    v = 0

    # 定义时间间隔
    t = 0.3
    tracks = []

    # 当前距离
    current = 0

    # 加速和减速的分割线
    mid = distance * 3 / 5

    while current < distance:
        # 定义加速度
        if current < mid:
            a = 2
        else:
            a = -3
        # 移动了
        # 定义初速度
        v0 = v
        s = v0 * t + 0.5 * a * t * t
        current += s
        # 保持移动的时候有效果
        # 0.1个像素。像素不能是小数
        tracks.append(round(s))
        # 设置当前速度
        v = v0 + a * t
    return tracks
