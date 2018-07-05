# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/superl-url.git
'''
    Save the url into the file
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

class OutFile(object):

    def __init__(self, filename):
        filepath = 'result/' + filename + '.txt'
        self.handle = open(filepath, 'a')

    @staticmethod
    def getFilePath(keyword):
        return 'result/' + keyword + '.txt'


    def writeToFile(self, content):
        self.handle.write(content+'\n')


    def closeFile(self):
        self.handle.close()


    def writeToMysql(self):
        pass