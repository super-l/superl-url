# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/superl-url.git
'''
    搜索引擎模块
    Created by superl[N.S.T].         忘忧草安全团队(Nepenthes Security Team)
                                                                      00000
                                                                      00000
                                                                      00000
      00000000    00000  00000  00000000000     00000000    000000000 00000
     00000000000  00000  00000  000000000000   00000000000  000000000 00000
     00000  000   00000  00000  000000 00000  000000 00000  00000000  00000
     000000000    00000  00000  00000   0000  0000000000000 000000    00000
      0000000000  00000  00000  00000   00000 0000000000000 00000     00000
         0000000  00000  00000  00000   00000 00000         00000     00000
     00000  0000  000000000000  000000000000  000000000000  00000     00000
     00000000000  000000000000  000000000000   00000000000  00000     00000
      000000000   0000000000    00000000000     00000000    00000     00000
                                00000
                                00000                   Blog:www.superl.org
                                00000
'''
import re

from core.filter import *
from core.config import Config

class Engine(object):

    def __init__(self, searchname, OutData=None):
        self.searchName = searchname
        self.config = Config()

        self.OutData = OutData
        self.Filter = Filter()

        self.filterStatus = self.config.datas['filter_status']

        # 已经采集到的网址
        self.tempUrlList = []

        # 保存地址 标题等多种信息
        self.tempUrlTextList = []


    def get_url(self, target_url):
        pass


    # 过滤器进行处理 如果被过滤，则跳过本次循环
    def check_filter(self,realurl, title):
        return self.Filter.filter_data(realurl, title)


    # 格式化输出并写入内容
    def write_print(self, id, baseurl, realurl, urlparam, title):

        # 如果被过滤 就仅仅输出，不写入
        if self.check_filter(realurl, title):

            self.outprint(id, realurl, title)
            self.write(baseurl, realurl, urlparam, title)
        else:
            self.outprint(id, realurl, title)


    # 写入内容
    def write(self, baseurl, realurl, urlparam, title):
        if realurl not in self.tempUrlList:
            self.tempUrlList.append(realurl)
            self.OutData.write(baseurl, realurl, urlparam, title, self.searchName)

    # 格式化输出内容
    def outprint(self, id, realurl, title):
        print("[ID]:%d  [URL]:%s  [TITLE]:%s  [Engine]:%s" % (id, realurl, title, self.searchName))

