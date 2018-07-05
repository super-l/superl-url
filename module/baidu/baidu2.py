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

try:
    import urllib2
except ImportError:
    import urllib.request

from core.filter import *
from utils.http import getHtmlContent


class Baidu():

    search_name = '[baidu]'

    def __init__(self):
        self.config = Config()

        self.write_webtitle = self.config.getValue("log", "write_title")
        self.write_enginename = self.config.getValue("log", "write_name")

        self.filter = Filter()


    '''
    Get the real URL of baidu search results
    '''
    def getRealUrl(self, target_url):
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


    def search(self, keyword, pagesize, page_pn, outfile = None):

        page_num = str(page_pn/pagesize + 1)

        search_url = 'http://www.baidu.com/s?wd=key&rn='+str(pagesize)+'&pn='+str(page_pn)
        search_url = search_url.replace('key', keyword)

        htmlcontent = getHtmlContent(search_url, 'baidu')
        print(htmlcontent)

        regex_page = r'<span class="pc">'+page_num+'</span>'
        page_compile = re.compile(regex_page)
        page_result = page_compile.findall(htmlcontent)

        if not page_result:
            return

        regex_titleurl = r'<div class="result c-container ".*<h3 class=".*"><a(?:[^\<]*\n[^\<]*)href = "(?P<url>.+?)"(?:[^\<]*\n[^\<]*)target="_blank"(?:[^\<]*\n[^\<]*)>(?P<title>.+?)</a></h3>'

        content = re.compile(regex_titleurl)
        find_result = content.findall(htmlcontent)

        for i in range(len(find_result)):
            dr = re.compile(r'<[^>]+>', re.S)
            title = dr.sub('', find_result[i][1])

            realurl = self.getRealUrl(find_result[i][0])

            # If you start the filter module, do so...
            filter_status = bool(self.config.getValue("filter", "filter_status"))
            if filter_status:
                realurl = self.filter.filter_data(realurl, title)


            if realurl != "filter":
                print ("[ID]:%d  [URL]:%s  [TITLE]:%s" % (i, realurl, title))
                if outfile:
                    have_url = False
                    with open(keyword + '.txt', 'r') as foo:
                        for line in foo.readlines():
                            if realurl in line:
                                have_url = True

                        if not have_url:
                            if self.write_webtitle:
                                if self.write_enginename:
                                    outfile.writeToFile(self.search_name + realurl+'    '+title+'\n')
                                else:
                                    outfile.writeToFile(realurl+'    '+title+'\n')
                            else:
                                if self.write_enginename:
                                    outfile.writeToFile(self.search_name + realurl+'\n')
                                else:
                                    outfile.writeToFile(realurl+'\n')
