import MySQLdb



# class MysqlUtil(object):
#     # db = MySQLdb.connect("localhost", "root", "123456", "systest", charset='utf8')
#
#     def content(self, host, user, pwd, database):
#         self.db = MySQLdb.connect(host, user, pwd, database, charset='utf8')
#         cursor = self.db.cursor()
#         return cursor
#
#     def close(self):
#         self.db.close()
#
#     def select(self, cursor, sql):
#         try:
#             cursor.execute(sql)
#             results = cursor.fetchall()
#             return results[:]
#         except:
#             print("Error:unable to fecth data")
#         self.close()
#
#     def insert(self, cursor, sql):
#         try:
#             cursor.execute(sql)
#             # 提交到数据库执行
#             self.db.commit()
#         except:
#             # Rollback in case there is any error
#             self.db.rollback()
#             print("数据更新失败")
#         # 关闭数据库连接
#         self.close()
#
#     def delete(self, cursor, sql):
#         try:
#             # 执行SQL语句
#             cursor.execute(sql)
#             # 提交修改
#             self.db.commit()
#         except:
#             # 发生错误时回滚
#             self.db.rollback()
#             print("数据更新失败")
#         # 关闭连接
#         self.db.close()
import pymysql
from utils.LogUtil import my_log


class MysqlUtil:
    def __init__(self,host,user,password,database,charset="utf8",port=3306):
        self.log=my_log()
        try:
            self.conn=pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                charset=charset,
                port=port
            )
            self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        except:
            self.log.error(f"初始化数据库失败")
    def fetchone(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    def fetchall(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def exec(self,sql):
        """
        执行更新
        :return:
        """
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.log.error(f"Mysql 执行失败,{e}")
            return False
        return True
    def __del__(self):
        if not self.cursor:
            self.cursor.close()
        if not self.cursor:
            self.conn.close()

"""
sql="select name,password from systest.user_info where 0=0 and name='root';"
cursor.execute(sql)
ss=cursor.fetchone()
cursor.close()
conn.close()
print(ss)
"""

if __name__ == "__main__":
    sql = "select name,password from systest.user_info where 0=0 and name='root';"
    b = MysqlUtil("localhost", "root", "123456", "systest")
    data = b.fetchone( sql)
    print(type(data))
