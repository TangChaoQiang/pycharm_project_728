import socket

# if __name__ == '__main__':
#     # 1．创建socket对象( socket.socket())
#     # socket.AF_INET 代表IPV4 socket.AF_INET6 代表IPV6
#     cl_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # 2．和服务器建立连接( socket对象.connect( ))
#     cl_socket.connect(("192.168.247.136", 9000))
#     # 3．发送信息( socket对象.send( ) )
#     data = "hello world".encode()  # 默认utf-8
#     cl_socket.send(data)
#     # 4．接收对对方的信息(socket对象.recv ( ) )
#     buff = cl_socket.recv(4096)
#     # 异常捕获
#     try:
#         print(buff.decode())
#     except UnicodeError:
#         print(buff.decode("gbk"))
#     # 5．关闭连接(socket对象.close())
#     cl_socket.close()

if __name__ == '__main__':
    cl_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cl_socket.connect(("192.168.247.136", 8989))
    cl_socket.send("你好啊".encode())
    buf = cl_socket.recv(4096)
    print(buf.decode())
    cl_socket.close()


