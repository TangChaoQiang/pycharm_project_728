def dance():
    for i in range(5):
        print("正在跳舞————————")
        yield


def sing():
    for i in range(7):
        print("正在唱歌-----")
        yield


if __name__ == '__main__':
    dance = dance()
    sing = sing()
    isdance = None
    issing = None
    while True:
        try:
            next(dance)
        except:
            isdance = True

        try:
            next(sing)
        except:
            issing = True

        if issing and isdance:
            break