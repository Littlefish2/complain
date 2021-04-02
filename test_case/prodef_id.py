#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Project：complain 
# @File：prodef_id.py
# @IDE：PyCharm 
# @Date：2021/3/12 16:06 
# @Author: zhangy
import requests
import json
from common import login
from config import config

def find_modlegroup(token):
    url = config.url+"/uap/flow/modelgroup?page=1&pageSize=0&withProcessDefinitions=true"
    header ={
        "Authorization":token
    }
    res =requests.get(url=url,headers=header)
    #print(res.text)
    return res.json()["data"]["list"]
token = login.access_Token_Login(config.username,config.password)
find_modlegroup(token)
#(find_modlegroup(token))