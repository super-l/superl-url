# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/superl-url.git

'''
    程序基础功能模块
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
try:
    import ConfigParser
except ImportError:
    import configparser

class Config():

    def __init__(self):
        # python2和python3的ConfigParser大小写不同
        try:
            self.cfg = ConfigParser.ConfigParser()
        except:
            self.cfg = configparser.ConfigParser()

        self.cfg.read("config/setting.conf")

        self.sleeptime = int(self.cfg.get("global", "sleeptime"))

        self.baidu_search = self.cfg.get("search", "baidu_search")
        self.sougou_search = self.cfg.get("search", "sougou_search")
        self.so_search = self.cfg.get("search", "so_search")


    def getValue(self, type, name):
        return self.cfg.get(type, name)

