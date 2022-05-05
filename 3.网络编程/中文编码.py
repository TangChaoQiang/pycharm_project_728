str = "中国"

# 查看转码后

utf_8 = str.encode("utf-8")
print(utf_8)
gbk = str.encode("gbk")
print(gbk)

# 转码回来
print(utf_8.decode("utf-8"))
print(gbk.decode("gbk"))
