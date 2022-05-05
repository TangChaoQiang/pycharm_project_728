import threading

# 创建锁
mutex = threading.Lock()
list_num = 0


def test1():
    global list_num
    # 加锁
    mutex.acquire()
    for i in range(1000000):
        list_num += 1
    # 解锁
    mutex.release()

    print("线程{}执行结束, num值为{}".format(threading.currentThread().name, list_num))


# def test2():
#     global list_num
#     time.sleep(0.5)
#     for i in range(10000):
#         list_num += 1
#
#     print("线程{}执行结束, num值为{}".format(threading.currentThread().name, list_num))

if __name__ == '__main__':
    # 创建线程
    test_1 = threading.Thread(target=test1)
    test_2 = threading.Thread(target=test1)
    # 线程执行
    test_1.start()
    # 线程2执行
    test_2.start()
    print("主线程{}执 行结束, num值为{}".format(threading.currentThread().name, list_num))
