# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/search-url.git
# Author  = superl
# Blog    = www.superl.org   QQ:86717375
# Team    = Code Security Team(C.S.T) | 铭剑创鼎
import ConfigParser

class Supstatus():

    baidu_search = True
    sougou_search = True
    so_search = True


    def __init__(self) :
        cfg = ConfigParser.ConfigParser()
        cfg.read("config/setting.conf")

        self.baidu_search = cfg.get("search", "baidu_search")
        self.sougou_search = cfg.get("search", "sougou_search")
        self.so_search = cfg.get("search", "so_search")