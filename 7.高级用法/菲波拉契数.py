def feibo(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    num = feibo(10)
    for i in num:
        print(i, end=" ")
