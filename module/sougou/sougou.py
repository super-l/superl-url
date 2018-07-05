# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/superl-url.git
'''
    搜狗采集功能模块
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
from module.engine import Engine
import sys
try:
    import urllib2
except ImportError:
    import urllib.request

from core.filter import *
from utils.http import getHtmlContent


class Sougou(Engine):

    def __init__(self, outfile=None):
        search_name = '[搜狗]'
        Engine.__init__(self, search_name, outfile)


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



    def search(self, keyword, page):
        search_url = 'http://www.sogou.com/web?query=key&page='+str(page)
        search_url = search_url.replace('key', keyword)

        htmlcontent = getHtmlContent(search_url, 'sougou')

        regex_page = r'<span>'+str(page)+'</span>'
        page_compile = re.compile(regex_page)
        page_result = page_compile.findall(htmlcontent)

        if not page_result:
            print("当前页码" + str(page) + "不存在！")
            return

        regex_url = r'<h3 class="pt">.*?href="(?P<url>.+?)".*?>(?P<title>.+?)</a>.*?</h3>'

        content = re.compile(regex_url, re.S)

        find_result = content.findall(htmlcontent)

        for i in range(len(find_result)):
            # 去除标题中的HTML标签
            dr = re.compile(r'<[^>]+>', re.S)
            title = dr.sub('', find_result[i][1])

            url = str(find_result[i][0])
            print(url)
            realurl = self.get_realurl(url)

            filter_status = self.config.getValue("filter", "filter_status")
            if filter_status == 'True':
                realurl = self.filter.filter_data(realurl, title)

                if realurl == "filter":
                    continue

            print ("[ID]:%d  [URL]:%s  [TITLE]:%s  [Engine]:%s" % (i, realurl, title, self.searchName))

            if self.writeTitle == 'True':
                if self.writeEngineName == 'True':
                    urltext = realurl + '    ' + title + '    ' + self.searchName
                else:
                    urltext = realurl + '    ' + title
            else:
                if self.writeEngineName == 'True':
                    urltext = realurl + '    ' + self.searchName
                else:
                    urltext = realurl

            if realurl not in self.tempUrlList:
                self.tempUrlList.append(realurl)
                self.tempUrlTextList.append(urltext)

        if self.outfile:
            self.writefile()
