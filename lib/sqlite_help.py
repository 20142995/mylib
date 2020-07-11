#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sqlite3

from .logs_help import Logger

logger = Logger("debug",name=os.path.split(os.path.splitext(os.path.abspath(__file__))[0])[-1])

class sqliteDB():
    
    def __init__(self,dbnmae,create_table_sql=None):
        """
        初始化函数，创建数据库连接
        :param dbnmae: 传入数据库名称或数据库文件路径，eg: test.db
        :param create_table_sql: 传入的创建表SQL语句,eg:CREATE TABLE tablename (name TEXT NOT NULL);
        """
        self.conn = sqlite3.connect(dbnmae,check_same_thread = False)
        self.cursor = self.conn.cursor()
        if create_table_sql:
            self.set(create_table_sql)

    def set(self,sql,data=[],many=False):
        """
        数据库的插入、修改、删除函数
        :param sql: 传入的SQL语句 eg:INSERT INTO tablename (name) VALUES (?) / DELETE from tablename where name=? / UPDATE tablename set name = ? where name=?
        :param data: 传入对应数据，many=False:[a,b,c,d] many=True:[[a,b,c,d],[a,b,c,d],[a,b,c,d]]
        :param many: 传入批量数据，many=False
        :return: 返回操作数据库状态 eg: True or False
        """
        try:
            if many:
                self.cursor.executemany(sql,data)
            else:
                self.cursor.execute(sql,data)
            i = self.conn.total_changes
            logger.debug(f'数据操作成功,sql:{sql},改变数：{i}')
        except Exception:
            logger.error(f'数据操作失败,sql:{sql}', exc_info=True)
            return False
        finally:
            self.conn.commit()
        if i > 0:
            return True
        else:
            return False

    def get(self,sql,data=[]): 
        """
        数据库的查询函数
        :param sql: 传入的SQL语句,eg:select * from tablename where name=?
        :param data: 传入查询参数,eg: [name,]
        :return : 返回查询结果 eg: [(a,b,)]
        """
        results = self.cursor.execute(sql,data)
        logger.debug(f'数据查询,sql:{sql},结果数：{len(results)}')
        return results.fetchall()
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def __del__(self):
        self.close()



