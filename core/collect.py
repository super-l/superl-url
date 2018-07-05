# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/superl-url.git

'''
    采集任务
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

from module.sougou.sougou import Sougou

if sys.version < '3':
    from urllib2 import unquote
else:
    from urllib.parse import unquote


from core.config import Config
import time

from core.outfile import OutFile

from module.baidu.baidu import Baidu
from module.so.so import So


class Collect(object):

    def __init__(self, module, page, pagesize, keyword):
        self.config = Config()
        self.module = module
        self.page = int(page)
        self.keyword = keyword
        self.pageSize = int(pagesize)

        self.saveFile = self.config.getValue("global", "savefile")

        if self.saveFile == 'True':
            self.outfile = OutFile(unquote(self.keyword))
        else:
            self.outfile = None

        self.collection()



    def collection(self):

        for i in range(self.page):
            print("\033[1;37;40m[*]Search Engine [%s],Page [%s] Start collecting." % (self.module, i+1))

            page_pn = (i * self.pageSize)

            if self.module == "baidu":
                my_baidu = Baidu(self.outfile)
                my_baidu.search(self.keyword, self.pageSize, page_pn)

            elif self.module == "so":
                my_so = So(self.outfile)
                my_so.search(self.keyword, i+1)

            elif self.module == "sougou":
                my_sougou = Sougou(self.outfile)
                my_sougou.search(self.keyword, i+1)

            if self.config.sleeptime > 0:
                time.sleep(self.config.sleeptime)

        if self.outfile == 'True':
            self.outfile.closeFile()









