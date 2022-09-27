import os
import random
import re
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# 实例化driver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path=r"F:\google\chromedriver.exe")
# driver.get('https://www.douban.com/')
# ## 切换iframe子框架
# driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])
#
# driver.maximize_window()  # 最大化窗口
# driver.find_element(By.CSS_SELECTOR, 'li.account-tab-account').click()  # 点击密码登录的标签
# driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('13934392919')
# driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('fsr991212')
# # 点击‘登录豆瓣’按钮
# # 这里需要注意，当元素的class属性有好几个的时候，此函数的参数填class的第一个就好
# driver.find_element(By.CLASS_NAME, 'btn').click()  # 元素的class属性：btn btn-account
# # 获取cookies,字典推导式
# cookies = {i['name']: i['value'] for i in driver.get_cookies()}
# print(cookies)
#
# time.sleep(5)
# driver.quit()  # 退出浏览器

cookie_info = 'douban-fav-remind=1; gr_user_id=bfbf6b0d-b0c0-4653-88d4-f2bd7cb31b5d; ll="118107"; bid=uqxq8W9k26w; push_doumail_num=0; __utmv=30149280.14192; push_noty_num=0; _pk_ref.100001.8cb4=["","",1663578352,"https://www.google.com/"]; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.280507868.1583798340.1663319925.1663578353.16; __utmc=30149280; __utmz=30149280.1663578353.16.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not provided); ct=y; __utmt=1; _pk_id.100001.8cb4=d33d4b7b45923444.1662625569.10.1663581535.1663320605.; __utmb=30149280.30.10.1663578353; dbcl2="141920748:taE/ULJRGBk"'
cookie_list = [info.strip().split('=') for info in cookie_info.split(';')]
cookies = {data[0]:data[1].replace('"', '') for data in cookie_list}
print(cookies)

url = 'https://movie.douban.com/chart'
headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
# html = requests.get(url, headers=headers, cookies=cookies).content.decode()

session = requests.session() #创建session对象
requests.utils.add_dict_to_cookiejar(session.cookies, cookies) #将cookie信息存入cookiejar对象中
html = session.get(url, headers=headers).content.decode() #进行请求

soup = BeautifulSoup(html, "html.parser")  # 解析html代码
movie_list = []

movie_div = soup.find_all('div', class_= 'pl2')

for movie in movie_div:
    movie_list.append(movie.find('a')['href'])

for _ in range(len(movie_list)):
    movie_page = session.get(movie_list[_], headers=headers).content.decode()

    movie_soup = BeautifulSoup(movie_page, "html.parser")
    number_content = movie_soup.find('div', class_='mod-hd').find('span', class_ = 'pl').find('a').string
    number = re.sub(u"([^\u0030-\u0039])", "", number_content)
    print(number)
    movie_title = movie_soup.title.text.replace(' ', '').replace('\n', '')
    with open('./' + movie_title + '.txt', 'a', encoding='utf-8') as f:
        for i in range(int(int(number)/20)):
            review_url = movie_list[_] + 'comments?' + 'start='+str(i*20)+'&limit=20&status=P&sort=new_score'
            review_page = session.get(review_url, headers=headers).content.decode()
            time.sleep(random.uniform(0, 2))
            review_soup = BeautifulSoup(review_page, "html.parser")
            # print(review_soup)
            # print(review_soup)
            review_list = review_soup.find_all('div', class_ = 'comment-item')
            if len(review_list) == 0:
                break
            else:
                print(review_list)
                for review in review_list:
                    print(review.find('span', class_ = 'short').string)
                    f.write(review.find('span', class_ = 'short').string)
                    f.write('\n')