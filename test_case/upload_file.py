#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Project：complain 
# @File：upload_file.py
# @IDE：PyCharm 
# @Date：2021/3/19 14:28 
# @Author: zhangy
from common import login
from config import config
import requests

def upload_flie():
    '''

    :return:
    '''
    url =config.url+"/uap/file/upload"
    token = login.access_Token_Login(config.username,config.password)
    headers = {
        "Authorization":token
    }
    file_data = {'file': ("fd.jpg", open(r"C:\Users\Administrator\Desktop\图片\fd.jpg", 'rb'), 'image/jpg')}
    r = requests.post(url=url, headers=headers, files=file_data)
    #print(r.text)
    return r.json()["data"]
upload_flie()
