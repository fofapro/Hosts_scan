#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author:R3start
#这是一个用于IP和域名碰撞匹配访问的小工具

import requests
import re


lists=[]
files = open('hosts_ok.txt','w+')
#读取IP地址
print("====================================开 始 匹 配====================================")
for iplist in open("ip.txt"):
    ip = iplist.strip('\n')
    #读取host地址
    http_s = ['http://','https://']
    for h in http_s :
        for hostlist in open("host.txt",'r'):
            host = hostlist.strip('\n')
            headers = {'Host':host,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
            try:
                r = requests.session()
                requests.packages.urllib3.disable_warnings()
                rhost = r.get(h + ip,verify=False,headers=headers,timeout=5)
                rhost.encoding='utf-8'
                title = re.search('<title>(.*)</title>', rhost.text).group(1) #获取标题
                info = '%s -- %s 协议：%s 数据包大小：%d 标题：%s' % (ip,host,h,len(rhost.text),title)
                lists.append(info)
                files.write(info + "\n")
                print(info)
            except Exception :
                error = ip + " --- " + host + " --- 访问失败！~"
                print(error)
print("====================================匹 配 成 功 的 列 表====================================")
for i in lists:
    print(i)