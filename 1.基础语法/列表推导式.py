# 1．变量=[生成数据的规则for临时变量in xxx ]#每循环一次,就会创建一个数据
my_list = [i for i in range(5)]
print(my_list)  # [e,1，2,3,4]
# hello充当变量
my_list1 = ['he11o' for i in range(5)]
print(my_list1)
# f是占位符
my_list2 = [f'num:{i}' for i in my_list]
print(my_list2)

# 2．变量=[生成数据的规则for临时变量in xxx if xxx]#每循环一次,并且i于条件为True,生成一个数据
my_list = [i for i in range(5) if i % 2 == 0]

print(my_list)  # [e, l 2,3，4]

# 3.变量=[生成数据的规则for临时变量 in xxx for j in xxI#第二个for循环循环一次，生成一个数据
my_list4 = [(i, j) for i in range(3) for j in range(3)]
print(my_list4)


