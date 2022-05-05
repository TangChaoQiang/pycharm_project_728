import os

os.chdir(r"C:\Users\Ju-Ta\Desktop\python学习\文件夹")
list = os.listdir()
num = "1"
for i in list:
    str = i.split(num)
    num = int(num) + 5
    os.rename(i, str[0]+f"{num}.txt")
    num = str(num)


