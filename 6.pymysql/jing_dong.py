from handle_pymysql import handle_mysql


class handle_jingdong(object):
    def __init__(self):
        self.mysql = handle_mysql()
    def select_all_info(self):
        # print("1．查询所有商品信息")
        sql = "SELECT * from goods"
        response = self.mysql.fetchall(sql)
        print(response)

    def select_group_goods(self):
        # print("2．查询所有包含商品的分类")
        sql = "SELECT name from good_cates where id in (SELECT cate_id from goods)"
        response = self.mysql.fetchall(sql)
        print(response)

    def add_new_cate(self):
        # print("3．添加新商品分类")
        name = input("请输入新分类的名字:")
        sql = f"insert into good_cates (name) values ({repr(name)})"
        response = self.mysql.handle(sql)
        print(response)

    def updata_price(self):
        # print("4、将所有商品价格加1000")
        method1 = input("请输入操作方法：")
        num = int(input("请输入操作数"))
        sql = f"UPDATE goods set price=price{method1}{num}"
        response = self.mysql.handle(sql)
        print(response)

    def updata_name(self):
        # print("5．将所有笔记本的分类改为超级本")
        sql = "UPDATE goods set cate_id = 7 where name like '%笔记本%'"
        response = self.mysql.handle(sql)
        print(response)

    def select_id_info(self):
        # print("6．根据id查询商品信息")

        num = input("请输入id:")
        sql = f"SELECT * from goods WHERE id = {num}"
        response = self.mysql.fetchall(sql)
        print(response)

    def select_id_notsql_info(self):
        # print("7．根据id查询商品信息安全方式")
        num = input("请输入id:")
        print(repr(num), type(num))
        sql = "SELECT * from goods WHERE id = %s"
        response = self.mysql.fetchall(sql, (num,))
        print(response)

    def exit(self):
        # print("8．退出系统")
        self.mysql.close()

if __name__ == '__main__':
    jingdong = handle_jingdong()
    jingdong.select_id_notsql_info()
