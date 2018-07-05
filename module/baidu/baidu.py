# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/superl-url.git
'''
    百度采集功能模块
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
import sys

from module.engine import Engine

try:
    import urllib2
except ImportError:
    import urllib.request

from core.filter import *
from utils.http import getHtmlContent


class Baidu(Engine):

    def __init__(self, outfile=None):
        search_name = '[baidu]'
        Engine.__init__(self, search_name, outfile)


    '''
    Get the real URL of baidu search results
    '''
    def get_realurl(self, target_url):
        try:
            if sys.version > '3':
                response = urllib.request.urlopen(target_url, timeout=3)
                realurl = response.geturl()
                return realurl
            else:
                response = urllib2.urlopen(target_url, timeout=3)
                realurl = response.geturl()
                return realurl
        except:
            return target_url

    def search(self, keyword, pagesize, page_pn):
        page_num = int(page_pn/pagesize + 1)

        search_url = 'http://www.baidu.com/s?wd=key&rn='+str(pagesize)+'&pn='+str(page_pn)
        search_url = search_url.replace('key', keyword)

        htmlcontent = getHtmlContent(search_url, 'baidu')

        regex_page = r'<span class="pc">'+str(page_num)+'</span>'
        page_compile = re.compile(regex_page)
        page_result = page_compile.findall(htmlcontent)

        # 判断是否存在当前页
        if not page_result:
            print("当前页码"+str(page_num)+"不存在！")
            return

        regex_titleurl = r'<div class="result c-container ".*<h3 class=".*"><a(?:[^\<]*\n[^\<]*)href = "(?P<url>.+?)"(?:[^\<]*\n[^\<]*)target="_blank"(?:[^\<]*\n[^\<]*)>(?P<title>.+?)</a></h3>'

        content = re.compile(regex_titleurl)
        find_result = content.findall(htmlcontent)

        for i in range(len(find_result)):
            dr = re.compile(r'<[^>]+>', re.S)
            title = dr.sub('', find_result[i][1])

            realurl = self.get_realurl(find_result[i][0])


            # [old code] If you start the filter module, do so...
            filter_status = self.config.getValue("filter", "filter_status")
            if filter_status == 'True':
                realurl = self.filter.filter_data(realurl, title)

            if realurl == "filter":
                continue

            print ("[ID]:%d  [URL]:%s  [TITLE]:%s  [Engine]:%s" % (i, realurl, title, self.searchName))

            if self.writeTitle == 'True':
                if self.writeEngineName == 'True':
                    urltext = realurl+'    '+title+'    '+self.searchName
                else:
                    urltext = realurl+'    '+title
            else:
                if self.writeEngineName == 'True':
                    urltext = realurl+'    '+self.searchName
                else:
                    urltext = realurl

            if realurl not in self.tempUrlList:
                self.tempUrlList.append(realurl)
                self.tempUrlTextList.append(urltext)

        if self.outfile:
            self.writefile()
