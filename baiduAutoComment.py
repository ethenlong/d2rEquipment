# -*-coding:utf-8-*-

from selenium import webdriver
import json
import time

print ("hekko")

from selenium.webdriver.chrome.service import Service
import os

#
driver = webdriver.Chrome()
driver.get("https://tieba.baidu.com/f?kw=%B0%B5%BA%DA2")
time.sleep(60)
cookies = driver.get_cookies()
with open("qrsncookies.txt", "w") as fp:
    json.dump(cookies, fp)
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

    #chrome
    option = webdriver.ChromeOptions()
    # option.set_headless()
    option.add_argument("--headless")
    option.add_argument("--no-sandbox")
    driver = webdriver.Chrome(chrome_options=option)
    # driver = webdriver.Chrome()

    #firefox
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
    print (driver.title)
    time.sleep(20)
    return driver, c_service

def publishing(list):
    driver, c_service = read_cookies()
    # time.sleep(10)
    # print(list)
    # driver.find_element_by_xpath('//*[@id="global-new-tweet-button"]').click()
    # '//*[@id="thread_list"]/li[2]/div/div[2]/div[1]/div[1]/a'
    driver.find_element_by_xpath('//*[@id="thread_list"]/li[2]/div/div[2]/div[1]/div[1]/a').click()
    print("click first article")
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div').send_keys(list[0])
    print("send text")
    time.sleep(10)
    lenth = len(list)
    for lis in list[1:lenth]:
        lis = lis.strip()
        if lis is None:
            break

        # driver.find_element_by_xpath(
        #     '//*[@id="Tweetstorm-tweet-box-0"]/div[2]/div[2]/div[1]/span[1]/div/div/label/input').send_keys(
        #     "/home/centos/shell/tianxiubot/" + lis)
        driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[1]/input').send_keys(
            "/home/centos/shell/tianxiubot/" + lis)
        # print("click publish")
        # /home/centos/shell/tianxiubot/
        # E:\work\\twbot\\tianxiubot\\
        # print(lis)
        time.sleep(1)
    print("send pics")
    time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="Tweetstorm-tweet-box-0"]/div[2]/div[2]/div[2]/span/button[2]').click()
    #driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]/div').click()
    pub_button = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
    driver.execute_script("arguments[0].click();", pub_button)

    print("click publish")
    time.sleep(30)
    driver.quit()
    c_service.stop()
    os.system('bash killchrome.sh')

def publish(list):
    try:
        publishing(list)
    except Exception as e:
        os.system('bash killchrome.sh')
        print("publishing error")
        print(e)
