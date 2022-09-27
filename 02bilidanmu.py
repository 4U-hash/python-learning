import requests
import re

response = requests.get('https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid=822587296&pid=857726292&segment_index=2')
data = response.text

string_code = re.sub(u"([^\u4e00-\u9fa5])", " ", data)
content_list = string_code.split(' ')

content = []

for con in content_list:
    if con == '':
        continue
    else:
        content.append(con)
print(content)
