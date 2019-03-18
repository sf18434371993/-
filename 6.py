
# -*- coding: utf-8 -*-
import sys
import requests  # 导入requests 模块
import re
import xlwt
import time
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
key = '大黄'
p=1
for num in range(1,5):
    web_url='http://s.wanfangdata.com.cn/Paper.aspx?q='+ key +'&f=top&p=%s'%num

    header={'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

    r= requests.get(web_url,header,timeout=30)
    print r

    number = re.findall(r'<a class="title"(.*?)<span class="cited">', r.text,re.S)
    print(repr(number).decode('unicode-escape'))

    for i in number:
        k=re.findall(r'href=(.*?) target=', i)
        k=' '.join(k)
    
        sub=re.sub(r'\'','',k)
    
        url =sub
        r2=requests.get(url,header,timeout=20)
        wenxian=r2.content
        print wenxian
    
        abstract=re.findall(r'<div class="text">(.*?)</div>', r2.text,re.S)
        print (repr(abstract).decode('unicode-escape'))
        for zhaiyao in abstract:
            with open('wenxian.txt' ,'a') as f:
                 f.write(zhaiyao+'\n')
    
    
    
    
