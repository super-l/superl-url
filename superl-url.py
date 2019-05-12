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

try:
    # python2
    from urllib2 import quote

except ImportError:
    # python3
    from urllib.parse import quote

if sys.version < '3':
    try:
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
    except:
        pass

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
     {Author:superl(Nepenthes security team)                   Version 4.0            
"""
    print(logostr)

if __name__=='__main__':

    # Record the start time
    startTime = datetime.datetime.now()

    show_logo()

    # read config
    config = Config()

    # Set global variables and initialize
    gol._init()
    gol.set_value('process', [])


    # Sets the keyword and number of pages
    if sys.version > '3':
        keyword = input('\033[1;33;40mplease input keyword:')
        page = int(input("Search Number of pages:"))
    else:
        keyword = raw_input('\033[1;33;40mplease input keyword:')
        page = input("Search Number of pages:")


    # Perform the collection task concurrently
    for engine in(config.engine):
        task = Task(engine, page, quote(keyword))


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


