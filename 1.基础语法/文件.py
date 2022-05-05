f = open('c.txt ', 'wb')
f.write('你好'.encode())  # encode()将str转换为二进制格式的字符串f.close()

f1 = open('c.txt', 'rb')
buf = f1.read()
print(buf)
f1.close()
