import threading

mutex = threading.Lock()

data = [2, 3, 4, 5, 6]


def test(index):
    mutex.acquire()
    if index >= len(data):
        print(threading.currentThread().name, "下标越界")
        mutex.release()
        return
    print(threading.currentThread().name, data[index])
    mutex.release()

if __name__ == '__main__':
    for i in range(10):
        test_1 = threading.Thread(target=test, args=(i,))
        test_1.start()
        