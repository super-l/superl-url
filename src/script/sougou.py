# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/search-url.git
# Author  = superl
# Blog    = www.superl.org   QQ:86717375
# Team    = Code Security Team(C.S.T) | 铭剑创鼎
import urllib2
import re 
import ConfigParser

from lib.filter import *
from lib.getdata import *
from lib.count import *
from lib.status import *

class Sougou():

    search_name = '[搜狗]'

    def __init__(self,count) :
        cfg = ConfigParser.ConfigParser()
        cfg.read("config/setting.conf")

        self.savefile = cfg.get("global", "savefile")
        self.write_title = cfg.get("log", "write_title")
        self.write_name = cfg.get("log", "write_name")
        self.my_filter = SupFilter()
        self.my_data = SupGetData()
        self.my_status = Supstatus()
        self.count = count


    #Get the web page source code
    def search(self,key,page):
        search_url = 'https://www.sogou.com/web?query=key&page='+str(page)
        search_url = search_url.replace('key',key)

        htmlcontent = self.my_data.get_pagehtml(search_url,'sougou')

        regex_page = r'<span>'+str(page)+'</span>'
        page_compile = re.compile(regex_page)
        page_result = page_compile.findall(htmlcontent)

        if page_result:
            pass
        else:
            self.my_status.sougou_search = False
            return

        regex_url = r'<h3.*?href="http://www.sogou.com/link(?P<url>.+?)".*?>(?P<title>.+?)</a>.*?</h3>'

        content = re.compile(regex_url,re.S)
        find_result = content.findall(htmlcontent)


        print ("\033[1;37;40m==========================搜狗 第%s页采集开始================\n"%(page))


        if self.savefile == 'True':
            logfile = open(key+'.txt','a')

        for i in range(len(find_result)):
            dr = re.compile(r'<[^>]+>',re.S)
            title = dr.sub('',find_result[i][1])
            url = "http://www.sogou.com/link"+str(self.my_data.get_sougou_realurl(find_result[i][0]))
            realurl = self.my_data.get_sougou_realurl(url)

            self.count.all_totals+=1
            realurl = self.my_filter.filter_data(realurl,title)

            if realurl != "filter":
                self.count.all_checked_totals+=1

                print ("[ID]:%d  [URL]:%s  [TITLE]:%s"%(i,realurl,title))
                if self.savefile == 'True':
                    have_url = 0
                    with open(key+'.txt','r') as foo:
                        for line in foo.readlines():
                            if realurl in line:
                                have_url = 1
                        if have_url ==0:
                            if self.write_title:
                                if self.write_name:
                                    logfile.write(self.search_name+realurl+'    '+title+'\n')
                                else:
                                    logfile.write(realurl+'    '+title+'\n')
                            else:
                                if self.write_name:
                                    logfile.write(self.search_name+realurl+'\n')
                                else:
                                    logfile.write(realurl+'\n')
                        else:
                            self.count.all_delete_totals+=1   
            else:
                self.count.all_filter_totals+=1
        if self.savefile == 'True':        
            logfile.close()        
        print ("==========================搜狗 第%s页采集结束================\n"%(page)) 
                  
        
    