#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Test sequence feature
# list
l_foo = ["i", "learn", "python", "now", "and", "you"]
print(" ".join(l_foo))

print(l_foo[1:3])
print(l_foo[-3:-1])  # reverse slice
print(l_foo[:4:2])  # step size
print("*"*100)
print(l_foo.reverse())  # reverse
print(l_foo)

# tuple
t_foo = ("i", "am", "a", "tuple")
print(id(t_foo))
print(id(t_foo*2))

'''tuple vs list
1. tuple 占用的空间更小的访问和操作速度比 list 快
2. tuple 内的元素不可新增、修改、删除
3. 因为 tuple 的异质性，所以 tuple 可以作为 dict 的 key 值，而 list 不可以
'''



