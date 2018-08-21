# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/superl-url.git
'''
    过滤模块
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
import re 
import sys

try:
    import tldextract
except ImportError:
    print("There is no tldextract module installed, please follow the instructions -> pip install tldextract")

from core.config import Config


class Filter(object):

    # filter_title_array = ['翻译', '词典']

    def __init__(self):
        self.config = Config()
        self.filterUrlParam = self.config.getValue("filter", "filter_urlparam")
        self.filterUrl = self.config.getValue("filter", "filter_url")
        self.filterTitle = self.config.getValue("filter", "filter_title")

        self.filterUrlList = self.get_filterurl()
        self.filterTitleList = self.get_filtertitle()


    # Filter the real URL
    def filter_data(self, url, title):
        try:
            #domain = get_tld(url)
            urldata = tldextract.extract(url)
            domain = '.'.join(urldata[1:3])
        except:
            print("解析URL:"+url+" 失败!")
            domain = url
            
        if self.filterUrl == 'True':
            if domain in self.filterUrlList:
                return 'filter'

        if self.filterTitle == 'True':
            for filter_titlestr in self.filterTitleList:
                if filter_titlestr in title:
                    return 'filter'
        
        if self.filterUrlParam == 'True':
            reg = r'^https?:\/\/([a-z0-9\-\.]+)[\/\?]?'
            m = re.match(reg, url)
            if m:
                uri = m.groups()[0]
                return uri[uri.rfind('//', 0, uri.rfind('.')) + 1:]
        else:
            return url


    def get_filterurl(self):
        file_object = open('config/filter_url.txt')
        try:
            file_context = file_object.read()
        finally:
            file_object.close()

        return file_context



    def get_filtertitle(self):
        file_object = open('config/filter_title.txt')
        try:
            if sys.version > '3':
                file_context = file_object.read()
            else:
                file_context = file_object.read().decode("utf-8")
        finally:
            file_object.close()

        return file_context