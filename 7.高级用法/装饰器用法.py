import time

def outer(fn):
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print("time:", end-start)
    return inner

@outer
def put():
    for i in range(10000):
        print(i)


if __name__ == '__main__':
    put()