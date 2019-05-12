# -*- coding: utf-8 -*-

import logging
import time
import sys

if sys.version < '3':
    # python2
    try:
        import MySQLdb
    except ImportError:
        print("MySQLdb is not install!please run: pip install MySQLdb")
else:
    # python3
    try:
        import pymysql.cursors
    except ImportError:
        print("pymysql is not install!please run: pip install pymysql")



from core.config import Config



class MyDb(object):

    def __init__(self):
        self.config = Config()


    def getConnection(self):

        if sys.version < '3':
            try:
                conn = MySQLdb.connect(
                    host=self.config.datas['host'],
                    port=self.config.datas['port'],
                    user=self.config.datas['user'],
                    passwd=self.config.datas['password'],
                    db=self.config.datas['database'],
                    charset='utf8',
                )
                return conn
            except Exception as e:
                logging.error("Error:数据库连接错误！ 原因：%s"%e)
                return False

        else:
            try:
                conn = pymysql.connect(
                               host=self.config.datas['host'],
                               port=self.config.datas['port'],
                               user=self.config.datas['user'],
                               passwd=self.config.datas['password'],
                               db=self.config.datas['database'],
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor
                            )
                return conn
            except Exception as e:
                logging.error("Error:数据库连接错误！ 原因：%s"%e)
                return False


    def insert(self, sql):
        try:
            conn = self.getConnection()

            cursor = conn.cursor()
            cursor.execute(sql)
            lastid = int(cursor.lastrowid)

            #self.conn.commit()
            cursor.close()
            conn.close()

            return lastid

        except Exception as e:
            #self.conn.rollback()
            logging.error("Error:插入操作失败,语句：%s  原因：%s" % (sql, e))
            self.conn = self.getConnection()


    def insert_url(self, engine_name, keyword, baseurl, realurl, urlparam, title):
        table_name = self.config.datas['table']

        nowtime = int(time.time())
        insert_sql = "INSERT INTO "+table_name+"(engine,keyword,baseurl,realurl,urlparam,webtitle,create_time) VALUES('%s','%s','%s','%s','%s','%s','%s')" % (engine_name, keyword, baseurl, realurl, urlparam, title, nowtime)
        return self.insert(insert_sql)
