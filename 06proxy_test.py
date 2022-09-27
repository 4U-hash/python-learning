#代理没法用


import random
import re
import time

import requests
from bs4 import BeautifulSoup

headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
#
#
# proxy={
#     'http':'122.9.101.6:8888'  #可以找找国内的一些免费ip
# }
#
# response = requests.get('https://www.zdaye.com/dayProxy.html', headers=headers, verify=False, proxies=proxy).content.decode()
# print(response)
#
#
# url_soup = BeautifulSoup(response, "html.parser")  # 解析html代码
# proxy_a = url_soup.find_all('div', class_='thread_footer')[0]
# proxy_url_part = proxy_a.find('a', class_='thread_theme_type')['href']
# # print(proxy_url_part)
#
# proxy_list = []
# for i in range(1, 4):
#     time.sleep(random.uniform(0, 10))
#     proxy_url = 'https://www.zdaye.com' + proxy_url_part.replace('.html', '') +'/'+ str(i) + '.html'
#     print(proxy_url)
#     proxy_response = requests.get(proxy_url, headers=headers, verify = False, proxies=proxy).content.decode(encoding='UTF-8', errors='ignore')
#     proxy_soup = BeautifulSoup(proxy_response, 'html.parser')
#     print(proxy_soup)
#
#     proxy_content_list = proxy_soup.find_all('tr')[1:]
#     print(proxy_content_list)
#
#     for proxy_each in proxy_content_list:
#         proxy_ip = proxy_each.find('td')[0].get_text()
#         proxy_port = proxy_each.find('td')[1].get_text()
#         proxy_list.append([proxy_ip, proxy_port])
#     print(proxy_list)
#
# proxy_pool = []
#
# for proxy_iter in proxy_list:
#     proxy_pool.append(http=proxy_ip+':'+proxy_port)
#
# print(proxy_pool)


# proxy = re.findall(r'((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?[1-9])))(\:\d)*)', proxy_each)
# print(proxy)


# proxy={
#     'HTTPS': "HTTPS://36.138.56.214:3128"  #可以找找国内的一些免费ip
# }
# response = requests.get('https://2022.ip138.com/', headers=headers,  proxies=proxy).content.decode()
# print(response)


# 导入requests库
import requests

# 设置自己的代理IP和端口如下：
proxies = {
    "HTTP": "HTTP://36.138.56.214:3128",
    "HTTPS": "HTTPS://36.138.56.214:3128",
}

# 要获取的URl地址，这里里ip138为例用来验证自己的代理是否成功，如果和使用浏览器访问结果一样就证明成功了
get_url = 'https://2022.ip138.com'

# 根据实际情况设置请求头信息
header = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36 Edg/97.0.1072.76'
}
# 屏蔽https证书警告
requests.packages.urllib3.disable_warnings()

# 获取远程网页数据
body = requests.get(url=get_url, proxies=proxies, headers=header, verify=False).content.decode()
print(body)
