def outer(num1):
    def inner(num2):
        print(num2+num1)
    return inner

if __name__ == '__main__':
    func1 = outer(100)
    func2 = outer(1000)
    func1(10)
    func2(100)