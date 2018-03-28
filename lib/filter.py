# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/search-url.git
# Author  = superl
# Blog    = www.superl.org   QQ:86717375
# Team    = 忘忧草安全团队(Nepenthes Security Team)
import re 
import ConfigParser
from tld import get_tld

class SupFilter():

    filter_title_array = ['翻译','词典']

    filter_url_array1 = ['baidu.com','sina.com.cn','sohu.com','taobao.com','douban.com','163.com','tianya.cn','qq.com','1688.com','sogou.com','so.com','360.cn']
    filter_url_array2 = ['ganji.com','58.com','baixing.com','zhaopin.com']
    filter_url_array3 = ['zhihu.com','weibo.com','iqiyi.com','kugou.com','51.com','youku.com','soku.com','acfun.cn','verycd.com']
    filter_url_array4 = ['google.cn','youdao.com','iciba.com','cdict.net']
    filter_url_array5 = ['pconline.com.cn','zcool.com.cn','csdn.net','lofter.com']

    filter_url_all = filter_url_array1+filter_url_array2+filter_url_array3+filter_url_array4+filter_url_array5

    filter_urlparam = True
    filter_url  = True
    filter_title = False


    def __init__(self) :
        cfg = ConfigParser.ConfigParser()
        cfg.read("config/setting.conf")

        self.filter_urlparam = cfg.get("filter", "filter_urlparam")
        self.filter_url = cfg.get("filter", "filter_url")
        self.filter_title = cfg.get("filter", "filter_title")

    #Filter the real URL
    def filter_data(self, target_url, title):
        try:
            domain = get_tld(target_url)
        except Exception as e:
            domain = target_url
            
        if self.filter_url == 'True':
            if domain in self.filter_url_all:
                return 'filter'

        if self.filter_title == 'True':
            for filter_titlestr in self.filter_title_array:
                if filter_titlestr in title:
                    return 'filter'
        
        if self.filter_urlparam == 'True':
            reg = r'^https?:\/\/([a-z0-9\-\.]+)[\/\?]?'
            m = re.match(reg, target_url)
            if m :
                uri = m.groups()[0]
                return uri[uri.rfind('//', 0, uri.rfind('.')) + 1:]
            else:
                return target_url
        else:
            return target_url
           