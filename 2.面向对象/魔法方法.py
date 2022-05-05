class Dog():
    def __init__(self, name):
        print("我是魔法方法__init__")
        self.name = name

    def __str__(self):
        return self.name


dog = Dog("tang")
dog1 = Dog("tang2")

print(dog1)
print(dog)
