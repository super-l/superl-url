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
import sys
import re

from core.engine import Engine

try:
    import urllib2
except ImportError:
    import urllib.request

from utils.http import get_html_content


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
        #search_url = 'http://www.sogou.com/web?query=key&page='+str(page)
        search_url = 'https://www.sogou.com/websearch/sogou.jsp?query=key&page=' + str(page)+'&ie=utf8&_ast=1557664512&_asf=null&w=01029901&cid=&s_from=result_up'

        search_url = search_url.replace('key', keyword)

        htmlcontent = get_html_content(search_url, 'sougou')

        regex_page = r'<span>'+str(page)+'</span>'
        page_compile = re.compile(regex_page)
        page_result = page_compile.findall(htmlcontent)

        if not page_result:
            print("[SOUGOU]当前页码" + str(page) + "不存在！")
            return

        regex_url = r'<h3 class="pt">.*?href="(?P<url>.+?)".*?>(?P<title>.+?)</a>.*?</h3>'
        content = re.compile(regex_url, re.S)
        find_result = content.findall(htmlcontent)


        for i in range(len(find_result)):
            # 去除标题中的HTML标签
            dr = re.compile(r'<[^>]+>', re.S)

            # 标题
            title = dr.sub('', find_result[i][1])

            # 网址
            baseurl = str(find_result[i][0])

            # 搜索引擎链接转码后的真实网页地址 带url参数
            urlparam = self.get_realurl(baseurl)

            # 搜索引擎链接转码后的真实网页地址 去除url参数
            realurl = ''
            reg_url = r'(^https?:\/\/[a-z0-9\-\.]+)[\/\?]?'
            reg_m = re.match(reg_url, urlparam)
            if reg_m:
                realurl = reg_m.groups()[0]

            # 格式化输出并写入内容
            self.write_print(i, baseurl, realurl, urlparam, title)


