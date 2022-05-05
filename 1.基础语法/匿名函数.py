# 1.无参无返回值
(lambda: print("hello"))()

f1 = lambda: print("nihao")
f1()


# 2.无参有返回值
def f1():
    return 1 + 2


f1 = f1()
print(f1)
f2 = lambda: 1 + 2
print(f2())
# 定义一个列表嵌套字典
list = [
    {"name": "tang2", "age": 10},
    {"name": "tang1", "age": 9},
    {"name": "tang3", "age": 9}
]
# 排序，如果直接调用sort方法，会报错，
# 使用lambda传入字典的键，sort通过键查找值，然后进行排序
list.sort(key=lambda list1: list1["name"])
print(list)
list.sort(key=lambda list1: list1["age"])
print(list)

list2 = ['a', 'bsghfgc', "defghtrhh", 'hijkl']
# 按照字符串首字母排序
list2.sort()
print(list2)
# 按照字符串长度排序
list2.sort(key=lambda x: len(x))
print(list2)

# sort( key= Lambda 形参:(排序规则，排序规则2，...))
# 当第一个规则相同，会按照第二个规则排序
list.sort(key=lambda x: (x['age'], x['name']))
print(list)
