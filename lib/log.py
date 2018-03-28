# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/search-url.git
# Author  = superl
# Blog    = www.superl.org   QQ:86717375
# Team    = 忘忧草安全团队(Nepenthes Security Team)
import ConfigParser

class SupLog():

    def __init__(self) :
        cfg = ConfigParser.ConfigParser()
        cfg.read("config/setting.conf")

        self.log_file = cfg.get("global", "log_file")



