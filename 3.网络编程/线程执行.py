import threading
import time


def fun():
    time.sleep(0.5)
    print("当前：", threading.currentThread().name)


if __name__ == "__main__":
    for i in range(10):
        sub_threading = threading.Thread(target=fun)
        sub_threading.start()

