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
import re

from core.engine import Engine

try:
    import urllib2
except ImportError:
    import urllib.request

from utils.http import get_html_content


class Baidu(Engine):

    def __init__(self, outfile=None):
        search_name = '[baidu]'
        Engine.__init__(self, search_name, outfile)


    # 获取百度搜索引擎结果页面的网页真实URL地址，而不是百度自己的链接地址
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

    # 搜索并采集处理内容
    def search(self, keyword, pagesize, page_pn):
        page_num = int(page_pn/pagesize + 1)

        search_url = 'http://www.baidu.com/s?wd=key&rn='+str(pagesize)+'&pn='+str(page_pn)
        search_url = search_url.replace('key', keyword)

        htmlcontent = get_html_content(search_url, 'baidu')
        # print(type(htmlcontent))

        regex_page = r'<span class="pc">'+str(page_num)+'</span>'
        page_compile = re.compile(regex_page)
        page_result = page_compile.findall(htmlcontent)

        # 判断是否存在当前页
        if not page_result:
            print("[baidu]当前页码"+str(page_num)+"不存在！")
            return

        regex_titleurl = r'<div class="result c-container ".*<h3 class=".*"><a(?:[^\<]*\n[^\<]*)href = "(?P<url>.+?)"(?:[^\<]*\n[^\<]*)target="_blank"(?:[^\<]*\n[^\<]*)>(?P<title>.+?)</a></h3>'

        content = re.compile(regex_titleurl)
        find_result = content.findall(htmlcontent)

        for i in range(len(find_result)):
            dr = re.compile(r'<[^>]+>', re.S)

            # 百度链接的网页地址
            baseurl = find_result[i][0]

            # 网页的标题
            title = dr.sub('', find_result[i][1])

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
