#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Project：complain 
# @File：findme.py
# @IDE：PyCharm 
# @Date：2021/3/12 10:50 
# @Author: zhangy
import json

import requests

from config import config
from common import login
def findme(token):
    url = config.url+"/uap/auth/sys/me"
    #print(token)
    header={
        "Content-Type":"application/json;charset=UTF-8",
        "Authorization":token
    }
    res = requests.request("GET", url=url, headers=header)
    #print(res.text)
    #print(type(res.text))
    #print(type(json.loads(res.text)))
    #print(type(json.dumps(json.loads(res.text))))
    #print(res.json())
    #print(type(res.json()))

    #res1=json.dumps(json.loads(res.text), indent=4, sort_keys=False, ensure_ascii=False)
    res1=json.dumps(res.json(),indent=4,sort_keys=False,ensure_ascii=False)
    #print(res1)
    return res.json()["data"]


token = login.access_Token_Login(config.username,config.password)
findme(token)
#print(type(findme(token)))
#print(findme(token))