import csv
import json
import pickle
import time

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

class Douban():

    def __init__(self):

        self.driver = webdriver.Chrome(executable_path=r"F:\google\chromedriver.exe")

    def get_cookies(self):

        browser = self.driver.get('https://www.douban.com/')

        elementi= self.driver.find_element(By.XPATH, '//*[@id="anony-reg-new"]/div/div[1]/iframe')
        #再将定位对象传给switch_to_frame()方法
        self.driver.switch_to.frame(elementi)

        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/ul[1]/li[2]').click() #class_name不好用
        time.sleep(10)

        username = '' #输入为字符串
        password = ''

        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)

        #关于验证码
        #下载图片
        #送入卷积网络得到结果
        #Selnium输入结果

        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
        self.driver.switch_to.default_content() #必须返回主frame

        dictCookies = self.driver.get_cookies()  # 获取list的cookies
        jsonCookies = json.dumps(dictCookies)
        time.sleep(10)

        with open('./douban_cookies', 'wb') as f:
            pickle.dump(jsonCookies, f)
        # print('cookies保存成功！')
        # pickle.dump(dictCookies, open('douabn-cookies.pkl', 'wb'))
        # print('cookies保存成功！')


    def get_looked_movies(self):
        # driver = self.webdriver.Chrome(executable_path=r"F:\google\chromedriver.exe")
        cookie_info = ''
        cookie_list = [info.strip().split('=') for info in cookie_info.split(';')]
        cookies = {data[0]: data[1].replace('"', '') for data in cookie_list}
        print(cookies)
        self.driver.get('https://www.douban.com/')
        self.driver.delete_all_cookies()

        # with open('./damai_cookies.txt', 'r', encoding='utf8') as f:
        #     listCookies = json.loads(f.read())
        #
        # # 往browser里添加cookies
        # for cookie in listCookies:
        #     cookie_dict = {
        #         'domain': cookie.get('domain'),
        #         'name': cookie.get('name'),
        #         'value': cookie.get('value'),
        #         "expires": cookie.get('expires'),
        #         'path': '/',
        #         'httpOnly': False,
        #         'Secure': False
        #     }
        # print(cookie_dict)
        self.driver.add_cookie(cookies)

        self.driver.get('https://www.douban.com/')
        # self.driver.refresh()
        time.sleep(10)

        self.driver.find_element(By.XPATH, '//*[@id="db-nav-sns"]/div/div/div[3]/ul/li[2]/a').click()
        looked = self.driver.find_elements(By.XPATH, '//*[@id="movie"]/div[2]/ul/li')
        time.sleep(10)

        with open('./looked_movies.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(["title", "href", "img_href"])
            for i in range(len(looked)):
                # print(looked[i].find_element(By.TAG_NAME, 'a').get_attribute('href')) #查询结果也可以用find_element
                # #即使img在a标签里，也可以直接使用标签名查询
                # print(looked[i].find_element(By.TAG_NAME, 'img').get_attribute('src'))
                writer.writerow([looked[i].find_element(By.TAG_NAME, 'a').get_attribute('title'),
                                looked[i].find_element(By.TAG_NAME, 'a').get_attribute('href'),
                                looked[i].find_element(By.TAG_NAME, 'img').get_attribute('src')])
    def req(self):
        global cookie_dict
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
        }

        with open('./douban_cookies', 'r', encoding='utf8') as f:
            listCookies = json.loads(f.read())

        # 往browser里添加cookies
        for cookie in listCookies:
            cookie_dict = {
                'domain': cookie.get('domain'),
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                "expires": cookie.get('expires'),
                'path': '/',
                'httpOnly': False,
                'Secure': False
            }
        print(cookie_dict)

        res = requests.get('https://accounts.douban.com/passport/login?redir=https://www.douban.com/gallery/mine',
                       headers = headers, cookie = cookie_dict).content.decode()
        print(res)

if __name__ == "__main__":
    douban = Douban()
    # douban.get_cookies()
    douban.get_looked_movies()
    # douban.req()
