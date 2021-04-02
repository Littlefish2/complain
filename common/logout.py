#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Project：complain 
# @File：logout.py
# @IDE：PyCharm 
# @Date：2021/3/12 11:52 
# @Author: zhangy

import requests

from config import config
from common import login
import json

def logout(token):
    url = config.url+"/sys/logout"
    header = {
        "Authorization":token
    }
    res =requests.post(url=url, headers=header, data=None)
    print(res.status_code)
    print(json.dumps(res.json(),indent=4 , ensure_ascii=False))
    assert res.status_code == 200
token = login.access_Token_Login(config.username,config.password)
logout(token)