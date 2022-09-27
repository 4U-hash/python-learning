#selnium获取cookie,失败，只能取到局部cookies
#网站取得cookies也用不上，必须要domain


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json


# 首先获取cookies保存至本地
def get_cookie():
    driver = webdriver.Chrome('F:\google\chromedriver.exe')
    page_url = 'https://www.douban.com/'
    driver.get(page_url)
    driver.maximize_window()
    # 进行扫码登录
    time.sleep(20)
    # 获取列表形式的cookies
    cookies = driver.get_cookies()
    print(cookies)
    # 转换成字符串保存
    jsonCookie = json.dumps(cookies)
    # 保存到txt文件
    with open('./cookies.txt','w') as f:
        f.write(jsonCookie)

def login():
    with open('./cookies.txt', 'r') as f:
        jsonCookie = f.read()

    cookies = json.loads(jsonCookie)
    # 给浏览器添加cookies
    cookie_dict = {}
    for cookie in cookies:
        cookie_dict = {
            'name': cookie.get('name'),
            'value': cookie.get('value'),
        }
        driver = webdriver.Chrome('F:\google\chromedriver.exe')
    driver.add_cookie(cookie_dict)
    page_url = 'https://www.douban.com/'
    driver.get(page_url)
    driver.refresh()
    driver.find_element(By.NAME, 'q').send_keys('三体')
    driver.find_element(By.CLASS_NAME, 'inp-btn').click()
    time.sleep(10)
    driver.quit()

if __name__ == '__main__':
    get_cookie()
    login()



# driver = webdriver.Chrome(executable_path=r"F:\google\chromedriver.exe")
# browser = driver.get('https://www.douban.com/')
#
# time.sleep(5)
# login_class = driver.find_element(By.CLASS_NAME, 'tab-start')
# driver.execute_script('arguments[1].click()', login_class)
#
# driver.find_element(By.ID, 'username').send_keys('13934392919')
# driver.find_element(By.ID, 'password').send_keys('fsr991212')
#
# driver.find_element(By.CLASS_NAME, 'btn btn-account').click()
#
# driver.find_element(By.NAME, 'inp-query').send_keys('三体')
# driver.find_element(By.CLASS_NAME, 'inp-btn').click()
# time.sleep(10)
# driver.quit()

