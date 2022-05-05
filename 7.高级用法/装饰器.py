class make_tag(object):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, fn):
        def inner(*args, **kwargs):
            result = fn(*args, **kwargs)
            return fr"<{self.tag}> {result} <\{self.tag}>"
        return inner

@make_tag("div")
def put(info):
    return info


if __name__ == '__main__':
    put = put("nihao")
    print(put)
