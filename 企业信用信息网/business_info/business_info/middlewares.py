# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
import urllib.request

import scrapy
import time
import requests


class ProxyMiddleware(object):

    def __init__(self):
        self.url = 'http://dev.kuaidaili.com/api/getproxy/?orderid=980124232095767&num=20&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_tr=1&an_an=1&an_ha=1&sp1=1&sp2=1&sp3=1&sort=1&dedup=1&sep=1'
        self.num = 0
        # self.prox_list = requests.get(self.url).content
        self.prox_list = []
        self.get_proxy()

    def get_proxy(self):
        request = urllib.request.Request(self.url)
        response = urllib.request.urlopen(request)
        self.prox_list = response.read().decode().split('\r\n')
        # self.prox_list = scrapy.Request(self.url).body.decode().split('\r\n')


    # def get_list(self, response):
    #     self.prox_list = response.body.decode().split('\r\n')
    #     print(self.prox_list)

    def process_request(self, request, spider):
        prox = random.choice(self.prox_list)
        print(prox)
        request.meta['proxy'] = 'http://' + str(prox)
        self.num += 1
        if self.num > 60:
            # self.prox_list = requests.get(self.url).content
            self.get_proxy()
            self.num = 0
