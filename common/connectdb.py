import pymysql
from common.handleconfig import conf

class DB:
    def __init__(self):
        #创建一个连接对象
        self.conn = pymysql.connect(host=conf.get("db","host"),
                                    port=conf.getint("db","port"),
                                    user=conf.get("db","user"),
                                    password=conf.get("db","pwd"),
                                    charset=conf.get("db","charset"),
                                    #通过设置游标类型，可以控制查询出来的数据类型
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
        self.cur = self.conn.cursor()

    def find_one(self,sql):
        '''获取查询出来的第一条数据'''
        #提交事务
        self.conn.commit()
        #执行查询语句
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def find_all(self,sql):
        '''获取查询出来的所有数据'''
        #提交事务
        self.conn.commit()
        #执行查询语句
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def find_count(self,sql):
        '''查询返回数据的条数'''
        self.conn.commit()
        return self.cur.execute(sql)


    def close(self):
        '''关闭游标，断开连接'''
        self.cur.close()
        self.conn.close()



if __name__ == '__main__':

    conn = pymysql.connect(host="127.0.0.1",
                           port=3306,
                           user="root",
                           password="root",
                           cursorclass=pymysql.cursors.DictCursor,
                           charset="utf8")

    #第二步  创建一个游标对象
    cur = conn.cursor()

    sql2 = "SELECT f_pwd FROM recruit_students.t_login_account WHERE f_laccount = 'admin'"
    res = cur.execute(sql2)
    #返回的是查询到的数据条数
    print(res)
    data = cur.fetchone()
    print(data)