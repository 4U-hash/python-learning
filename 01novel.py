#小说

from selenium import webdriver
from bs4 import BeautifulSoup
import os

# Chrome浏览器
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(executable_path=r"F:\google\chromedriver.exe", options= chrome_options)
browser = driver.get('https://book.zhulang.com/399241/')

data = driver.page_source
# print(data)
# browser.quit()

soup = BeautifulSoup(data, "html.parser")  # 解析html代码
# 打印HTML代码中的关键代码
# print(soup)
li_list = soup.find_all('div', class_='catalog-cnt')[1].find('div', class_='chapter-list').find_all('li')  # 锁定ul后获取20个li

title = soup.find('div', class_='crumbs').find_all('a')[2].string # 锁定ul后获取20个li
print(title)
href_list = []
name_list= []

for li in li_list:
   # print(li.find('a')['href'])
   # print(li.find('a').string)
   href_list.append(li.find('a')['href'])
   name_list.append(li.find('a').string)

file_path = os.path.join('..', title, )
os.mkdir(file_path)

for _ in range(len(href_list)):
   if name_list[_] is None:
      continue
   else:
      # print(name_list[_])
      txt_path = os.path.join(file_path, name_list[_].replace(' ', '')+'.txt')
      with open(txt_path, 'a', encoding='utf-8') as f:
         driver = webdriver.Chrome(executable_path=r"F:\google\chromedriver.exe", options=chrome_options)
         browser = driver.get(href_list[_])

         data = driver.page_source
         # print(data)
         # browser.quit()

         soup = BeautifulSoup(data, "html.parser")  # 解析html代码
         # 打印HTML代码中的关键代码
         # print(soup)
         chapter_name = soup.find('div', class_='read-content').find('h2').get_text()
         f.write(chapter_name+ '\n')
         print(chapter_name)
         p_list = soup.find('div', class_='read-content').find_all('p')
         for p in p_list:
            if p.string is None:
               break
            else:
               f.write(p.string+'\n')
         f.close()








# positionInfo = []
# floor = []
# build_year = []
# for li in li_list:
#     positionInfo.append(li.find('div', class_='positionInfo').find('a').get_text())# 逐个解析获取书名
#     floor.append(li.find('div', class_='houseInfo').get_text().split('|')[0].replace('\n', '').replace(' ', ''))
#     build_year.append(li.find('div', class_='houseInfo').get_text().split('|')[1])
#
# print(positionInfo)
# print(floor)
# print(build_year)





