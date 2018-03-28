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

class Baidu():

    baidu_page_size = 50
    search_name = '[baidu]'

    def __init__(self,count) :
        cfg = ConfigParser.ConfigParser()
        cfg.read("config/setting.conf")

        self.baidu_page_size = int(cfg.get("search", "baidu_page_size"))
        self.savefile = cfg.get("global", "savefile")
        self.write_title = cfg.get("log", "write_title")
        self.write_name = cfg.get("log", "write_name")
        self.my_filter = SupFilter()
        self.my_data = SupGetData()
        self.my_status = Supstatus()
        self.count = count


    #Get the web page source code
    def search(self,key,page_pn):
        #The number of baidu pages currently viewed
        #page_num = page_pn/baidu_page_size
        page_num = str(page_pn/self.baidu_page_size+1)

        search_url = 'http://www.baidu.com/s?wd=key&rn='+str(self.baidu_page_size)+'&pn='+str(page_pn)
        search_url = search_url.replace('key',key)
        #print search_url
        htmlcontent = self.my_data.get_pagehtml(search_url,'baidu')

        regex_page = r'<span class="pc">'+page_num+'</span>'
        page_compile = re.compile(regex_page)
        page_result = page_compile.findall(htmlcontent)

        if page_result:
            pass
        else:
            self.my_status.baidu_search = False
            return

        regex_titleurl = r'<div class="result c-container ".*<h3 class=".*"><a(?:[^\<]*\n[^\<]*)href = "(?P<url>.+?)"(?:[^\<]*\n[^\<]*)target="_blank"(?:[^\<]*\n[^\<]*)>(?P<title>.+?)</a></h3>'

        content = re.compile(regex_titleurl)
        find_result = content.findall(htmlcontent)

        print ("\033[1;37;40m==========================百度 第%s页采集开始================\n"%(page_num))
       
        if self.savefile == 'True':
            logfile = open(key+'.txt','a')

        for i in range(len(find_result)):
            dr = re.compile(r'<[^>]+>',re.S)
            title = dr.sub('',find_result[i][1])

            realurl = self.my_data.get_baidu_realurl(find_result[i][0])

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
        print ("==========================百度 第%s页采集结束================\n"%(page_num))           
        
    