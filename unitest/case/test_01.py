#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Project：complain 
# @File：test_01.py
# @IDE：PyCharm 
# @Date：2021/3/3 10:32 
# @Author: zhangy
import unittest

class testA(unittest.TestCase):
    def setUP(self):
        pass
    def test_01(self):
        print("用例1")
    def test_02(self):
        print("用例2")
    def tearDown(self):
        pass
