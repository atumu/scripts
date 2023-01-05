# encoding: utf-8
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def get_tracks(distance, rate=0.6, t=0.2, v=0):
    """
    将distance分割成小段的距离
    :param distance: 总距离
    :param rate: 加速减速的临界比例
    :param a1: 加速度
    :param a2: 减速度
    :param t: 单位时间
    :param t: 初始速度
    :return: 小段的距离集合
    """
    tracks = []
    # 加速减速的临界值
    mid = rate * distance
    # 当前位移
    s = 0
    # 循环
    while s < distance:
        # 初始速度
        v0 = v
        if s < mid:
            a = 20
        else:
            a = -3
        # 计算当前t时间段走的距离
        s0 = v0 * t + 0.5 * a * t * t
        # 计算当前速度
        v = v0 + a * t
        # 四舍五入距离，因为像素没有小数
        tracks.append(round(s0))
        # 计算当前距离
        s += s0

    return tracks


def slide(driver):
    """滑动验证码"""
    # 切换iframe
    driver.switch_to.frame(1)
    #找到滑块
    block = driver.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
    #找到刷新
    reload = driver.find_element_by_xpath('//*[@id="reload"]')
    while True:
        # 摁下滑块
        ActionChains(driver).click_and_hold(block).perform()
        # 移动
        ActionChains(driver).move_by_offset(180, 0).perform()
        #获取位移
        tracks = get_tracks(30)
        #循环
        for track in tracks:
            #移动
            ActionChains(driver).move_by_offset(track, 0).perform()
        # 释放
        ActionChains(driver).release().perform()
        #停一下
        time.sleep(2)
        #判断
        if driver.title == "登录豆瓣":
            print("失败...再来一次...")
            #单击刷新按钮刷新
            reload.click()
            # 停一下
            time.sleep(2)
        else:
            break

def main():
    """主程序"""
    url = "https://accounts.douban.com/passport/login"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("zl409730739@163.com")
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("1qaz@WSXDbvv")
    driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a').click()
    # 停一下，等待出现
    time.sleep(2)
    #滑动验证码
    slide(driver)

    print("成功")
    # driver.quit()


if __name__ == '__main__':
    main()
