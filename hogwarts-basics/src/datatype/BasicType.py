#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 将对象 x 转换为表达式字符串
b = {"name": "linda", "age": 18}
str_b = repr(b)
print(str_b)
print(str_b[0:3])


# 用来计算在字符串中的有效Python表达式,并返回一个对象
a = "[1,2,3]"
list_a = eval(a)
print(list_a)
print(list_a[0])
