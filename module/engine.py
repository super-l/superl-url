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
from core.filter import *


class Engine(object):

    def __init__(self, searchname, outfile=None):
        self.searchName = searchname
        self.config = Config()
        self.outfile = outfile

        self.writeTitle = self.config.getValue("log", "write_title")
        self.writeEngineName = self.config.getValue("log", "write_name")

        self.filterStatus = self.config.getValue("filter", "filter_status")

        self.filter = Filter()
        self.tempUrlList = []
        self.tempUrlTextList = []

    def get_url(self, target_url):
        pass

    def writefile(self):
        for content in self.tempUrlTextList:
            self.outfile.writeToFile(content)




