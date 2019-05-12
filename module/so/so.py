# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/superl-url.git
'''
    360搜索采集功能模块
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


class So(Engine):

    def __init__(self, outfile=None):
        search_name = '[360搜索]'
        Engine.__init__(self, search_name, outfile)


    def search(self, keyword, page):

        search_url = 'https://www.so.com/s?q=key&pn='+str(page)
        search_url = search_url.replace('key', keyword)

        # print(search_url)
        htmlcontent = get_html_content(search_url, 'so')

        regex_page = r'<strong>'+str(page)+'</strong>'
        page_compile = re.compile(regex_page)
        page_result = page_compile.findall(htmlcontent)

        if not page_result:
            print("[360-SO]当前页码" + str(page) + "不存在！")
            return

        regex_url = '<h3 class="res-title.*?<a href="(?P<url>.*?)".?(?:data-url="(?P<dataurl>.*?)")?.*?>(?P<title>.+?)</a>.*?</h3>'

        content = re.compile(regex_url, re.S)
        find_result = content.findall(htmlcontent)

        for i in range(len(find_result)):
            # 去除标题中的HTML标签
            dr = re.compile(r'<[^>]+>', re.S)

            # 网页的标题
            title = dr.sub('', find_result[i][2])

            # 搜搜链接的网页地址
            if str(find_result[i][0])[0:17] == 'http://www.so.com':
                baseurl = str(find_result[i][1])
            else:
                baseurl = str(find_result[i][0])

            # 获取真实URL地址 带参数
            urlparam = baseurl

            # 搜索引擎链接转码后的真实网页地址 去除url参数
            realurl = ''
            reg_url = r'(^https?:\/\/[a-z0-9\-\.]+)[\/\?]?'
            reg_m = re.match(reg_url, urlparam)
            if reg_m:
                realurl = reg_m.groups()[0]

            # 格式化输出并写入内容
            self.write_print(i, baseurl, realurl, urlparam, title)
