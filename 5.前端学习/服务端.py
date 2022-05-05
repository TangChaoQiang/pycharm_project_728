import socket
import threading
import gevent

mutex = threading.Lock()


def handler(new_socket, ip_port):
    mutex.acquire()
    while True:
        buff = new_socket.recv(4096)
        if buff:
            print(buff.decode())
            new_socket.send("服务端已经收到".encode())

        else:
            print(f"客户端{ip_port}断开连接-----------")
            new_socket.close()
            break
    mutex.release()


class sever(object):
    se_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    se_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    se_socket.bind(("", 8989))
    se_socket.listen(128)
    print("等待连接‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’")

    while True:
        new_socket, ip_port = se_socket.accept()
        print(f"客户端{ip_port}连接-----------")
        # threading_handle = threading.Thread(handler(new_socket, ip_port))
        # threading_handle.start()

        # 协程实现
        socket_gevent = gevent.spawn(handler, new_socket, ip_port)
        print(socket_gevent.name)
        socket_gevent.join()
