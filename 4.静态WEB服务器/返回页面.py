import socket
import gevent
from gevent import monkey
import threading
# 创建锁
mutex = threading.Lock()
monkey.patch_all()

# 6、返回数据
def handle_client_index(new_socket, ip_port):
    # 加锁
    mutex.acquire()
    buff = new_socket.recv(4096).decode()
    if buff:
        # 获得请求什么资源
        print(buff)
        get_url = buff.split(" ", 2)[1]
        # print(get_url)
        # 判断没有路径或者只有“/”，使用默认页面
        if get_url == "/":
            get_url = r"/index.html"
        response_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "NAME：tang\r\nServer:tang2\r\n"
        try:
            # 找到资源
            f = open(r"static" + get_url, "rb")
            data = f.read()
            f.close()
        except FileNotFoundError:
            # 文件不存在
            f = open(r"static/error.html", "rb")
            data = f.read()
            f.close()
        response = (response_line + response_headers + "\r\n").encode() + data
        new_socket.send(response)
        # 输出完释放锁
        mutex.release()
        new_socket.close()
    else:
        print(f"客户端{ip_port}下线了")
        new_socket.close()
        # 关闭也释放锁
        mutex.release()


if __name__ == '__main__':
    # 1、创建socket对象
    se_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、端口复用
    se_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 3、绑定ip
    se_socket.bind(("", 8989))
    # 4、监听
    se_socket.listen(128)
    print("等待连接---------")
    # 5、阻塞等待
    while True:
        new_socket, ip_port = se_socket.accept()
        print(f"客户端{ip_port}连接了")
        new_gevent = gevent.spawn(handle_client_index, new_socket, ip_port)
        new_gevent.join()
