# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/search-url.git
# Author  = superl
# Blog    = www.superl.org   QQ:86717375
# Team    = Code Security Team(C.S.T) | 铭剑创鼎
import urllib2
import requests
import re
import ConfigParser
import httplib

class SupGetData():


    def __init__(self) :
        cfg = ConfigParser.ConfigParser()
        cfg.read("config/setting.conf")
        self.sougou_page_size = cfg.get("search", "sougou_page_size")

        #httplib.HTTPConnection._http_vsn = 10  
        #httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

    #Get the web page source code
    def get_pagehtml(self,target_url,header_type):
        try:
            if header_type=='sougou':
                send_headers = {
                 'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
                 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                 'Connection':'keep-alive',
                 'Cookie':'com_sohu_websearch_ITEM_PER_PAGE='+str(self.sougou_page_size)
                }
            else:
                send_headers = {
                 'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
                 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                 'Connection':'keep-alive'
                }

            req = urllib2.Request(target_url,headers=send_headers)
            get_request = urllib2.urlopen(req,timeout = 30)
            #print get_request.info()
            result_htmlcontent = get_request.read()
            return result_htmlcontent;
        except urllib2.HTTPError, e:
            print e.code

    #获取百度搜索结果真实地址
    def get_baidu_realurl(self,target_url):
        try:
            response = urllib2.urlopen(target_url,timeout = 3)
            realurl = response.geturl()
            return realurl
        except Exception, e:
            return target_url


    #获取搜狗搜索结果真实地址
    def get_sougou_realurl(self,target_url):
        try:
            result_htmlcontent = requests.get(target_url, allow_redirects=False)
            realurl = re.search(r'[a-zA-z]+://[^\s]*(?=\')',result_htmlcontent.text)
            return realurl.group()
        except Exception, e:
            return target_url


    #获取360搜索结果真实地址
    def get_so_realurl(self,target_url):
        try:
            result_htmlcontent = requests.get(target_url, allow_redirects=False)
            realurl = re.search(r'[a-zA-z]+://[^\s]*(?=\')',result_htmlcontent.text)
            return realurl.group()
        except Exception, e:
            return target_url

