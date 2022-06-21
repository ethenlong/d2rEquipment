# -*-coding:utf-8-*-

from selenium import webdriver
import json
import time
import random
from selenium.webdriver.chrome.service import Service
import os


#
# driver = webdriver.Chrome()
# driver.get("https://tieba.baidu.com/f?kw=%B0%B5%BA%DA2")
# time.sleep(60)
# cookies = driver.get_cookies()
# with open("qrsncookies.txt", "w") as fp:
#     json.dump(cookies, fp)
# # https://twitter.com/login

# option = webdriver.FirefoxOptions()
# option.add_argument("headless")
# option.add_argument('--no-sandbox')
# driver = webdriver.Firefox(firefox_options=option)
# driver.get("https://twitter.com/login")
# with open("qrsncookies.txt", "r") as fp:
#     cookies = json.load(fp)
#     for cookie in cookies:
#         driver.add_cookie(cookie)
#
# driver.get("https://twitter.com")
# print driver.title

def read_cookies():
    # c_service = Service('E:\work\\twbot\chromedriver.exe')
    c_service = Service('chromedriver')
    c_service.command_line_args()
    c_service.start()

    # chrome
    option = webdriver.ChromeOptions()
    # option.set_headless()
    # option.add_argument("--headless")
    # option.add_argument("--no-sandbox")
    driver = webdriver.Chrome(chrome_options=option)
    # driver = webdriver.Chrome()

    # firefox
    # option = webdriver.FirefoxOptions()
    # # option.add_argument("headless")
    # # option.add_argument('--no-sandbox')
    # option.set_headless()
    # driver = webdriver.Firefox(firefox_options=option)

    driver.get("https://tieba.baidu.com/f?kw=%B0%B5%BA%DA2")
    with open("qrsncookies.txt", "r") as fp:
        cookies = json.load(fp)
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            driver.add_cookie(cookie)

    driver.get("https://tieba.baidu.com/f?kw=%B0%B5%BA%DA2")
    print(driver.title)
    time.sleep(10)
    return driver, c_service


def publishing():
    driver, c_service = read_cookies()
    opened_url = []
    while True:
        try:
            driver.get("https://tieba.baidu.com/f?kw=%B0%B5%BA%DA2")
            time.sleep(5)
            article_url = driver.find_element_by_xpath('//*[@id="thread_list"]/li[2]/div/div[2]/div[1]/div[1]/a').get_attribute(
                'href')
            if article_url in opened_url:
                time.sleep(60)
                continue
            opened_url.append(article_url)
            print(opened_url)
            driver.get(article_url)
            time.sleep(3)
            print(driver.title)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            edit_area = driver.find_element_by_xpath('//*[@id="ueditor_replace"]')
            time.sleep(1)
            it = random.randint(0, len(lis))
            print(lis[it])
            edit_area.send_keys(lis[it])
            print("send text")
            time.sleep(2)
            pub_button = driver.find_element_by_xpath('//*[@id="tb_rich_poster"]/div[3]/div[3]/div/a/span/em')
            driver.execute_script("arguments[0].click();", pub_button)
            print("click publish")

            time.sleep(60)
        except Exception as e:
            print(e)
            # driver.quit()
        # c_service.stop()


def publish(list):
    try:
        publishing(list)
    except Exception as e:
        print("publishing error")
        print(e)



lis = ['说的好，老哥，来群里水水经验吧 777344078',
       '情怀老哥，一起玩啊。暗黑2欢乐裙 777344078',
       '兄弟，有装备要卖的吗，来群 777344078，找群主，高价收。',
       '老哥有点东西啊，来群，咱们一起玩啊。777344078',
       '高价回收装备，极品装备，来群围观 777344078',
       '点一下，van一年，装逼不花一分钱，来群一起搞吧 777344078',
       '不会玩，可以来群里，热心老哥，亲情解答 777344078',
       '滴滴，来这群777344078，经常有老哥开升级车，偷渡车。']



publishing()