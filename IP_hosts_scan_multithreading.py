#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author:Rivaill
#这是一个用于IP和域名碰撞匹配访问的小工具(多线程)
import itertools
import threading
from multiprocessing.dummy import Pool
import requests
import re


def host_check(host_ip):
    host,ip = host_ip
    urls = ["http://"+ip,"https://"+ip]
    for url in urls :
        headers = {'Host':host.strip(),'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        try:
            r = requests.session()
            requests.packages.urllib3.disable_warnings()
            rhost = r.get(url,verify=False,headers=headers,timeout=30)
            rhost.encoding='utf-8'
            title = ""
            try:
                title = re.search('<title>(.*)</title>', rhost.text).group(1) #获取标题
            except Exception as ex:
                title = u"获取标题失败"
            info = u'%s -- %s 数据包大小：%d 标题：%s' % (host,url,len(rhost.text),title)

            if lock.acquire():
                try:
                    success_list.append(info)
                    with open('hosts_ok.txt','a+') as f:
                        f.write(info.encode("utf-8") + "\n")
                        f.close()
                        print(info)
                finally:
                    lock.release()

        except Exception as ex:
            if lock.acquire():
                try:
                    # print ex.message
                    # logging.exception(ex)
                    error = ip + " --- %s:%s --- 访问失败！~" % (host, url)
                    print(error)
                finally:
                    lock.release()



if __name__ == '__main__':
    lock = threading.Lock()
    success_list = []
    ip_list = open("ip.txt").read().splitlines()
    host_list = open("host.txt").read().splitlines()
    host_ip_list = list(itertools.product(host_list,ip_list))

    print("====================================开 始 匹 配====================================")

    pool = Pool(50)
    pool.map(host_check,host_ip_list)
    pool.close()
    pool.join()

    print("====================================匹 配 成 功 的 列 表====================================")
    for i in success_list:
        print(i)

