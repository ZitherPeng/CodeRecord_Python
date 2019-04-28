#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Test dict feature

# merge dict
d_foo = {"name": "zither", "org": "lucky coding"}
d_bar = {"today": "happy", "I'am": "vary good", "name": "lucky"}
print(id(d_bar))
d_bar.update(d_foo)
print(d_bar)
print(id(d_bar))

# translation



