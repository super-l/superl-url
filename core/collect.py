# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/superl-url.git

'''
    采集任务核心
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
import sys
import time

if sys.version < '3':
    try:
        # python2
        from urllib2 import unquote
    except ImportError:
        print("urllib2 's unquote import error!")
else:
    try:
        # python3
        from urllib.parse import unquote
    except ImportError:
        print("urllib.parse 's unquote import error!")


from core.config import Config
from core.outdata import OutData

class Collect(object):

    def __init__(self, module, page, pagesize, keyword):
        self.config = Config()
        self.module = module
        self.page = int(page)
        self.keyword = keyword
        self.pageSize = int(pagesize)

        self.OutData = OutData(unquote(self.keyword))

        self.collection()


    def collection(self):

        for i in range(self.page):
            print("\033[1;37;40m[*]Search Engine [%s],Page [%s] Start collecting." % (self.module, i+1))

            if self.module == "baidu":
                page_pn = (i * self.pageSize)

                from module.baidu.baidu import Baidu
                my_baidu = Baidu(self.OutData)
                my_baidu.search(self.keyword, self.pageSize, page_pn)

            elif self.module == "so":
                from module.so.so import So
                my_so = So(self.OutData)
                my_so.search(self.keyword, i+1)

            elif self.module == "sougou":
                from module.sougou.sougou import Sougou
                my_sougou = Sougou(self.OutData)
                my_sougou.search(self.keyword, i+1)


            if int(self.config.datas['sleep_time']) > 0:
                time.sleep(int(self.config.datas['sleep_time']))
