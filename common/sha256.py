#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Project：complain 
# @File：sha256.py
# @IDE：PyCharm 
# @Date：2021/3/11 16:51 
# @Author: zhangy
import hashlib
def sha256hex(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode("utf-8"))
    res = sha256.hexdigest()
    return res
sha256hex("Aa111111#")