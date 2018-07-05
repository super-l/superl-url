# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/superl-url.git
'''
    superl-url
    Created by superl.                Nepenthes Security Team(忘忧草安全团队)
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
from __future__ import print_function

import datetime
import sys

if sys.version < '3':
    reload(sys)
    sys.setdefaultencoding('utf8')
    from urllib2 import quote
elif sys.version_info < (3, 3):
    import imp
    imp.reload(sys)
    from urllib.parse import quote
else:
    import importlib
    importlib.reload(sys)
    from urllib.parse import quote

from core import gol
from core.config import Config
from core.task import Task


def show_logo():
    logostr = """\033[1;32;40m \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
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
                                00000                 blog:www.superl.org       
                                00000                                           
     {Author:superl(Nepenthes security team)                   Version 3.0            
"""
    print(logostr)

if __name__=='__main__':

    # Record the start time
    startTime = datetime.datetime.now()

    show_logo()

    # Set global variables and initialize
    gol._init()
    gol.set_value('process', [])


    # Sets the keyword and number of pages
    if sys.version > '3':
        keyword = input('\033[1;33;40mplease input keyword:')
        page = int(input("Search Number of pages:"))
    else:
        keyword = raw_input('\033[1;33;40mplease input keyword:')
        page = int(raw_input("Search Number of pages:"))

    config = Config()

    searchEngine = []

    if config.baidu_search == 'True':
        searchEngine.append("baidu")

    if config.sougou_search == 'True':
        searchEngine.append("sougou")

    if config.so_search == 'True':
        searchEngine.append("so")

    # Perform the collection task concurrently
    for i in range(len(searchEngine)):
        task = Task(searchEngine[i], page, quote(keyword))

    # Wait for all child processes to complete
    processList = gol.get_value("process")
    for i in range(len(processList)):
        processList[i].join()

    # Displays the computational execution time
    endTime = datetime.datetime.now()
    runTime = (endTime - startTime).seconds

    print("\033[1;33;40[*]The url collection task is complete! runs in %s seconds" % runTime)

    '''
    # 过滤无用的域名
    filter_status = config.getValue("filter", "filter_status")
    if filter_status == 'True':

        print("\033[1;33;40[*]Start Filtering useless url...")

        filePath = OutFile.getFilePath(keyword)

    #print("\033[1;33;40[*]Start exporting content to Mysql...")
    '''


