#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Test set feature
set_foo = {}
set_bar = set()
print(type(set_foo), type(set_bar))

set_foo = {1, 2, 3, 6}
set_bar = {1, 2, 3, 4, 5}

# 合并
print(set_foo.union(set_bar))
# 交集
print(set_foo.intersection(set_bar))
# 差集
print(set_bar.difference(set_foo))
# 对称差集
print(set_bar.symmetric_difference(set_foo))
