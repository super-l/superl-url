# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/search-url.git
# Author  = superl
# Blog    = www.superl.org   QQ:86717375
# Team    = 忘忧草安全团队(Nepenthes Security Team)
import datetime
import time
import sys

from script.baidu import *
from script.sougou import *
from script.so import *
from lib.count import *

reload(sys)
sys.setdefaultencoding('utf8')


def show_logo():
    logostr = """\033[1;32;40m
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
                                00000                 blog:www.superl.org       
                                00000                                           
             {Author:superl   Version 2.1.0   Email:superl@nepenthes.cn}            
"""  
    print logostr


if __name__=='__main__':

    starttime = datetime.datetime.now()

    show_logo()

    key = raw_input('\033[1;33;40mplease input keyword:')
    key = key.encode('utf-8')
    key = urllib2.quote(key)

    page = int(raw_input("Search Number of pages:"))

    cfg = ConfigParser.ConfigParser()
    cfg.read("config/setting.conf")

    sleeptime = int(cfg.get("global", "sleeptime"))
    baidu_page_size = int(cfg.get("search", "baidu_page_size"))
    
    count = SupCount()
    my_baidu = Baidu(count)
    my_sougou = Sougou(count)
    my_so = So(count)
    my_status = Supstatus()

    for i in range(page):
        page_pn = (i * baidu_page_size)

        if my_status.baidu_search != 'False':
            my_baidu.search(key, page_pn)
            
        if my_status.sougou_search != 'False':  
            my_sougou.search(key, i+1)

        if my_status.so_search != 'False':  
            my_so.search(key, i+1)

        time.sleep(sleeptime)

    endtime = datetime.datetime.now()
    runtime = (endtime - starttime).seconds

    print("\033[1;36;40m%d found | %d checked | %d filter | %d delete | %d success      The program runs in %s seconds\033[1;37;40m"%(count.all_totals,count.all_checked_totals,count.all_filter_totals,count.all_delete_totals,count.all_checked_totals-count.all_delete_totals,runtime))
