# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/superl-url.git
'''
    保存搜索的结果
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

from core.config import Config
from utils.dbutil import MyDb

class OutData(object):

    def __init__(self, keyword):
        self.keyword = keyword
        self.config = Config()
        self.save_type = self.config.datas['save_type']

        self.writeTitle = self.config.datas['write_title']
        self.writeEngineName = self.config.datas['write_name']

        # 写入的url类型 baseurl = 默认搜索引擎的链接地址 realurl=真实网页地址 urlparam = 真实网页地址带url参数
        self.url_type = self.config.datas['url_type']


    # 写入内容
    def write(self, baseurl, realurl, urlparam, title, engine_name):

        # 如果保存类型为文件
        if self.save_type == 'file':
            if self.url_type == 'baseurl':
                url = baseurl
            elif self.url_type == 'realurl':
                url = realurl
            elif self.url_type == 'urlparam':
                url = urlparam
            else:
                url = realurl


            # 是否写入标题
            if self.writeTitle == 'True':

                # 是否写入搜索引擎名称
                if self.writeEngineName == 'True':
                    content = url + '    ' + title + '    ' + engine_name
                else:
                    content = url + '    ' + title

            else:
                # 每条记录是否显示搜索引擎的名称
                if self.writeEngineName == 'True':
                    content = url + '    ' + engine_name
                else:
                    content = url

            self.writeToFile(content)

        # 如果保存类型为Mysql
        elif self.save_type == 'mysql':
            self.writeToMysql(baseurl, realurl, urlparam, title, engine_name)

        else:
            print('保存结果类型错误！')



    # 写入到文件
    def writeToFile(self, content):
        save_pathdir = self.config.datas['save_pathdir']
        filepath = save_pathdir + '/' + self.keyword + '.txt'
        file_handle = open(filepath, 'a')
        file_handle.write(content+'\n')
        file_handle.close()


    # 写入到mysql
    def writeToMysql(self, baseurl, realurl, urlparam, title, engine_name):
        mydb = MyDb()
        result = mydb.insert_url(engine_name, self.keyword, baseurl, realurl, urlparam, title)
        if result >= 1:
            #print("写入数据库成功！")
            pass
        else:
            print("写入数据库失败！")



