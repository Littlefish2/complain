#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Date:{DATE}{TIME}
# @Author: zhangy

from config import config
import  requests
import json
from common import sha256

def access_Token_Login(username, password):
    # 获取登录成功后的access_token
    url=config.url
    data = dict(username=username, password=sha256.sha256hex(password), formPlat='web',
                sysId='1000000000000000001')
    headers={
        "Content-Type" : "application/json"
    }
    data=json.dumps(data)

    # 登录完成后获
    r = requests.request("POST", url + '/sys/login', data=data, headers=headers, verify=False)

    access_token = r.json()['data']['access_token']
    #print(access_token)
    return 'bearer ' + access_token

access_Token_Login(config.username,config.password)


'''
def login(user, password):
  """
  :param user:用户名
  :param password:密码
  :return:token
  """
  login_url = config.url+"/sys/login"
  print(login_url)
  data = {"username": user, "password":password,"formPlat":"web","sysId":"1000000000000000001"}
  print(data)
  headers = {"Content-Type": "application/json;charset=UTF-8"}
  response = requests.post(url=login_url, data=json.dumps(data), headers=headers,verify=False)
  print(response.text)
  response = response.json()

login(config.username,sha256.sha256hex(config.password))
'''