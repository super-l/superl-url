# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/search-url.git
# Author  = superl
# Blog    = www.superl.org   QQ:86717375
# Team    = 忘忧草安全团队(Nepenthes Security Team) | 铭剑创鼎

import re 
import urllib2
from tld import get_tld
import time

import os
import datetime
#the baidu page size

all_totals = 0
all_checked_totals = 0
all_filter_totals = 0
all_delete_totals = 0


baidu_page_size = 50

filter_array1 = ['baidu.com','sina.com.cn','sohu.com','taobao.com','douban.com','163.com','tianya.cn','qq.com','1688.com']
filter_array2 = ['ganji.com','58.com','baixing.com']
filter_array3 = ['zhihu.com','weibo.com','iqiyi.com','kugou.com','51.com','youku.com','soku.com','acfun.cn','verycd.com']
filter_array4 = ['google.cn','youdao.com','iciba.com','cdict.net']
filter_array5 = ['pconline.com.cn','zcool.com.cn','csdn.net','lofter.com']

filter_array_all = filter_array1+filter_array2+filter_array3+filter_array4+filter_array5

  
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
             {Author:superl   Version 1.0.0   Email:superl@nepenthes.cn}            
"""  
    print logostr


#Get the web page source code
def get_pagehtml(url):
    try:
        get_request = urllib2.urlopen(url)   
        result_htmlcontent = get_request.read()
        return result_htmlcontent;
    except urllib2.HTTPError, e:
        print e.code


#Get the real url
def get_realurl(target_url):
    try:
        response = urllib2.urlopen(target_url,timeout = 3)
        realurl = response.geturl()
        return realurl
    except Exception, e:
        return target_url


#Filter the real URL
def filter_url(target_url,urlparam):
    domain = get_tld(target_url)
    if domain in filter_array_all:
        return 'filter'
    else:
        if urlparam == 1:
            reg = r'^https?:\/\/([a-z0-9\-\.]+)[\/\?]?'
            m = re.match(reg, target_url)
            if m :
                uri = m.groups()[0]
                return uri[uri.rfind('//', 0, uri.rfind('.')) + 1:]
            else:
                return target_url
        else:
            return target_url



def baidu_search(key,page_pn=50,filter=1,savefile=1,urlparam=1):
    #The number of baidu pages currently viewed
    #page_num = page_pn/baidu_page_size
    page_num = str(page_pn/baidu_page_size+1)

    search_url = 'http://www.baidu.com/s?wd=key&rn='+str(baidu_page_size)+'&pn='+str(page_pn)
    search_url = search_url.replace('key',key)
    htmlcontent = get_pagehtml(search_url)

    regex_titleurl = r'<div class="result c-container ".*<h3 class=".*"><a(?:[^\<]*\n[^\<]*)href = "(?P<url>.+?)"(?:[^\<]*\n[^\<]*)target="_blank"(?:[^\<]*\n[^\<]*)>(?P<title>.+?)</a></h3>'

    content = re.compile(regex_titleurl)
    find_result = content.findall(htmlcontent)

    print ("\033[1;37;40m==========================第%s页采集开始================\n"%(page_num))
    

    if savefile ==1:
        logfile = open(key+'.txt','a')
        #logfile.write("==========================第"+page_num+"页采集开始================\n")

    for i in range(len(find_result)):
        dr = re.compile(r'<[^>]+>',re.S)
        title = dr.sub('',find_result[i][1])

        realurl = get_realurl(find_result[i][0])

        global all_totals
        all_totals+=1

        if filter == 1:
            realurl = filter_url(realurl,urlparam)

        if realurl != "filter":
            global all_checked_totals
            all_checked_totals+=1

            print ("[ID]:%d  [URL]:%s  [TITLE]:%s"%(i,realurl,title))
            if savefile ==1:
                have_url = 0
                with open(key+'.txt','r') as foo:
                    for line in foo.readlines():
                        if realurl in line:
                            have_url = 1
                    if have_url ==0:
                        logfile.write(realurl+'\n')
                    else:
                        global all_delete_totals
                        all_delete_totals+=1
        else:
            global all_filter_totals
            all_filter_totals+=1

    print ("==========================第%s页采集结束================\n"%(page_num))           
    if savefile ==1:  
        #logfile.write("==========================第"+page_num+"页采集结束================\n")      
        logfile.close()  


if __name__=='__main__':
    #Get the start time
    starttime = datetime.datetime.now()
    show_logo()
    key = raw_input('\033[1;33;40mplease input keyword:')
    key = key.encode('utf-8')
    key = urllib2.quote(key)

    page = int(raw_input("Search Number of pages:"))

    for i in range(page):
        page_pn = (i*baidu_page_size)
        baidu_search(key,page_pn)
    #Get the end time    
    endtime = datetime.datetime.now()
    runtime = (endtime - starttime).seconds

    print("\033[1;36;40m%d found | %d checked | %d filter | %d delete      The program runs in %s seconds\033[1;37;40m"%(all_totals,all_checked_totals,all_filter_totals,all_delete_totals,runtime))
