class tag():
    def __init__(self, fnu):
        self.__fn = fnu

    def __call__(self, *args, **kwargs):
        print("在调用前添加装饰功能")
        result = self.__fn(*args, **kwargs)
        print("在调用后添加装饰功能")
        return result



@tag
def sum(a, b):
    return a + b


if __name__ == '__main__':
    print(sum(1, 3))
