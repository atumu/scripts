import json
import time

import chardet
import pymysql
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from douban_sliding_code import sliding_code
from similarity import ratio_top

ch_options = webdriver.ChromeOptions()
ch_options.add_experimental_option("prefs", {"profile.mamaged_default_content_settings.images": 2})
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
ch_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# ch_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
ch_options.add_argument('--proxy--server=127.0.0.1:8080')
ch_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
ch_options.add_argument('--incognito')
browser = webdriver.Chrome(options=ch_options)

# browser = webdriver.Chrome()

# browser = webdriver.PhantomJS()
WAIT = WebDriverWait(browser, 10)

db = pymysql.connect('192.168.3.88', 'root', 'zhangL', 'movie')
cursor = db.cursor()


def login():
    browser.get("https://accounts.douban.com/passport/login")
    passlogin = WAIT.until(
        EC.element_to_be_clickable((By.XPATH, "//li[@class='account-tab-account']")))
    passlogin.click()

    username = WAIT.until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='username']")))
    password = WAIT.until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))
    username.send_keys("zl409730739@163.com")
    password.send_keys("1qaz@WSXDb")

    submit = WAIT.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-account btn-active']")))
    submit.click()
    time.sleep(4)
    # print(browser.title)
    if browser.title == '登录豆瓣':
        # 出现了验证码
        print("请尽快处理滑动验证码!!!!!!!!")
        # if sliding_code(browser):
        #     print('登录成功！')
        time.sleep(8)
    else:
        print('登录成功！')


warning_count = 1


def main():
    sql = 'SELECT movieid,moviename,showyear FROM movie2 where version = -2 and douban_movies is null'
    cursor.execute(sql)
    results = cursor.fetchall()
    print("任务量: %d" % len(results))
    for row in results:
        movieid = row[0]
        moviename = row[1]
        showyear = row[2]
        try:
            browser.get('https://search.douban.com/movie/subject_search/?search_text=' + moviename)
            year = 0
            if showyear is not None:
                year = showyear.year
            save_to_mysql(movieid, moviename, year)
            WAIT.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='inp-btn']/input")))
        except Exception as ex:
            print(movieid, moviename, 'Exception', ex)


def save_to_mysql(movieid, moviename, year):
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    list = soup.findAll(class_='sc-bZQynM')
    end = 5
    length = len(list)
    if length == 0:
        if ("没有找到关于" in html) \
                or "根据相关法律法规和政策" in html:
            print(movieid, moviename, year, "EMPTY")
            sql = "update movie2 set version = -2 where movieid = %s" % (movieid)
            execute_sql(sql)
        else:
            print(movieid, moviename, year, "WARNING")

            global warning_count
            time.sleep(warning_count * 30)
            warning_count = warning_count + 1
            login()
        return
    warning_count = 1
    if length < 5:
        end = length
    success = False
    titles = []
    for item in list[0:end]:
        item_title = item.find(class_='title').find('a').text.replace("\u200e", "")
        titles.append(item_title)

        if (year == 0 or str(year) in item_title or str(year - 1) in item_title or str(year + 1) in item_title) \
                and moviename.lower() in item_title.lower():
            sql = "update movie2 set moviename_CN = '%s', version = 1 where movieid = %s" \
                  % (pymysql.escape_string(item_title), movieid)
            execute_sql(sql)
            success = True
            print(movieid, moviename, year, "OKKK")
            return
    # 相似度判定
    if not success:
        top = ratio_top(moviename, titles)
        if top[0] != 0:
            sql = "update movie2 set moviename_CN = '%s', douban_movies = '%s', version = 1 where movieid = %s" \
                  % (pymysql.escape_string(top[1]), pymysql.escape_string('|||'.join(titles)), movieid)
            execute_sql(sql)
            success = True
    # 还是未成功, 保存抓取结果列表
    if not success:
        print(movieid, moviename, year, "ERRR")
        print(titles)
        sql = "update movie2 set version = -1, douban_movies = '%s' where movieid = %s;" \
              % (pymysql.escape_string('|||'.join(titles)), movieid)
        execute_sql(sql)


def debug(movieid):
    try:
        sql = 'SELECT movieid,moviename,showyear FROM movie2 where movieid = %d' % movieid
        cursor.execute(sql)
        result = cursor.fetchone()
        movieid = result[0]
        moviename = result[1]
        # moviename = "sdfsd 啊实打"
        showyear = result[2]
        year = 0
        if showyear is not None:
            year = showyear.year

        browser.get('https://search.douban.com/movie/subject_search/?search_text=' + moviename)
        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')
        list = soup.findAll(class_='sc-bZQynM')
        end = 5
        length = len(list)
        if length == 0:
            if "没有找到关于" in html and "的电影，换个搜索词试试吧。" in html:
                print(movieid, moviename, year, "EMPTY")
                sql = "update movie2 set version = -2 where movieid = %s" % (movieid)
                execute_sql(sql)
            else:
                time.sleep(30)
                print(movieid, moviename, year, "WARNING")
            return

        if length < 5:
            end = length
        success = False
        titles = []
        for item in list[0:end]:
            item_title = item.find(class_='title').find('a').text.replace("\u200e", "")
            titles.append(item_title)

            if (year == 0 or str(year) in item_title or str(year - 1) in item_title or str(year + 1) in item_title) \
                    and moviename.lower() in item_title.lower():
                sql = "update movie2 set moviename_CN = '%s', version = 1 where movieid = %s" \
                      % (pymysql.escape_string(item_title), movieid)
                execute_sql(sql)
                success = True
                print(movieid, moviename, year, "OKKK")
                return
        # 相似度判定
        if not success:
            top = ratio_top(moviename, titles)
            if top[0] != 0:
                sql = "update movie2 set moviename_CN = '%s', douban_movies = '%s', version = 1 where movieid = %s" \
                      % (pymysql.escape_string(top[1]), pymysql.escape_string('|||'.join(titles)), movieid)
                execute_sql(sql)
                success = True
        # 还是未成功, 保存抓取结果列表
        if not success:
            sql = "update movie2 set version = -1, douban_movies = '%s' where movieid = %s" \
                  % (pymysql.escape_string('|||'.join(titles)), movieid)
            execute_sql(sql)
            print(movieid, moviename, year, "ERRR")
            print(titles)
    finally:
        browser.quit()


def execute_sql(sql):
    # level = 'dev'
    level = 'pro'
    if level == 'dev':
        print(sql)
    elif level == 'pro':
        cursor.execute(sql)
        db.commit()


if __name__ == '__main__':
    login()
    main()
    # debug(119218)
    db.close()
    browser.quit()
