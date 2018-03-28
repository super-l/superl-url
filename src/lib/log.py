# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/search-url.git
# Author  = superl
# Blog    = www.superl.org   QQ:86717375
# Team    = Code Security Team(C.S.T) | 铭剑创鼎
import urllib2

class SupLog():

    def __init__(self) :
        cfg = ConfigParser.ConfigParser()
        cfg.read("config/setting.conf")

        self.log_file = cfg.get("global", "log_file")



