#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Project：complain 
# @File：test_demo.py
# @IDE：PyCharm 
# @Date：2021/3/26 14:36 
# @Author: zhangy
import pytest


def add(x, y):
    return x + y


def test_add_1():
    assert add(1, 2) == 3


@pytest.mark.demo1
def test_add_2():
    assert add(1, 3) == 3


@pytest.mark.demo1
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)



table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:5d}'.format(name, number))

