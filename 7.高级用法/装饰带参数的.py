import time

def logging(fn):
    def inner(*args, **kwargs):
        print("正在计算")
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"花费:{end-start}")
        return result
    return inner

@logging
def sum(a, b):
    return (a + b)

@logging
def dict(name, age):
    print(name, age)

if __name__ == '__main__':
    sum(1, 3)

    dict(name="tang", age=22)
