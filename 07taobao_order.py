import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
import pandas as pd
import time
import random


class AlibabaBought:
    '''
    抓取个人淘宝订单的已购买的订单
    '''

    url = 'https://www.taobao.com'
    mytaobao_xpath = '//*[@id="J_SiteNavMytaobao"]/div[1]/a'
    bought_xpath = '//*[@id="bought"]'
    page_xpath = '//*[@id="tp-bought-root"]/div[14]/div[2]/ul/li[@class="pagination-next"]'

    date_list = []
    order_list = []
    title_list = []
    shop_list = []
    num_list = []
    price_list = []
    statecode_list = []
    unit_price_list = []

    total_list = []

    def __init__(self):

        '''
        实例化的时候自动设置浏览器的参数
        '''
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1500,1366')
        self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"F:\google\chromedriver.exe")

    def click_case(self, my_xpath):

        '''
        点击事件
        '''

        button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, my_xpath))
        )
        button.click()

    def click_mytaobao(self):
        '''
        打开需要访问的网站,点击我的淘宝
        '''

        self.browser.get(self.url)
        self.click_case(my_xpath=self.mytaobao_xpath)

    # 扫码登录
    def click_bought(self):
        '''
        点击已买到的宝贝
        '''
        self.click_case(self.bought_xpath)

    def click_next_page(self):
        '''
        点击下一页
        '''
        self.click_case(self.page_xpath)

    def analysis_web(self, order_list_xpath, order_list):
        '''解析网页源代码'''
        page_taobao_html = self.browser.page_source
        my_data = etree.HTML(page_taobao_html).xpath(order_list_xpath)
        print(my_data)
        order_list.append(my_data)
        # print(my_data[0])
        print('-' * 100)

    def make_data_xpath(self):
        '''构造订单信息的xpath路径并解析源码保存到列表中'''
        for i in range(4, 14):
            # date_xpath= '//*[@id="tp-bought-root"]/div[%s]/div/table/tbody[1]/tr/td[1]/label/span[2]/text()' % i
            # order_xpath= '//*[@id="tp-bought-root"]/div[%s]/div/table/tbody[1]/tr/td[1]/span/span[3]/text()' % i
            title_path = '//*[@id="tp-bought-root"]/div[%s]/div/table/tbody[2]/tr/td[1]/div/div[2]/p[1]/a/span[2]/text()' % i
            # shop_path= '//*[@id="tp-bought-root"]/div[%s]/div/table/tbody[1]/tr/td[2]/span/a/text()' % i
            num_path = '//*[@id="tp-bought-root"]/div[%s]/div/table/tbody[2]/tr/td[3]/div/p/text()' % i
            price_path = '//*[@id="tp-bought-root"]/div[%s]/div/table/tbody[2]/tr/td[5]/div/div[1]/p/strong/span[2]/text()' % i
            # statecode_path= '//*[@id="tp-bought-root"]/div[%s]/div/table/tbody[2]/tr/td[6]/div/p/span/text()' % i
            unit_price_path = '//*[@id="tp-bought-root"]/div[%s]/div/table/tbody[2]/tr/td[2]/div/p/span[2]/text()' % i
            try:
                # self.analysis_web(date_xpath, self.date_list)
                # self.analysis_web(order_xpath, self.order_list)
                self.analysis_web(title_path, self.title_list)
                # self.analysis_web(shop_path, self.shop_list)
                self.analysis_web(num_path, self.num_list)
                self.analysis_web(price_path, self.price_list)
                # self.analysis_web(statecode_path, self.statecode_list)
                self.analysis_web(unit_price_path, self.unit_price_list)
            except Exception:
                break


    def save_date(self):
        '''保存到指定路径下面为excel'''

        print(self.title_list)
        print(self.unit_price_list)
        print(self.price_list)
        print(self.num_list)

        with open('taobao.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["title", "price", "num"])
            for i in range(0, len(self.price_list)):
                if self.price_list[i] == []:
                    break
                else:
                    for j in range(0, len(self.unit_price_list[i])):
                        if self.title_list[i][j] == '保险服务':
                            continue
                        else:
                            writer.writerow([self.title_list[i][j], self.unit_price_list[i][j], self.num_list[i][j]])
                    writer.writerow([self.price_list[i][0]])

    def run(self):
        self.click_mytaobao()
        self.click_bought()

        while True:
            self.make_data_xpath()

            is_go_on = int(input("继续抓取请输入 1 ；退出请输入 2："))
            if is_go_on == 1:
                self.click_next_page()
                time.sleep(random.uniform(3, 5))
            elif is_go_on == 2:
                self.browser.close()
                break
        self.save_date()

def main():
    alibaba_bought = AlibabaBought()
    alibaba_bought.run()

if __name__== '__main__':
    main()


