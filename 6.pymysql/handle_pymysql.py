import pymysql


class handle_mysql(object):

    def __init__(self):
        self.conn = pymysql.connect(
            host="192.168.247.1",
            port=3306,
            database="jing_dong",
            user="root",
            password="Tcq980422",
            charset="utf8"
        )

        self.cur = self.conn.cursor()

    def fetchall(self, sql, *args):
        self.cur.execute(sql, args)
        return self.cur.fetchall()

    def handle(self, sql):
        try:
            res = self.cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            return res

    def close(self):
        self.cur.close()
        self.conn.close()
