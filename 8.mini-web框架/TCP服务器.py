import socket
import os
import framework


def main():
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用，程序退出端口号立即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    tcp_server_socket.bind(("", 8989))
    # 设置监听
    tcp_server_socket.listen(128)
    # 循环等待接受客户端的连接请求
    while True:
        # 等待接受客户端的连接请求
        new_socket, ip_port = tcp_server_socket.accept()
        # 代码执行到此，说明连接建立成功
        # 接收客户端的请求信息
        recv_data = new_socket.recv(4096)
        # 判断接收的数据长度是否为0
        if len(recv_data) == 0:
            new_socket.close()
            return

        # 对二进制数据进行解码
        recv_content = recv_data.decode("utf-8")
        # print(recv_content)

        # 对数据按照空格进行分割
        request_list = recv_content.split(" ", maxsplit=2)
        # 获取请求的资源路径
        file_name = request_list[1]
        # print(file_name)

        # 判断请求的是否是根目录，如果是根目录设置返回的信息
        if file_name == "/":
            file_name = "/index.html"
        # 判断是否为动态
        if file_name.endswith(".html"):
            # 需要处理的动态的数据
            env = {
                "filename": file_name
            }
            # 调用框架,获得返回值
            status, header, data = framework.handle_client(env)
            response_line = f"HTTP/1.1 {status}\r\n"
            response_header = f"Server: {header}\r\ncontent-type: text/html; charset=utf-8\r\n"
            response_body = data
        # 1. os.path.exits
        # os.path.exists("static/" + file_name)
        else:
            # 2. try-except
            # 代码执行到此，说明文件存在，返回200状态信息
            # 响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_header = "Server: tang/1.0\r\n"
            # 打开文件读取文件中的数据, 提示：这里使用rb模式，兼容打开图片文件
            try:
                with open("static" + file_name, "rb") as file:  # 这里的file表示打开文件的对象
                    file_data = file.read()
            except:
                with open("static/error.html", "rb") as file1:
                    file_data = file1.read()
                    response_line = "HTTP/1.1 404 NOT FOUND\r\n"
            # 响应体
            response_body = file_data
        # 提示： with open 关闭文件这步操作不用程序员来完成，系统帮我们来完成

        # 把数据封装成http 响应报文格式的数据
        response = (response_line + response_header + "\r\n").encode("utf-8") + response_body

        # 发送给浏览器的响应报文数据
        new_socket.send(response)
        # 关闭服务于客户端的套接字
        new_socket.close()


# 判断是否是主模块的代码
if __name__ == '__main__':
    main()
