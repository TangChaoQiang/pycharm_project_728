import socket

if __name__ == '__main__':
    cl_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cl_socket.connect(("192.168.247.136", 8989))
    cl_socket.send("我是客户端".encode())
    buff = cl_socket.recv(4096)
    if buff:
        print(buff.decode())
    cl_socket.close()
