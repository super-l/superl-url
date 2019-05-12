# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/superl-url.git

'''
    创建任务 根据搜索引擎的不同 多进程并发搜索
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

import multiprocessing
from core import gol
from core.collect import Collect
from core.config import Config


class Task(object):

    def __init__(self, module, page, keyword):
        config = Config()
        pagesize = config.getValue("pagesize", module+"_pagesize")

        print("\033[1;37;40m[*]Search Engine [%s] starting！The number of display bars per page is %s" % (module, pagesize))

        myps = multiprocessing.Process(target=Collect, args=(module, page, pagesize, keyword,))
        myps.start()

        processList = gol.get_value("process")
        processList.append(myps)
        gol.set_value("process", processList)



