def fun():
    for i in range(10):
        print(f"第{i+1}次执行开始")
        yield i
        print(f"第{i+1}次执行结束")

if __name__ == '__main__':
    num = fun()
    for i in num:
        print(i)