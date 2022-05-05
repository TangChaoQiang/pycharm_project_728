import time
import pymysql
import json

# # django方式路由开发--新建列表
# route_list = [
#     ("/index.html", Index),
#     ("/center.html", Center)
# ]

# flask方式的路由开发--装饰器
route_list = []
def tag(filename):
    def outer(fn):
        def inner(*args, **kwargs):
            return fn(*args, **kwargs)
        route_list.append((filename, fn))
        return inner
    return outer

# 数据库
def conndb(sql):
    # 建立连接
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        database="stock",
        charset="utf8",
        user="root",
        password="Tcq980422"
    )
    # 创建游标
    cur = conn.cursor()
    # 执行语句
    cur.execute(sql)
    cur.close()
    conn.close()
    return cur.fetchall()


@tag("/index.html")
def Index():
    # 处理首页的请求
    # 1、读取模板的首页页面
    with open("template/index.html", "r", encoding="utf-8") as file:
        data = file.read()
    # 2、获得数据库中的数据
    sql = "select * from info"
    get_data = conndb(sql)
    # 3、整合数据
    web_data = ''
    for i in get_data:
        web_data += """
        <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td><input type="button" value="添加" id="toAdd" systemidvalue="000007"></td>
    </tr>
        """ % i
    data = data.replace("{%content%}", web_data)
    # 4、将处理的结构返回
    # 响应行
    response_line = "200 OK"
    # 响应头
    response_header = "tang/1.0"
    return response_line, response_header, data.encode()

@tag("/center_data.html")
def Center_data():
    # 2、获得数据库中的数据
    sql = "select code, short, chg, turnover, price, highs, note_info from info inner join focus as f on info.id = f.info_id;"
    # 获得元组类型数据， 调用数据库连接返回数据
    get_data = conndb(sql)
    # 定义空列表
    data_list = []
    # 将元组里面的数据组合为字典，追加到列表中
    for i in get_data:
        data_dict = dict()
        data_dict["code"] = i[0]
        data_dict["short"] = str(i[1])
        data_dict["chg"] = str(i[2])
        data_dict["turnover"] = str(i[3])
        data_dict["price"] = str(i[4])
        data_dict["highs"] = str(i[5])
        data_dict["note_info"] = str(i[6])
        data_list.append(data_dict)
    # 利用json转换为python数据格式
    data_json = json.dumps(data_list, ensure_ascii=False)
    # 响应行
    response_line = "200 OK"
    # 响应头
    response_header = "tang/1.0"
    return response_line, response_header, data_json.encode("utf8")


@tag("/center.html")
def Center():
    # 处理个人中心的请求
    # 1、读取模板的首页页面
    with open("template/center.html", "r", encoding="utf-8") as file:
        data = file.read()
    # 2、获得数据库中的数据
    # 3、整合数据
    # data = data.replace("{%content%}", time.ctime())
    # 4、将处理的结构返回
    # 响应行
    response_line = "200 OK"
    # 响应头
    response_header = "tang/1.0"
    return response_line, response_header, data.encode()

def Error():
    # 1、读取模板的首页页面
    with open("static/error.html", "r", encoding="utf-8") as file:
        data = file.read()
    response_line = "404 NOT FOUND"
    response_header = "tang/1.0"
    return response_line, response_header, data.encode()

def handle_client(env):
    # 需要处理的资源
    file_name = env["filename"]
    print(file_name)
    for route in route_list:
        if route[0] == file_name:
            func = route[1]
            return func()
    return Error()

# if __name__ == '__main__':
#     Center_data()