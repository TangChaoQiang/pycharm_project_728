import socket
import threading
import multiprocessing
import gevent
import os
import time

"""
def handle_client_request(new_socket, ip_port):
    while True:
        # 5．阻塞等待新的socket 收信息
        buff = new_socket.recv(4096)
        if buff:
            print(buff.decode())
            # 6．新的socket发信息
            new_socket.send("收到".encode())
        else:
            print("客户端{}已下线".format(ip_port))
            break
        # 7．关闭
    new_socket.close()


if __name__ == '__main__':
    # 1．创建socket对象
    se_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    # level设置哪个级别的socket,socket.soL_SOCKET当前的 socket
    # optname设置什么内容(权限)socket.sSo_REUSEADDR端口复用
    # value设置为什么值,True
    se_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 2．绑定IP和端口,元组类型
    se_socket.bind(("", 9000))
    # 3．设置监听，数字表示同时连接的数量，成功后不占用名额
    se_socket.listen(128)
    # 4．阻塞等待客户端的链接，拆包获得新的socket和连接的ip
    print("等待连接中——————")
    while True:
        new_socket, ip_port = se_socket.accept()
        print("客户端{}连接".format(ip_port))
        # 进程实现
        # socket_Process = multiprocessing.Process(target=handle_client_request(new_socket, ip_port))
        # socket_Process.start()

        # 线程实现
        # socket_threading = threading.Thread(target=handle_client_request(new_socket, ip_port))
        # socket_threading.start()
        #
        # 协程实现
        socket_gevent = gevent.spawn(handle_client_request, new_socket, ip_port)
        socket_gevent.join()

"""


def handle_cl_socket(new_socket, ip_port):
    while True:
        buff = new_socket.recv(4096).decode()
        if buff:
            print(f"收到{ip_port}的消息{buff}")
            new_socket.send("OK收到".encode())
        else:
            print(f"客户端{ip_port}已下线")
            break

if __name__ == '__main__':
    se_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    se_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    se_socket.bind(("", 8050))
    se_socket.listen(128)
    print("等待连接————————")

    while True:
        new_socket, ip_port = se_socket.accept()
        print("客户端{}连接".format(ip_port))
        socket_gevent = gevent.spawn(handle_cl_socket, new_socket, ip_port)
        socket_gevent.join()
