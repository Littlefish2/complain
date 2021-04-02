#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Project：complain 
# @File：test_publish.py
# @IDE：PyCharm 
# @Date：2021/3/2 14:55 
# @Author: zhangy
import openpyxl
import requests
import json
from config import config
from common import login
from common import findme
from test_case import prodef_id
from test_case import upload_file
def read_txt():
    contents = []
    file_txt = open(r"C:\Users\Administrator\Desktop\phonenumber.txt","r",encoding="utf-8")
    for i in file_txt:
        contents.append(i.split()[0])
    #print(contents)
    file_txt.close()
    return contents
read_txt()
''''
def make_orders(token):
    url =config.url+"/uap/flow/startAndComplete/procdef/master-204:1:1a965dfa-7d80-11eb-a674-02424f0dfc43"
    txt_list=read_txt()
    print(txt_list)
    list = findme.findme(token)
    for i in txt_list:
        data={
            "name": "发布",
            "username": list["loginName"],
            "formRecord": {
                "input1": "测试1",
                "input2": i,
                "text3": "Tq09SktFBACz3TGGIEfgRZUEq49AMNPYvLzXYYnp5OP539doktBZmiOHoiJJm/Zvl4gcEq6R9AB4XSeQB9OonSOKJApKVGT7Gsca75IUZOtq1mAvRU8BPqfrzD9rQJmG9s7d8FuW7YxtbIC/PU2kUuNIGlerC+rMsJXN+435Soqwrb1lOY7x/UfGXaX9hUT2",
                "userName": list["loginName"],
                "mobilePhone": list["mobile"],
                "org": list["orgList"][0],
                "orgCode": list["orgDataList"][0]["name"],
                "account": list["loginName"],
                "roleName": list["roleDataList"][0]["name"]
            },
            "procdefId": "master-204:1:1a965dfa-7d80-11eb-a674-02424f0dfc43"
        }
        data1=json.dumps(data)
        print(data)
        header={
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        res=requests.request("POST",url=url,headers=header,data=data1)
        print(res.text)
a = login.access_Token_Login(y99,Aa111111#)
make_orders(a)

url = config.url+"/uap/flow/startAndComplete/procdef/master-204:1:1a965dfa-7d80-11eb-a674-02424f0dfc43"
txt_list=read_txt()
for i in txt_list:
    data={
        "name": "发布",
        "username": "test88",
        "formRecord": {
            "input1": "测试1",
            "input2": i,
            "text3": "Tq09SktFBACz3TGGIEfgRZUEq49AMNPYvLzXYYnp5OP539doktBZmiOHoiJJm/Zvl4gcEq6R9AB4XSeQB9OonSOKJApKVGT7Gsca75IUZOtq1mAvRU8BPqfrzD9rQJmG9s7d8FuW7YxtbIC/PU2kUuNIGlerC+rMsJXN+435Soqwrb1lOY7x/UfGXaX9hUT2",
            "userName": "test88",
            "mobilePhone": "18421145544",
            "org": "测试1",
            "orgCode": "20109920181",
            "account": "test88",
            "roleName": "中台支撑"
            },
            "procdefId": "master-204:1:1a965dfa-7d80-11eb-a674-02424f0dfc43"
        }
    data =json.dumps(data)
    print(data)
    headers = {
                  'Authorization': login.access_Token_Login(config.username,config.password),
                  'Content-Type': 'application/json'

                }

    response = requests.request("POST", url, headers=headers, data=data)
    print(response.text)
'''
# 创建订单
'''
def make_orders(token, input1, input2):
    """

    :param token:用户的token
    :param input1:单行输入框
    :param input2: 手机输入框
    :return:
    """
    pro_list=prodef_id.find_modlegroup(token)
    url =config.url+"/uap/flow/startAndComplete/procdef/"+pro_list[0]["processDefinitions"][0]["id"]
    print(url)
    list = findme.findme(token)
    data={
        "name": "发布",
        "username": list["loginName"],
        "formRecord": {
            "input1": input1,
            "input2": input2,
            "text3": "Tq09SktFBACz3TGGIEfgRZUEq49AMNPYvLzXYYnp5OP539doktBZmiOHoiJJm/Zvl4gcEq6R9AB4XSeQB9OonSOKJApKVGT7Gsca75IUZOtq1mAvRU8BPqfrzD9rQJmG9s7d8FuW7YxtbIC/PU2kUuNIGlerC+rMsJXN+435Soqwrb1lOY7x/UfGXaX9hUT2",
            "userName": list["realName"],
            "mobilePhone": list["mobile"],
            "org": list["orgList"][0],
            "orgCode": list["orgDataList"][0]["name"],
            "account": list["loginName"],
            "roleName": list["roleDataList"][0]["name"]
        },
        "procdefId": pro_list[0]["processDefinitions"][0]["id"]
    }
    data1=json.dumps(data)
    print(data)
    header={
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    res=requests.request("POST", url=url, headers=header, data=data1)
    print(res.text)
token =login.access_Token_Login(config.username,config.password)
#print(token)
make_orders(token, "你好", "18180982480")


# 通过读取txt的手机号循环创建订单
def make_orders_txt(token,input1):
    """
    :param token:用户的token
    :param input1: 单行输入框
    :return:
    """
    pro_list = prodef_id.find_modlegroup(token)
    url = config.url + "/uap/flow/startAndComplete/procdef/" + pro_list[2]["processDefinitions"][6]["id"]
    txt_list=read_txt()
    list = findme.findme(token)
    for input2 in txt_list:
        data = {
            "name": "发布",
            "username": list["loginName"],
            "formRecord": {
                "input1": input1,
                "input2": input2,
                "text3": "Tq09SktFBACz3TGGIEfgRZUEq49AMNPYvLzXYYnp5OP539doktBZmiOHoiJJm/Zvl4gcEq6R9AB4XSeQB9OonSOKJApKVGT7Gsca75IUZOtq1mAvRU8BPqfrzD9rQJmG9s7d8FuW7YxtbIC/PU2kUuNIGlerC+rMsJXN+435Soqwrb1lOY7x/UfGXaX9hUT2",
                "userName": list["realName"],
                "mobilePhone": list["mobile"],
                "org": list["orgList"][0],
                "orgCode": list["orgDataList"][0]["name"],
                "account": list["loginName"],
                "roleName": list["roleDataList"][0]["name"]
            },
            "procdefId": pro_list[2]["processDefinitions"][6]["id"]
        }
        data1=json.dumps(data)
        print(data)
        header = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        res = requests.request("POST", url=url, headers=header, data=data1)
        print(res.text)
token=login.access_Token_Login(config.username,config.password)
make_orders_txt(token,"ceshi")

'''
def make_orders_confile():
    list = upload_file.upload_flie()
    a = list["id"]
    print(a)
    token=login.access_Token_Login(config.username,config.password)
    list1 = findme.findme(token)
    pro_list = prodef_id.find_modlegroup(token)
    url = config.url + "/uap/flow/startAndComplete/procdef/" + pro_list[2]["processDefinitions"][7]["id"]
    data = {
        "name": "发布",
        "username": list1["loginName"],
        "formRecord": {
            "input1": "",
            "input2": "",
            "text1": "",
            "input3": 0,
            "input4": "",
            "input5": "",
            "input6": "",
            "input7": "",
            "input8": "",
            "input9": "",
            "input10": "",
            "input11": "",
            "input12": "",
            "input13": list["id"],
            "text3": "Tq09SktFBACz3TGGIEfgRZUEq49AMNPYvLzXYYnp5OP539doktBZmiOHoiJJm/Zvl4gcEq6R9AB4XSeQB9OonSOKJApKVGT7Gsca75IUZOtq1mAvRU8BPqfrzD9rQJmG9s7d8FuW7YxtbIC/PU2kUuNIGlerC+rMsJXN+435Soqwrb1lOY7x/UfGXaX9hUT2",
            "userName": list1["realName"],
            "mobilePhone": list1["mobile"],
            "org": list1["orgList"][0],
            "orgCode": list1["orgDataList"][0]["name"],
            "account": list1["loginName"],
            "roleName": list1["roleDataList"][0]["name"],
            "formFiles": [
                {
                    "id": list["id"],
                    "fileName": list["fileName"]
                }
            ]
        },
        "procdefId": pro_list[2]["processDefinitions"][7]["id"]
    }
    data1= json.dumps(data)
    header = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    res = requests.request("POST", url=url, headers=header, data=data1)
    print(res.text)
make_orders_confile()