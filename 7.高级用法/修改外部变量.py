def outer(num1):
    def inner(num2):
        nonlocal num1
        num1 = 100
        print(num2+num1)
    print(f"前：{num1}")
    inner(2000)
    print(f"后：{num1}")
    return inner

if __name__ == '__main__':
    outer = outer(20)
    outer(10)
