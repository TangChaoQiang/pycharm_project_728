import gevent
from gevent import monkey

monkey.patch_all()
# 创建函数
def dance(dancer, name):
    for i in range(5):
        print(f"{dancer}正在跳{name}")
        gevent.sleep(0.1)


def sing(singer, name):
    for i in range(8):
        print(f"{singer}正在唱{name}1111")
        gevent.sleep(0.1)


if __name__ == '__main__':
    g1 = gevent.spawn(dance, "tang1", "绝世")
    g2 = gevent.spawn(sing, "tang2", "世界")
    g2.join()
    g1.join()
