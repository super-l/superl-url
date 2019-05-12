# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/superl-url.git
'''
    程序基础功能模块
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

from core.config import Config

# 获取网页内容
def get_html_content(target_url, header_type):

    config = Config()

    try:
        # 如果是搜狗，需要通道自定义请求头来实现页码参数的设置
        if header_type == 'sougou':
            send_headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Connection': 'keep-alive',
                'Referer': 'https://www.sogou.com/websearch/sogou.jsp?query=superl&page=1',
                'Cookie': 'com_sohu_websearch_ITEM_PER_PAGE='+str(config.datas['sougou_pagesize'])
            }
        else:
            send_headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Connection': 'keep-alive'
            }

        if sys.version > '3':
            req = urllib.request.Request(target_url, headers=send_headers)
            response = urllib.request.urlopen(req, timeout=10)
        else:
            req = urllib2.Request(target_url, headers=send_headers)
            response = urllib2.urlopen(req, timeout=30)
            # print get_request.info()

        return response.read().decode('utf-8')

    except Exception as e:
        print("Get html page content error:%s"%(e))