import threading

# 数字
Lock1 = threading.Lock()
# 字母
Lock2 = threading.Lock()


def print_num():
    for i in range(1, 52, 2):
        # 线程2加锁
        Lock2.acquire()
        print("{}{}".format(i, i+1), end="")
        # 线程1解锁
        Lock1.release()


def print_str():
    for j in range(65, 91):
        # 线程1加锁
        Lock1.acquire()
        print(chr(j))
        # 线程2解锁
        Lock2.release()


if __name__ == '__main__':
    print_num = threading.Thread(target=print_num)
    print_str = threading.Thread(target=print_str)
    # 锁住线程1
    Lock1.acquire()
    print_num.start()
    print_str.start()
