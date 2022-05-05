class File(object):
    def __init__(self, filename, method):

        self.filename = filename
        self.method = method

    def __enter__(self):
        self.fp = open(self.filename, self.method, encoding="utf-8")
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()

if __name__ == '__main__':
    with File("a.txt", "r") as F:
        print(F.read())

