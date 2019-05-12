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
try:
    import tldextract
except ImportError:
    print("There is no tldextract module installed, please follow the instructions -> pip install tldextract")

from core.config import Config


class Filter(object):

    # filter_title_array = ['翻译', '词典']

    def __init__(self):

        self.config = Config()

        self.filter_status = self.config.datas['filter_status']
        self.filter_domain = self.config.datas['filter_domain']
        self.filter_title = self.config.datas['filter_title']

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

        if self.filter_status == 'True':
            if self.filter_domain == 'True':
                if domain in self.filterUrlList:
                    print("URL:" + url + " 被过滤!")
                    return False

            if self.filter_title == 'True':
                for filter_titlestr in self.filterTitleList:
                    if filter_titlestr in title:
                        print("URL:" + url + " 被过滤!")
                        return False

        return True


    # 获取域名黑名单列表
    def get_filterurl(self):
        file_object = open('filter/filter_domain.txt')
        try:
            file_context = file_object.read().encode('utf-8').decode('utf-8')
        finally:
            file_object.close()

        return file_context


    # 获取标题文字黑名单列表
    def get_filtertitle(self):
        file_object = open('filter/filter_title.txt')
        try:
            file_context = file_object.read().encode('utf-8').decode('utf-8')
        finally:
            file_object.close()

        return file_context