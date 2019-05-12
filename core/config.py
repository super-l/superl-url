#coding:utf-8
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

# python2和python3的ConfigParser大小写不同

try:
    # python2
    from configparser import ConfigParser

    configHeader = ConfigParser()

except ImportError:

    # python3
    import configparser

    configHeader = configparser.ConfigParser()


class Config():

    datas = dict()
    engine = dict()

    def __init__(self):
        configHeader.read("config.cfg")

        # 得到所有的配置节点
        sections = configHeader.sections()

        for i in sections:
            section = i

            keys = configHeader.options(section)

            for key in keys:
                if key != 'port':
                    value = configHeader.get(section, key)
                else:
                    value = configHeader.getint(section, key)

                #print("key:%s value:%s"%(key,value))

                self.datas[key] = value

                if(section == 'engine'):
                    if value == 'True':
                        self.engine[key] = value


    # 根据节点类型以及名称，获取配置的值
    def getValue(self, type, name):
        return configHeader.get(type, name)

