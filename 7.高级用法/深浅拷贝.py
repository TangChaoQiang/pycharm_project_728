i = 10
f = 10.0
s = "tang"
t = (1,)
d = {"tang": "1"}
l = [1, 2, 3]
se = {1, 2, 3}

import copy

copy_s = copy.deepcopy(s)
copy_d = copy.deepcopy(d)
copy_se = copy.deepcopy(se)

print(id(s), id(copy_s))
print(id(d), id(copy_d))
print(id(se), id(copy_se))
