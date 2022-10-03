#json

import requests
import json
import re


import csv
import pandas as pd
import time
def req(df):
    for i in df['单号']:
		cookies = {
		}
		headers = {
			'Connection': 'keep-alive',
			'Pragma': 'no-cache',
			'Cache-Control': 'no-cache',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
			'Accept': '*/*',
			'Referer': 'http://travel.yundasys.com:31432/index',
			'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
		}

		params = (
		)

		response = requests.get('', headers=headers, params=params, cookies=cookies, verify=False).text
		time.sleep(1)
		res=json.loads(response)

		print(res)
		if len(res) != 0:
			data = [res[0].get('txm'), '山东临沂']
			for i in res:
				if getOneData(i)[0] != '' and getOneData(i)[1] != '':
					data = data + [getOneData(i)[0], getOneData(i)[1]]
					# print(data)
			with open(r'./data.csv', 'a+', encoding="utf-8-sig", newline="")as f:
				writer = csv.writer(f)
				writer.writerows([data])
			print(data)
		else:
			continue

def getOneData(i):#获取一条数据x
    realweight=''
    countweight=''
    redAddress = ''.join(re.findall('class="wltz">.*?\((.*?)\)</span>',i['record'],re.S))  # 记录地址
    redAddress=redAddress[0:6]
    # print(redAddress)
    if redAddress[0:18]=='276088':
        if i['realweight']== '':
            realweight='×'
        else:
            realweight=i['realweight']#称重重量(千克)
        if i['countweight'] == '':
            countweight = '×'
        else:
            countweight = i['countweight']  # 称重重量(千克)
    else:
        pass
    return realweight,countweight


if __name__ == '__main__':
    df=pd.read_excel(r'C:\Users\范斯锐\Documents\Tencent Files\1524820943\FileRecv\单号.xlsx',engine='openpyxl')
    req(df)

