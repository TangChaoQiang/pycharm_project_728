import multiprocessing
import os
import time

def sing():
    # 获得ID
    print(multiprocessing.current_process().name, os.getpid(), os.getppid())
    for i in range(5):
        print("hello sing")
        # 进程休眠
        time.sleep(0.1)
    # kill杀死进程
    os.kill(os.getpid(), 9)

def draw():
    # 获得ID
    print("drawID:", multiprocessing.current_process().pid)
    for i in range(5):
        print("hello draw")
        time.sleep(0.1)


if __name__ == "__main__":
    # 获得ID
    print(multiprocessing.current_process().name, os.getpid())
    # 创建进程对象
    # target指定进程执行的任务,也就是函数的名字,不能加括号
    process_sing = multiprocessing.Process(target=sing)
    process_draw = multiprocessing.Process(target=draw)

    # 启动进程
    process_sing.start()
    process_draw.start()
